const KEY = 'cyberme_session_token'

export function getAuthToken(): string {
  try {
    return localStorage.getItem(KEY) || ''
  } catch {
    return ''
  }
}

export function setAuthToken(token: string | undefined): void {
  try {
    if (token) localStorage.setItem(KEY, token)
    else localStorage.removeItem(KEY)
  } catch {
    // Storage can be unavailable in private webviews.
  }
}

export function clearAuthToken(): void {
  setAuthToken(undefined)
}
