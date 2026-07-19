import { useEffect } from 'react'
import { Routes, Route, Navigate, Outlet } from 'react-router-dom'
import { useAuthStore } from './stores/authStore'
import AppLayout from './components/layout/AppLayout'

import DashboardPage from './pages/DashboardPage'
import LoginPage from './pages/LoginPage'
import ChatPage from './pages/ChatPage'
import TutorPage from './pages/TutorPage'
import ReviewPage from './pages/ReviewPage'
import CourseListPage from './pages/CourseListPage'
import CourseDetailPage from './pages/CourseDetailPage'
import KnowledgeDetailPage from './pages/KnowledgeDetailPage'
import GraphPage from './pages/GraphPage'
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

function RequireAuth() {
  const { isAuthenticated, isLoading } = useAuthStore()

  if (isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-background">
        <div className="flex flex-col items-center gap-3">
          <span className="text-3xl animate-pulse">🧠</span>
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

  return (
    <>
      <ToastContainer />
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
          <Route path="/knowledge/:documentId" element={<KnowledgeDetailPage />} />
          <Route path="/graph" element={<GraphPage />} />
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
