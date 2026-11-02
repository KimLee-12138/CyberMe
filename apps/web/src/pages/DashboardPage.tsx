import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import {
  Activity,
  ArrowUpRight,
  BookOpen,
  CheckCircle2,
  Clock3,
  Layers,
  Network,
  RotateCcw,
  Sparkles,
} from 'lucide-react'
import { useTitle } from '../lib/useTitle'
import { fetchDashboard } from '../api/learning'
import type { TopAction } from '../api/learning'
import { getYuketangOverview } from '../api/yuketang'
import { useAuthStore } from '../stores/authStore'

const PRIORITY_STYLES: Record<TopAction['priority'], string> = {
  critical: 'border-l-[#e5484d] bg-[#fff8f8]',
  warning: 'border-l-[#f79009] bg-[#fffdf5]',
  info: 'border-l-[#2563eb] bg-[#f8fbff]',
}

const PRIORITY_DOT: Record<TopAction['priority'], string> = {
  critical: 'bg-[#e5484d]',
  warning: 'bg-[#f79009]',
  info: 'bg-[#2563eb]',
}

function SkeletonCard() {
  return <div className="app-skeleton h-40" />
}

function StatRow({ label, value, ok, sub }: { label: string; value: string | number; ok?: boolean; sub?: string }) {
  return (
    <div className="flex items-center justify-between gap-4 py-2.5">
      <span className="text-[12px] text-muted-foreground">{label}</span>
      <span className="flex items-center gap-1.5 text-right text-[12px] font-semibold text-foreground">
        {ok !== undefined && <span className={`h-1.5 w-1.5 rounded-full ${ok ? 'bg-emerald-500' : 'bg-red-500'}`} />}
        {value}
        {sub && <span className="max-w-[160px] truncate text-[10px] font-normal text-muted-foreground">{sub}</span>}
      </span>
    </div>
  )
}

function Panel({ title, eyebrow, action, children, className = '' }: { title: string; eyebrow?: string; action?: React.ReactNode; children: React.ReactNode; className?: string }) {
  return (
    <section className={`app-card app-card-hover p-5 ${className}`}>
      <div className="mb-3 flex items-start justify-between gap-3">
        <div>
          {eyebrow && <p className="app-eyebrow mb-1.5">{eyebrow}</p>}
          <h2 className="text-[13px] font-bold tracking-[-0.015em] text-foreground">{title}</h2>
        </div>
        {action}
      </div>
      {children}
    </section>
  )
}

export default function DashboardPage() {
  useTitle('驾驶舱')
  const navigate = useNavigate()
  const user = useAuthStore((state) => state.user)
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['dashboard'],
    queryFn: fetchDashboard,
    refetchInterval: 60_000,
  })
  const { data: ykt } = useQuery({
    queryKey: ['ykt-overview'],
    queryFn: () => getYuketangOverview(),
    staleTime: 60_000,
    refetchInterval: 60_000,
  })
  const yktPending = (ykt?.assignments ?? []).filter((assignment) => assignment.pending)

  if (isLoading) {
    return (
      <div className="space-y-5">
        <div className="app-skeleton h-52 rounded-[24px]" />
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 6 }).map((_, index) => <SkeletonCard key={index} />)}
        </div>
      </div>
    )
  }

  if (error || !data) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="app-card max-w-sm p-8 text-center">
          <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-[#fff1f1] text-[#e5484d]">
            <AlertCircleIcon />
          </span>
          <h2 className="mt-4 text-lg font-bold">驾驶舱加载失败</h2>
          <p className="mt-2 text-sm leading-6 text-muted-foreground">后端服务可能暂时不可用，请稍后重试。</p>
          <button onClick={() => refetch()} className="app-button app-button-primary mt-5 w-full">重新加载</button>
        </div>
      </div>
    )
  }

  const { top_actions, due_reviews, knowledge_debt, digital_twin, system_health, project_risks } = data
  const hour = new Date().getHours()
  const greeting = hour < 6 ? '夜深了' : hour < 12 ? '早上好' : hour < 18 ? '下午好' : '晚上好'
  const debtTotal = knowledge_debt.high_importance_low_mastery.count + knowledge_debt.missing_verification.count + knowledge_debt.orphaned_nodes.count + knowledge_debt.needs_review_total

  return (
    <div className="space-y-5 pb-8">
      {/* Hero */}
      <section className="relative overflow-hidden rounded-[26px] bg-[#071A33] px-5 py-6 text-white shadow-[0_30px_70px_-36px_rgba(7,26,51,0.8)] sm:px-7 sm:py-7">
        <div className="pointer-events-none absolute -right-20 -top-28 h-72 w-72 rounded-full bg-[#2563EB]/30 blur-3xl" />
        <div className="pointer-events-none absolute -bottom-32 left-1/3 h-64 w-64 rounded-full bg-[#4F8BFF]/15 blur-3xl" />
        <div className="relative flex flex-col justify-between gap-6 lg:flex-row lg:items-end">
          <div className="max-w-2xl">
            <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#8bb3ff]">Personal learning OS</p>
            <h1 className="mt-3 text-[clamp(1.8rem,3.6vw,2.8rem)] font-[750] leading-[1.02] tracking-[-0.055em]">
              {greeting}，{user?.username || '同学'}。
            </h1>
            <p className="mt-3 max-w-lg text-[13px] leading-6 text-white/50">
              今天不需要学完所有东西，只需要推进一件重要的事。
            </p>
            <div className="mt-5 flex flex-wrap gap-2">
              <button onClick={() => navigate('/ask')} className="app-button app-button-accent !min-h-10 !rounded-full !px-4 !text-[12px]">
                <Sparkles size={15} /> 向知识库提问
              </button>
              <button onClick={() => navigate('/notes')} className="app-button !min-h-10 !rounded-full border border-white/15 !bg-white/[0.07] !px-4 !text-[12px] !text-white/85 hover:!bg-white/[0.12]">
                <BookOpen size={15} /> 浏览笔记
              </button>
            </div>
          </div>
          <div className="grid grid-cols-3 gap-2 lg:w-[330px]">
            {[
              { label: '待复习', value: due_reviews.count, icon: RotateCcw },
              { label: '待复核', value: knowledge_debt.needs_review_total, icon: Activity },
              { label: '近24h事件', value: digital_twin.recent_audit_count, icon: Clock3 },
            ].map((item) => (
              <div key={item.label} className="rounded-2xl border border-white/10 bg-white/[0.06] px-3 py-3 backdrop-blur-sm">
                <item.icon size={14} className="text-[#8bb3ff]" />
                <p className="mt-2 text-[11px] text-white/45">{item.label}</p>
                <p className="mt-0.5 text-xl font-bold tracking-tight">{item.value}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {ykt?.configured && yktPending.length > 0 && (
        <button onClick={() => navigate('/yuketang')} className="app-card app-card-hover flex w-full items-center gap-4 border-[#fde2af] bg-[#fffdf5] p-4 text-left">
          <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-[#fff4de] text-[#b45309]"><BookOpen size={18} /></span>
          <span className="min-w-0 flex-1">
            <span className="block text-[13px] font-bold text-[#7c3e00]">雨课堂 · {yktPending.length} 个待完成作业</span>
            <span className="mt-0.5 block truncate text-[11px] text-[#a16207]">{yktPending.slice(0, 2).map((a) => a.title).join(' · ')}</span>
          </span>
          <ArrowUpRight size={17} className="shrink-0 text-[#b45309]" />
        </button>
      )}

      {/* Actions */}
      <section>
        <div className="mb-2.5 flex items-center justify-between">
          <div>
            <p className="app-eyebrow">Today’s focus</p>
            <h2 className="mt-1 text-[15px] font-bold tracking-tight">今日行动</h2>
          </div>
          <span className="app-chip">{top_actions.length} 条建议</span>
        </div>
        {top_actions.length === 0 ? (
          <div className="app-card flex items-center gap-3 p-4">
            <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-[#eef4ff] text-[#2563eb]"><CheckCircle2 size={17} /></span>
            <div>
              <p className="text-[13px] font-semibold">今天没有紧急行动</p>
              <p className="mt-0.5 text-[11px] text-muted-foreground">系统会根据学习进度自动生成下一步建议。</p>
            </div>
          </div>
        ) : (
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {top_actions.slice(0, 6).map((action, index) => (
              <button
                key={`${action.title}-${index}`}
                onClick={() => action.link && navigate(action.link)}
                className={`app-card app-card-hover flex flex-col border-l-[3px] p-4 text-left ${PRIORITY_STYLES[action.priority]}`}
              >
                <div className="flex items-center gap-2">
                  <span className={`h-1.5 w-1.5 rounded-full ${PRIORITY_DOT[action.priority]}`} />
                  <span className="line-clamp-1 text-[12px] font-bold text-foreground">{action.title}</span>
                </div>
                <p className="mt-1.5 line-clamp-2 text-[11px] leading-5 text-muted-foreground">{action.description}</p>
                {action.link && <span className="mt-3 text-[10px] font-semibold text-[#2563eb]">去处理 →</span>}
              </button>
            ))}
          </div>
        )}
      </section>

      {/* Main grid */}
      <div className="grid gap-4 lg:grid-cols-3">
        <Panel
          title="待复习知识"
          eyebrow="Spaced repetition"
          action={<span className="app-chip app-chip-amber">{due_reviews.count}</span>}
        >
          {due_reviews.documents.length === 0 ? (
            <div className="rounded-xl bg-[#f8fafc] px-4 py-6 text-center">
              <CheckCircle2 size={22} className="mx-auto text-emerald-500" />
              <p className="mt-2 text-[12px] font-semibold">今天没有到期复习</p>
              <p className="mt-1 text-[10px] text-muted-foreground">保持节奏，明天见。</p>
            </div>
          ) : (
            <div className="space-y-1.5">
              {due_reviews.documents.map((doc) => (
                <button key={doc.id} onClick={() => navigate(`/knowledge/${doc.id}`)} className="flex w-full items-center gap-2 rounded-xl bg-[#f8fafc] px-3 py-2.5 text-left transition-colors hover:bg-[#f1f5fb]">
                  <span className="min-w-0 flex-1 truncate text-[12px] font-medium">{doc.title || '未命名'}</span>
                  <span className="shrink-0 text-[10px] text-muted-foreground">{doc.mastery === 'unknown' ? '未掌握' : doc.mastery}</span>
                </button>
              ))}
            </div>
          )}
        </Panel>

        <Panel
          title="知识债务"
          eyebrow="Knowledge health"
          action={<button onClick={() => navigate('/quality')} className="app-button app-button-ghost !min-h-7 !px-2 !text-[10px]">查看质量</button>}
        >
          <div className="divide-y divide-[#edf1f7]">
            <StatRow label="高重要低掌握" value={knowledge_debt.high_importance_low_mastery.count} ok={knowledge_debt.high_importance_low_mastery.count === 0} />
            <StatRow label="缺失来源验证" value={knowledge_debt.missing_verification.count} ok={knowledge_debt.missing_verification.count === 0} />
            <StatRow label="孤立知识节点" value={knowledge_debt.orphaned_nodes.count} ok={knowledge_debt.orphaned_nodes.count === 0} />
            <StatRow label="待复核知识" value={knowledge_debt.needs_review_total} ok={knowledge_debt.needs_review_total === 0} />
          </div>
          <div className="mt-3 flex items-center justify-between rounded-xl bg-[#f8fafc] px-3 py-2">
            <span className="text-[10px] text-muted-foreground">知识债务总量</span>
            <span className={`text-[12px] font-bold ${debtTotal > 0 ? 'text-[#d97706]' : 'text-emerald-600'}`}>{debtTotal > 0 ? debtTotal : '整洁'}</span>
          </div>
        </Panel>

        <Panel
          title="数字分身"
          eyebrow="Personal model"
          action={<span className="app-chip app-chip-blue">Beta</span>}
        >
          <div className="space-y-1.5">
            <div className="flex items-center gap-3 rounded-xl bg-[#f8fafc] p-3">
              <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-white text-[#2563eb] shadow-sm"><Network size={15} /></span>
              <div className="flex-1">
                <p className="text-[11px] font-semibold">AI 候选关联</p>
                <p className="mt-0.5 text-[10px] text-muted-foreground">等待你确认的知识连接</p>
              </div>
              <span className="text-lg font-bold">{digital_twin.ai_candidate_edges}</span>
            </div>
            <div className="flex items-center gap-3 rounded-xl bg-[#f8fafc] p-3">
              <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-white text-[#64748b] shadow-sm"><Activity size={15} /></span>
              <div className="flex-1">
                <p className="text-[11px] font-semibold">近 24h 审计事件</p>
                <p className="mt-0.5 text-[10px] text-muted-foreground">系统活动记录</p>
              </div>
              <span className="text-lg font-bold">{digital_twin.recent_audit_count}</span>
            </div>
          </div>
          <button onClick={() => navigate('/self')} className="app-button app-button-secondary mt-3 w-full !min-h-9 !text-[11px]">打开个人模型 <ArrowUpRight size={13} /></button>
        </Panel>
      </div>

      {/* Quick links */}
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        {[
          { label: '知识问答', sub: 'RAG · 引用', icon: Sparkles, to: '/ask', tint: 'bg-[#eef4ff] text-[#2563eb]' },
          { label: '笔记库', sub: '433 notes', icon: BookOpen, to: '/notes', tint: 'bg-[#ecfdf5] text-[#047857]' },
          { label: '雨课堂', sub: '课程与课件', icon: Layers, to: '/yuketang', tint: 'bg-[#fff7ed] text-[#c2410c]' },
          { label: '知识图谱', sub: '概念连接', icon: Network, to: '/graph', tint: 'bg-[#f5f3ff] text-[#7c3aed]' },
        ].map((item) => (
          <button key={item.label} onClick={() => navigate(item.to)} className="app-card app-card-hover flex items-center gap-3 p-3.5 text-left">
            <span className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-xl ${item.tint}`}><item.icon size={17} /></span>
            <span className="min-w-0">
              <span className="block truncate text-[12px] font-bold">{item.label}</span>
              <span className="mt-0.5 block truncate text-[10px] text-muted-foreground">{item.sub}</span>
            </span>
          </button>
        ))}
      </div>

      {/* System */}
      <div className="grid gap-4 lg:grid-cols-[1.2fr_0.8fr]">
        <Panel title="系统健康" eyebrow="Runtime">
          <div className="grid gap-x-7 sm:grid-cols-2">
            <StatRow label="知识文档" value={system_health.document_count.toLocaleString()} />
            <StatRow label="语义切片" value={system_health.chunk_count.toLocaleString()} />
            <StatRow label="课程数" value={system_health.course_count} />
            <StatRow label="同步状态" value={system_health.sync.status === 'connected' ? '已配对' : '未配对'} ok={system_health.sync.status === 'connected'} />
            <StatRow label="数据库" value={system_health.database === 'connected' ? '正常' : '异常'} ok={system_health.database === 'connected'} />
            <StatRow label="Redis" value={system_health.redis === 'connected' ? '正常' : '异常'} ok={system_health.redis === 'connected'} />
          </div>
          <div className="mt-3 border-t border-[#edf1f7] pt-3">
            <div className="flex items-center justify-between text-[11px]">
              <span className="text-muted-foreground">模型预算 · 本月</span>
              <span className="font-semibold">${system_health.budget.monthly_cost_estimate.toFixed(2)}<span className="font-normal text-muted-foreground"> / ${system_health.budget.monthly_budget_limit.toFixed(0)}</span></span>
            </div>
            <div className="mt-2 h-1.5 overflow-hidden rounded-full bg-[#eef2f7]">
              <div className="h-full rounded-full bg-gradient-to-r from-[#2563eb] to-[#4f8bff]" style={{ width: `${Math.min(100, (system_health.budget.monthly_cost_estimate / system_health.budget.monthly_budget_limit) * 100)}%` }} />
            </div>
            <p className="mt-1.5 text-[10px] text-muted-foreground">今日 ${system_health.budget.daily_cost_estimate.toFixed(4)} · Token {system_health.budget.monthly_tokens.toLocaleString()}</p>
          </div>
        </Panel>

        <Panel title="项目概览" eyebrow="Workspace" action={<button onClick={() => navigate('/projects')} className="app-button app-button-ghost !min-h-7 !px-2 !text-[10px]">全部项目 →</button>}>
          {project_risks.recent_projects && project_risks.recent_projects.length > 0 ? (
            <div className="space-y-1.5">
              {project_risks.recent_projects.slice(0, 4).map((project) => (
                <button key={project.id} onClick={() => navigate(`/projects/${project.id}`)} className="flex w-full items-center justify-between gap-3 rounded-xl bg-[#f8fafc] px-3 py-2.5 text-left hover:bg-[#f1f5fb]">
                  <span className="truncate text-[11px] font-medium">{project.title}</span>
                  <span className="shrink-0 text-[10px] text-muted-foreground">{project.status === 'active' ? '进行中' : project.status === 'completed' ? '已完成' : project.status}</span>
                </button>
              ))}
            </div>
          ) : (
            <div className="rounded-xl bg-[#f8fafc] px-4 py-6 text-center">
              <Layers size={22} className="mx-auto text-[#94a3b8]" />
              <p className="mt-2 text-[11px] font-medium text-muted-foreground">还没有项目</p>
              <button onClick={() => navigate('/projects')} className="mt-2 text-[10px] font-semibold text-[#2563eb]">创建一个 →</button>
            </div>
          )}
          {project_risks.total_open_risks ? (
            <div className="mt-2 rounded-xl bg-[#fff8f8] px-3 py-2 text-[10px] text-[#b42318]">{project_risks.total_open_risks} 个开放风险需要关注</div>
          ) : null}
        </Panel>
      </div>
    </div>
  )
}

function AlertCircleIcon() {
  return <span className="text-xl font-bold">!</span>
}
