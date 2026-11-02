import { Capacitor } from '@capacitor/core'
import { Directory, Filesystem } from '@capacitor/filesystem'
import { Share } from '@capacitor/share'
import { getAuthToken } from '../lib/authToken'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1'
const NATIVE = Capacitor.isNativePlatform()

function authHeaders(): Record<string, string> {
  const token = getAuthToken()
  return token ? { Authorization: `Bearer ${token}` } : {}
}

interface RequestOptions extends RequestInit {
  params?: Record<string, string | undefined>
}

class ApiError extends Error {
  status: number
  code: string
  meta?: Record<string, unknown>

  constructor(status: number, code: string, message: string, meta?: Record<string, unknown>) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.code = code
    this.meta = meta
  }
}

async function request<T = unknown>(endpoint: string, options: RequestOptions = {}): Promise<T> {
  const { params, ...init } = options

  // Build URL with query params
  let url = `${BASE_URL}${endpoint}`
  if (params) {
    const searchParams = new URLSearchParams()
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined) searchParams.set(key, value)
    })
    const qs = searchParams.toString()
    if (qs) url += `?${qs}`
  }

  const response = await fetch(url, {
    ...init,
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      ...(NATIVE ? { 'X-CyberMe-Client': 'native' } : {}),
      ...authHeaders(),
      ...init.headers,
    },
  })

  if (!response.ok) {
    let errorData: { code?: string; detail?: string; meta?: Record<string, unknown> } = {}
    try {
      errorData = await response.json()
    } catch {
      // Response is not JSON
    }
    throw new ApiError(
      response.status,
      errorData.code || 'UNKNOWN_ERROR',
      errorData.detail || response.statusText,
      errorData.meta,
    )
  }

  // Handle 204 No Content
  if (response.status === 204) return undefined as T

  return response.json()
}

export const api = {
  get: <T = unknown>(endpoint: string, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'GET' }),

  post: <T = unknown>(endpoint: string, body?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, {
      ...options,
      method: 'POST',
      body: body ? JSON.stringify(body) : undefined,
    }),

  patch: <T = unknown>(endpoint: string, body?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, {
      ...options,
      method: 'PATCH',
      body: body ? JSON.stringify(body) : undefined,
    }),

  delete: <T = unknown>(endpoint: string, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'DELETE' }),
}

export async function download(endpoint: string, filename: string): Promise<void> {
  const response = await fetch(`${BASE_URL}${endpoint}`, {
    credentials: 'include',
    headers: {
      ...(NATIVE ? { 'X-CyberMe-Client': 'native' } : {}),
      ...authHeaders(),
    },
  })
  if (!response.ok) {
    let message = response.statusText
    try {
      const body = await response.json()
      message = body.detail || body.message || message
    } catch {
      // not JSON
    }
    throw new Error(message || '下载失败')
  }
  const blob = await response.blob()
  if (Capacitor.isNativePlatform()) {
    const base64 = await new Promise<string>((resolve, reject) => {
      const reader = new FileReader()
      reader.onload = () => {
        const value = String(reader.result || '')
        resolve(value.includes(',') ? value.split(',')[1] : value)
      }
      reader.onerror = () => reject(new Error('读取 PDF 失败'))
      reader.readAsDataURL(blob)
    })
    const path = `CyberMe/${filename}`
    const saved = await Filesystem.writeFile({
      path,
      data: base64,
      directory: Directory.Documents,
      recursive: true,
    })
    try {
      await Share.share({
        title: filename,
        url: saved.uri,
        dialogTitle: '导出课件 PDF',
      })
    } catch {
      // The file is already saved even if the user dismisses the share sheet.
    }
    return
  }

  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  document.body.appendChild(a)
  a.click()
  a.remove()
  window.setTimeout(() => URL.revokeObjectURL(url), 60_000)
}

export { ApiError }
