# CyberMe Android

> 状态：debug APK 可构建、可安装、已登录实测；目标设备 Android 15 / WebView 124。
> 本文只覆盖 **debug APK**；release 签名与商店上架未做。

---

## 1. 架构

Android WebView 不打包静态页面，而是直接打开 FastAPI 托管的 `apps/web/dist`：

```text
Android WebView
  └─ http://<LAN-IP>:8002/        # FastAPI 托管的 SPA
       └─ /api/v1/*               # 同源 API
```

这样做的原因：

- API 和页面同源，HttpOnly session cookie 直接可用；
- 不需要 CORS，也不受 `SameSite=Lax` 跨站限制；
- 一套构建产物，Web、Android、PWA 共用。

FastAPI 在 `apps/web/dist` 存在时会挂 SPA fallback；缺失的 JS/CSS 返回 404，不会错误地回 index.html。

---

## 2. 前置条件

| 项 | 要求 |
|---|---|
| JDK | **21**（Capacitor 8 生成 `sourceCompatibility 21`） |
| Android SDK | platform 35 / build-tools 35 |
| Node | 22+ |
| 手机 | Android WebView **111+**（Tailwind 4 的 `@layer`/`@property`/`color-mix`） |
| 网络 | 手机与电脑同一 Wi-Fi，电脑 8002 端口可达 |

> 模拟器 Android 10 自带 WebView 74，CSS 不兼容；JS 已降到 es2017，但 Tailwind 4 CSS 仍需新 WebView。用 Android 15 模拟器或现代真机。

---

## 3. 启动后端

```powershell
cd apps/api
uvicorn app.main:app --host 0.0.0.0 --port 8002
```

`0.0.0.0` 是为了让手机访问；只建议在可信局域网使用。

验证电脑本机：

```powershell
curl http://<LAN-IP>:8002/
```

---

## 4. 构建 APK

自动检测当前 LAN IP：

```powershell
cd apps/web
npm run android:debug
```

或显式指定：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build-android.ps1 -ApiHost 192.168.31.244
```

脚本行为：

1. `npm run build`（Vite target `es2017`）；
2. `CAP_SERVER_URL=http://<IP>:8002 npx cap sync android`；
3. `JAVA_HOME=<Temurin 21> gradlew assembleDebug`。

产物：

```text
apps/web/android/app/build/outputs/apk/debug/app-debug.apk
```

---

## 5. 安装与登录

```powershell
adb install -r apps/web/android/app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.cyberme.os/.MainActivity
```

登录：

```text
demo / cyberme2026
```

如果换 Wi-Fi / IP 变化：重新运行构建脚本，APK 里的 `server.url` 会更新。

---

## 6. Debug 网络配置

- `capacitor.config.ts` 不再写死 IP；由 `CAP_SERVER_URL` 注入；
- `android/app/src/debug/AndroidManifest.xml` 仅 debug 打开 `usesCleartextTraffic`；
- release 默认不允许 cleartext，生产应使用 HTTPS：

```powershell
$env:CAP_SERVER_URL='https://cyberme.example.com'
npm run android:debug
```

---

## 7. 已实测

Android 15 模拟器（1080×1920，WebView 124）：

| 场景 | 结果 |
|---|---|
| 安装 / 启动 | 通过 |
| 登录 `demo` | 通过 |
| 驾驶舱 | 通过 |
| 笔记 433 篇 / 课程筛选 | 通过 |
| 数据质量看板 | 通过 |
| 知识图谱 24 课程 / 18 边 | 通过 |
| RAG 提问 | 通过，返回 8 条证据 |
| 移动证据面板 | 通过 |

截图：

- `docs/screenshots/19-android-app.png` — 登录
- `docs/screenshots/20-android-home.png` — 驾驶舱
- `docs/screenshots/21-android-notes.png` — 笔记
- `docs/screenshots/22-android-quality.png` — 质量
- `docs/screenshots/23-android-graph.png` — 图谱
- `docs/screenshots/24-android-ask.png` — 问答
- `docs/screenshots/27-android-rag-evidence.png` — RAG 证据面板
- `docs/screenshots/26-android-notes-lan.png` — 最终 LAN APK 笔记页

---

## 8. 踩过的坑

### 8.1 JDK 17 编不过

```text
无效的源发行版：21
```

Capacitor 8 生成 Java 21。安装 Temurin 21 并让 Gradle 使用：

```powershell
$env:JAVA_HOME='C:\Program Files\Eclipse Adoptium\jdk-21.0.13.9-hotspot'
```

### 8.2 白屏 / `Cannot destructure 'null'`

生产构建里 Phosphor Icons 的 `IconBase` 被转成：

```js
{ } = null
```

登录后侧边栏一渲染就崩。已替换为 **Lucide React**，并移除 `@phosphor-icons/react`。

### 8.3 旧 WebView 语法错误

Android 10 WebView 74 不支持 `?.` / `??`：

```text
Uncaught SyntaxError: Unexpected token ?
```

Vite 已设置 `build.target: 'es2017'`。

### 8.4 Cookie 跨站

不要用 `http://localhost` 页面去请求 `http://192.168.x.x:8002`：跨站 + `SameSite=Lax` 会导致登录态丢失。本方案让 WebView 直接打开 API 同源地址。

### 8.5 找不到 APK

路径是 `apps/web/android/app/build/outputs/apk/debug/app-debug.apk`，不是 `android/app/build/outputs/apk/debug`。
