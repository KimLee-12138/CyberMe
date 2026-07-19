---
id: extract-xigai-ae23fc0b
type: extract
status: extracted
course: XIGAI
source:
  - "[[91_Raw-Archive/DOC/XIGAI_README.md_笔记_未知日期_ae23fc0b.md]]"
source_pages: all
source_hash: "ae23fc0b98921103498a4060ac71fed030461c901da58fba5d1dc59bd3c890f5"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# README.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 长江雨课堂 PPT 批量下载器

批量下载长江雨课堂某门课程的全部课件，自动合并为 PDF。

## 功能

- 列出全部课程，勾选下载
- 内容指纹去重 — 同一份 PPT 不重复下载
- 断点续传，中断后可继续
- 一键浏览器自动登录

## 使用

双击 `点我运行.bat`，或：

```bash
pip install -r requirements.txt
playwright install chromium
python gui.py
```

首次运行点击「粘贴 Cookie」粘贴，或点击「浏览器登录」扫码自动获取。

## 文件

| 文件 | 说明 |
|------|------|
| `gui.py` | 主程序 |
| `login.py` | Playwright 自动登录 |
| `点我运行.bat` | 一键启动 |

---

感谢 @Zhao2441010 的技术支持

@PanSomeone


## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_习概复习_课程MOC|习概复习 MOC]]
