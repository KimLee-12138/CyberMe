import { useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import Markdown from '../components/ui/Markdown'
import { fetchProject, updateProject, createHypothesis, updateHypothesis, createExperiment, createRisk } from '../api/projects'
import { projectStatusLabel, impactLabel } from '../lib/enums'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'

type Tab = 'overview' | 'hypotheses' | 'experiments' | 'risks'

const TABS: { key: Tab; label: string }[] = [
  { key: 'overview', label: '概览' },
  { key: 'hypotheses', label: '假设' },
  { key: 'experiments', label: '实验' },
  { key: 'risks', label: '风险' },
]

const hypStatusColors: Record<string, string> = {
  proposed: 'bg-gray-100 text-gray-600', testing: 'bg-amber-100 text-amber-700',
  confirmed: 'bg-emerald-100 text-emerald-700', rejected: 'bg-red-100 text-red-700',
}
const riskImpactColors: Record<string, string> = {
  low: 'bg-gray-100 text-gray-600', medium: 'bg-amber-100 text-amber-700',
  high: 'bg-red-100 text-red-700', critical: 'bg-red-200 text-red-800',
}

export default function ProjectPage() {
  useTitle('项目详情')
  const { projectId } = useParams<{ projectId: string }>()
  const qc = useQueryClient()
  const [tab, setTab] = useState<Tab>('overview')

  const { data, isLoading } = useQuery({
    queryKey: ['project', projectId],
    queryFn: () => fetchProject(projectId!),
    enabled: !!projectId,
  })

  if (isLoading) return <div className="py-12 text-center text-muted-foreground">加载中...</div>
  if (!data) return <div className="py-12 text-center text-muted-foreground">项目未找到</div>

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div>
        <Link to="/projects" className="text-xs text-muted-foreground hover:text-foreground">← 返回项目列表</Link>
        <h1 className="mt-1 text-2xl font-bold">{data.title}</h1>
        <div className="mt-2 flex items-center gap-2">
          <span className="rounded-md bg-primary/10 px-2 py-0.5 text-xs text-primary">{projectStatusLabel(data.status)}</span>
          {data.deadline && <span className="text-xs text-muted-foreground">截止: {data.deadline}</span>}
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 rounded-xl bg-secondary p-1">
        {TABS.map(t => (
          <button key={t.key} onClick={() => setTab(t.key)}
            className={`flex-1 rounded-lg py-2 text-sm font-medium transition-colors ${
              tab === t.key ? 'bg-white text-foreground shadow-sm' : 'text-muted-foreground hover:text-foreground'
            }`}
          >
            {t.label}
            {t.key === 'hypotheses' && data.hypotheses.length > 0 && ` (${data.hypotheses.length})`}
            {t.key === 'experiments' && data.experiments.length > 0 && ` (${data.experiments.length})`}
            {t.key === 'risks' && data.risks.length > 0 && ` (${data.risks.length})`}
          </button>
        ))}
      </div>

      {/* Overview tab */}
      {tab === 'overview' && (
        <div className="space-y-4">
          <OverviewCard title="目标" content={data.goal} />
          <OverviewCard title="成功标准" content={data.success_criteria} />
          <OverviewCard title="约束条件" content={data.constraints} />
          <OverviewEditor projectId={projectId!} qc={qc} />
        </div>
      )}

      {/* Hypotheses tab */}
      {tab === 'hypotheses' && (
        <div className="space-y-3">
          <HypothesisForm projectId={projectId!} qc={qc} />
          {data.hypotheses.map(h => (
            <div key={h.id} className="rounded-xl border bg-white p-4 shadow-sm">
              <div className="flex items-start justify-between">
                <span className={`rounded-full px-2 py-0.5 text-xs ${hypStatusColors[h.status] || ''}`}>
                  {h.status === 'proposed' ? '待验证' : h.status === 'testing' ? '验证中' : h.status === 'confirmed' ? '已确认' : '已否定'}
                </span>
                <HypothesisActions projectId={projectId!} hypothesis={h} qc={qc} />
              </div>
              <p className="mt-2 text-sm font-medium">{h.statement}</p>
              {h.verification_criteria && <p className="mt-1 text-xs text-muted-foreground">验证标准: {h.verification_criteria}</p>}
              {h.evidence_for && <p className="mt-1 text-xs text-emerald-600">支持: {h.evidence_for}</p>}
              {h.evidence_against && <p className="mt-1 text-xs text-red-600">反对: {h.evidence_against}</p>}
            </div>
          ))}
        </div>
      )}

      {/* Experiments tab */}
      {tab === 'experiments' && (
        <div className="space-y-3">
          <ExperimentForm projectId={projectId!} qc={qc} />
          {data.experiments.map(e => (
            <div key={e.id} className="rounded-xl border bg-white p-4 shadow-sm">
              <span className={`rounded-full px-2 py-0.5 text-xs ${e.failed ? 'bg-red-100 text-red-700' : 'bg-emerald-100 text-emerald-700'}`}>
                {e.failed ? '失败' : '成功'}
              </span>
              {e.design && <p className="mt-2 text-sm">{e.design}</p>}
              {e.environment && <p className="text-xs text-muted-foreground">环境: {e.environment}</p>}
              {Object.keys(e.result).length > 0 && <p className="text-xs text-muted-foreground">结果: {JSON.stringify(e.result)}</p>}
              {e.lessons_learned && <p className="mt-1 text-xs italic text-muted-foreground">教训: {e.lessons_learned}</p>}
            </div>
          ))}
        </div>
      )}

      {/* Risks tab */}
      {tab === 'risks' && (
        <div className="space-y-3">
          <RiskForm projectId={projectId!} qc={qc} />
          {data.risks.map(r => (
            <div key={r.id} className="rounded-xl border bg-white p-4 shadow-sm">
              <div className="flex items-center gap-2">
                <span className={`rounded-full px-2 py-0.5 text-xs ${riskImpactColors[r.impact] || ''}`}>{impactLabel(r.impact)}</span>
                <span className="text-xs text-muted-foreground">概率: {(r.probability * 100).toFixed(0)}%</span>
                <span className="ml-auto text-xs text-muted-foreground">{r.status === 'open' ? '开放' : r.status === 'monitoring' ? '监控中' : '已解决'}</span>
              </div>
              <p className="mt-2 text-sm">{r.description}</p>
              {r.mitigation && <p className="mt-1 text-xs text-emerald-600">缓解: {r.mitigation}</p>}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

// ── Sub-components ───────────────────────────────────────

function OverviewCard({ title, content }: { title: string; content: string | null }) {
  return (
    <div className="rounded-xl border bg-white p-4 shadow-sm">
      <h3 className="text-xs font-semibold uppercase text-muted-foreground">{title}</h3>
      <div className="mt-2">{content ? <Markdown>{content}</Markdown> : <span className="text-muted-foreground">未设置</span>}</div>
    </div>
  )
}

function OverviewEditor({ projectId, qc }: { projectId: string; qc: ReturnType<typeof useQueryClient> }) {
  const [goal, setGoal] = useState('')
  const mut = useMutation({
    mutationFn: () => updateProject(projectId, { goal }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['project', projectId] }); setGoal(''); toast.success('目标已更新') },
  })
  return (
    <div className="flex gap-2">
      <input value={goal} onChange={e => setGoal(e.target.value)} placeholder="更新目标..." className="flex-1 rounded-xl border px-4 py-2 text-sm" />
      <button onClick={() => mut.mutate()} disabled={!goal.trim()} className="rounded-xl bg-primary px-4 py-2 text-sm text-primary-foreground disabled:opacity-40">更新</button>
    </div>
  )
}

function HypothesisForm({ projectId, qc }: { projectId: string; qc: ReturnType<typeof useQueryClient> }) {
  const [s, setS] = useState('')
  const mut = useMutation({
    mutationFn: () => createHypothesis(projectId, { statement: s }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['project', projectId] }); setS(''); toast.success('假设已添加') },
  })
  return (
    <div className="flex gap-2">
      <input value={s} onChange={e => setS(e.target.value)} placeholder="新假设..." className="flex-1 rounded-xl border px-4 py-2 text-sm" />
      <button onClick={() => mut.mutate()} disabled={!s.trim()} className="rounded-xl bg-primary px-4 py-2 text-sm text-primary-foreground disabled:opacity-40">添加</button>
    </div>
  )
}

function HypothesisActions({ projectId, hypothesis, qc }: { projectId: string; hypothesis: { id: string; status: string }; qc: ReturnType<typeof useQueryClient> }) {
  const mut = useMutation({
    mutationFn: (status: string) => updateHypothesis(projectId, hypothesis.id, { status }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['project', projectId] }); toast.success('状态已更新') },
  })
  return (
    <select value={hypothesis.status} onChange={e => mut.mutate(e.target.value)} className="rounded border px-2 py-0.5 text-xs">
      <option value="proposed">待验证</option>
      <option value="testing">验证中</option>
      <option value="confirmed">已确认</option>
      <option value="rejected">已否定</option>
    </select>
  )
}

function ExperimentForm({ projectId, qc }: { projectId: string; qc: ReturnType<typeof useQueryClient> }) {
  const [design, setDesign] = useState(''); const [failed, setFailed] = useState(false)
  const mut = useMutation({
    mutationFn: () => createExperiment(projectId, { design, failed }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['project', projectId] }); setDesign(''); setFailed(false); toast.success('实验已记录') },
  })
  return (
    <div className="flex gap-2 items-center">
      <input value={design} onChange={e => setDesign(e.target.value)} placeholder="实验描述..." className="flex-1 rounded-xl border px-4 py-2 text-sm" />
      <label className="flex items-center gap-1 text-xs"><input type="checkbox" checked={failed} onChange={e => setFailed(e.target.checked)} />失败</label>
      <button onClick={() => mut.mutate()} disabled={!design.trim()} className="rounded-xl bg-primary px-4 py-2 text-sm text-primary-foreground disabled:opacity-40">记录</button>
    </div>
  )
}

function RiskForm({ projectId, qc }: { projectId: string; qc: ReturnType<typeof useQueryClient> }) {
  const [desc, setDesc] = useState(''); const [impact, setImpact] = useState('medium')
  const mut = useMutation({
    mutationFn: () => createRisk(projectId, { description: desc, impact }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['project', projectId] }); setDesc(''); toast.success('风险已添加') },
  })
  return (
    <div className="flex gap-2">
      <input value={desc} onChange={e => setDesc(e.target.value)} placeholder="新风险..." className="flex-1 rounded-xl border px-4 py-2 text-sm" />
      <select value={impact} onChange={e => setImpact(e.target.value)} className="rounded-xl border px-3 py-2 text-sm">
        <option value="low">低</option><option value="medium">中</option><option value="high">高</option><option value="critical">严重</option>
      </select>
      <button onClick={() => mut.mutate()} disabled={!desc.trim()} className="rounded-xl bg-primary px-4 py-2 text-sm text-primary-foreground disabled:opacity-40">添加</button>
    </div>
  )
}
