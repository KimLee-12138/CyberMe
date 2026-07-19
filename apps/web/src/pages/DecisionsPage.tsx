import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import Markdown from '../components/ui/Markdown'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'
import { createDecision, listDecisions } from '../api/learning'
import type { Decision } from '../api/learning'

const ROLE_COLORS: Record<string, string> = {
  past_self: 'border-blue-400 bg-blue-50',
  present_self: 'border-emerald-400 bg-emerald-50',
  opponent: 'border-red-400 bg-red-50',
  auditor: 'border-purple-400 bg-purple-50',
}

export default function DecisionsPage() {
  useTitle('决策分析')
  const qc = useQueryClient()
  const [topic, setTopic] = useState('')
  const [context, setContext] = useState('')
  const [viewing, setViewing] = useState<Decision | null>(null)

  const { data } = useQuery({
    queryKey: ['decisions'],
    queryFn: listDecisions,
  })

  const createMut = useMutation({
    mutationFn: () => createDecision(topic, context),
    onSuccess: (d) => {
      qc.invalidateQueries({ queryKey: ['decisions'] })
      setViewing(d)
      setTopic('')
      setContext('')
      toast.success('决策分析完成')
    },
  })

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <h1 className="text-2xl font-bold">决策实验室</h1>

      {/* Create form */}
      <div className="rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-sm font-semibold">新建决策分析</h2>
        <p className="mt-1 text-xs text-muted-foreground">输入待决策的问题，四个角色将从不同角度帮你分析</p>
        <div className="mt-3 space-y-3">
          <input value={topic} onChange={e => setTopic(e.target.value)}
            placeholder="决策题目，如：是否应该先学操作系统还是先学计算机网络？"
            className="w-full rounded-xl border px-4 py-2.5 text-sm placeholder:text-muted-foreground" />
          <textarea value={context} onChange={e => setContext(e.target.value)}
            placeholder="背景信息（可选）：如时间限制、已有基础、目标..."
            rows={2} className="w-full rounded-xl border px-4 py-2.5 text-sm placeholder:text-muted-foreground resize-none" />
          <button onClick={() => createMut.mutate()} disabled={!topic.trim() || createMut.isPending}
            className="rounded-xl bg-primary px-6 py-2.5 text-sm font-semibold text-primary-foreground hover:bg-primary/90 disabled:opacity-40">
            {createMut.isPending ? '四角色分析中...' : '开始分析'}
          </button>
        </div>
      </div>

      {/* Analyzing indicator */}
      {createMut.isPending && (
        <div className="flex items-center gap-2 rounded-xl border bg-white p-6 text-sm text-muted-foreground">
          <span className="inline-block h-3 w-3 animate-spin rounded-full border-2 border-primary border-t-transparent" />
          四角色分析进行中...（历史上的我 → 现在的我 → 反对者 → 证据审计者）
        </div>
      )}

      {/* Analysis result */}
      {viewing && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">{viewing.topic}</h2>
            <button onClick={() => setViewing(null)} className="text-sm text-muted-foreground hover:text-foreground">收起</button>
          </div>
          <div className="grid gap-4 md:grid-cols-2">
            {viewing.analyses.map((a) => (
              <div key={a.role} className={`rounded-xl border-l-4 border bg-white p-4 shadow-sm ${ROLE_COLORS[a.role] || ''}`}>
                <h3 className="flex items-center gap-2 text-sm font-semibold">
                  <span>{a.icon}</span>
                  {a.label}
                </h3>
                <div className="mt-2 text-sm">
                  <Markdown>{a.content}</Markdown>
                </div>
              </div>
            ))}
          </div>
          <p className="text-center text-xs text-muted-foreground">
            以上为四个角色的独立分析。系统不会替你做出最终决定 — 决策权在你手中。
          </p>
        </div>
      )}

      {/* History */}
      {data && data.decisions.length > 0 && (
        <section className="rounded-2xl border bg-white p-5 shadow-sm">
          <h2 className="text-sm font-semibold">历史决策 ({data.decisions.length})</h2>
          <div className="mt-3 space-y-2">
            {data.decisions.map((d) => (
              <button key={d.id} onClick={() => setViewing(d)}
                className={`w-full rounded-lg px-4 py-2.5 text-left text-sm transition-colors ${
                  viewing?.id === d.id ? 'bg-primary/10' : 'bg-secondary/30 hover:bg-secondary/60'
                }`}>
                <span className="font-medium">{d.topic}</span>
                <span className="ml-2 text-xs text-muted-foreground">
                  {new Date(d.created_at).toLocaleString('zh-CN')}
                </span>
              </button>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}
