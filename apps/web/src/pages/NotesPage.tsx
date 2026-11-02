import { useEffect, useMemo, useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Link, useSearchParams } from 'react-router-dom'
import { NotebookPen } from 'lucide-react'
import Markdown from '../components/ui/Markdown'
import { useTitle } from '../lib/useTitle'
import type { NoteDetail, NoteSummary } from '../api/notes'
import { fetchNote, fetchNotes } from '../api/notes'

const FLAG_META: Record<string, { label: string; cls: string }> = {
  formula_missing: { label: '公式缺失', cls: 'border-amber-200 bg-amber-50 text-amber-700' },
  no_definition: { label: '缺定义', cls: 'border-sky-200 bg-sky-50 text-sky-700' },
  has_conflict: { label: '有冲突', cls: 'border-red-200 bg-red-50 text-red-700' },
}

const RELATION_LABELS: Record<string, string> = {
  related_to: '相关',
  prerequisite_of: '前置',
  contrasts_with: '对比',
}

function pagesLabel(pages: number[] | undefined): string {
  if (!pages || pages.length === 0) return ''
  if (pages.length === 1) return `p.${pages[0]}`
  return `p.${pages[0]}–${pages[pages.length - 1]}`
}

function FlagBadges({ flags }: { flags: string[] }) {
  if (!flags?.length) return null
  return (
    <span className="inline-flex flex-wrap gap-1">
      {flags.map(f => {
        const m = FLAG_META[f] || { label: f, cls: 'border-border bg-secondary text-muted-foreground' }
        return (
          <span key={f} className={`rounded border px-1.5 py-0.5 text-[10px] ${m.cls}`}>
            {m.label}
          </span>
        )
      })}
    </span>
  )
}

function NoteCard({
  note,
  selected,
  onSelect,
}: {
  note: NoteSummary
  selected: boolean
  onSelect: () => void
}) {
  return (
    <button
      data-note-id={note.note_id}
      onClick={onSelect}
      className={`w-full rounded-xl border p-3 text-left transition-colors ${
        selected
          ? 'border-primary bg-primary/5'
          : 'border-border bg-white hover:bg-secondary/40'
      }`}
    >
      <div className="flex items-start justify-between gap-2">
        <span className="rounded bg-secondary px-1.5 py-0.5 text-[10px] text-muted-foreground">
          {note.course_name}
        </span>
        <span className="shrink-0 text-[10px] tabular-nums text-muted-foreground">
          {Math.round(note.confidence * 100)}%
        </span>
      </div>
      <p className="mt-1 line-clamp-2 text-xs font-semibold leading-snug text-foreground">{note.title}</p>
      <p className="mt-0.5 line-clamp-1 text-[10px] text-muted-foreground">{note.chapter}</p>
      <div className="mt-1.5 flex flex-wrap items-center gap-1">
        <FlagBadges flags={note.flags} />
        <span className="text-[10px] text-muted-foreground">
          {note.source_count} 来源 · {note.unit_count} 单元
        </span>
      </div>
      <p className="mt-1.5 line-clamp-2 text-[10px] leading-relaxed text-muted-foreground">{note.snippet || note.summary}</p>
    </button>
  )
}

function NoteDetailPanel({ note, loading }: { note?: NoteDetail; loading: boolean }) {
  const [copied, setCopied] = useState('')
  const relations = useMemo(() => {
    const raw = note?.topic?.relations
    return Array.isArray(raw) ? raw.filter((r: any) => r && r.type && r.target) : []
  }, [note])

  if (loading) {
    return (
      <div className="space-y-3 p-5">
        <div className="h-5 w-2/3 animate-pulse rounded bg-muted" />
        <div className="h-3 w-1/3 animate-pulse rounded bg-muted" />
        <div className="mt-6 space-y-2">
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="h-3 animate-pulse rounded bg-muted" style={{ width: `${95 - (i % 3) * 12}%` }} />
          ))}
        </div>
      </div>
    )
  }

  if (!note) {
    return (
      <div className="flex h-full items-center justify-center p-8 text-center">
        <div>
          <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-[#eef4ff] text-[#2563eb]">
            <NotebookPen size={22} />
          </div>
          <p className="mt-3 text-sm font-medium text-foreground">选择一篇笔记</p>
          <p className="mt-1 text-xs text-muted-foreground">左侧可以按课程、flag 或关键词筛选。</p>
        </div>
      </div>
    )
  }

  return (
    <div className="flex h-full min-h-0 flex-col">
      <div className="border-b border-border px-5 py-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded bg-secondary px-2 py-0.5 text-[11px] text-muted-foreground">{note.course_name}</span>
          <span className="text-[11px] text-muted-foreground">{note.chapter}</span>
          <FlagBadges flags={note.flags} />
        </div>
        <h2 className="mt-2 text-lg font-bold leading-snug text-foreground">{note.title}</h2>
        <div className="mt-1 flex flex-wrap gap-3 text-[11px] text-muted-foreground">
          <span>置信度 {Math.round(note.confidence * 100)}%</span>
          <span>{note.unit_count} 单元</span>
          <span>{note.key_points} 关键点</span>
          <span>{note.formulas} 公式</span>
          <span>{note.source_count} 来源</span>
          <span>{note.verification || 'inferred'}</span>
        </div>
        <div className="mt-3 flex flex-wrap gap-2">
          <Link
            to={`/graph?course=${encodeURIComponent(note.course)}`}
            className="rounded-lg bg-primary/10 px-3 py-1.5 text-xs font-medium text-primary hover:bg-primary/20"
          >
            在知识图谱中查看
          </Link>
          <button
            onClick={() => {
              navigator.clipboard?.writeText(note.path)
              setCopied('path')
            }}
            className="rounded-lg border border-border px-3 py-1.5 text-xs text-muted-foreground hover:bg-secondary"
          >
            {copied === 'path' ? '已复制路径' : '复制笔记路径'}
          </button>
          <button
            onClick={() => {
              navigator.clipboard?.writeText(note.body)
              setCopied('body')
            }}
            className="rounded-lg border border-border px-3 py-1.5 text-xs text-muted-foreground hover:bg-secondary"
          >
            {copied === 'body' ? '已复制正文' : '复制正文'}
          </button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto px-5 py-4">
        {note.flags?.includes('formula_missing') && (
          <div className="mb-4 rounded-lg border border-amber-200 bg-amber-50 px-3 py-2 text-xs text-amber-800">
            这篇笔记有公式缺失标记：原文公式/变量未完整提取，正文没有补写。
          </div>
        )}

        <div className="mb-4 grid gap-2 sm:grid-cols-2">
          <div className="rounded-xl border border-border bg-secondary/20 p-3">
            <p className="text-[10px] font-medium text-muted-foreground">来源</p>
            <div className="mt-1.5 space-y-1.5">
              {note.sources.map(s => (
                <div key={`${s.source_id}-${s.section_id}`} className="text-[11px]">
                  <p className="text-foreground/80">{s.rel || s.source_id}</p>
                  <p className="mt-0.5 flex flex-wrap gap-2 font-mono text-[10px] text-muted-foreground">
                    <span>{s.source_id}</span>
                    {s.source_pages?.length > 0 && <span>{pagesLabel(s.source_pages)}</span>}
                    {s.section_title && <span>{s.section_title}</span>}
                  </p>
                </div>
              ))}
            </div>
          </div>
          <div className="rounded-xl border border-border bg-secondary/20 p-3">
            <p className="text-[10px] font-medium text-muted-foreground">笔记元数据</p>
            <div className="mt-1.5 space-y-1 text-[11px] text-muted-foreground">
              <p className="break-all font-mono text-[10px]">{note.path}</p>
              <p>topic: {note.topic_id}</p>
              {note.tags?.length > 0 && <p>tags: {note.tags.join(' / ')}</p>}
            </div>
          </div>
        </div>

        {relations.length > 0 && (
          <div className="mb-4 rounded-xl border border-border bg-white p-3">
            <p className="text-[10px] font-medium text-muted-foreground">关联主题</p>
            <div className="mt-1.5 flex flex-wrap gap-1">
              {relations.slice(0, 12).map((r: any, i: number) => (
                <span key={`${r.type}-${r.target}-${i}`} className="rounded bg-secondary px-2 py-1 text-[10px] text-muted-foreground">
                  {RELATION_LABELS[r.type] || r.type} → {r.target}
                </span>
              ))}
            </div>
          </div>
        )}

        <Markdown math>{note.body}</Markdown>
      </div>
    </div>
  )
}

export default function NotesPage() {
  useTitle('笔记')
  const [params, setParams] = useSearchParams()
  const [q, setQ] = useState('')
  const [debouncedQ, setDebouncedQ] = useState('')
  const [course, setCourse] = useState('')
  const [flag, setFlag] = useState('')
  const [selectedId, setSelectedId] = useState(params.get('note') || '')

  useEffect(() => {
    const t = setTimeout(() => setDebouncedQ(q.trim()), 250)
    return () => clearTimeout(t)
  }, [q])

  const listQ = useQuery({
    queryKey: ['notes', debouncedQ, course, flag],
    queryFn: () => fetchNotes({
      q: debouncedQ || undefined,
      course: course || undefined,
      flag: flag || undefined,
    }),
  })

  const data = listQ.data
  const selectedInList = data?.items.some(x => x.note_id === selectedId)

  useEffect(() => {
    if (!data) return
    if (selectedId && selectedInList) return
    const next = data.items[0]?.note_id || ''
    setSelectedId(next)
    setParams(prev => {
      const p = new URLSearchParams(prev)
      if (next) p.set('note', next)
      else p.delete('note')
      return p
    }, { replace: true })
  }, [data, selectedId, selectedInList, setParams])

  const detailQ = useQuery({
    queryKey: ['note', selectedId],
    queryFn: () => fetchNote(selectedId),
    enabled: !!selectedId,
  })

  useEffect(() => {
    if (!selectedId) return
    const el = document.querySelector(`[data-note-id="${selectedId}"]`)
    el?.scrollIntoView({ block: 'nearest', behavior: 'smooth' })
  }, [selectedId, data])

  const selectNote = (id: string) => {
    setSelectedId(id)
    setParams(prev => {
      const p = new URLSearchParams(prev)
      p.set('note', id)
      return p
    }, { replace: true })
  }

  const stats = data?.stats
  const total = data?.total ?? 0
  const reset = () => {
    setQ('')
    setCourse('')
    setFlag('')
  }

  return (
    <div className="space-y-4">
      <header className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-2xl font-bold">笔记浏览器</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            433 篇可追溯笔记 · 按课程浏览、搜索、查看来源页码
          </p>
        </div>
        <div className="flex flex-wrap gap-2 text-[11px]">
          <span className="rounded-full border border-border bg-white px-2.5 py-1 text-muted-foreground">
            全部 {stats?.all_notes ?? 433}
          </span>
          <span className="rounded-full border border-amber-200 bg-amber-50 px-2.5 py-1 text-amber-700">
            公式缺失 {stats?.formula_missing ?? 73}
          </span>
          <span className="rounded-full border border-sky-200 bg-sky-50 px-2.5 py-1 text-sky-700">
            缺定义 {stats?.no_definition ?? 51}
          </span>
          <span className="rounded-full border border-red-200 bg-red-50 px-2.5 py-1 text-red-700">
            冲突 {stats?.conflicts ?? 3}
          </span>
        </div>
      </header>

      <div className="flex flex-col gap-3 lg:h-[calc(100vh-10rem)] lg:flex-row">
        {/* Filters */}
        <aside className="w-full shrink-0 rounded-2xl border border-border bg-white p-3 shadow-sm lg:w-56 lg:overflow-y-auto">
          <div className="relative">
            <input
              value={q}
              onChange={e => setQ(e.target.value)}
              placeholder="搜索标题 / 正文…"
              className="w-full rounded-lg border border-border bg-background px-3 py-2 text-xs placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/10"
            />
          </div>

          <div className="mt-4">
            <p className="mb-1.5 text-[10px] font-medium uppercase tracking-wide text-muted-foreground">课程</p>
            <div className="space-y-0.5">
              <button
                onClick={() => setCourse('')}
                className={`flex w-full items-center justify-between rounded-md px-2 py-1.5 text-left text-xs ${
                  course === '' ? 'bg-primary/10 text-primary' : 'text-muted-foreground hover:bg-secondary'
                }`}
              >
                <span>全部课程</span>
                <span className="tabular-nums">{stats?.all_notes ?? 433}</span>
              </button>
              {(data?.courses || []).map(c => (
                <button
                  key={c.course}
                  onClick={() => setCourse(c.course)}
                  className={`flex w-full items-center justify-between rounded-md px-2 py-1.5 text-left text-xs ${
                    course === c.course ? 'bg-primary/10 text-primary' : 'text-muted-foreground hover:bg-secondary'
                  }`}
                >
                  <span className="truncate">{c.name}</span>
                  <span className="tabular-nums">{c.count}</span>
                </button>
              ))}
            </div>
          </div>

          <div className="mt-4">
            <p className="mb-1.5 text-[10px] font-medium uppercase tracking-wide text-muted-foreground">标记</p>
            <div className="space-y-0.5">
              <button
                onClick={() => setFlag('')}
                className={`flex w-full items-center justify-between rounded-md px-2 py-1.5 text-left text-xs ${
                  flag === '' ? 'bg-primary/10 text-primary' : 'text-muted-foreground hover:bg-secondary'
                }`}
              >
                <span>全部</span>
              </button>
              {(data?.flags || []).map(f => (
                <button
                  key={f.flag}
                  onClick={() => setFlag(f.flag)}
                  className={`flex w-full items-center justify-between rounded-md px-2 py-1.5 text-left text-xs ${
                    flag === f.flag ? 'bg-primary/10 text-primary' : 'text-muted-foreground hover:bg-secondary'
                  }`}
                >
                  <span>{f.label}</span>
                  <span className="tabular-nums">{f.count}</span>
                </button>
              ))}
            </div>
          </div>

          <button
            onClick={reset}
            className="mt-4 w-full rounded-lg border border-border px-2 py-1.5 text-[11px] text-muted-foreground hover:bg-secondary"
          >
            清空筛选
          </button>
        </aside>

        {/* List */}
        <section className="flex w-full shrink-0 flex-col overflow-hidden rounded-2xl border border-border bg-white shadow-sm lg:w-80">
          <div className="flex items-center justify-between border-b border-border px-3 py-2.5">
            <p className="text-xs font-semibold text-foreground">
              {listQ.isLoading ? '加载中…' : `${total} 篇`}
            </p>
            <p className="text-[10px] text-muted-foreground">
              {debouncedQ ? `“${debouncedQ}”` : '按课程排序'}
            </p>
          </div>
          <div className="flex-1 space-y-1.5 overflow-y-auto p-2">
            {listQ.isLoading && (
              <div className="space-y-2 p-2">
                {Array.from({ length: 6 }).map((_, i) => (
                  <div key={i} className="h-20 animate-pulse rounded-xl bg-muted" />
                ))}
              </div>
            )}
            {listQ.isError && (
              <div className="p-8 text-center">
                <p className="text-sm text-muted-foreground">笔记列表加载失败</p>
                <button onClick={() => listQ.refetch()} className="mt-2 text-xs text-primary hover:underline">
                  重试
                </button>
              </div>
            )}
            {!listQ.isLoading && !listQ.isError && data?.items.map(n => (
              <NoteCard
                key={n.note_id}
                note={n}
                selected={n.note_id === selectedId}
                onSelect={() => selectNote(n.note_id)}
              />
            ))}
            {!listQ.isLoading && total === 0 && (
              <div className="p-8 text-center">
                <p className="text-sm text-muted-foreground">没有匹配的笔记</p>
                <button onClick={reset} className="mt-2 text-xs text-primary hover:underline">
                  清空筛选
                </button>
              </div>
            )}
          </div>
        </section>

        {/* Detail */}
        <main className="min-h-[420px] min-w-0 flex-1 overflow-hidden rounded-2xl border border-border bg-white shadow-sm">
          {detailQ.isError ? (
            <div className="flex h-full items-center justify-center p-8 text-center">
              <div>
                <p className="text-sm font-medium text-foreground">笔记详情加载失败</p>
                <button onClick={() => detailQ.refetch()} className="mt-2 text-xs text-primary hover:underline">
                  重试
                </button>
              </div>
            </div>
          ) : (
            <NoteDetailPanel note={detailQ.data} loading={detailQ.isLoading && !!selectedId} />
          )}
        </main>
      </div>
    </div>
  )
}
