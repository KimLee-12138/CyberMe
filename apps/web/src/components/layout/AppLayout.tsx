import { useEffect, useRef, useState } from 'react'
import { Outlet, useLocation } from 'react-router-dom'
import Sidebar from './Sidebar'
import TopBar from './TopBar'
import MobileNav from './MobileNav'
import MobileSidebar from './MobileSidebar'

export default function AppLayout() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const mainRef = useRef<HTMLElement>(null)
  const location = useLocation()

  useEffect(() => {
    mainRef.current?.scrollTo({ top: 0 })
  }, [location.pathname])

  return (
    <div className="flex h-dvh overflow-hidden bg-background">
      {/* Desktop Sidebar */}
      <Sidebar />

      <div className="flex min-w-0 flex-1 flex-col overflow-hidden">
        {/* Top bar */}
        <TopBar onMenuToggle={() => setMobileMenuOpen(true)} />

        {/* Main content — bottom padding for mobile nav */}
        <main ref={mainRef} className="flex-1 overflow-y-auto px-4 pb-[calc(6.5rem+env(safe-area-inset-bottom))] pt-5 md:px-7 md:pb-8 md:pt-7">
          <div className="mx-auto w-full max-w-[1500px]">
            <Outlet />
          </div>
        </main>
      </div>

      {/* Mobile bottom navigation */}
      <MobileNav onMore={() => setMobileMenuOpen(true)} />

      {/* Mobile sidebar drawer */}
      <MobileSidebar open={mobileMenuOpen} onClose={() => setMobileMenuOpen(false)} />
    </div>
  )
}
