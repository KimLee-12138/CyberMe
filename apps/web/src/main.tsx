import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import App from './App'
import './index.css'

// PWA — register service worker for offline support
import { registerSW } from 'virtual:pwa-register'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5,
      retry: 1,
    },
  },
})

// Register service worker with auto-update
registerSW({
  onNeedRefresh() {
    // A new version is available — could show a toast to the user
    console.log('[PWA] New content available')
  },
  onOfflineReady() {
    console.log('[PWA] App ready for offline use')
  },
})

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </QueryClientProvider>
  </StrictMode>,
)
