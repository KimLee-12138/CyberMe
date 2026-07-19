import { useState } from 'react'
import { useMutation } from '@tanstack/react-query'
import { generateWriting, auditWriting } from '../api/learning'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'
import type { AuditParagraph } from '../api/learning'

const OUTPUT_TYPES = [
  { key: 'report', label: '实验报告', icon: '📊' },
  { key: 'summary', label: '学习总结', icon: '📝' },
  { key: 'essay', label: '课程论文', icon: '📄' },
  { key: 'presentation', label: 'PPT 大纲', icon: '📽️' },
  { key: 'resume', label: '简历描述', icon: '💼' },
]

const FACT_COLORS: Record<string, string> = {
  direct_fact: 'border-l-emerald-500 bg-emerald-50',
  rewrite: 'border-l-amber-500 bg-amber-50',
  inference: 'border-l-orange-500 bg-orange-50',
  gap: 'border-l-red-500 bg-red-50',
  model_knowledge: 'border-l-purple-500 bg-purple-50',
}

const FACT_LABELS: Record<string, string> = {
  direct_fact: '直接事实', rewrite: '合理改写', inference: '推断',
  gap: '待补充', model_knowledge: '通用知识',
}

export default function WritingPage() {
  useTitle('写作')
  const [topic, setTopic] = useState('')
  const [outputType, setOutputType] = useState('report')
  const [draft, setDraft] = useState('')
  const [audit, setAudit] = useState<AuditParagraph[]>([])
  const [bindings, setBindings] = useState<Array<{ ref: string; path: string }>>([])

  const genMut = useMutation({
    mutationFn: () => generateWriting(topic, outputType),
    onSuccess: (data) => {
      setDraft(data.draft)
      setBindings(data.fact_bindings)
      auditMut.mutate(data.draft)
      toast.success('文章生成完成')
    },
  })

  const auditMut = useMutation({
    mutationFn: (text: string) => auditWriting(text),
    onSuccess: (data) => { setAudit(data.paragraphs); toast.success('事实审校完成') },
  })

  return (
    <div className="flex gap-6">
      {/* Left: Controls + Evidence */}
      <aside className="hidden w-56 flex-shrink-0 lg:block">
        <div className="sticky top-6 space-y-4">
          <div className="rounded-xl border bg-white p-4 shadow-sm">
            <h3 className="mb-3 text-xs font-semibold uppercase text-muted-foreground">写作设置</h3>

            <label className="mb-2 block text-xs text-muted-foreground">题材</label>
            <div className="grid grid-cols-2 gap-1">
              {OUTPUT_TYPES.map((t) => (
                <button key={t.key} onClick={() => setOutputType(t.key)}
                  className={`flex flex-col items-center rounded-lg p-2 text-xs transition-colors ${
                    outputType === t.key ? 'bg-primary/10 text-primary font-medium' : 'bg-secondary/50 text-muted-foreground hover:bg-secondary'
                  }`}>
                  <span className="text-lg">{t.icon}</span>
                  {t.label}
                </button>
              ))}
            </div>

            <label className="mb-1 mt-4 block text-xs text-muted-foreground">主题</label>
            <textarea value={topic} onChange={e => setTopic(e.target.value)}
              placeholder="要写什么？如：数据库事务隔离级别实验报告"
              rows={3} className="w-full rounded-lg border px-3 py-2 text-xs placeholder:text-muted-foreground resize-none" />

            <button onClick={() => { if (topic.trim()) genMut.mutate() }}
              disabled={!topic.trim() || genMut.isPending}
              className="mt-3 w-full rounded-lg bg-primary py-2 text-xs font-semibold text-primary-foreground hover:bg-primary/90 disabled:opacity-40">
              {genMut.isPending ? '生成中...' : 'AI 生成草稿'}
            </button>
          </div>

          {bindings.length > 0 && (
            <div className="rounded-xl border bg-white p-4 shadow-sm">
              <h3 className="mb-2 text-xs font-semibold uppercase text-muted-foreground">引用 ({bindings.length})</h3>
              <div className="space-y-1 max-h-48 overflow-y-auto">
                {bindings.map((b, i) => (
                  <div key={i} className="rounded bg-secondary/40 px-2 py-1 text-xs">
                    <span className="font-medium text-primary">[{b.ref}]</span>
                    <span className="ml-1 text-muted-foreground">{b.path.split('/').pop()}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </aside>

      {/* Center: Editor */}
      <div className="min-w-0 flex-1 space-y-4">
        <h1 className="text-2xl font-bold">写作工作室</h1>

        {/* Mobile controls */}
        <div className="flex flex-wrap gap-2 lg:hidden">
          {OUTPUT_TYPES.map((t) => (
            <button key={t.key} onClick={() => setOutputType(t.key)}
              className={`rounded-full px-3 py-1 text-xs ${outputType === t.key ? 'bg-primary text-primary-foreground' : 'bg-secondary text-muted-foreground'}`}>
              {t.icon} {t.label}
            </button>
          ))}
          <input value={topic} onChange={e => setTopic(e.target.value)} placeholder="主题..." className="flex-1 rounded-full border px-3 py-1 text-xs" />
          <button onClick={() => { if (topic.trim()) genMut.mutate() }}
            disabled={!topic.trim() || genMut.isPending}
            className="rounded-full bg-primary px-4 py-1 text-xs text-primary-foreground disabled:opacity-40">
            {genMut.isPending ? '...' : '生成'}
          </button>
        </div>

        {genMut.isPending && (
          <div className="flex items-center gap-2 rounded-xl border bg-white p-8 text-sm text-muted-foreground">
            <span className="inline-block h-3 w-3 animate-spin rounded-full border-2 border-primary border-t-transparent" />
            AI 正在撰写...
          </div>
        )}

        {draft && (
          <div className="rounded-2xl border bg-white p-6 shadow-sm">
            <textarea
              value={draft}
              onChange={(e) => { setDraft(e.target.value); auditMut.mutate(e.target.value) }}
              className="min-h-[400px] w-full resize-y rounded-lg border bg-background p-4 font-mono text-sm focus:border-primary focus:outline-none"
            />
            <p className="mt-2 text-xs text-muted-foreground">可直接编辑，修改后自动重新审计</p>
          </div>
        )}

        {!draft && !genMut.isPending && (
          <div className="flex min-h-[50vh] items-center justify-center rounded-2xl border bg-white">
            <div className="text-center max-w-md px-8">
              <span className="text-4xl">✍️</span>
              <h2 className="mt-3 text-lg font-semibold">写作工作室</h2>
              <p className="mt-2 text-sm text-muted-foreground">
                选择题材、输入主题，AI 将基于你的知识库生成草稿，并自动审计每段的事实来源。
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Right: Fact Audit */}
      {audit.length > 0 && (
        <aside className="hidden w-64 flex-shrink-0 xl:block">
          <div className="sticky top-6 rounded-xl border bg-white p-4 shadow-sm max-h-[80vh] overflow-y-auto">
            <h3 className="mb-3 text-xs font-semibold uppercase text-muted-foreground">
              事实审计 ({audit.length} 段)
            </h3>
            <div className="space-y-2">
              {audit.map((p, i) => (
                <div key={i} className={`rounded-lg border-l-4 p-2.5 ${FACT_COLORS[p.type] || ''}`}>
                  <span className="text-[10px] font-semibold uppercase">{FACT_LABELS[p.type] || p.type}</span>
                  <p className="mt-0.5 text-xs text-foreground line-clamp-3">{p.text}</p>
                  {p.note && <p className="mt-0.5 text-[10px] italic text-muted-foreground">{p.note}</p>}
                </div>
              ))}
            </div>
          </div>
        </aside>
      )}
    </div>
  )
}
