import { useToastStore, type ToastType } from '../../stores/toastStore'

const ICONS: Record<ToastType, string> = {
  success: '✓',
  error: '✗',
  info: 'ℹ',
}

const BG: Record<ToastType, string> = {
  success: 'border-emerald-300 bg-emerald-50 text-emerald-800',
  error: 'border-red-300 bg-red-50 text-red-800',
  info: 'border-blue-300 bg-blue-50 text-blue-800',
}

export default function ToastContainer() {
  const toasts = useToastStore((s) => s.toasts)
  const remove = useToastStore((s) => s.remove)

  if (toasts.length === 0) return null

  return (
    <div className="fixed top-4 right-4 z-[100] flex flex-col gap-2 w-72">
      {toasts.map((t) => (
        <div
          key={t.id}
          className={`flex items-start gap-2 rounded-lg border px-3 py-2.5 text-sm shadow-md animate-in slide-in-from-right ${BG[t.type]}`}
          onClick={() => remove(t.id)}
        >
          <span className="mt-0.5 font-bold text-base leading-none">{ICONS[t.type]}</span>
          <span className="flex-1">{t.message}</span>
          <button className="ml-1 opacity-50 hover:opacity-100 text-sm leading-none" onClick={() => remove(t.id)}>
            ×
          </button>
        </div>
      ))}
    </div>
  )
}
