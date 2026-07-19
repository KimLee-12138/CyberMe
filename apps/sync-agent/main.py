"""CyberMe Sync Agent — Local Vault Synchronization."""

import os
import platform
import socket
import time

import click

from agent.db import init_db, get_config, set_config, get_device_info, save_device_info, get_stats
from agent.scanner import scan_vault
from agent.client import (
    pair_device,
    upload_manifest,
    flush_pending_events,
    check_server_health,
    fetch_writeback_patches,
)
from agent.policy import load_policy


@click.group()
def cli():
    """CyberMe 本地同步代理 — 将 Obsidian Vault 安全同步到私人云端."""
    init_db()


@cli.command()
def status():
    """显示同步状态."""
    init_db()
    device = get_device_info()
    policy = load_policy()
    stats = get_stats()

    click.echo("=== CyberMe 同步代理 ===")
    click.echo()

    if not device:
        click.echo("状态:   未配对 — 请先执行 'pair' 命令")
        return

    click.echo(f"设备:   {device['name']} ({device['platform']})")
    click.echo(f"服务器: {device['api_base_url']}")
    click.echo()

    # Check server health
    healthy = check_server_health()
    click.echo(f"云端连接: {'[OK] 正常' if healthy else '[FAIL] 无法连接'}")

    # Stats
    click.echo(f"待上传事件: {stats['pending_events']}")
    click.echo(f"失败事件:   {stats['failed_events']}")
    click.echo(f"待应用补丁: {stats['pending_patches']}")

    # Policy info
    vault_root = get_config("vault_root")
    if vault_root:
        click.echo(f"\nVault 目录: {vault_root}")
        click.echo(f"Include: {', '.join(policy.get('include', [])[:3])}")


@cli.command()
def pair():
    """输入配对码连接云端."""
    code = click.prompt("请输入网页端显示的 6 位配对码", type=str)

    api_url = click.prompt(
        "请输入云端 API 地址",
        type=str,
        default="http://localhost:8000",
    )

    hostname = socket.gethostname()
    device_name = click.prompt(
        "设备名称",
        type=str,
        default=hostname,
    )
    device_platform = platform.system().lower()

    click.echo(f"正在连接 {api_url} ...")

    try:
        result = pair_device(code, device_name, device_platform, api_url)
        click.echo(f"[OK] 配对成功！设备 ID: {result['device_id']}")
        save_device_info(
            result["device_id"],
            device_name,
            device_platform,
            result["device_token"],
            api_url,
        )
        click.echo("设备信息已保存。")
    except Exception as e:
        click.echo(f"[FAIL] 配对失败: {e}")
        return

    # Prompt for vault root
    vault_root = click.prompt(
        "\n请输入 Obsidian Vault 根目录路径",
        type=str,
        default=os.getcwd(),
    )
    vault_root = os.path.abspath(vault_root)
    if os.path.isdir(vault_root):
        set_config("vault_root", vault_root)
        click.echo(f"Vault 路径已保存: {vault_root}")
    else:
        click.echo(f"警告: 目录不存在 — {vault_root}")


@cli.command()
def now():
    """手动触发全量同步."""
    init_db()
    device = get_device_info()
    if not device:
        click.echo("错误: 未配对设备，请先执行 'pair' 命令")
        return

    vault_root = get_config("vault_root")
    if not vault_root or not os.path.isdir(vault_root):
        click.echo("错误: Vault 目录未配置或不存在")
        return

    # Scan
    click.echo("正在扫描 Vault ...")
    manifest = scan_vault(vault_root)
    click.echo(
        f"扫描完成: {manifest['stats']['synced']} 个文件可同步, "
        f"{manifest['stats']['skipped']} 个跳过, "
        f"{manifest['stats']['total_size_mb']} MB"
    )

    if manifest["stats"]["skipped"] > 0:
        click.echo(f"\n跳过文件 (前 10 个):")
        for s in manifest["skipped"][:10]:
            click.echo(f"  - {s['path']}: {s['reason']}")

    # Upload manifest
    diff = {}
    if manifest["files"]:
        click.echo("\n正在上传清单...")
        diff = upload_manifest(manifest["vault_id"], manifest["files"]) or {}
        if diff:
            click.echo(f"[OK] 清单已上传: {diff.get('new_count',0)} 新文件, {diff.get('updated_count',0)} 已更新")
        else:
            click.echo("[FAIL] 上传失败，请检查网络和服务端日志")
    else:
        click.echo("没有可同步的文件。")

    # Upload actual file contents for new/changed files
    changed = diff.get("new_files", []) + diff.get("updated_files", [])
    if changed:
        click.echo(f"\n正在上传 {len(changed)} 个文件的完整内容...")
        from agent.client import push_document
        import hashlib
        uploaded = 0
        for rel_path in changed:
            full_path = os.path.join(vault_root, rel_path.replace("/", os.sep))
            if not os.path.isfile(full_path):
                continue
            with open(full_path, "rb") as f:
                content_bytes = f.read()
            # Try reading as text
            try:
                content = content_bytes.decode("utf-8")
            except UnicodeDecodeError:
                continue
            content_hash = hashlib.sha256(content_bytes).hexdigest()
            if push_document("upsert", rel_path, content, None, content_hash):
                uploaded += 1
        click.echo(f"[OK] 已上传 {uploaded}/{len(changed)} 个文件的内容")

    # Flush pending events
    click.echo("\n正在同步增量事件...")
    flush_result = flush_pending_events()
    click.echo(f"增量同步: {flush_result['synced']} 成功, {flush_result['failed']} 失败")


@cli.group()
def patch():
    """管理待应用的写回补丁."""
    pass


@patch.command(name="list")
def patch_list():
    """列出待应用的写回补丁."""
    patches = fetch_writeback_patches()
    if not patches:
        click.echo("暂无待应用补丁")
        return

    for p in patches:
        click.echo(f"\n补丁 {p['id']}: {p.get('title', '无标题')}")
        click.echo(f"  目标文件: {p.get('target_path', '?')}")
        click.echo(f"  风险级别: {p.get('risk_level', '?')}")


@patch.command(name="apply")
@click.argument("patch_id", required=False)
def patch_apply(patch_id):
    """应用指定的或全部待处理的写回补丁."""
    click.echo("补丁应用功能将在写回系统完成后实现")


@cli.command()
def doctor():
    """诊断并修复同步问题."""
    init_db()
    click.echo("=== 系统诊断 ===")

    # Check DB
    try:
        stats = get_stats()
        click.echo(f"[OK] 本地数据库: 正常 ({stats['total_events']} 条记录)")
    except Exception as e:
        click.echo(f"[FAIL] 本地数据库: 异常 ({e})")

    # Check device
    device = get_device_info()
    if device:
        click.echo(f"[OK] 设备已配对: {device['name']}")
    else:
        click.echo("[FAIL] 设备未配对")

    # Check network
    if device:
        healthy = check_server_health()
        click.echo(f"{'[OK]' if healthy else '[FAIL]'} 云端连接: {'正常' if healthy else '无法连接'}")

    # Check vault
    vault_root = get_config("vault_root")
    if vault_root and os.path.isdir(vault_root):
        click.echo(f"[OK] Vault 目录: {vault_root}")
    else:
        click.echo(f"[FAIL] Vault 目录未配置或不存在")

    # Check policy
    try:
        policy = load_policy()
        click.echo(f"[OK] 同步策略: {len(policy.get('include', []))} include / {len(policy.get('exclude', []))} exclude")
    except Exception as e:
        click.echo(f"[FAIL] 同步策略: 解析失败 ({e})")


@cli.command()
def watch():
    """启动文件监听，自动同步 Vault 变更到云端."""
    init_db()
    device = get_device_info()
    if not device:
        click.echo("错误: 未配对设备，请先执行 'pair' 命令")
        return

    vault_root = get_config("vault_root")
    if not vault_root or not os.path.isdir(vault_root):
        click.echo("错误: Vault 目录未配置")
        return

    from agent.watcher import start_watcher

    click.echo(f"=== CyberMe 同步代理 — 监听模式 ===")
    click.echo(f"Vault: {vault_root}")
    click.echo(f"服务器: {device['api_base_url']}")
    click.echo(f"设备: {device['name']}")
    click.echo()
    click.echo("正在监听文件变更... (Ctrl+C 停止)")

    observer, handler = start_watcher(vault_root)

    try:
        while True:
            time.sleep(5)
            try:
                result = flush_pending_events()
                if result["synced"] > 0:
                    click.echo(f"  [SYNC] 已上传 {result['synced']} 个变更")
                if result["failed"] > 0:
                    click.echo(f"  [FAIL] {result['failed']} 个上传失败")
            except Exception as e:
                click.echo(f"  [WARN] 上传异常: {e}")
    except KeyboardInterrupt:
        click.echo("\n正在停止监听...")
        observer.stop()
        observer.join()
        flush_pending_events()
        click.echo("同步代理已停止。")


if __name__ == "__main__":
    cli()
