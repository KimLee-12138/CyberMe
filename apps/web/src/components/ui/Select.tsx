import { useEffect, useId, useRef, useState } from 'react'
import { Check, ChevronDown } from 'lucide-react'
import { cn } from '../../lib/utils'

export interface SelectOption {
  value: string
  label: string
  hint?: string
}

interface SelectProps {
  value: string
  options: SelectOption[]
  onChange: (value: string) => void
  placeholder?: string
  ariaLabel?: string
  className?: string
  buttonClassName?: string
  menuClassName?: string
  size?: 'sm' | 'md'
  disabled?: boolean
}

export default function Select({
  value,
  options,
  onChange,
  placeholder = '请选择',
  ariaLabel,
  className,
  buttonClassName,
  menuClassName,
  size = 'md',
  disabled = false,
}: SelectProps) {
  const [open, setOpen] = useState(false)
  const [activeIndex, setActiveIndex] = useState(-1)
  const rootRef = useRef<HTMLDivElement>(null)
  const buttonRef = useRef<HTMLButtonElement>(null)
  const listId = useId()
  const selected = options.find((option) => option.value === value)

  useEffect(() => {
    if (!open) return
    const onPointerDown = (event: MouseEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) setOpen(false)
    }
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setOpen(false)
        buttonRef.current?.focus()
      }
    }
    document.addEventListener('mousedown', onPointerDown)
    document.addEventListener('keydown', onKey)
    return () => {
      document.removeEventListener('mousedown', onPointerDown)
      document.removeEventListener('keydown', onKey)
    }
  }, [open])

  useEffect(() => {
    if (!open) setActiveIndex(-1)
  }, [open])

  const choose = (option: SelectOption) => {
    onChange(option.value)
    setOpen(false)
    buttonRef.current?.focus()
  }

  const onButtonKeyDown = (event: React.KeyboardEvent) => {
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      event.preventDefault()
      if (!open) {
        setOpen(true)
        setActiveIndex(0)
        return
      }
      setActiveIndex((index) => {
        const next = event.key === 'ArrowDown' ? index + 1 : index - 1
        return (next + options.length) % options.length
      })
    } else if (event.key === 'Enter' || event.key === ' ') {
      if (!open) {
        event.preventDefault()
        setOpen(true)
        setActiveIndex(Math.max(0, options.findIndex((o) => o.value === value)))
      } else if (activeIndex >= 0 && options[activeIndex]) {
        event.preventDefault()
        choose(options[activeIndex])
      }
    }
  }

  return (
    <div ref={rootRef} className={cn('relative', className)}>
      <button
        ref={buttonRef}
        type="button"
        disabled={disabled}
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-controls={listId}
        aria-label={ariaLabel}
        onClick={() => setOpen((next) => !next)}
        onKeyDown={onButtonKeyDown}
        className={cn(
          'flex w-full items-center justify-between gap-3 rounded-xl border border-border bg-white text-left text-foreground shadow-[0_1px_1px_rgba(15,31,58,0.02)] transition-colors hover:border-[#c7d8ee] focus:border-[#6ea0ff] focus:outline-none focus:ring-4 focus:ring-[#2563eb]/10 disabled:cursor-not-allowed disabled:opacity-50',
          size === 'sm' ? 'min-h-9 px-3 text-xs' : 'min-h-11 px-3.5 text-sm',
          open && 'border-[#8bb3ff] ring-4 ring-[#2563eb]/10',
          buttonClassName,
        )}
      >
        <span className={cn('truncate', !selected && 'text-muted-foreground')}>
          {selected?.label || placeholder}
        </span>
        <ChevronDown
          size={size === 'sm' ? 14 : 16}
          className={cn('shrink-0 text-muted-foreground transition-transform duration-200', open && 'rotate-180')}
        />
      </button>

      {open && (
        <div
          id={listId}
          role="listbox"
          aria-label={ariaLabel}
          className={cn(
            'app-pop-in absolute left-0 right-0 top-[calc(100%+6px)] z-[80] max-h-72 overflow-y-auto rounded-xl border border-border bg-white p-1.5 shadow-[0_22px_55px_-20px_rgba(15,31,58,0.4)]',
            menuClassName,
          )}
        >
          {options.map((option, index) => {
            const isSelected = option.value === value
            return (
              <button
                key={option.value}
                type="button"
                role="option"
                aria-selected={isSelected}
                onMouseEnter={() => setActiveIndex(index)}
                onClick={() => choose(option)}
                className={cn(
                  'flex w-full items-start gap-2.5 rounded-lg px-3 py-2 text-left text-sm transition-colors',
                  activeIndex === index ? 'bg-[#f2f6ff] text-primary' : 'text-foreground hover:bg-[#f7f9fd]',
                  isSelected && 'font-semibold',
                )}
              >
                <span className="min-w-0 flex-1">
                  <span className="block truncate">{option.label}</span>
                  {option.hint && (
                    <span className="mt-0.5 block truncate text-[11px] font-normal text-muted-foreground">
                      {option.hint}
                    </span>
                  )}
                </span>
                {isSelected && <Check size={15} className="mt-0.5 shrink-0 text-accent" />}
              </button>
            )
          })}
          {options.length === 0 && (
            <p className="px-3 py-3 text-sm text-muted-foreground">没有可选项</p>
          )}
        </div>
      )}
    </div>
  )
}
