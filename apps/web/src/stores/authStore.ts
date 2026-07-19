import { create } from 'zustand'
import * as authApi from '../api/auth'

interface User {
  id: string
  username: string
}

interface AuthState {
  isAuthenticated: boolean
  user: User | null
  isLoading: boolean

  checkSession: () => Promise<void>
  login: (username: string, password: string) => Promise<{ status: string; tempToken?: string }>
  verifyTotp: (tempToken: string, code: string) => Promise<void>
  logout: () => Promise<void>
}

export const useAuthStore = create<AuthState>((set) => ({
  isAuthenticated: false,
  user: null,
  isLoading: true,

  checkSession: async () => {
    try {
      const session = await authApi.getSession()
      if (session.authenticated && session.user) {
        set({ isAuthenticated: true, user: session.user, isLoading: false })
      } else {
        set({ isAuthenticated: false, user: null, isLoading: false })
      }
    } catch {
      set({ isAuthenticated: false, user: null, isLoading: false })
    }
  },

  login: async (username: string, password: string) => {
    const result = await authApi.login(username, password)
    if (result.status === 'authenticated' && result.user) {
      set({ isAuthenticated: true, user: result.user, isLoading: false })
      return { status: 'authenticated' }
    }
    return { status: result.status, tempToken: result.temp_token }
  },

  verifyTotp: async (tempToken: string, code: string) => {
    const result = await authApi.verifyTotp(tempToken, code)
    if (result.status === 'authenticated' && result.user) {
      set({ isAuthenticated: true, user: result.user, isLoading: false })
    }
  },

  logout: async () => {
    try {
      await authApi.logout()
    } catch {
      // Ignore errors on logout
    }
    set({ isAuthenticated: false, user: null, isLoading: false })
  },
}))
