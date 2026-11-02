import { create } from 'zustand'
import { AlertTriangle } from 'lucide-react'

interface ConfirmOptions {
  title: string
  message?: string
  confirmLabel?: string
  cancelLabel?: string
  danger?: boolean
}

interface ConfirmState {
  open: boolean
  options: ConfirmOptions
  resolve: ((ok: boolean) => void) | null
  request: (options: ConfirmOptions) => Promise<boolean>
  close: (ok: boolean) => void
}

const useConfirmStore = create<ConfirmState>((set, get) => ({
  open: false,
  options: { title: '' },
  resolve: null,
  request: (options) =>
    new Promise<boolean>((resolve) => {
      set({ open: true, options, resolve })
    }),
  close: (ok) => {
    get().resolve?.(ok)
    set({ open: false, resolve: null })
  },
}))

export function confirm(options: ConfirmOptions): Promise<boolean> {
  return useConfirmStore.getState().request(options)
}

export function ConfirmHost() {
  const { open, options, close } = useConfirmStore()
  if (!open) return null

  return (
    <div
      className="fixed inset-0 z-[300] flex items-end justify-center bg-[#071a33]/45 p-0 backdrop-blur-[3px] sm:items-center sm:p-4"
      onClick={() => close(false)}
      role="dialog"
      aria-modal="true"
      aria-label={options.title}
    >
      <div
        className="app-pop-in w-full max-w-sm rounded-t-[24px] border border-border bg-white p-5 shadow-2xl sm:rounded-[22px] sm:p-6"
        onClick={(event) => event.stopPropagation()}
      >
        <div className="flex items-start gap-3">
          <span
            className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl ${
              options.danger ? 'bg-[#fff1f1] text-[#e5484d]' : 'bg-[#eef4ff] text-[#2563eb]'
            }`}
          >
            <AlertTriangle size={18} />
          </span>
          <div className="min-w-0 pt-0.5">
            <h3 className="text-base font-semibold text-foreground">{options.title}</h3>
            {options.message && (
              <p className="mt-1.5 text-sm leading-6 text-muted-foreground">{options.message}</p>
            )}
          </div>
        </div>
        <div className="mt-6 flex gap-2">
          <button
            type="button"
            onClick={() => close(false)}
            className="app-button app-button-secondary flex-1"
          >
            {options.cancelLabel || '取消'}
          </button>
          <button
            type="button"
            onClick={() => close(true)}
            className={`app-button flex-1 ${
              options.danger
                ? 'bg-[#e5484d] text-white hover:bg-[#d6393e]'
                : 'app-button-primary'
            }`}
          >
            {options.confirmLabel || '确认'}
          </button>
        </div>
      </div>
    </div>
  )
}
