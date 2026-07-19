interface Props {
  icon?: string
  title?: string
  description?: string
  action?: {
    label: string
    onClick: () => void
  }
}

export default function EmptyState({
  icon = '📭',
  title = '暂无数据',
  description,
  action,
}: Props) {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4">
      <span className="text-4xl">{icon}</span>
      <p className="mt-4 text-sm font-medium text-foreground">{title}</p>
      {description && (
        <p className="mt-1 text-sm text-muted-foreground">{description}</p>
      )}
      {action && (
        <button
          onClick={action.onClick}
          className="mt-4 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 transition-colors"
        >
          {action.label}
        </button>
      )}
    </div>
  )
}
