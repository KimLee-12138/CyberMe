import { useEffect } from 'react'
import { Routes, Route, Navigate, Outlet } from 'react-router-dom'
import { Capacitor } from '@capacitor/core'
import { App as NativeApp } from '@capacitor/app'
import { useAuthStore } from './stores/authStore'
import AppLayout from './components/layout/AppLayout'

import DashboardPage from './pages/DashboardPage'
import LoginPage from './pages/LoginPage'
import ChatPage from './pages/ChatPage'
import TutorPage from './pages/TutorPage'
import ReviewPage from './pages/ReviewPage'
import CourseListPage from './pages/CourseListPage'
import CourseDetailPage from './pages/CourseDetailPage'
import NotesPage from './pages/NotesPage'
import YuketangPage from './pages/YuketangPage'
import KnowledgeDetailPage from './pages/KnowledgeDetailPage'
import GraphPage from './pages/GraphPage'
import QualityPage from './pages/QualityPage'
import ProjectListPage from './pages/ProjectListPage'
import ProjectPage from './pages/ProjectPage'
import WritingPage from './pages/WritingPage'
import DecisionsPage from './pages/DecisionsPage'
import SelfModelPage from './pages/SelfModelPage'
import EvaluationsPage from './pages/EvaluationsPage'
import SyncPage from './pages/SyncPage'
import SettingsPage from './pages/SettingsPage'
import PairPage from './pages/PairPage'
import DistillPage from './pages/DistillPage'
import ToastContainer from './components/ui/Toast'
import { ConfirmHost } from './components/ui/ConfirmDialog'

function RequireAuth() {
  const { isAuthenticated, isLoading } = useAuthStore()

  if (isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-background">
        <div className="flex flex-col items-center gap-3">
          <img src="/app-icon.png" alt="" className="h-10 w-10 animate-pulse rounded-xl object-cover" />
          <p className="text-sm text-muted-foreground">加载中...</p>
        </div>
      </div>
    )
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }

  return <Outlet />
}

function App() {
  const checkSession = useAuthStore((s) => s.checkSession)

  useEffect(() => {
    checkSession()
  }, [checkSession])

  useEffect(() => {
    if (!Capacitor.isNativePlatform()) return
    let disposed = false
    let remove: (() => Promise<void>) | undefined

    NativeApp.addListener('backButton', ({ canGoBack }) => {
      if (canGoBack) window.history.back()
      else NativeApp.exitApp()
    }).then((handle) => {
      if (disposed) void handle.remove()
      else remove = () => handle.remove()
    })

    return () => {
      disposed = true
      if (remove) void remove()
    }
  }, [])

  return (
    <>
      <ToastContainer />
      <ConfirmHost />
      <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route element={<RequireAuth />}>
        <Route element={<AppLayout />}>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/ask" element={<ChatPage />} />
          <Route path="/learn" element={<TutorPage />} />
          <Route path="/review" element={<ReviewPage />} />
          <Route path="/courses" element={<CourseListPage />} />
          <Route path="/courses/:courseId" element={<CourseDetailPage />} />
          <Route path="/notes" element={<NotesPage />} />
          <Route path="/yuketang" element={<YuketangPage />} />
          <Route path="/knowledge/:documentId" element={<KnowledgeDetailPage />} />
          <Route path="/graph" element={<GraphPage />} />
          <Route path="/quality" element={<QualityPage />} />
          <Route path="/projects" element={<ProjectListPage />} />
          <Route path="/projects/:projectId" element={<ProjectPage />} />
          <Route path="/write" element={<WritingPage />} />
          <Route path="/decisions" element={<DecisionsPage />} />
          <Route path="/self" element={<SelfModelPage />} />
          <Route path="/evaluations" element={<EvaluationsPage />} />
          <Route path="/sync" element={<SyncPage />} />
          <Route path="/settings" element={<SettingsPage />} />
          <Route path="/pair" element={<PairPage />} />
          <Route path="/distill" element={<DistillPage />} />
        </Route>
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
    </>
  )
}

export default App
