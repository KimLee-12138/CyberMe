import { api } from './client'

interface LoginResponse {
  status: 'authenticated' | 'totp_required'
  user?: { id: string; username: string }
  refresh_token?: string
  temp_token?: string
}

interface SessionResponse {
  user: { id: string; username: string } | null
  authenticated: boolean
}

export async function login(
  username: string,
  password: string,
): Promise<LoginResponse> {
  return api.post<LoginResponse>('/auth/login', { username, password })
}

export async function verifyTotp(
  tempToken: string,
  code: string,
): Promise<LoginResponse> {
  return api.post<LoginResponse>('/auth/totp/verify', {
    temp_token: tempToken,
    code,
  })
}

export async function logout(): Promise<void> {
  return api.post('/auth/logout')
}

export async function getSession(): Promise<SessionResponse> {
  return api.get<SessionResponse>('/auth/session')
}

export async function refreshSession(
  refreshToken: string,
): Promise<{ status: string }> {
  return api.post('/auth/refresh', { refresh_token: refreshToken })
}
