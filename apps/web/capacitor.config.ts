import type { CapacitorConfig } from '@capacitor/cli'

const config: CapacitorConfig = {
  appId: 'com.cyberme.os',
  appName: 'CyberMe',
  webDir: 'dist',

  // Android-specific
  android: {
    allowMixedContent: true,
    backgroundColor: '#ffffff',
  },

  // Server config — in production, point to your VPS
  server: {
    // Uncomment for production:
    // url: 'https://cyberme.example.com',
    // cleartext: false,

    // For local WiFi testing (update IP to your LAN IP):
    url: 'http://192.168.10.244:3000',
    cleartext: true,
  },
}

export default config
