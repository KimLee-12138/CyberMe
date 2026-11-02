import type { CapacitorConfig } from '@capacitor/cli'

/**
 * Local/Android builds:
 *   1. Build the web assets:      npm run build
 *   2. Point the WebView at the API host that also serves dist/:
 *        $env:CAP_SERVER_URL='http://192.168.31.244:8002'
 *        npm run cap:sync
 *        npm run android:debug
 *
 * The API serves apps/web/dist at /, so the WebView and /api/v1 are
 * same-origin: the HttpOnly session cookie works without cross-site tricks.
 *
 * For a production HTTPS deployment, set CAP_SERVER_URL to that origin.
 * Leaving CAP_SERVER_URL unset uses bundled assets; in that mode
 * VITE_API_BASE_URL must be an absolute HTTPS API origin (and cookie auth
 * needs HTTPS/SameSite changes).
 */
const serverUrl = process.env.CAP_SERVER_URL?.trim()

const config: CapacitorConfig = {
  appId: 'com.cyberme.os',
  appName: 'CyberMe',
  webDir: 'dist',

  android: {
    allowMixedContent: true,
    backgroundColor: '#ffffff',
  },

  ...(serverUrl
    ? {
        server: {
          url: serverUrl,
          cleartext: serverUrl.startsWith('http://'),
        },
      }
    : {
        server: {
          androidScheme: process.env.CAP_ANDROID_SCHEME === 'http' ? 'http' : 'https',
        },
      }),
}

export default config
