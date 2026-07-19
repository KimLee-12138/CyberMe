import { useState, useMemo } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { fetchCourses } from '../api/knowledge'
import { useTitle } from '../lib/useTitle'

type SortKey = 'name' | 'knowledge' | 'indexed'

export default function CourseListPage() {
  useTitle('课程')
  const [search, setSearch] = useState('')
  const [sortBy, setSortBy] = useState<SortKey>('name')

  const { data, isLoading, error } = useQuery({
    queryKey: ['courses'],
    queryFn: fetchCourses,
  })

  const filtered = useMemo(() => {
    if (!data?.courses) return []
    let list = data.courses
    if (search) {
      const q = search.toLowerCase()
      list = list.filter(
        (c) =>
          c.code.toLowerCase().includes(q) ||
          c.name.toLowerCase().includes(q),
      )
    }
    return [...list].sort((a, b) => {
      if (sortBy === 'knowledge') return b.knowledge_count - a.knowledge_count
      if (sortBy === 'indexed') {
        const aTime = a.last_indexed_at ? new Date(a.last_indexed_at).getTime() : 0
        const bTime = b.last_indexed_at ? new Date(b.last_indexed_at).getTime() : 0
        return bTime - aTime
      }
      return a.name.localeCompare(b.name, 'zh-CN')
    })
  }, [data, search, sortBy])

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">课程列表</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          {data?.courses.length || 0} 门课程 — 从 Vault 自动发现
        </p>
      </div>

      <div className="flex flex-wrap gap-3">
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="搜索课程名或代码..."
          className="flex-1 rounded-xl border border-border bg-white px-4 py-2 text-sm placeholder:text-muted-foreground focus:border-primary focus:outline-none"
        />
        <select
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value as SortKey)}
          className="rounded-xl border border-border bg-white px-3 py-2 text-sm"
        >
          <option value="name">按名称</option>
          <option value="knowledge">按知识数量</option>
          <option value="indexed">按索引时间</option>
        </select>
      </div>

      {isLoading && (
        <div className="py-12 text-center text-muted-foreground">加载中...</div>
      )}

      {error && (
        <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          加载失败，请确认后端已启动
        </div>
      )}

      {!isLoading && filtered.length === 0 && (
        <div className="rounded-2xl border border-border bg-white py-12 text-center shadow-sm">
          <span className="text-3xl">📚</span>
          <p className="mt-3 text-sm text-muted-foreground">
            {search ? '未找到匹配的课程' : '暂无课程数据'}
          </p>
        </div>
      )}

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {filtered.map((course) => (
          <Link
            key={course.id}
            to={`/courses/${course.id}`}
            className="group rounded-2xl border border-border bg-white p-5 shadow-sm transition-all hover:border-primary/30 hover:shadow-md"
          >
            <div className="flex items-start justify-between">
              <span className="rounded-lg bg-primary/10 px-2.5 py-1 text-xs font-bold text-primary">
                {course.code}
              </span>
              {course.last_indexed_at && (
                <span className="text-xs text-muted-foreground">已索引</span>
              )}
            </div>
            <h3 className="mt-3 text-sm font-semibold text-foreground group-hover:text-primary transition-colors line-clamp-2">
              {course.name}
            </h3>
            <div className="mt-3 flex items-center gap-4 text-xs text-muted-foreground">
              <span>知识点 {course.knowledge_count}</span>
              {course.extract_count > 0 && (
                <span>提取 {course.extract_count}</span>
              )}
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
