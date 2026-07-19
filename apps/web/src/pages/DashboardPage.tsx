import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { useTitle } from '../lib/useTitle'
import { fetchDashboard } from '../api/learning'
import type { TopAction } from '../api/learning'

// ── Color Helpers ──────────────────────────────────────

const PRIORITY_COLORS: Record<TopAction['priority'], string> = {
  critical: 'border-l-red-500 bg-red-50/60',
  warning: 'border-l-amber-500 bg-amber-50/60',
  info: 'border-l-blue-400 bg-blue-50/60',
}

const PRIORITY_DOT: Record<TopAction['priority'], string> = {
  critical: 'bg-red-500',
  warning: 'bg-amber-500',
  info: 'bg-blue-400',
}

const healthColor = (ok: boolean) =>
  ok ? 'bg-emerald-500' : 'bg-red-500'

// ── Skeleton ───────────────────────────────────────────

function SkeletonCard({ lines = 3 }: { lines?: number }) {
  return (
    <div className="rounded-2xl border border-border bg-white p-5 shadow-sm animate-pulse">
      <div className="mb-4 h-4 w-1/3 rounded bg-muted" />
      {Array.from({ length: lines }).map((_, i) => (
        <div
          key={i}
          className="mb-2 h-3 rounded bg-muted"
          style={{ width: `${70 - i * 15}%` }}
        />
      ))}
    </div>
  )
}

// ── Stat Row ───────────────────────────────────────────

function StatRow({
  label,
  value,
  ok,
  sub,
}: {
  label: string
  value: string | number
  ok?: boolean
  sub?: string
}) {
  return (
    <div className="flex items-center justify-between py-1.5">
      <span className="text-sm text-muted-foreground">{label}</span>
      <span className="flex items-center gap-1.5 text-sm font-medium">
        {ok !== undefined && (
          <span className={`inline-block h-2 w-2 rounded-full ${healthColor(ok)}`} />
        )}
        {value}
        {sub && (
          <span className="text-xs text-muted-foreground font-normal">{sub}</span>
        )}
      </span>
    </div>
  )
}

// ── Main Component ─────────────────────────────────────

export default function DashboardPage() {
  useTitle('驾驶舱')
  const navigate = useNavigate()
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['dashboard'],
    queryFn: fetchDashboard,
    refetchInterval: 60_000,
  })

  // ── Loading ────────────────────────────────────────
  if (isLoading) {
    return (
      <div className="space-y-6">
        <h1 className="text-2xl font-bold">今日认知驾驶舱</h1>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <SkeletonCard key={i} lines={3} />
          ))}
        </div>
      </div>
    )
  }

  // ── Error ──────────────────────────────────────────
  if (error || !data) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="text-center max-w-sm">
          <span className="text-4xl">⚠️</span>
          <h2 className="mt-3 text-lg font-semibold text-foreground">
            加载驾驶舱数据失败
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            后端服务可能暂时不可用，请稍后重试
          </p>
          <button
            onClick={() => refetch()}
            className="mt-4 rounded-lg bg-primary px-5 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 transition-colors"
          >
            重新加载
          </button>
        </div>
      </div>
    )
  }

  const { top_actions, due_reviews, knowledge_debt, digital_twin, system_health, project_risks } = data

  // ── Data ───────────────────────────────────────────
  return (
    <div className="space-y-6 pb-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">今日认知驾驶舱</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            知识状态一览 · 自动刷新
          </p>
        </div>
      </div>

      {/* ── SECTION 1: Top Actions ─────────────────── */}
      <section>
        <h2 className="mb-3 text-sm font-semibold text-muted-foreground uppercase tracking-wider">
          今日行动
        </h2>
        {top_actions.length === 0 ? (
          <p className="rounded-xl border border-border bg-white px-5 py-4 text-sm text-muted-foreground">
            暂无推荐行动，系统将根据学习进度自动生成
          </p>
        ) : (
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {top_actions.slice(0, 6).map((action, i) => (
              <button
                key={i}
                onClick={() => action.link && navigate(action.link)}
                className={`flex flex-col rounded-xl border border-border bg-white px-4 py-3.5 text-left shadow-sm transition-all hover:shadow-md border-l-4 ${PRIORITY_COLORS[action.priority]} ${action.link ? 'cursor-pointer' : ''}`}
              >
                <div className="flex items-center gap-2">
                  <span className={`inline-block h-2 w-2 rounded-full shrink-0 ${PRIORITY_DOT[action.priority]}`} />
                  <span className="text-sm font-semibold text-foreground line-clamp-1">
                    {action.title}
                  </span>
                </div>
                <p className="mt-1 text-xs text-muted-foreground line-clamp-2">
                  {action.description}
                </p>
              </button>
            ))}
          </div>
        )}
      </section>

      {/* ── SECTION 2: Card Grid ───────────────────── */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">

        {/* Due Reviews */}
        <section className="rounded-2xl border border-border bg-white p-5 shadow-sm">
          <h3 className="flex items-center gap-2 text-sm font-semibold text-foreground">
            待复习知识
            {due_reviews.count > 0 && (
              <span className="rounded-full bg-amber-100 px-2 py-0.5 text-xs font-medium text-amber-700">
                {due_reviews.count}
              </span>
            )}
          </h3>
          <div className="mt-3 space-y-2">
            {due_reviews.documents.length === 0 ? (
              <p className="text-sm text-muted-foreground">
                暂无待复习知识，继续保持！
              </p>
            ) : (
              due_reviews.documents.map((doc) => (
                <div
                  key={doc.id}
                  className="flex items-center justify-between rounded-lg bg-secondary/40 px-3 py-2 cursor-pointer hover:bg-secondary/70 transition-colors"
                  onClick={() => navigate(`/knowledge/${doc.id}`)}
                >
                  <span className="text-sm line-clamp-1 flex-1">
                    {doc.title || '未命名'}
                  </span>
                  <span className="ml-2 shrink-0 text-xs text-muted-foreground">
                    {doc.mastery === 'unknown' ? '未掌握' : doc.mastery}
                  </span>
                </div>
              ))
            )}
          </div>
        </section>

        {/* Knowledge Debt */}
        <section className="rounded-2xl border border-border bg-white p-5 shadow-sm">
          <h3 className="text-sm font-semibold text-foreground">知识债务</h3>
          <div className="mt-3 space-y-0.5">
            <StatRow
              label="高重要低掌握"
              value={knowledge_debt.high_importance_low_mastery.count}
              ok={knowledge_debt.high_importance_low_mastery.count === 0}
            />
            <StatRow
              label="缺失来源验证"
              value={knowledge_debt.missing_verification.count}
              ok={knowledge_debt.missing_verification.count === 0}
            />
            <StatRow
              label="孤立知识节点"
              value={knowledge_debt.orphaned_nodes.count}
              ok={knowledge_debt.orphaned_nodes.count === 0}
            />
            <StatRow
              label="待复核知识"
              value={knowledge_debt.needs_review_total}
              ok={knowledge_debt.needs_review_total === 0}
            />
          </div>
        </section>

        {/* Digital Twin */}
        <section className="rounded-2xl border border-border bg-white p-5 shadow-sm">
          <h3 className="text-sm font-semibold text-foreground">数字分身状态</h3>
          <div className="mt-3 space-y-0.5">
            <StatRow
              label="AI 候选关联"
              value={digital_twin.ai_candidate_edges}
              ok={true}
            />
            <StatRow
              label="近24h审计事件"
              value={digital_twin.recent_audit_count}
              ok={true}
            />
          </div>
          <p className="mt-3 text-xs text-muted-foreground border-t border-border pt-2">
            个人模型和推断确认功能即将上线
          </p>
        </section>
      </div>

      {/* ── SECTION 3: System Health (full-width) ────── */}
      <section className="rounded-2xl border border-border bg-white p-5 shadow-sm">
        <h3 className="text-sm font-semibold text-foreground">系统健康</h3>
        <div className="mt-3 grid gap-x-8 gap-y-0.5 sm:grid-cols-2 lg:grid-cols-3">
          <StatRow label="知识文档" value={system_health.document_count.toLocaleString()} />
          <StatRow label="语义切片" value={system_health.chunk_count.toLocaleString()} />
          <StatRow label="课程数" value={system_health.course_count} />
          <StatRow
            label="数据库"
            value={system_health.database === 'connected' ? '正常' : '异常'}
            ok={system_health.database === 'connected'}
          />
          <StatRow
            label="Redis"
            value={system_health.redis === 'connected' ? '正常' : '异常'}
            ok={system_health.redis === 'connected'}
          />
          <StatRow
            label="同步状态"
            value={system_health.sync.status === 'connected' ? '已配对' : '未配对'}
            ok={system_health.sync.status === 'connected'}
            sub={
              system_health.sync.last_seen
                ? `最后: ${new Date(system_health.sync.last_seen).toLocaleString('zh-CN')}`
                : undefined
            }
          />
        </div>

        {/* Budget bar */}
        <div className="mt-4 border-t border-border pt-3">
          <div className="flex items-center justify-between text-sm">
            <span className="text-muted-foreground">模型预算 (本月)</span>
            <span className="font-medium">
              ${system_health.budget.monthly_cost_estimate.toFixed(2)}
              <span className="text-muted-foreground font-normal">
                {' / $'}{system_health.budget.monthly_budget_limit.toFixed(0)}
              </span>
            </span>
          </div>
          <div className="mt-1.5 h-2 rounded-full bg-secondary">
            <div
              className="h-full rounded-full bg-primary transition-all"
              style={{
                width: `${Math.min(
                  100,
                  (system_health.budget.monthly_cost_estimate / system_health.budget.monthly_budget_limit) * 100
                ).toFixed(0)}%`,
              }}
            />
          </div>
          <p className="mt-1 text-xs text-muted-foreground">
            今日: ${system_health.budget.daily_cost_estimate.toFixed(4)} · Token: {system_health.budget.monthly_tokens.toLocaleString()}
          </p>
        </div>
      </section>

      {/* ── SECTION 4: Project Overview ────────── */}
      <section className="rounded-2xl border border-border bg-white p-5 shadow-sm">
        <h3 className="text-sm font-semibold text-foreground">
          项目概览
          <span className="ml-2 text-xs font-normal text-muted-foreground">
            {project_risks.total_projects || 0} 个项目
            {project_risks.total_open_risks ? ` · ${project_risks.total_open_risks} 个风险` : ''}
          </span>
        </h3>

        {project_risks.stub ? (
          <p className="mt-3 text-sm text-muted-foreground">创建项目并添加风险项后，将在此处显示风险概览。</p>
        ) : project_risks.recent_projects && project_risks.recent_projects.length > 0 ? (
          <div className="mt-3 space-y-2">
            {project_risks.recent_projects.slice(0, 5).map((p) => (
              <a
                key={p.id}
                href={`/projects/${p.id}`}
                className="flex items-center justify-between rounded-lg bg-muted/50 px-3 py-2 text-sm hover:bg-muted transition-colors"
              >
                <span className="truncate">{p.title}</span>
                <span className={`ml-2 shrink-0 rounded-full px-2 py-0.5 text-xs ${
                  p.status === 'active' ? 'bg-emerald-100 text-emerald-700' :
                  p.status === 'completed' ? 'bg-blue-100 text-blue-700' : 'bg-gray-100 text-gray-500'
                }`}>
                  {p.status === 'active' ? '进行中' : p.status === 'completed' ? '已完成' : p.status}
                </span>
              </a>
            ))}
          </div>
        ) : (
          <p className="mt-3 text-sm text-muted-foreground">暂无项目。在「项目」页面创建或从 GitHub 导入。</p>
        )}

        {/* Open risks warning */}
        {project_risks.open_risks && project_risks.open_risks.length > 0 && (
          <div className="mt-3 rounded-lg border border-red-200 bg-red-50/60 p-3">
            <p className="text-xs font-medium text-red-700">待处理风险</p>
            {project_risks.open_risks.slice(0, 3).map((r) => (
              <div key={r.id} className="mt-1 flex items-center gap-2 text-xs text-red-600">
                <span className={`h-1.5 w-1.5 rounded-full ${r.impact === 'critical' ? 'bg-red-600' : 'bg-red-400'}`} />
                <span className="truncate">{r.description}</span>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  )
}
