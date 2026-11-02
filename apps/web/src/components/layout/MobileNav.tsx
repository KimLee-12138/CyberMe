import { NavLink } from 'react-router-dom'
import { MoreHorizontal } from 'lucide-react'
import Icon from '../ui/Icon'
import { MOBILE_NAV_ITEMS } from '../../lib/nav'

export default function MobileNav({ onMore }: { onMore: () => void }) {
  return (
    <nav className="safe-area-bottom fixed inset-x-0 bottom-0 z-50 px-3 pb-3 md:hidden">
      <div className="mx-auto flex max-w-md items-center justify-around rounded-[22px] border border-[#e3eaf3]/90 bg-white/92 px-1 py-1.5 shadow-[0_20px_45px_-18px_rgba(15,31,58,0.45)] backdrop-blur-xl">
        {MOBILE_NAV_ITEMS.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              `relative flex min-h-[52px] min-w-[54px] flex-col items-center justify-center gap-0.5 rounded-[16px] px-1 transition-colors ${
                isActive ? 'text-[#2563eb]' : 'text-[#7b8da5]'
              }`
            }
          >
            {({ isActive }) => (
              <>
                <span className={`flex h-8 w-8 items-center justify-center rounded-xl transition-all ${isActive ? 'bg-[#eef4ff]' : ''}`}>
                  <Icon name={item.icon} size={20} />
                </span>
                <span className="text-[9px] font-semibold">{item.label}</span>
              </>
            )}
          </NavLink>
        ))}
        <button
          onClick={onMore}
          className="flex min-h-[52px] min-w-[54px] flex-col items-center justify-center gap-0.5 rounded-[16px] px-1 text-[#7b8da5] transition-colors hover:text-[#2563eb]"
          aria-label="更多"
        >
          <span className="flex h-8 w-8 items-center justify-center rounded-xl">
            <MoreHorizontal size={21} />
          </span>
          <span className="text-[9px] font-semibold">更多</span>
        </button>
      </div>
    </nav>
  )
}
