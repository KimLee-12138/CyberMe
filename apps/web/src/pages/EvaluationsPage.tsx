import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { listSuites, createSuite, deleteSuite, runEvaluation, listRuns } from '../api/learning'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'
import type { EvalRun } from '../api/learning'

export default function EvaluationsPage() {
  useTitle('评测')
  const qc = useQueryClient()
  const [showCreate, setShowCreate] = useState(false)
  const [name, setName] = useState('')
  const [questions, setQuestions] = useState('')
  const [running, setRunning] = useState<string | null>(null)
  const [viewRun, setViewRun] = useState<EvalRun | null>(null)

  const { data: suites } = useQuery({ queryKey: ['eval-suites'], queryFn: listSuites })
  const { data: runs } = useQuery({ queryKey: ['eval-runs'], queryFn: listRuns })

  const createMut = useMutation({
    mutationFn: () => createSuite({
      name,
      cases: questions.split('\n').filter(Boolean).map(q => ({ question: q.trim() })),
    }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['eval-suites'] }); setShowCreate(false); setName(''); setQuestions(''); toast.success('评测套件已创建') },
  })

  const runMut = useMutation({
    mutationFn: (sid: string) => runEvaluation(sid),
    onSuccess: (r: EvalRun) => {
      qc.invalidateQueries({ queryKey: ['eval-runs'] })
      setViewRun(r)
      setRunning(null)
      toast.success('评测完成')
    },
  })

  const deleteMut = useMutation({
    mutationFn: (sid: string) => deleteSuite(sid),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['eval-suites'] }); toast.success('评测套件已删除') },
  })

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">评测中心</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            评估检索和问答质量 · 回归检测
          </p>
        </div>
        <button onClick={() => setShowCreate(true)} className="rounded-xl bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground">
          + 新建评测集
        </button>
      </div>

      {/* Create suite form */}
      {showCreate && (
        <div className="rounded-2xl border border-primary/30 bg-primary/5 p-5 space-y-3">
          <input value={name} onChange={e => setName(e.target.value)} placeholder="评测集名称，如：数据库课程核心题" className="w-full rounded-xl border px-4 py-2 text-sm" />
          <textarea value={questions} onChange={e => setQuestions(e.target.value)}
            placeholder="每行一道题，如：&#10;事务隔离级别有哪些？&#10;什么是ACID？&#10;索引的优缺点？"
            rows={5} className="w-full rounded-xl border px-4 py-2 text-sm resize-none" />
          <div className="flex gap-2">
            <button onClick={() => createMut.mutate()} disabled={!name.trim() || !questions.trim()}
              className="rounded-lg bg-primary px-4 py-1.5 text-sm text-primary-foreground disabled:opacity-40">创建</button>
            <button onClick={() => setShowCreate(false)} className="rounded-lg px-4 py-1.5 text-sm text-muted-foreground">取消</button>
          </div>
        </div>
      )}

      {/* Suites list */}
      <div className="space-y-3">
        {suites && suites.suites.length === 0 && (
          <div className="rounded-2xl border bg-white py-12 text-center">
            <span className="text-3xl">🧪</span>
            <p className="mt-3 text-sm text-muted-foreground">暂无评测集，点击「新建评测集」开始</p>
          </div>
        )}
        {suites?.suites.map(s => (
          <div key={s.id} className="rounded-xl border bg-white p-4 shadow-sm">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="font-semibold">{s.name}</h3>
                <p className="text-xs text-muted-foreground">{s.case_count} 道题 · {s.description || '无描述'}</p>
              </div>
              <div className="flex gap-2">
                <button onClick={() => { setRunning(s.id); runMut.mutate(s.id) }}
                  disabled={running === s.id}
                  className="rounded-lg bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-700 hover:bg-emerald-200 disabled:opacity-50">
                  {running === s.id ? '运行中...' : '▶ 运行'}
                </button>
                <button onClick={() => { if (confirm(`确定要删除评测套件「${s.name}」吗？`)) deleteMut.mutate(s.id) }}
                  className="rounded-lg px-3 py-1 text-xs text-red-500 hover:bg-red-50">删除</button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Run result */}
      {viewRun && (
        <div className="rounded-2xl border bg-white p-5 shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="font-semibold">{viewRun.suite_name} — 评测结果</h2>
            <button onClick={() => setViewRun(null)} className="text-xs text-muted-foreground">关闭</button>
          </div>

          <div className="grid grid-cols-4 gap-3">
            <Stat label="通过率" value={`${(viewRun.pass_rate * 100).toFixed(0)}%`} ok={viewRun.pass_rate > 0.7} />
            <Stat label="通过" value={`${viewRun.passed}/${viewRun.total}`} ok={viewRun.passed > viewRun.total / 2} />
            <Stat label="平均召回率" value={viewRun.avg_recall.toFixed(2)} ok={viewRun.avg_recall > 0.5} />
            <Stat label="平均延迟" value={`${viewRun.avg_latency_ms.toFixed(0)}ms`} />
          </div>

          <div className="space-y-2">
            {viewRun.case_results.map((c, i) => (
              <div key={i} className={`rounded-lg border-l-4 p-3 ${c.pass ? 'border-l-emerald-500 bg-emerald-50' : 'border-l-red-500 bg-red-50'}`}>
                <div className="flex items-center justify-between">
                  <span className="text-sm font-medium">{c.question}</span>
                  <span className="text-xs">{c.pass ? '✅' : '❌'}</span>
                </div>
                <div className="mt-1 flex gap-3 text-xs text-muted-foreground">
                  {c.citation_count != null && <span>引用: {c.citation_count}</span>}
                  {c.recall != null && <span>召回率: {c.recall}</span>}
                  {c.latency_ms != null && <span>{c.latency_ms}ms</span>}
                  {c.model && <span>{c.model}</span>}
                  {c.error && <span className="text-red-500">{c.error}</span>}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Run history */}
      {runs && runs.runs.length > 0 && (
        <section className="rounded-2xl border bg-white p-5 shadow-sm">
          <h2 className="text-sm font-semibold">运行历史</h2>
          <div className="mt-2 space-y-1">
            {runs.runs.slice(0, 10).map(r => (
              <button key={r.id} onClick={() => setViewRun(r)}
                className="flex w-full items-center justify-between rounded-lg bg-secondary/30 px-3 py-2 text-sm hover:bg-secondary/60 transition-colors">
                <span>{r.suite_name}</span>
                <span className="text-xs text-muted-foreground">
                  {r.passed}/{r.total} · {(r.pass_rate * 100).toFixed(0)}% · {new Date(r.run_at).toLocaleString('zh-CN')}
                </span>
              </button>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}

function Stat({ label, value, ok }: { label: string; value: string; ok?: boolean }) {
  return (
    <div className={`rounded-xl border px-3 py-2.5 text-center ${ok === undefined ? '' : ok ? 'border-emerald-200 bg-emerald-50' : 'border-red-200 bg-red-50'}`}>
      <p className="text-lg font-bold">{value}</p>
      <p className="text-xs text-muted-foreground">{label}</p>
    </div>
  )
}
