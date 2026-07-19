"""Sync all course documents to database."""
import asyncio, os, hashlib
from sqlalchemy import text
from app.core.database import async_session_factory

VAULT = r"C:\Users\22067\Desktop\李尚凯蒸馏\CyberMe-Vault"
COURSE_CODES = {
    "DB_数据库": "DB", "DS_数据结构": "DS", "CPP_C++": "CPP",
    "JAVA_java": "JAVA", "PY_python": "PY", "SE_软件工程": "SE",
    "PROB_概率论": "PROB", "LINALG_线性代数": "LINALG",
    "PHYSICS_大学物理": "PHYSICS", "EDA_EDA": "EDA",
    "ENGLISH_学术英语": "ENGLISH", "HISTORY_近代史": "HISTORY",
    "JUNLI_军理": "JUNLI", "MAOGAI_毛概自用资料": "MAOGAI",
    "MAYUAN_马原复习": "MAYUAN", "SIXIANG_思想与政治": "SIXIANG",
    "XIGAI_习概复习": "XIGAI", "ZHENGCE_政策与形势": "ZHENGCE",
    "INFO_信息导论": "INFO",
}

async def sync():
    async with async_session_factory() as db:
        total_updated = 0
        for cname, code in COURSE_CODES.items():
            base = os.path.join(VAULT, f"20_University/{cname}")
            if not os.path.exists(base):
                continue
            updated = 0
            for root, dirs, files in os.walk(base):
                # Skip 90_ and 01_
                if "90_" in root or "01_" in root or "提取资料" in root:
                    continue
                for fn in files:
                    if not fn.endswith(".md") or fn.startswith("."):
                        continue
                    fp = os.path.join(root, fn)
                    rp = os.path.relpath(fp, VAULT).replace("\\", "/")
                    with open(fp, "r", encoding="utf-8") as f:
                        content = f.read()
                    nh = hashlib.sha256(content.encode()).hexdigest()
                    r = await db.execute(text("SELECT id, content_hash FROM vault_documents WHERE relative_path=:p AND deleted_at IS NULL"), {"p": rp})
                    row = r.fetchone()
                    if row and row[1] != nh:
                        await db.execute(text("UPDATE vault_documents SET markdown_body=:c, content_hash=:h, updated_at=NOW() WHERE id=:i"), {"c": content, "h": nh, "i": row[0]})
                        updated += 1
                    elif not row:
                        title = fn.replace(".md", "")
                        dt = "concept"
                        if "MOC" in fn: dt = "moc"
                        elif "速查" in fn or "速记" in fn: dt = "reference"
                        elif "例题" in fn: dt = "problem-set"
                        elif "错题" in fn: dt = "tracker"
                        await db.execute(text("INSERT INTO vault_documents (id, vault_id, relative_path, title, course_code, document_type, markdown_body, content_hash, status, created_at, updated_at) VALUES (gen_random_uuid(), (SELECT vault_id FROM vault_documents WHERE course_code=:co LIMIT 1), :p, :t, :co, :dt, :b, :h, 'active', NOW(), NOW())"), {"co": code, "p": rp, "t": title, "dt": dt, "b": content, "h": nh, "active": "active"})
                        updated += 1
            if updated > 0:
                print(f"  {cname}: {updated} updated/inserted")
                total_updated += updated
        await db.commit()
        print(f"\\nTOTAL: {total_updated} docs synced across {len(COURSE_CODES)} courses")

asyncio.run(sync())
