import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'
import { listProposals, getProposal, approveProposal, rejectProposal, applyProposal, generateProposal } from '../api/learning'
import type { WritebackProposal, DiffLine } from '../api/learning'

const statusLabels: Record<string, string> = {
  draft: '草稿', validating: '验证中', ready: '待审批', approved: '已批准', rejected: '已拒绝', applied: '已应用',
}
const statusColors: Record<string, string> = {
  draft: 'bg-gray-100 text-gray-600', validating: 'bg-blue-100 text-blue-700',
  ready: 'bg-amber-100 text-amber-700', approved: 'bg-emerald-100 text-emerald-700',
  rejected: 'bg-red-100 text-red-700', applied: 'bg-purple-100 text-purple-700',
}

export default function SyncPage() {
  useTitle('同步')
  const navigate = useNavigate()
  const qc = useQueryClient()
  const [viewing, setViewing] = useState<WritebackProposal | null>(null)
  const [docId, setDocId] = useState('')
  const [instruction, setInstruction] = useState('')

  const { data } = useQuery({ queryKey: ['proposals'], queryFn: listProposals })

  const viewMut = useMutation({
    mutationFn: (id: string) => getProposal(id),
    onSuccess: (p) => setViewing(p),
  })

  const approveMut = useMutation({
    mutationFn: (id: string) => approveProposal(id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['proposals'] }); setViewing(null); toast.success('提案已通过') },
  })

  const rejectMut = useMutation({
    mutationFn: (id: string) => rejectProposal(id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['proposals'] }); setViewing(null); toast.success('提案已拒绝') },
  })

  const applyMut = useMutation({
    mutationFn: (id: string) => applyProposal(id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['proposals'] }); setViewing(null); toast.success('提案已应用') },
  })

  const genMut = useMutation({
    mutationFn: () => generateProposal(docId, instruction),
    onSuccess: (p) => { qc.invalidateQueries({ queryKey: ['proposals'] }); setViewing(p); setDocId(''); setInstruction(''); toast.success('提案已生成') },
  })

  const proposals = data?.proposals || []

  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <h1 className="text-2xl font-bold">同步与写回</h1>

      {/* AI proposal generator */}
      <div className="rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-sm font-semibold">AI 写回提案</h2>
        <p className="mt-1 text-xs text-muted-foreground">选择一篇文档，让 AI 根据指令改进内容</p>
        <div className="mt-3 space-y-2">
          <input value={docId} onChange={e => setDocId(e.target.value)}
            placeholder="文档 ID（从知识详情页获取）"
            className="w-full rounded-lg border px-3 py-2 text-sm" />
          <input value={instruction} onChange={e => setInstruction(e.target.value)}
            placeholder="指令，如：补充ACID四个特性的中文解释"
            className="w-full rounded-lg border px-3 py-2 text-sm" />
          <button onClick={() => genMut.mutate()} disabled={!docId.trim() || !instruction.trim() || genMut.isPending}
            className="rounded-lg bg-primary px-4 py-2 text-sm text-primary-foreground disabled:opacity-40">
            {genMut.isPending ? 'AI 生成中...' : '生成提案'}
          </button>
        </div>
      </div>

      {/* Proposals list */}
      <div className="rounded-2xl border bg-white shadow-sm">
        <div className="border-b px-5 py-3">
          <h2 className="text-sm font-semibold">写回提案 ({proposals.length})</h2>
        </div>
        {proposals.length === 0 ? (
          <div className="px-5 py-8 text-center text-sm text-muted-foreground">
            暂无写回提案。使用上方 AI 生成器创建第一个提案。
          </div>
        ) : (
          <div className="divide-y">
            {proposals.map((p) => (
              <div key={p.id} className="flex items-center justify-between px-5 py-3 hover:bg-secondary/30 transition-colors">
                <button onClick={() => viewMut.mutate(p.id)} className="text-left flex-1 min-w-0">
                  <p className="text-sm font-medium truncate">{p.document_title || p.document_path}</p>
                  <p className="text-xs text-muted-foreground">{p.reason?.slice(0, 60) || '无描述'}</p>
                </button>
                <span className={`ml-2 shrink-0 rounded-full px-2 py-0.5 text-xs ${statusColors[p.status]}`}>
                  {statusLabels[p.status]}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Detail with diff */}
      {viewing && (
        <div className="rounded-2xl border bg-white p-5 shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="font-semibold">{viewing.document_title}</h3>
              <p className="text-xs text-muted-foreground">{viewing.document_path}</p>
            </div>
            <span className={`rounded-full px-2 py-0.5 text-xs ${statusColors[viewing.status]}`}>
              {statusLabels[viewing.status]}
            </span>
          </div>

          <p className="text-sm text-muted-foreground">{viewing.reason}</p>

          {/* Diff preview */}
          {viewing.diff && viewing.diff.length > 0 && (
            <div className="rounded-lg border bg-secondary/20 p-3 max-h-64 overflow-y-auto font-mono text-xs space-y-1">
              {viewing.diff.map((d: DiffLine, i: number) => (
                <div key={i} className={d.type === 'added' ? 'text-emerald-700' : d.type === 'removed' ? 'text-red-700' : 'text-amber-700'}>
                  <span className="text-muted-foreground">L{d.line}</span>
                  {d.type === 'changed' && <span> <span className="line-through text-red-500">{d.old}</span> → <span className="text-emerald-600">{d.new}</span></span>}
                  {d.type === 'added' && <span className="text-emerald-600"> + {d.new}</span>}
                  {d.type === 'removed' && <span className="text-red-500"> - {d.old}</span>}
                </div>
              ))}
            </div>
          )}

          {/* Actions */}
          <div className="flex gap-2">
            {viewing.status !== 'applied' && viewing.status !== 'rejected' && (
              <>
                <button onClick={() => approveMut.mutate(viewing.id)}
                  className="rounded-lg bg-emerald-100 px-4 py-1.5 text-sm font-medium text-emerald-700 hover:bg-emerald-200">批准</button>
                <button onClick={() => rejectMut.mutate(viewing.id)}
                  className="rounded-lg bg-red-100 px-4 py-1.5 text-sm font-medium text-red-700 hover:bg-red-200">拒绝</button>
              </>
            )}
            {viewing.status === 'approved' && (
              <button onClick={() => applyMut.mutate(viewing.id)}
                className="rounded-lg bg-primary px-4 py-1.5 text-sm font-medium text-primary-foreground">应用变更</button>
            )}
            <button onClick={() => setViewing(null)} className="rounded-lg px-4 py-1.5 text-sm text-muted-foreground">关闭</button>
          </div>
        </div>
      )}

      <button onClick={() => navigate('/pair')}
        className="w-full rounded-lg bg-primary py-3 text-sm font-semibold text-primary-foreground">
        配对新设备
      </button>
    </div>
  )
}
