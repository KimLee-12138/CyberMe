import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../../stores/authStore'
import Icon from '../ui/Icon'

const navItems = [
  { to: '/', label: '驾驶舱', icon: 'house' as const },
  { to: '/ask', label: '问答', icon: 'chat' as const },
  { to: '/learn', label: '学习', icon: 'learn' as const },
  { to: '/review', label: '复习', icon: 'review' as const },
  { to: '/courses', label: '课程', icon: 'courses' as const },
  { to: '/graph', label: '图谱', icon: 'graph' as const },
  { to: '/projects', label: '项目', icon: 'projects' as const },
  { to: '/write', label: '写作', icon: 'write' as const },
  { to: '/decisions', label: '决策', icon: 'decisions' as const },
  { to: '/self', label: '个人', icon: 'self' as const },
  { to: '/evaluations', label: '评测', icon: 'evaluations' as const },
  { to: '/sync', label: '同步', icon: 'sync' as const },
  { to: '/settings', label: '设置', icon: 'settings' as const },
]

interface Props {
  open: boolean
  onClose: () => void
}

export default function MobileSidebar({ open, onClose }: Props) {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose() }
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
    if (!window.confirm('确定要退出登录吗？')) return
    await logout()
    onClose()
    navigate('/login', { replace: true })
  }

  return (
    <div className="fixed inset-0 z-50 flex md:hidden" onClick={onClose}>
      {/* Backdrop */}
      <div className="absolute inset-0 bg-black/40" />

      {/* Drawer */}
      <aside
        className="relative z-10 flex h-full w-64 flex-col bg-background border-r border-border shadow-xl"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Logo + Close */}
        <div className="flex h-14 shrink-0 items-center gap-2.5 border-b border-border px-4">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary">
            <Icon name="brain" size={18} weight="fill" className="text-primary-foreground" />
          </div>
          <span className="flex-1 text-sm font-semibold tracking-tight text-foreground">CyberMe OS</span>
          <button
            onClick={onClose}
            className="rounded-md p-1.5 text-muted-foreground hover:bg-muted hover:text-foreground transition-colors"
            aria-label="关闭菜单"
          >
            <Icon name="x" size={18} />
          </button>
        </div>

        {/* Navigation */}
        <nav className="flex-1 overflow-y-auto py-2">
          {navItems.map((item) => (
            <button
              key={item.to}
              onClick={() => handleNav(item.to)}
              className="mx-2 flex w-[calc(100%-16px)] items-center gap-3 rounded-lg px-3 py-3 text-sm text-muted-foreground transition-colors hover:bg-muted hover:text-foreground"
            >
              <Icon name={item.icon} size={20} weight="regular" className="shrink-0" />
              <span>{item.label}</span>
            </button>
          ))}
        </nav>

        {/* Footer */}
        <div className="shrink-0 border-t border-border p-3 space-y-2">
          {user && (
            <div className="flex items-center gap-2 rounded-lg bg-secondary px-3 py-2">
              <span className="flex h-7 w-7 items-center justify-center rounded-full bg-primary/10 text-xs font-semibold text-primary">
                {user.username.slice(0, 1).toUpperCase()}
              </span>
              <div className="flex-1 min-w-0">
                <p className="text-xs font-medium text-foreground truncate">{user.username}</p>
              </div>
              <button
                onClick={handleLogout}
                className="text-muted-foreground hover:text-foreground transition-colors"
                title="退出登录"
              >
                <Icon name="logout" size={16} />
              </button>
            </div>
          )}
          <div className="flex items-center gap-2 px-1 text-xs text-muted-foreground">
            <span className="h-2 w-2 rounded-full bg-emerald-500" />
            <span>系统运行中</span>
          </div>
        </div>
      </aside>
    </div>
  )
}
