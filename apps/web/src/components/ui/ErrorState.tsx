import { AlertTriangle } from 'lucide-react'

interface Props {
  message?: string
  onRetry?: () => void
}

export default function ErrorState({ message = '加载失败，请稍后重试', onRetry }: Props) {
  return (
    <div className="flex flex-col items-center justify-center px-4 py-16">
      <span className="flex h-12 w-12 items-center justify-center rounded-2xl bg-[#fff1f1] text-[#e5484d]">
        <AlertTriangle size={22} />
      </span>
      <p className="mt-4 text-sm text-muted-foreground">{message}</p>
      {onRetry && (
        <button onClick={onRetry} className="app-button app-button-primary mt-4 !min-h-9 !text-xs">
          重新加载
        </button>
      )}
    </div>
  )
}
