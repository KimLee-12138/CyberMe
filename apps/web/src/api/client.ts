const BASE_URL = '/api/v1'

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

export { ApiError }
