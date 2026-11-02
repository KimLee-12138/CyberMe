# 长江雨课堂只读同步

> 状态：已用真实账号验收通过（账号信息已脱敏），同步到 **56 门课程、43 个历史作业、406 条上课记录**；按“未截止 + 未完成”口径，当前待完成 **0**。
> 只读：不签到、不答题、不提交作业、不发讨论。

## 已验证

- `/yuketang` 页面正常显示课程、作业、课件
- 微积分课程课件读取成功：3 份 presentation，单份 34 页
- 课件图片 `https://changjiang-private-qn.yuketang.cn/...` 返回 200，可在页面直接显示
- 单节课 PDF 导出：34 页，3.7MB；桌面下载，Android 保存到 `Documents/CyberMe/`
- Android WebView 页面同步显示 56 门课程 / 43 个作业 / 406 条课件
- 驾驶舱没有未截止作业，因此不显示待办卡片
- 后端离线测试 16 passed

## 1. 打开页面

电脑浏览器：

```text
http://127.0.0.1:8002/yuketang
```

手机（同一 Wi-Fi）：

```text
http://192.168.31.244:8002/yuketang
```

如果页面提示未登录，先用 `demo / cyberme2026` 登录 CyberMe。

## 2. 获取 sessionid

1. Chrome 打开并登录：

   ```text
   https://changjiang.yuketang.cn/
   ```

2. 按 `F12`；
3. 打开 **Application / 应用** → **Cookies** → `https://changjiang.yuketang.cn`；
4. 找到 `sessionid`；
5. 复制它的 **Value**。

> `sessionid` 等于登录态，不要发到群里、截图里或公开仓库。
> CyberMe 只会把它加密保存在本机 `data/integrations/yuketang/session.enc`。

## 3. 保存并同步

回到 CyberMe 的 `/yuketang` 页面，把 `sessionid` 粘贴到输入框，点「保存并同步」。

首次同步会：

1. 验证账号；
2. 拉课程列表；
3. 每门课拉活动时间轴（作业/公告/上课记录）；
4. 拉章节进度与截止时间；
5. 写入本机缓存。

之后每 `YKT_REFRESH_MINUTES`（默认 15 分钟）自动刷新，也可以点「立即同步」。

## 4. 能看到什么

- 课程列表：课程名、教师、学期、班级
- 作业：标题、类型、发布时间、完成状态
- **待完成口径：`deadline > 当前时间` 且未完成**；已截止的只显示「已截止」，不计入待完成
- 公告：课程活动里的公告
- 截止时间：章节进度里的 `score_deadline`
- 课件：先按课程分组，点课程后再看第几次课；点单节课加载幻灯片
- PDF：课件弹层右上角「导出 PDF」
  - 电脑浏览器：直接下载 PDF
  - Android：保存到 `Documents/CyberMe/`，并打开系统分享面板
- 驾驶舱：只有存在未截止且未完成的作业时才显示提醒

## 5. 接口

```text
GET    /api/v1/integrations/yuketang/status
GET    /api/v1/integrations/yuketang/overview
POST   /api/v1/integrations/yuketang/session   { "sessionid": "..." }
DELETE /api/v1/integrations/yuketang/session
POST   /api/v1/integrations/yuketang/sync
GET    /api/v1/integrations/yuketang/courseware/{lesson_id}
GET    /api/v1/integrations/yuketang/courseware/{lesson_id}/pdf
```

全部需要 CyberMe 登录 Cookie。

## 6. 边界

- 雨课堂没有公开 API，这里用的是网页端只读接口；平台改版可能失效。
- `sessionid` 过期后需要重新粘贴。
- 已截止作业的题面通常无权限，只能看到标题/时间/状态。
- 课件图片来自雨课堂 CDN；少数课件在平台端没有 cover 图片，页面显示「无图片」，这类课件无法导出 PDF。
- 首次同步完成后页面会自动刷新；旧课件/旧作业可能没有可读课件。
- PDF 文件由后端从幻灯片图片合成；第一次导出会花几秒。
- 不做签到、答题、提交作业、发讨论等写操作。

## 7. 排查

### 页面一直提示未配置

确认 `https://changjiang.yuketang.cn/` 登录的不是「标准雨课堂」或「荷塘雨课堂」；四个区域 Cookie 不通用。

### 保存时报 401 / 会话无效

重新登录长江雨课堂，复制新的 `sessionid`。

### 同步很慢

首次同步要拉所有课程；后续走 15 分钟缓存。可在页面点「立即同步」强制刷新。

### 课件打不开

先确认该活动是「上课记录」；作业/公告没有课件。课件图片加载失败时，点图片可在新标签打开原图。

### 清除

页面点「断开」，或删除：

```text
data/integrations/yuketang/session.enc
data/integrations/yuketang/cache.json
```
