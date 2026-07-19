import { NavLink } from 'react-router-dom'
import Icon from '../ui/Icon'

const NAV_ITEMS = [
  { to: '/', label: '驾驶舱', icon: 'house' as const },
  { to: '/ask', label: '问答', icon: 'chat' as const },
  { to: '/review', label: '复习', icon: 'review' as const },
  { to: '/learn', label: '学习', icon: 'learn' as const },
  { to: '/courses', label: '课程', icon: 'courses' as const },
  { to: '/projects', label: '项目', icon: 'projects' as const },
  { to: '/graph', label: '图谱', icon: 'graph' as const },
]

export default function MobileNav() {
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-50 border-t border-border bg-card safe-area-bottom md:hidden">
      <div className="flex items-center justify-around overflow-x-auto h-14">
        {NAV_ITEMS.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              `flex flex-col shrink-0 items-center justify-center min-w-[48px] min-h-[44px] rounded-lg transition-colors duration-150 ${
                isActive
                  ? 'text-primary'
                  : 'text-muted-foreground hover:text-foreground'
              }`
            }
          >
            <Icon name={item.icon} size={22} weight="regular" />
            <span className="text-[10px] font-medium mt-0.5">{item.label}</span>
          </NavLink>
        ))}
      </div>
    </nav>
  )
}
