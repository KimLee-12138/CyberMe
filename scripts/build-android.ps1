# Build a debug APK that loads the API server over the local network.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File scripts/build-android.ps1
#   powershell -ExecutionPolicy Bypass -File scripts/build-android.ps1 -ApiHost 192.168.31.244
#
# The backend must listen on 0.0.0.0:8002 for a physical phone:
#   uvicorn app.main:app --host 0.0.0.0 --port 8002
param(
  [string]$ApiHost = "",
  [switch]$Bundled
)

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot

if (-not $ApiHost) {
  # Prefer the real Wi-Fi / Ethernet adapter. Skip VMware, WSL, VPN and
  # virtual adapters, which often have a lower sort order.
  $candidate = Get-NetIPAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue |
    Where-Object {
      $_.IPAddress -notlike "127.*" -and
      $_.IPAddress -notlike "169.254.*" -and
      $_.IPAddress -notlike "172.*" -and
      $_.IPAddress -notlike "198.18.*" -and
      $_.InterfaceAlias -notmatch "VMware|vEthernet|WSL|Hyper-V|Loopback|Virtual|VPN|TAP|yepfast"
    } |
    Sort-Object @{
      Expression = {
        if ($_.InterfaceAlias -match "WLAN|Wi-Fi|Wireless") { 0 }
        elseif ($_.InterfaceAlias -match "Ethernet") { 1 }
        else { 2 }
      }
    }, InterfaceAlias |
    Select-Object -First 1
  if (-not $candidate) { throw "No LAN IPv4 found. Pass -ApiHost explicitly." }
  $ApiHost = $candidate.IPAddress
}

$jdk = Get-ChildItem "C:\Program Files\Eclipse Adoptium" -Directory -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "jdk-21*" } |
  Select-Object -First 1
if (-not $jdk) { throw "JDK 21 not found under C:\Program Files\Eclipse Adoptium. Install Temurin 21." }

$env:JAVA_HOME = $jdk.FullName
$env:Path = "$env:JAVA_HOME\bin;$env:Path"
$env:NODE_OPTIONS = "--max-old-space-size=4096"

if ($Bundled) {
  # Bundle dist/ inside the APK. API requests go directly to the LAN host and
  # use an Authorization token (cross-site cookies are unreliable in WebView).
  Remove-Item Env:CAP_SERVER_URL -ErrorAction SilentlyContinue
  $env:VITE_API_BASE_URL = "http://${ApiHost}:8002/api/v1"
  $env:CAP_ANDROID_SCHEME = "https"
  Write-Host "Mode: bundled frontend + remote API"
  Write-Host "API base: $env:VITE_API_BASE_URL"
} else {
  $env:CAP_SERVER_URL = "http://${ApiHost}:8002"
  Remove-Item Env:VITE_API_BASE_URL -ErrorAction SilentlyContinue
  Write-Host "Mode: remote frontend (API-served SPA)"
  Write-Host "WebView URL: $env:CAP_SERVER_URL"
}

Write-Host "API host: $ApiHost"
Write-Host "JDK: $env:JAVA_HOME"

Push-Location (Join-Path $repo "apps\web")
try {
  npm run build
  npx cap sync android
  Push-Location "android"
  try {
    .\gradlew.bat assembleDebug --no-daemon
  } finally {
    Pop-Location
  }
} finally {
  Pop-Location
}

$apk = Join-Path $repo "apps\web\android\app\build\outputs\apk\debug\app-debug.apk"
Write-Host ""
Write-Host "APK: $apk"
Write-Host "Backend must be reachable from the phone:"
Write-Host "  uvicorn app.main:app --host 0.0.0.0 --port 8002"
Write-Host "Then install with: adb install -r `"$apk`""
