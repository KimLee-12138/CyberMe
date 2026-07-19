"""Sync CALCULUS course documents from Vault to database."""
import asyncio, os, hashlib
from sqlalchemy import text
from app.core.database import async_session_factory

VAULT = r"C:\Users\22067\Desktop\李尚凯蒸馏\CyberMe-Vault"
DIRS = [
    "20_University/CALCULUS_微积分/00_微积分_课程MOC.md",
    "20_University/CALCULUS_微积分/02_知识点",
    "20_University/CALCULUS_微积分/03_公式与规则",
    "20_University/CALCULUS_微积分/04_例题与错题",
]

async def sync():
    async with async_session_factory() as db:
        updated = 0
        total = 0
        for d in DIRS:
            full = os.path.join(VAULT, d)
            if os.path.isfile(full):
                files = [(full, d)]
            else:
                files = []
                for root, dirs, fnames in os.walk(full):
                    for fn in fnames:
                        if fn.endswith(".md"):
                            fp = os.path.join(root, fn)
                            rp = os.path.relpath(fp, VAULT).replace("\\", "/")
                            files.append((fp, rp))
            for fp, rp in files:
                with open(fp, "r", encoding="utf-8") as f:
                    content = f.read()
                total += len(content)
                nh = hashlib.sha256(content.encode()).hexdigest()
                r = await db.execute(text("SELECT id, content_hash FROM vault_documents WHERE relative_path=:p AND deleted_at IS NULL"), {"p": rp})
                row = r.fetchone()
                if row and row[1] != nh:
                    await db.execute(text("UPDATE vault_documents SET markdown_body=:c, content_hash=:h, updated_at=NOW() WHERE id=:i"), {"c": content, "h": nh, "i": row[0]})
                    updated += 1
                elif not row:
                    fn = os.path.basename(fp)
                    title = fn.replace(".md", "")
                    dt = "concept"
                    if "MOC" in fn: dt = "moc"
                    elif "速查" in fn: dt = "reference"
                    elif "例题" in fn: dt = "problem-set"
                    elif "错题" in fn: dt = "tracker"
                    await db.execute(text("INSERT INTO vault_documents (id, vault_id, relative_path, title, course_code, document_type, markdown_body, content_hash, status, created_at, updated_at) VALUES (gen_random_uuid(), (SELECT vault_id FROM vault_documents WHERE course_code=:c LIMIT 1), :p, :t, :c, :dt, :b, :h, 'active', NOW(), NOW())"), {"c": "CALCULUS", "p": rp, "t": title, "dt": dt, "b": content, "h": nh, "active": "active"})
                    updated += 1
        await db.commit()
        print(f"CALCULUS: {updated} docs updated/inserted. Total {total} chars.")

asyncio.run(sync())
