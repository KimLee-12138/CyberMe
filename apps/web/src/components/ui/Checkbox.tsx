import { Check } from 'lucide-react'
import { cn } from '../../lib/utils'

interface CheckboxProps {
  checked: boolean
  onChange: (checked: boolean) => void
  label?: string
  description?: string
  disabled?: boolean
  className?: string
}

export default function Checkbox({
  checked,
  onChange,
  label,
  description,
  disabled = false,
  className,
}: CheckboxProps) {
  return (
    <div
      className={cn(
        'group inline-flex min-h-10 cursor-pointer items-center gap-2.5 select-none',
        disabled && 'cursor-not-allowed opacity-50',
        className,
      )}
      onClick={() => {
        if (!disabled) onChange(!checked)
      }}
    >
      <button
        type="button"
        role="checkbox"
        aria-checked={checked}
        aria-label={label}
        disabled={disabled}
        onClick={(event) => {
          event.stopPropagation()
          onChange(!checked)
        }}
        className={cn(
          'flex h-5 w-5 shrink-0 items-center justify-center rounded-[6px] border transition-all duration-150',
          checked
            ? 'border-accent bg-accent text-white shadow-[0_4px_10px_-4px_rgba(37,99,235,0.6)]'
            : 'border-[#cbd5e1] bg-white text-transparent hover:border-[#8bb3ff]',
        )}
      >
        <Check size={13} strokeWidth={3} className={cn('transition-transform duration-150', checked ? 'scale-100' : 'scale-75')} />
      </button>
      {(label || description) && (
        <span className="min-w-0">
          {label && <span className="block text-xs font-medium text-foreground">{label}</span>}
          {description && <span className="block text-[11px] text-muted-foreground">{description}</span>}
        </span>
      )}
    </div>
  )
}
