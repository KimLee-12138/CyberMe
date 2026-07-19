import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg'],
      manifest: {
        name: 'CyberMe OS — 个人学习操作系统',
        short_name: 'CyberMe',
        description: '围绕个人长期学习建立的认知操作系统',
        theme_color: '#2563eb',
        background_color: '#ffffff',
        display: 'standalone',
        orientation: 'any',
        start_url: '/',
        scope: '/',
        lang: 'zh-CN',
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'any maskable',
          },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,svg,png,woff2}'],
        runtimeCaching: [
          {
            urlPattern: /^\/api\/v1\/auth\/session/,
            handler: 'NetworkFirst',
            options: {
              cacheName: 'api-auth',
              expiration: { maxEntries: 1, maxAgeSeconds: 300 },
            },
          },
          {
            urlPattern: /^\/api\/v1\/courses/,
            handler: 'NetworkFirst',
            options: {
              cacheName: 'api-courses',
              expiration: { maxEntries: 50, maxAgeSeconds: 3600 },
            },
          },
          {
            urlPattern: /^\/api\/v1\/knowledge/,
            handler: 'NetworkFirst',
            options: {
              cacheName: 'api-knowledge',
              expiration: { maxEntries: 200, maxAgeSeconds: 86400 },
            },
          },
          {
            urlPattern: /^\/api\/v1\/reviews\/due/,
            handler: 'NetworkFirst',
            options: {
              cacheName: 'api-reviews',
              expiration: { maxEntries: 50, maxAgeSeconds: 1800 },
            },
          },
        ],
      },
    }),
  ],
  resolve: {
    dedupe: ['react', 'react-dom'],
  },
  optimizeDeps: {
    include: ['react-force-graph-2d'],
  },
  server: {
    port: 3000,
    host: '0.0.0.0',
    proxy: {
      '/api': {
        target: 'http://localhost:8002',
        changeOrigin: true,
      },
      '/ws': {
        target: 'ws://localhost:8000',
        ws: true,
      },
    },
  },
})
