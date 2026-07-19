import { NavLink, useNavigate } from 'react-router-dom'
import { cn } from '../../lib/utils'
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
  { to: '/distill', label: '蒸馏', icon: 'evaluations' as const },
  { to: '/settings', label: '设置', icon: 'settings' as const },
]

export default function Sidebar() {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()

  const handleLogout = async () => {
    if (!window.confirm('确定要退出登录吗？')) return
    await logout()
    navigate('/login', { replace: true })
  }

  return (
    <aside className="hidden w-56 flex-shrink-0 border-r border-border bg-card md:flex md:flex-col">
      {/* Logo */}
      <div className="flex h-14 items-center gap-2.5 border-b border-border px-4">
        <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary">
          <Icon name="brain" size={18} weight="fill" className="text-primary-foreground" />
        </div>
        <span className="text-sm font-semibold tracking-tight text-foreground">CyberMe OS</span>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto py-2">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              cn(
                'mx-2 flex items-center gap-3 rounded-lg px-3 py-2 text-sm transition-all duration-150',
                isActive
                  ? 'bg-primary/10 font-medium text-primary'
                  : 'text-muted-foreground hover:bg-muted hover:text-foreground',
              )
            }
          >
            <Icon name={item.icon} size={20} weight="regular" className="shrink-0" />
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>

      {/* Footer — user + status */}
      <div className="border-t border-border p-3 space-y-2">
        {user && (
          <div className="flex items-center gap-2 rounded-lg bg-muted px-3 py-2">
            <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-primary text-xs font-semibold text-primary-foreground">
              {user.username.slice(0, 1).toUpperCase()}
            </span>
            <div className="flex-1 min-w-0">
              <p className="text-xs font-medium text-foreground truncate">{user.username}</p>
            </div>
            <button
              onClick={handleLogout}
              className="shrink-0 rounded p-1 text-muted-foreground hover:bg-muted hover:text-destructive transition-colors"
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
  )
}
