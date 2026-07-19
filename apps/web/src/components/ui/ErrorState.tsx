interface Props {
  message?: string
  onRetry?: () => void
}

export default function ErrorState({ message = '加载失败，请稍后重试', onRetry }: Props) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4">
      <span className="text-4xl">⚠️</span>
      <p className="mt-4 text-sm text-muted-foreground">{message}</p>
      {onRetry && (
        <button
          onClick={onRetry}
          className="mt-4 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 transition-colors"
        >
          重新加载
        </button>
      )}
    </div>
  )
}
