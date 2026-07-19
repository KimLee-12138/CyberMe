interface Props {
  message?: string
  lines?: number
}

export default function LoadingState({ message = '加载中...', lines = 3 }: Props) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4">
      <div className="w-full max-w-sm space-y-3">
        {Array.from({ length: lines }).map((_, i) => (
          <div
            key={i}
            className="h-4 animate-pulse rounded bg-muted"
            style={{ width: `${100 - i * 15}%` }}
          />
        ))}
      </div>
      <p className="mt-6 text-sm text-muted-foreground">{message}</p>
    </div>
  )
}
