import { NavLink, useNavigate } from 'react-router-dom'
import { cn } from '../../lib/utils'
import { useAuthStore } from '../../stores/authStore'
import { NAV_GROUPS } from '../../lib/nav'
import Icon from '../ui/Icon'
import { confirm } from '../ui/ConfirmDialog'

export default function Sidebar() {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()

  const handleLogout = async () => {
    const ok = await confirm({
      title: '退出 CyberMe？',
      message: '本机保存的登录态会被清除，下次需要重新登录。',
      confirmLabel: '退出登录',
      danger: true,
    })
    if (!ok) return
    await logout()
    navigate('/login', { replace: true })
  }

  return (
    <aside className="relative hidden w-[252px] flex-shrink-0 flex-col overflow-hidden bg-[#071A33] text-white md:flex">
      <div className="pointer-events-none absolute -left-24 top-[-8%] h-64 w-64 rounded-full bg-[#2563EB]/20 blur-3xl" />
      <div className="pointer-events-none absolute bottom-[-10%] right-[-20%] h-72 w-72 rounded-full bg-[#4F8BFF]/10 blur-3xl" />

      <div className="relative flex h-[76px] items-center gap-3 px-5">
        <img
          src="/app-icon.png"
          alt="CyberMe"
          className="h-10 w-10 rounded-[13px] object-cover shadow-[0_8px_24px_-10px_rgba(79,139,255,0.8)] ring-1 ring-white/20"
        />
        <div className="min-w-0">
          <p className="truncate text-[15px] font-bold tracking-[-0.02em]">CyberMe</p>
          <p className="mt-0.5 text-[10px] font-medium tracking-[0.16em] text-white/45">LEARNING OS</p>
        </div>
      </div>

      <nav className="relative flex-1 overflow-y-auto px-3 pb-3 pt-2">
        {NAV_GROUPS.map((group) => (
          <div key={group.label} className="mb-4">
            <p className="mb-1.5 px-3 text-[8px] font-bold uppercase tracking-[0.2em] text-white/35">
              {group.label}
            </p>
            <div className="space-y-0.5">
              {group.items.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === '/'}
                  className={({ isActive }) =>
                    cn(
                      'group relative flex min-h-9 items-center gap-2.5 rounded-xl px-3 py-2 text-[13px] transition-all duration-200',
                      isActive
                        ? 'bg-white/[0.09] font-semibold text-white shadow-[inset_0_1px_0_rgba(255,255,255,0.08)]'
                        : 'text-white/55 hover:bg-white/[0.05] hover:text-white/90',
                    )
                  }
                >
                  {({ isActive }) => (
                    <>
                      <span
                        className={cn(
                          'absolute left-0 top-1/2 h-4 w-[3px] -translate-y-1/2 rounded-r-full transition-all',
                          isActive ? 'bg-[#5b97ff] opacity-100' : 'opacity-0',
                        )}
                      />
                      <Icon
                        name={item.icon}
                        size={18}
                        className={isActive ? 'text-[#8bb3ff]' : 'text-white/45 group-hover:text-white/70'}
                      />
                      <span className="truncate">{item.label}</span>
                    </>
                  )}
                </NavLink>
              ))}
            </div>
          </div>
        ))}
      </nav>

      <div className="relative border-t border-white/10 p-3">
        {user && (
          <div className="flex items-center gap-2.5 rounded-xl bg-white/[0.06] px-3 py-2.5">
            <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-[#4F8BFF] to-[#2563EB] text-xs font-bold text-white">
              {user.username.slice(0, 1).toUpperCase()}
            </span>
            <div className="min-w-0 flex-1">
              <p className="truncate text-xs font-semibold text-white/90">{user.username}</p>
              <p className="mt-0.5 flex items-center gap-1 text-[10px] text-emerald-300/80">
                <span className="h-1 w-1 rounded-full bg-emerald-400" />
                本地会话
              </p>
            </div>
            <button
              onClick={handleLogout}
              className="shrink-0 rounded-lg p-1.5 text-white/35 transition-colors hover:bg-white/10 hover:text-white/90"
              title="退出登录"
              aria-label="退出登录"
            >
              <Icon name="logout" size={15} />
            </button>
          </div>
        )}
      </div>
    </aside>
  )
}
