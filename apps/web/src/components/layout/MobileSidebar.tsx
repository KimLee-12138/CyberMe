import { useEffect } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { X } from 'lucide-react'
import { useAuthStore } from '../../stores/authStore'
import { NAV_GROUPS } from '../../lib/nav'
import Icon from '../ui/Icon'
import { confirm } from '../ui/ConfirmDialog'
import { cn } from '../../lib/utils'

interface Props {
  open: boolean
  onClose: () => void
}

export default function MobileSidebar({ open, onClose }: Props) {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()
  const location = useLocation()

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') onClose()
    }
    if (open) {
      document.body.style.overflow = 'hidden'
      document.addEventListener('keydown', onKey)
    } else {
      document.body.style.overflow = ''
    }
    return () => {
      document.body.style.overflow = ''
      document.removeEventListener('keydown', onKey)
    }
  }, [open, onClose])

  if (!open) return null

  const handleNav = (to: string) => {
    navigate(to)
    onClose()
  }

  const handleLogout = async () => {
    const ok = await confirm({
      title: '退出 CyberMe？',
      message: '本机保存的登录态会被清除，下次需要重新登录。',
      confirmLabel: '退出登录',
      danger: true,
    })
    if (!ok) return
    await logout()
    onClose()
    navigate('/login', { replace: true })
  }

  return (
    <div className="fixed inset-0 z-[120] flex md:hidden" onClick={onClose}>
      <div className="absolute inset-0 bg-[#071a33]/45 backdrop-blur-[2px]" />
      <aside
        className="app-pop-in relative z-10 flex h-full w-[292px] flex-col overflow-hidden bg-[#071A33] text-white shadow-2xl"
        onClick={(event) => event.stopPropagation()}
      >
        <div className="pointer-events-none absolute -left-24 top-[-6%] h-64 w-64 rounded-full bg-[#2563EB]/25 blur-3xl" />

        <div className="relative flex h-[76px] shrink-0 items-center gap-3 px-4">
          <img src="/app-icon.png" alt="CyberMe" className="h-10 w-10 rounded-[13px] object-cover ring-1 ring-white/20" />
          <div className="min-w-0 flex-1">
            <p className="text-[15px] font-bold tracking-[-0.02em]">CyberMe</p>
            <p className="mt-0.5 text-[9px] font-medium tracking-[0.18em] text-white/40">LEARNING OS</p>
          </div>
          <button onClick={onClose} className="rounded-xl p-2 text-white/50 hover:bg-white/10 hover:text-white" aria-label="关闭菜单">
            <X size={18} />
          </button>
        </div>

        <nav className="relative flex-1 overflow-y-auto px-3 py-2">
          {NAV_GROUPS.map((group) => (
            <div key={group.label} className="mb-4">
              <p className="mb-1.5 px-3 text-[8px] font-bold uppercase tracking-[0.2em] text-white/35">{group.label}</p>
              <div className="space-y-0.5">
                {group.items.map((item) => {
                  const active = item.to === '/' ? location.pathname === '/' : location.pathname.startsWith(item.to)
                  return (
                    <button
                      key={item.to}
                      onClick={() => handleNav(item.to)}
                      className={cn(
                        'flex min-h-10 w-full items-center gap-3 rounded-xl px-3 py-2 text-left text-[13px] transition-colors',
                        active ? 'bg-white/[0.09] font-semibold text-white' : 'text-white/55 hover:bg-white/[0.05] hover:text-white/90',
                      )}
                    >
                      <Icon name={item.icon} size={18} className={active ? 'text-[#8bb3ff]' : 'text-white/40'} />
                      <span>{item.label}</span>
                    </button>
                  )
                })}
              </div>
            </div>
          ))}
        </nav>

        <div className="relative shrink-0 border-t border-white/10 p-3">
          {user && (
            <div className="flex items-center gap-2.5 rounded-xl bg-white/[0.06] px-3 py-2.5">
              <span className="flex h-8 w-8 items-center justify-center rounded-full bg-gradient-to-br from-[#4F8BFF] to-[#2563EB] text-xs font-bold">
                {user.username.slice(0, 1).toUpperCase()}
              </span>
              <div className="min-w-0 flex-1">
                <p className="truncate text-xs font-semibold">{user.username}</p>
                <p className="mt-0.5 text-[10px] text-emerald-300/80">本地会话</p>
              </div>
              <button onClick={handleLogout} className="rounded-lg p-1.5 text-white/40 hover:bg-white/10 hover:text-white" aria-label="退出登录">
                <Icon name="logout" size={15} />
              </button>
            </div>
          )}
        </div>
      </aside>
    </div>
  )
}
