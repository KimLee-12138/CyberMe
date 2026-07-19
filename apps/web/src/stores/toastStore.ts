import { create } from 'zustand'

export type ToastType = 'success' | 'error' | 'info'

export interface Toast {
  id: string
  type: ToastType
  message: string
}

interface ToastState {
  toasts: Toast[]
  add: (type: ToastType, message: string) => void
  remove: (id: string) => void
}

let counter = 0

export const useToastStore = create<ToastState>((set) => ({
  toasts: [],
  add: (type, message) => {
    const id = String(++counter)
    set((s) => ({ toasts: [...s.toasts.slice(-2), { id, type, message }] }))
    setTimeout(() => {
      set((s) => ({ toasts: s.toasts.filter((t) => t.id !== id) }))
    }, 3000)
  },
  remove: (id) => {
    set((s) => ({ toasts: s.toasts.filter((t) => t.id !== id) }))
  },
}))

/** Convenience functions usable outside React components */
export const toast = {
  success: (msg: string) => useToastStore.getState().add('success', msg),
  error: (msg: string) => useToastStore.getState().add('error', msg),
  info: (msg: string) => useToastStore.getState().add('info', msg),
}
