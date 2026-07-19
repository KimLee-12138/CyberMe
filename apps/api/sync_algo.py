"""Sync ALGO course documents from Vault to database."""
import asyncio, os, hashlib
from sqlalchemy import text
from app.core.database import async_session_factory

VAULT = r"C:\Users\22067\Desktop\李尚凯蒸馏\CyberMe-Vault"

async def sync_algo():
    async with async_session_factory() as db:
        updated = 0
        algo_dir = os.path.join(VAULT, "20_University", "ALGO_算法")
        for root, dirs, files in os.walk(algo_dir):
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                full_path = os.path.join(root, fname)
                rel = os.path.relpath(full_path, VAULT).replace("\\", "/")

                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                new_hash = hashlib.sha256(content.encode()).hexdigest()

                result = await db.execute(
                    text("SELECT id, content_hash FROM vault_documents WHERE relative_path = :p AND deleted_at IS NULL"),
                    {"p": rel},
                )
                row = result.fetchone()

                if row and row[1] != new_hash:
                    await db.execute(
                        text("UPDATE vault_documents SET markdown_body = :c, content_hash = :h, updated_at = NOW() WHERE id = :i"),
                        {"c": content, "h": new_hash, "i": row[0]},
                    )
                    updated += 1
                    print(f"  [UPDATED] {fname} ({len(content)} chars)")
                elif not row:
                    title = fname.replace(".md", "")
                    dtype = "concept"
                    if "MOC" in fname or "moc" in fname.lower():
                        dtype = "moc"
                    elif "公式" in fname or "速查" in fname:
                        dtype = "reference"
                    elif "例题" in fname:
                        dtype = "problem-set"
                    elif "错题" in fname:
                        dtype = "tracker"
                    await db.execute(
                        text("""INSERT INTO vault_documents
                            (id, vault_id, relative_path, title, course_code, document_type, markdown_body, content_hash, status, created_at, updated_at)
                            VALUES (gen_random_uuid(),
                            (SELECT vault_id FROM vault_documents WHERE course_code='ALGO' LIMIT 1),
                            :p, :t, 'ALGO', :dt, :c, :h, 'active', NOW(), NOW())"""),
                        {"p": rel, "t": title, "dt": dtype, "c": content, "h": new_hash},
                    )
                    updated += 1
                    print(f"  [INSERTED] {fname} ({len(content)} chars)")

        await db.commit()
        print(f"\nDone! {updated} documents synced.")

asyncio.run(sync_algo())
