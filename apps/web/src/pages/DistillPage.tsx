import { useState } from 'react'
import { useQuery, useMutation } from '@tanstack/react-query'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'

const COURSE_LIST = 'ALGO,ASM,CALCULUS,CO,CPP,DANGXIAO,DB,DISCRETE,DS,EDA,ENGLISH,HISTORY,INFO,JAVA,JUNLI,LINALG,MAOGAI,MAYUAN,PHYSICS,PROB,PY,RLMATH,SE,SIXIANG,XIGAI,ZHENGCE'.split(',')

interface PendingData {
  course_code: string; extract_count: number; concept_count: number
  extracts: { id: string; title: string; chars: number; path: string }[]
}

interface BatchItem {
  title: string; path: string; chars: number; preview?: string; error?: string
}
interface BatchState {
  running: boolean; total: number; done: number; items: BatchItem[]
}

async function fetchPending(c: string): Promise<PendingData> {
  const r = await fetch(`/api/v1/distill/pending/${c}`)
  if (!r.ok) throw new Error(r.statusText)
  return r.json()
}

async function runSingle(course: string, max: number) {
  const r = await fetch('/api/v1/distill/extract-to-knowledge', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ course_code: course, max_extracts: max }),
  })
  if (!r.ok) throw new Error((await r.json()).detail || '失败')
  return r.json()
}

export default function DistillPage() {
  useTitle('知识蒸馏')
  const [course, setCourse] = useState('DB')
  const [maxExtracts, setMaxExtracts] = useState(3)
  const [batch, setBatch] = useState<BatchState>({ running: false, total: 0, done: 0, items: [] })

  const { data: pending, isLoading, refetch } = useQuery({
    queryKey: ['distill-pending', course], queryFn: () => fetchPending(course), enabled: !!course,
  })

  const singleMut = useMutation({
    mutationFn: () => runSingle(course, maxExtracts),
    onSuccess: (d: any) => { toast.success(`蒸馏完成: ${d.distilled} 篇`); refetch() },
    onError: (e: Error) => toast.error(e.message),
  })

  const startBatch = () => {
    setBatch({ running: true, total: 0, done: 0, items: [] })
    const es = new EventSource(`/api/v1/distill/batch?course_code=${course}`)
    es.addEventListener('start', (e: any) => {
      const d = JSON.parse(e.data)
      setBatch((b) => ({ ...b, total: d.total }))
    })
    es.addEventListener('progress', (e: any) => {
      const d = JSON.parse(e.data)
      setBatch((b) => ({ ...b, done: d.done, total: d.total, items: [...b.items, { title: d.title, path: d.path, chars: d.chars, preview: d.preview }] }))
    })
    es.addEventListener('skip', (e: any) => {
      const d = JSON.parse(e.data)
      setBatch((b) => ({ ...b, done: b.done + 1, items: [...b.items, { title: d.title, path: '', chars: 0 }] }))
    })
    es.addEventListener('error_item', (e: any) => {
      const d = JSON.parse(e.data)
      setBatch((b) => ({ ...b, done: b.done + 1, items: [...b.items, { title: d.title, path: '', chars: 0, error: d.error }] }))
    })
    es.addEventListener('done', (e: any) => {
      const d = JSON.parse(e.data)
      setBatch((b) => ({ ...b, running: false }))
      toast.success(`批量蒸馏完成: ${d.total} 篇`)
      refetch()
      es.close()
    })
    es.addEventListener('error', () => {
      if (batch.running) { setBatch((b) => ({ ...b, running: false })); es.close() }
    })
  }

  const pct = batch.total > 0 ? Math.round((batch.done / batch.total) * 100) : 0

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div>
        <h1 className="text-2xl font-bold">AI 知识蒸馏</h1>
        <p className="mt-1 text-sm text-muted-foreground">将 90_课程提取资料 中的原始内容通过 DeepSeek AI 蒸馏为结构化知识点</p>
      </div>

      {/* Controls */}
      <div className="flex items-end gap-4 rounded-xl border border-border bg-card p-4">
        <label className="flex flex-col gap-1">
          <span className="text-xs text-muted-foreground">课程</span>
          <select value={course} onChange={(e) => setCourse(e.target.value)} className="rounded-lg border px-3 py-2 text-sm">
            {COURSE_LIST.map((c) => <option key={c} value={c}>{c}</option>)}
          </select>
        </label>

        {/* Single mode */}
        <label className="flex flex-col gap-1">
          <span className="text-xs text-muted-foreground">篇数</span>
          <select value={maxExtracts} onChange={(e) => setMaxExtracts(Number(e.target.value))} className="rounded-lg border px-3 py-2 text-sm">
            {[1,2,3,5].map((n) => <option key={n} value={n}>{n} 篇</option>)}
          </select>
        </label>
        <button onClick={() => singleMut.mutate()} disabled={singleMut.isPending || batch.running}
          className="rounded-lg bg-secondary px-4 py-2 text-sm font-medium hover:bg-muted transition-colors">
          {singleMut.isPending ? '蒸馏中...' : '蒸馏选中'}
        </button>

        {/* Batch button */}
        <button onClick={startBatch} disabled={batch.running || singleMut.isPending}
          className="rounded-lg bg-primary px-6 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 disabled:opacity-50 transition-colors">
          {batch.running ? `蒸馏中 ${pct}%` : '🚀 一键蒸馏整门课'}
        </button>
      </div>

      {/* Batch progress */}
      {batch.running && (
        <div className="rounded-xl border border-primary/30 bg-primary/5 p-4 space-y-2">
          <div className="flex items-center gap-3">
            <span className="text-sm font-semibold text-primary">AI 正在蒸馏...</span>
            <span className="text-xs text-muted-foreground">{batch.done}/{batch.total}</span>
          </div>
          <div className="h-2 rounded-full bg-muted overflow-hidden">
            <div className="h-full rounded-full bg-primary transition-all duration-500" style={{ width: `${pct}%` }} />
          </div>
          <div className="max-h-48 overflow-y-auto space-y-1 mt-2">
            {batch.items.map((it, i) => (
              <div key={i} className="flex items-center gap-2 rounded bg-white px-2 py-1 text-xs">
                <span className="text-emerald-500 shrink-0">✓</span>
                <span className="truncate">{it.title}</span>
                {it.chars > 0 && <span className="shrink-0 text-muted-foreground">{it.chars}字</span>}
                {it.error && <span className="shrink-0 text-red-500">{it.error}</span>}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Status */}
      {pending && (
        <div className="rounded-xl border border-border bg-card p-4">
          <div className="flex gap-6 text-sm">
            <span>📄 提取资料：<strong>{pending.extract_count}</strong> 篇</span>
            <span>📝 已有知识点：<strong>{pending.concept_count}</strong> 篇</span>
          </div>
        </div>
      )}

      {isLoading && <div className="py-12 text-center text-sm text-muted-foreground">加载中...</div>}

      {/* Extract list */}
      {pending && pending.extracts.length > 0 && !batch.running && (
        <div className="rounded-xl border border-border bg-card p-4">
          <h3 className="mb-3 text-sm font-semibold">待蒸馏资料（按内容量排序）</h3>
          <div className="space-y-1 max-h-72 overflow-y-auto">
            {pending.extracts.map((e) => (
              <div key={e.id} className="flex justify-between rounded-lg bg-muted px-3 py-1.5 text-xs">
                <span className="truncate">{e.title || e.path.split('/').pop()}</span>
                <span className="ml-2 shrink-0 text-muted-foreground">{e.chars} 字</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
