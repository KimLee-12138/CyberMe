import { useState, useMemo } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { fetchCourse } from '../api/knowledge'
import { importanceLabel, masteryLabel, docStatusLabel } from '../lib/enums'
import { useTitle } from '../lib/useTitle'

const typeLabels: Record<string, string> = {
  concept: '知识点', moc: 'MOC', example: '例题',
  mistake: '错题', formula: '公式', extract: '提取材料',
  project: '项目', chapter: '章节', unknown: '未分类',
  'problem-set': '习题集',
}

const masteryColors: Record<string, string> = {
  mastered: 'bg-emerald-100 text-emerald-700',
  reviewing: 'bg-amber-100 text-amber-700',
  learning: 'bg-blue-100 text-blue-700',
  unknown: 'bg-gray-100 text-gray-500',
}

export default function CourseDetailPage() {
  useTitle('课程详情')
  const { courseId } = useParams<{ courseId: string }>()
  const [search, setSearch] = useState('')
  const [collapsed, setCollapsed] = useState<Set<string>>(new Set())

  const { data, isLoading } = useQuery({
    queryKey: ['course', courseId],
    queryFn: () => fetchCourse(courseId!),
    enabled: !!courseId,
  })

  const byType = useMemo(() => {
    if (!data) return {}
    const groups: Record<string, typeof data.documents> = {}
    let docs = data.documents
    if (search) {
      const q = search.toLowerCase()
      docs = docs.filter((d) =>
        (d.title || '').toLowerCase().includes(q) ||
        d.relative_path.toLowerCase().includes(q),
      )
    }
    for (const doc of docs) {
      const t = doc.document_type || 'unknown'
      if (!groups[t]) groups[t] = []
      groups[t].push(doc)
    }
    return groups
  }, [data, search])

  const toggle = (key: string) => {
    setCollapsed((prev) => {
      const next = new Set(prev)
      if (next.has(key)) next.delete(key)
      else next.add(key)
      return next
    })
  }

  if (isLoading)
    return <div className="py-12 text-center text-muted-foreground">加载中...</div>
  if (!data)
    return <div className="py-12 text-center text-muted-foreground">课程未找到</div>

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div>
        <Link to="/courses" className="mb-2 inline-flex text-xs text-muted-foreground hover:text-foreground">
          ← 返回课程列表
        </Link>
        <h1 className="text-2xl font-bold">{data.name}</h1>
        <div className="mt-2 flex items-center gap-3">
          <span className="rounded-md bg-primary/10 px-2.5 py-0.5 text-xs font-bold text-primary">
            {data.code}
          </span>
          <span className="text-sm text-muted-foreground">{data.documents.length} 篇</span>
        </div>
      </div>

      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="搜索文档标题..."
        className="w-full rounded-xl border border-border bg-white px-4 py-2 text-sm placeholder:text-muted-foreground focus:border-primary focus:outline-none"
      />

      {Object.entries(byType).map(([docType, docs]) => (
        <div key={docType} className="rounded-2xl border border-border bg-white shadow-sm">
          <button
            onClick={() => toggle(docType)}
            className="flex w-full items-center justify-between border-b border-border px-5 py-3 text-left"
          >
            <h2 className="text-sm font-semibold">
              {typeLabels[docType] || docType}
              <span className="ml-2 text-xs font-normal text-muted-foreground">({docs.length})</span>
            </h2>
            <span className="text-xs text-muted-foreground">
              {collapsed.has(docType) ? '展开 ▸' : '折叠 ▾'}
            </span>
          </button>
          {!collapsed.has(docType) && (
            <div className="divide-y divide-border">
              {docs.map((doc) => (
                <Link
                  key={doc.id}
                  to={`/knowledge/${doc.id}`}
                  className="flex items-center justify-between px-5 py-3 transition-colors hover:bg-secondary/50"
                >
                  <div className="min-w-0 flex-1">
                    <p className="text-sm font-medium truncate">
                      {doc.title || doc.relative_path.split('/').pop()}
                    </p>
                    <p className="text-xs text-muted-foreground truncate">{doc.relative_path}</p>
                  </div>
                  <div className="ml-3 flex items-center gap-2 shrink-0">
                    {doc.importance && doc.importance !== 'low' && (
                      <span className="rounded-full bg-red-100 px-2 py-0.5 text-xs text-red-700">
                        {importanceLabel(doc.importance)}
                      </span>
                    )}
                    {doc.status && (
                      <span className="rounded-full bg-secondary px-2 py-0.5 text-xs text-muted-foreground">
                        {docStatusLabel(doc.status)}
                      </span>
                    )}
                    {doc.mastery && (
                      <span className={`rounded-full px-2 py-0.5 text-xs ${masteryColors[doc.mastery] || 'bg-gray-100'}`}>
                        {masteryLabel(doc.mastery)}
                      </span>
                    )}
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>
      ))}

      {data.documents.length === 0 && (
        <div className="rounded-2xl border bg-white py-12 text-center shadow-sm">
          <p className="text-sm text-muted-foreground">暂无文档</p>
        </div>
      )}
    </div>
  )
}
