import { useState, useCallback } from 'react'

interface ConfirmOptions {
  title: string
  message?: string
  confirmLabel?: string
  danger?: boolean
}

let confirmHandler: ((ok: boolean) => void) | null = null

export function useConfirm() {
  const [open, setOpen] = useState(false)
  const [opts, setOpts] = useState<ConfirmOptions>({ title: '' })

  const confirm = useCallback((options: ConfirmOptions): Promise<boolean> => {
    return new Promise((resolve) => {
      setOpts(options)
      setOpen(true)
      confirmHandler = (ok: boolean) => {
        setOpen(false)
        confirmHandler = null
        resolve(ok)
      }
    })
  }, [])

  const handleClose = useCallback((ok: boolean) => {
    confirmHandler?.(ok)
  }, [])

  const DialogComponent = open ? (
    <div className="fixed inset-0 z-[200] flex items-center justify-center px-4" onClick={() => handleClose(false)}>
      <div className="absolute inset-0 bg-black/40" />
      <div
        className="relative z-10 w-full max-w-sm rounded-2xl bg-background p-6 shadow-xl border border-border"
        onClick={(e) => e.stopPropagation()}
      >
        <h3 className="text-base font-semibold text-foreground">{opts.title}</h3>
        {opts.message && (
          <p className="mt-2 text-sm text-muted-foreground">{opts.message}</p>
        )}
        <div className="mt-5 flex justify-end gap-2">
          <button
            onClick={() => handleClose(false)}
            className="rounded-lg border border-border px-4 py-2 text-sm text-foreground hover:bg-secondary transition-colors"
          >
            取消
          </button>
          <button
            onClick={() => handleClose(true)}
            className={`rounded-lg px-4 py-2 text-sm font-medium text-white transition-colors ${
              opts.danger ? 'bg-red-600 hover:bg-red-700' : 'bg-primary hover:bg-primary/90'
            }`}
          >
            {opts.confirmLabel || '确认'}
          </button>
        </div>
      </div>
    </div>
  ) : null

  return { confirm, ConfirmDialog: DialogComponent }
}
