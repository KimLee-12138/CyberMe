import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { fetchSelfModel, addStyleSample, removeStyleSample } from '../api/self'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'

export default function SelfModelPage() {
  useTitle('个人模型')
  const navigate = useNavigate()
  const qc = useQueryClient()
  const [showAddStyle, setShowAddStyle] = useState(false)
  const [styleContent, setStyleContent] = useState('')
  const [styleType, setStyleType] = useState<'approved' | 'rejected'>('approved')
  const [hiddenInferences, setHiddenInferences] = useState<Set<string>>(new Set())

  const { data, isLoading } = useQuery({
    queryKey: ['self-model'],
    queryFn: fetchSelfModel,
  })

  const addMut = useMutation({
    mutationFn: () => addStyleSample({ content: styleContent, sample_type: styleType }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['self-model'] }); setShowAddStyle(false); setStyleContent(''); toast.success('风格样本已添加') },
  })

  const delMut = useMutation({
    mutationFn: (id: string) => removeStyleSample(id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['self-model'] }); toast.success('已删除') },
  })

  if (isLoading) return <div className="py-12 text-center text-muted-foreground">加载中...</div>
  if (!data) return <div className="py-12 text-center text-muted-foreground">数据加载失败</div>

  const edgeLabels: Record<string, string> = {
    candidate_link: 'AI 候选关联', related_to: '可能相关', belongs_to: '可能属于',
  }

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div>
        <h1 className="text-2xl font-bold">数字分身</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          {data.facts_count} 个事实 · {data.inferences_count} 个待确认推断 · {data.style_samples.length} 个风格样本
        </p>
      </div>

      {/* Facts */}
      <section className="rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="flex items-center gap-2 text-sm font-semibold">
          明确事实 ({data.facts_count})
          <span className="rounded-full bg-emerald-100 px-2 py-0.5 text-xs text-emerald-700">已确认</span>
        </h2>
        {data.facts.length === 0 ? (
          <p className="mt-3 text-sm text-muted-foreground">暂无明确事实。当 Vault 中的个人文档标记 verification=explicit 后会出现在这里。</p>
        ) : (
          <div className="mt-3 grid gap-2 sm:grid-cols-2">
            {data.facts.map((f) => (
              <div key={f.id}
                onClick={() => f.path && navigate(`/knowledge/${f.id}`)}
                className="rounded-lg border bg-secondary/30 px-3 py-2 cursor-pointer hover:bg-secondary/60 transition-colors"
              >
                <p className="text-sm font-medium">{f.title || f.label || '未命名'}</p>
                <p className="mt-0.5 text-xs text-muted-foreground">
                  {f.course_code && `${f.course_code} · `}{f.node_type || f.type}
                </p>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Inferences */}
      <section className="rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="flex items-center gap-2 text-sm font-semibold">
          待确认推断 ({data.inferences_count - hiddenInferences.size})
          <span className="rounded-full bg-amber-100 px-2 py-0.5 text-xs text-amber-700">待审核</span>
        </h2>
        {data.inferences.length === 0 || hiddenInferences.size >= data.inferences.length ? (
          <p className="mt-3 text-sm text-muted-foreground">暂无待确认推断。AI 在分析知识库时会自动发现潜在关联。</p>
        ) : (
          <div className="mt-3 space-y-2">
            {data.inferences.filter((inf) => !hiddenInferences.has(inf.id)).map((inf) => (
              <div key={inf.id} className="flex items-center justify-between rounded-lg bg-amber-50/60 px-3 py-2">
                <div className="text-sm">
                  <span className="font-medium">{inf.source_label}</span>
                  <span className="mx-1.5 text-muted-foreground">
                    {edgeLabels[inf.edge_type] || inf.edge_type} →
                  </span>
                  <span className="font-medium">{inf.target_label}</span>
                  {inf.confidence != null && (
                    <span className="ml-2 text-xs text-muted-foreground">
                      置信度: {(inf.confidence * 100).toFixed(0)}%
                    </span>
                  )}
                </div>
                <div className="flex gap-1">
                  <button onClick={() => setHiddenInferences((s) => new Set(s).add(inf.id))} className="rounded bg-emerald-100 px-2 py-0.5 text-xs text-emerald-700 hover:bg-emerald-200">确认</button>
                  <button onClick={() => setHiddenInferences((s) => new Set(s).add(inf.id))} className="rounded bg-red-100 px-2 py-0.5 text-xs text-red-700 hover:bg-red-200">忽略</button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Style Samples */}
      <section className="rounded-2xl border bg-white p-5 shadow-sm">
        <div className="flex items-center justify-between">
          <h2 className="text-sm font-semibold">风格样本库 ({data.style_samples.length})</h2>
          <button onClick={() => setShowAddStyle(true)} className="rounded-lg bg-primary px-3 py-1 text-xs text-primary-foreground">+ 添加</button>
        </div>

        {showAddStyle && (
          <div className="mt-3 space-y-2 rounded-xl border border-primary/30 bg-primary/5 p-4">
            <textarea value={styleContent} onChange={e => setStyleContent(e.target.value)}
              placeholder="输入一段你满意的文风示例..."
              rows={3} className="w-full rounded-lg border px-3 py-2 text-sm" />
            <div className="flex items-center gap-2">
              <select value={styleType} onChange={e => setStyleType(e.target.value as any)}
                className="rounded-lg border px-2 py-1 text-xs">
                <option value="approved">✅ 认可</option>
                <option value="rejected">❌ 不认可</option>
              </select>
              <button onClick={() => addMut.mutate()} disabled={!styleContent.trim()}
                className="rounded-lg bg-primary px-3 py-1 text-xs text-primary-foreground disabled:opacity-40">保存</button>
              <button onClick={() => setShowAddStyle(false)} className="text-xs text-muted-foreground">取消</button>
            </div>
          </div>
        )}

        {data.style_samples.length === 0 && !showAddStyle ? (
          <p className="mt-3 text-sm text-muted-foreground">暂无风格样本。添加你满意（或不满意）的文风示例，帮助 AI 更好地模仿你的写作风格。</p>
        ) : (
          <div className="mt-3 space-y-2">
            {data.style_samples.map((s) => (
              <div key={s.id} className={`flex items-start justify-between rounded-lg px-3 py-2 ${s.sample_type === 'approved' ? 'bg-emerald-50/60' : 'bg-red-50/60'}`}>
                <div className="flex-1 min-w-0">
                  <span className="text-xs font-medium">{s.sample_type === 'approved' ? '✅ 认可' : '❌ 不认可'}</span>
                  <p className="mt-0.5 text-sm line-clamp-2">{s.content}</p>
                </div>
                <button onClick={() => { if (window.confirm('确定要删除该风格样本吗？')) delMut.mutate(s.id) }} className="ml-2 shrink-0 text-xs text-red-400 hover:text-red-600">删除</button>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  )
}
