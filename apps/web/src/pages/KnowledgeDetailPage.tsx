import { useMemo, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import Markdown from '../components/ui/Markdown'
import { fetchDocument, fetchVersions, resolveWikiLink, updateDocument, searchDocuments } from '../api/knowledge'
import { masteryLabel, importanceLabel, docStatusLabel, docTypeLabel } from '../lib/enums'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'

// ── Edge labels ─────────────────────────────────────────

const edgeLabels: Record<string, string> = {
  belongs_to: '所属课程',
  related_to: '关联知识',
  prerequisite_of: '前置知识',
  example_of: '例题',
  sourced_from: '来源',
  contrasts_with: '对比',
  applies_to: '应用于',
  conflicts_with: '冲突',
  candidate_link: 'AI候选',
}

// ── TOC extraction ──────────────────────────────────────

interface TocItem {
  level: number
  text: string
  anchor: string
}

function extractToc(markdown: string): TocItem[] {
  const headingRegex = /^(#{2,4})\s+(.+)$/gm
  const items: TocItem[] = []
  let match
  while ((match = headingRegex.exec(markdown)) !== null) {
    const text = match[2].trim()
    const anchor = text
      .toLowerCase()
      .replace(/[^\w\u4e00-\u9fff\s-]/g, '')
      .replace(/\s+/g, '-')
    items.push({ level: match[1].length, text, anchor })
  }
  return items.slice(0, 30) // Limit to 30 entries
}

// ── WikiLink component ──────────────────────────────────

function WikiLinkRenderer({ href, children }: { href?: string; children?: React.ReactNode }) {
  const text = String(children || href || '')
  // Check if this looks like a wikilink target (no http, no /)
  if (href && (href.startsWith('http') || href.startsWith('/') || href.startsWith('#'))) {
    return <a href={href} className="text-primary underline">{children || href}</a>
  }
  return <WikiLink target={text}>{text}</WikiLink>
}

function WikiLink({ target, children }: { target: string; children: React.ReactNode }) {
  const navigate = useNavigate()
  const clean = target.replace(/\\/g, '').trim()

  const handleClick = async (e: React.MouseEvent) => {
    e.preventDefault()
    try {
      const result = await resolveWikiLink(clean)
      navigate(`/knowledge/${result.document_id}`)
    } catch {
      // If resolution fails, just show the text without link
    }
  }

  return (
    <button
      onClick={handleClick}
      className="text-primary underline decoration-primary/30 hover:decoration-primary cursor-pointer"
    >
      {children}
    </button>
  )
}

// ── Main component ──────────────────────────────────────

export default function KnowledgeDetailPage() {
  useTitle('知识详情')
  const { documentId } = useParams<{ documentId: string }>()
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const [editing, setEditing] = useState(false)
  const [editMastery, setEditMastery] = useState('')
  const [editImportance, setEditImportance] = useState('')
  const [editStatus, setEditStatus] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['document', documentId],
    queryFn: () => fetchDocument(documentId!),
    enabled: !!documentId,
  })

  const { data: versionData } = useQuery({
    queryKey: ['versions', documentId],
    queryFn: () => fetchVersions(documentId!),
    enabled: !!documentId,
  })

  // Related documents via title search
  const { data: relatedData } = useQuery({
    queryKey: ['related', documentId, data?.title],
    queryFn: () => searchDocuments(data?.title || '', data?.course_code || undefined),
    enabled: !!data?.title && data.title.length > 2,
    staleTime: 60_000,
  })

  const updateMutation = useMutation({
    mutationFn: (updates: { status?: string; mastery?: string; importance?: string }) =>
      updateDocument(documentId!, updates),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['document', documentId] })
      setEditing(false)
      toast.success('保存成功')
    },
  })

  const toc = useMemo(() => {
    if (!data?.markdown_body) return []
    return extractToc(data.markdown_body)
  }, [data?.markdown_body])

  const handleEdit = () => {
    setEditMastery(data?.mastery || '')
    setEditImportance(data?.importance || '')
    setEditStatus(data?.status || '')
    setEditing(true)
  }

  const handleSave = () => {
    updateMutation.mutate({
      mastery: editMastery || undefined,
      importance: editImportance || undefined,
      status: editStatus || undefined,
    })
  }

  if (isLoading) {
    return <div className="py-12 text-center text-muted-foreground">加载中...</div>
  }
  if (!data) {
    return <div className="py-12 text-center text-muted-foreground">文档未找到</div>
  }

  const frontmatter = data.frontmatter || {}
  const hasFrontmatter = Object.keys(frontmatter).length > 0

  return (
    <div className="flex gap-6">
      {/* Left: Table of Contents */}
      <aside className="hidden w-48 flex-shrink-0 md:block">
        <div className="sticky top-6 rounded-xl border border-border bg-white p-4 shadow-sm max-h-[80vh] overflow-y-auto">
          <h3 className="mb-2 text-xs font-semibold uppercase text-muted-foreground">
            目录
          </h3>
          {toc.length > 0 ? (
            <nav className="space-y-0.5">
              {toc.map((item, i) => (
                <a
                  key={i}
                  href={`#${item.anchor}`}
                  onClick={(e) => {
                    e.preventDefault()
                    document.getElementById(item.anchor)?.scrollIntoView({ behavior: 'smooth' })
                  }}
                  className="block rounded px-1.5 py-0.5 text-xs text-muted-foreground hover:bg-secondary hover:text-foreground transition-colors"
                  style={{ paddingLeft: `${4 + (item.level - 2) * 8}px` }}
                >
                  {item.text}
                </a>
              ))}
            </nav>
          ) : (
            <p className="text-xs text-muted-foreground">无标题</p>
          )}
        </div>
      </aside>

      {/* Center: Markdown Content */}
      <div className="min-w-0 flex-1">
        <div className="mb-4">
          <Link
            to={data.course_code ? `/courses/${data.course_code}` : '/courses'}
            className="text-xs text-muted-foreground hover:text-foreground"
          >
            ← {data.course_code ? `返回 ${data.course_code}` : '返回课程列表'}
          </Link>
        </div>

        <h1 className="text-2xl font-bold tracking-tight text-foreground">
          {data.title || data.relative_path.split('/').pop()}
        </h1>

        {/* Export buttons */}
        {data.markdown_body && (
          <div className="mt-2 flex items-center gap-2">
            <button
              onClick={() => {
                const blob = new Blob([data.markdown_body!], { type: 'text/markdown' })
                const url = URL.createObjectURL(blob)
                const a = document.createElement('a')
                a.href = url
                a.download = `${data.title || 'document'}.md`
                a.click()
                URL.revokeObjectURL(url)
              }}
              className="rounded-lg border border-border px-3 py-1 text-xs text-muted-foreground hover:bg-muted transition-colors"
            >
              📥 下载 .md
            </button>
            <button
              onClick={() => window.print()}
              className="rounded-lg border border-border px-3 py-1 text-xs text-muted-foreground hover:bg-muted transition-colors"
            >
              🖨️ 打印
            </button>
          </div>
        )}

        <div className="mt-2 flex flex-wrap items-center gap-2">
          {data.course_code && (
            <span className="rounded-md bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">
              {data.course_code}
            </span>
          )}
          {data.document_type && (
            <span className="rounded-md bg-secondary px-2 py-0.5 text-xs text-muted-foreground">
              {data.document_type}
            </span>
          )}
          {data.status && (
            <span className="rounded-md bg-secondary px-2 py-0.5 text-xs text-muted-foreground">
              {data.status}
            </span>
          )}
          {data.mastery && (
            <span className="rounded-md bg-amber-100 px-2 py-0.5 text-xs text-amber-700">
              {data.mastery}
            </span>
          )}
          {data.needs_review && (
            <span className="rounded-md bg-red-100 px-2 py-0.5 text-xs text-red-700">
              待核对
            </span>
          )}
          <button
            onClick={handleEdit}
            className="ml-auto rounded-md border border-border px-2 py-0.5 text-xs text-muted-foreground hover:bg-secondary"
          >
            编辑
          </button>
        </div>

        {/* Inline edit form */}
        {editing && (
          <div className="mt-3 flex flex-wrap items-end gap-3 rounded-xl border border-primary/30 bg-primary/5 p-4">
            <label className="flex flex-col gap-1 text-xs text-muted-foreground">
              掌握度
              <select
                value={editMastery}
                onChange={(e) => setEditMastery(e.target.value)}
                className="rounded border px-2 py-1 text-sm"
              >
                <option value="">-</option>
                <option value="unknown">未标记</option>
                <option value="learning">学习中</option>
                <option value="reviewing">复习中</option>
                <option value="mastered">已掌握</option>
              </select>
            </label>
            <label className="flex flex-col gap-1 text-xs text-muted-foreground">
              重要度
              <select
                value={editImportance}
                onChange={(e) => setEditImportance(e.target.value)}
                className="rounded border px-2 py-1 text-sm"
              >
                <option value="">-</option>
                <option value="low">低</option>
                <option value="medium">中</option>
                <option value="high">高</option>
                <option value="critical">紧急</option>
              </select>
            </label>
            <label className="flex flex-col gap-1 text-xs text-muted-foreground">
              状态
              <select
                value={editStatus}
                onChange={(e) => setEditStatus(e.target.value)}
                className="rounded border px-2 py-1 text-sm"
              >
                <option value="">-</option>
                <option value="extracted">已提取</option>
                <option value="cleaned">已清洗</option>
                <option value="active">活跃</option>
                <option value="resolved">已解决</option>
              </select>
            </label>
            <button
              onClick={handleSave}
              disabled={updateMutation.isPending}
              className="rounded bg-primary px-3 py-1 text-xs text-primary-foreground hover:bg-primary/90"
            >
              {updateMutation.isPending ? '保存中...' : '保存'}
            </button>
            <button
              onClick={() => setEditing(false)}
              className="rounded px-3 py-1 text-xs text-muted-foreground hover:bg-secondary"
            >
              取消
            </button>
          </div>
        )}

        {/* Markdown body */}
        <div className="mt-6 rounded-2xl border border-border bg-white p-6 shadow-sm">
          {data.markdown_body ? (
            <Markdown math extraComponents={{ a: WikiLinkRenderer as any }}>
              {data.markdown_body}
            </Markdown>
          ) : (
            <p className="text-sm text-muted-foreground">暂无正文内容</p>
          )}
        </div>

        {/* Version history */}
        {versionData && versionData.versions.length > 0 && (
          <div className="mt-6 rounded-2xl border border-border bg-white p-5 shadow-sm">
            <h3 className="mb-3 text-sm font-semibold text-foreground">
              版本历史 ({versionData.versions.length})
            </h3>
            <div className="space-y-1">
              {versionData.versions.map((v) => (
                <div key={v.id} className="flex items-center justify-between rounded bg-secondary/40 px-3 py-1.5 text-xs">
                  <code className="text-muted-foreground">{v.content_hash.slice(0, 12)}</code>
                  <span className="text-muted-foreground">
                    {v.created_at ? new Date(v.created_at).toLocaleString('zh-CN') : '-'}
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Right: Properties, Frontmatter, Relationships, Path */}
      <aside className="hidden w-56 flex-shrink-0 xl:block">
        <div className="sticky top-6 space-y-4">
          {/* Properties */}
          <div className="rounded-xl border border-border bg-white p-4 shadow-sm">
            <h3 className="mb-3 text-xs font-semibold uppercase text-muted-foreground">属性</h3>
            <dl className="space-y-2 text-xs">
              <div className="flex justify-between">
                <dt className="text-muted-foreground">类型</dt>
                <dd className="font-medium">{docTypeLabel(data.document_type) || '-'}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-muted-foreground">状态</dt>
                <dd className="font-medium">{docStatusLabel(data.status) || '-'}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-muted-foreground">掌握度</dt>
                <dd className="font-medium">{masteryLabel(data.mastery) || '-'}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-muted-foreground">重要度</dt>
                <dd className="font-medium">{importanceLabel(data.importance) || '-'}</dd>
              </div>
            </dl>
          </div>

          {/* Frontmatter */}
          {hasFrontmatter && (
            <div className="rounded-xl border border-border bg-white p-4 shadow-sm">
              <h3 className="mb-2 text-xs font-semibold uppercase text-muted-foreground">YAML 元数据</h3>
              <dl className="space-y-1.5 text-xs max-h-48 overflow-y-auto">
                {Object.entries(frontmatter).map(([key, val]) => (
                  <div key={key} className="flex justify-between gap-2">
                    <dt className="text-muted-foreground shrink-0">{key}</dt>
                    <dd className="font-medium text-right truncate">{String(val ?? '-')}</dd>
                  </div>
                ))}
              </dl>
            </div>
          )}

          {/* Relationships */}
          {data.edges.length > 0 && (
            <div className="rounded-xl border border-border bg-white p-4 shadow-sm">
              <h3 className="mb-3 text-xs font-semibold uppercase text-muted-foreground">
                关系 ({data.edges.length})
              </h3>
              <div className="space-y-1.5">
                {data.edges.map((edge, i) => (
                  <button
                    key={i}
                    onClick={async () => {
                      try {
                        // Resolve the target label as a wikilink to find its document
                        const result = await resolveWikiLink(edge.target_label)
                        navigate(`/knowledge/${result.document_id}`)
                      } catch {
                        // ignore
                      }
                    }}
                    className="w-full rounded-md bg-secondary px-2 py-1.5 text-xs text-left hover:bg-secondary/70 transition-colors"
                  >
                    <span className="font-medium text-foreground">
                      {edgeLabels[edge.edge_type] || edge.edge_type}
                    </span>
                    <span className="mx-1 text-muted-foreground">→</span>
                    <span className="text-muted-foreground">{edge.target_label}</span>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Related Documents */}
          {relatedData && relatedData.results.filter((r) => r.id !== documentId).length > 0 && (
            <div className="rounded-xl border border-border bg-white p-4 shadow-sm">
              <h3 className="mb-2 text-xs font-semibold uppercase text-muted-foreground">相关文档</h3>
              <div className="space-y-1.5 max-h-48 overflow-y-auto">
                {relatedData.results
                  .filter((r) => r.id !== documentId)
                  .slice(0, 6)
                  .map((r) => (
                    <Link
                      key={r.id}
                      to={`/knowledge/${r.id}`}
                      className="block rounded-lg bg-muted/50 px-2.5 py-1.5 text-xs text-muted-foreground hover:bg-muted hover:text-foreground transition-colors truncate"
                    >
                      <span className="font-medium text-foreground">{r.title || r.relative_path.split('/').pop()}</span>
                      {r.course_code && <span className="ml-1.5 text-muted-foreground/60">[{r.course_code}]</span>}
                    </Link>
                  ))}
              </div>
            </div>
          )}

          {/* Path */}
          <div className="rounded-xl border border-border bg-white p-4 shadow-sm">
            <h3 className="mb-2 text-xs font-semibold uppercase text-muted-foreground">路径</h3>
            <p className="text-xs text-muted-foreground break-all">{data.relative_path}</p>
          </div>
        </div>
      </aside>
    </div>
  )
}
