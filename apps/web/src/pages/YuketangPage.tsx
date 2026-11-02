import { useState } from 'react'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { useTitle } from '../lib/useTitle'
import {
  clearYuketangSession,
  downloadYuketangCoursewarePdf,
  getYuketangCourseware,
  getYuketangOverview,
  getYuketangStatus,
  saveYuketangSession,
  syncYuketang,
  type YktActivity,
  type YktCourse,
  type YktCourseware,
} from '../api/yuketang'
import { confirm } from '../components/ui/ConfirmDialog'

type Tab = 'courses' | 'assignments' | 'courseware'

const fmtTime = (ms?: number) => {
  if (!ms) return '—'
  const d = new Date(ms)
  if (Number.isNaN(d.getTime())) return '—'
  return d.toLocaleString('zh-CN', {
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  })
}

const fmtIso = (iso?: string | null) => {
  if (!iso) return '从未同步'
  const d = new Date(iso)
  if (Number.isNaN(d.getTime())) return iso
  return d.toLocaleString('zh-CN', {
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  })
}

function Stat({ label, value, tone = 'text-foreground' }: { label: string; value: number | string; tone?: string }) {
  return (
    <div className="rounded-xl border border-border bg-white px-4 py-3">
      <div className="text-xs text-muted-foreground">{label}</div>
      <div className={`mt-1 text-xl font-bold ${tone}`}>{value}</div>
    </div>
  )
}

function SetupCard({ onSaved }: { onSaved: () => void }) {
  const [sessionid, setSessionid] = useState('')
  const [error, setError] = useState('')
  const queryClient = useQueryClient()
  const mutation = useMutation({
    mutationFn: () => saveYuketangSession(sessionid.trim()),
    onSuccess: async () => {
      setSessionid('')
      await queryClient.invalidateQueries({ queryKey: ['ykt-status'] })
      await queryClient.invalidateQueries({ queryKey: ['ykt-overview'] })
      onSaved()
    },
    onError: (err) => setError(err instanceof Error ? err.message : '保存失败'),
  })

  return (
    <div className="mx-auto max-w-2xl space-y-5">
      <div className="rounded-2xl border border-border bg-white p-6 shadow-sm">
        <h2 className="text-lg font-semibold">连接长江雨课堂</h2>
        <p className="mt-2 text-sm text-muted-foreground">
          只读同步课程、作业、公告和课件；不会签到、答题或提交作业，也不会保存你的密码。
        </p>

        <ol className="mt-4 space-y-1.5 text-sm text-muted-foreground">
          <li>1. 浏览器打开并登录 <span className="font-medium text-foreground">changjiang.yuketang.cn</span></li>
          <li>2. F12 → Application → Cookies → 选中该域名</li>
          <li>3. 找到 <span className="font-medium text-foreground">sessionid</span>，复制它的值</li>
          <li>4. 粘贴到下面，保存后会立即同步</li>
        </ol>

        <div className="mt-5 space-y-3">
          <input
            type="password"
            value={sessionid}
            onChange={(e) => {
              setSessionid(e.target.value)
              setError('')
            }}
            placeholder="粘贴 sessionid"
            autoComplete="off"
            spellCheck={false}
            className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-sm outline-none transition-colors focus:border-primary"
          />
          {error && (
            <p className="rounded-lg border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">{error}</p>
          )}
          <button
            onClick={() => {
              setError('')
              mutation.mutate()
            }}
            disabled={!sessionid.trim() || mutation.isPending}
            className="w-full rounded-lg bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {mutation.isPending ? '验证中…' : '保存并同步'}
          </button>
          <p className="text-xs text-muted-foreground">
            首次同步会拉取所有课程的活动和进度，可能需要几十秒。
          </p>
        </div>
      </div>
    </div>
  )
}

function CoursewarePanel({ lesson, onClose }: { lesson: YktActivity; onClose: () => void }) {
  const lessonId = lesson.courseware_id || lesson.id
  const [exporting, setExporting] = useState(false)
  const [exportError, setExportError] = useState('')
  const [exportNotice, setExportNotice] = useState('')
  const { data, isLoading, error, refetch } = useQuery<YktCourseware>({
    queryKey: ['ykt-courseware', lessonId],
    queryFn: () => getYuketangCourseware(lessonId),
    staleTime: 6 * 60 * 60 * 1000,
  })

  const exportPdf = async () => {
    setExporting(true)
    setExportError('')
    setExportNotice('')
    try {
      await downloadYuketangCoursewarePdf(
        lessonId,
        data?.title || lesson.title || '雨课堂课件',
      )
      setExportNotice('PDF 已生成。手机端已保存到 Documents/CyberMe，并打开分享面板。')
    } catch (err) {
      setExportError(err instanceof Error ? err.message : '导出失败')
    } finally {
      setExporting(false)
    }
  }

  return (
    <div className="fixed inset-0 z-[60] flex items-end justify-center bg-black/45 p-0 sm:items-center sm:p-4" onClick={onClose}>
      <div
        className="flex max-h-[92vh] w-full max-w-5xl flex-col overflow-hidden rounded-t-2xl bg-background shadow-2xl sm:rounded-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-start justify-between gap-3 border-b border-border px-4 py-3 sm:px-6">
          <div className="min-w-0">
            <h2 className="truncate text-base font-semibold">{data?.title || lesson.title || '课程课件'}</h2>
            <p className="mt-0.5 truncate text-xs text-muted-foreground">
              {data?.course_name || '长江雨课堂'} {data?.teacher ? `· ${data.teacher}` : ''}
            </p>
          </div>
          <div className="flex shrink-0 gap-2">
            <button
              onClick={exportPdf}
              disabled={exporting || isLoading || !data?.presentations.some((p) => p.slides.some((s) => s.image))}
              className="rounded-lg bg-primary px-3 py-1.5 text-sm font-medium text-primary-foreground disabled:cursor-not-allowed disabled:opacity-50"
            >
              {exporting ? '生成中…' : '导出 PDF'}
            </button>
            <button onClick={onClose} className="rounded-lg border border-border px-3 py-1.5 text-sm">
              关闭
            </button>
          </div>
        </div>

        <div className="overflow-y-auto p-4 sm:p-6">
          {exportError && (
            <p className="mb-3 rounded-lg border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
              {exportError}
            </p>
          )}
          {exportNotice && (
            <p className="mb-3 rounded-lg border border-emerald-200 bg-emerald-50 px-3 py-2 text-sm text-emerald-700">
              {exportNotice}
            </p>
          )}
          {isLoading && <p className="py-12 text-center text-sm text-muted-foreground">正在加载课件…</p>}
          {error && (
            <div className="py-12 text-center">
              <p className="text-sm text-red-600">{error instanceof Error ? error.message : '课件加载失败'}</p>
              <button onClick={() => refetch()} className="mt-3 rounded-lg border border-border px-4 py-2 text-sm">
                重试
              </button>
            </div>
          )}
          {data && data.presentations.length === 0 && (
            <p className="py-12 text-center text-sm text-muted-foreground">这节课没有可读取的课件。</p>
          )}
          {data?.presentations.map((presentation) => (
            <section key={presentation.id} className="mb-8">
              <div className="mb-3 flex items-center justify-between">
                <h3 className="text-sm font-semibold">{presentation.title || '课件'}</h3>
                <span className="text-xs text-muted-foreground">{presentation.slides.length} 页</span>
              </div>
              <div className="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-4">
                {presentation.slides.map((slide) => (
                  <a
                    key={`${presentation.id}-${slide.index}`}
                    href={slide.image}
                    target="_blank"
                    rel="noreferrer"
                    className="group overflow-hidden rounded-lg border border-border bg-white"
                  >
                    {slide.image ? (
                      <img
                        src={slide.image}
                        alt={`第 ${slide.index} 页`}
                        loading="lazy"
                        className="aspect-[4/3] w-full object-cover transition-transform group-hover:scale-[1.02]"
                      />
                    ) : (
                      <div className="flex aspect-[4/3] items-center justify-center text-xs text-muted-foreground">无图片</div>
                    )}
                    <div className="px-2 py-1.5 text-center text-xs text-muted-foreground">第 {slide.index} 页</div>
                  </a>
                ))}
              </div>
            </section>
          ))}
        </div>
      </div>
    </div>
  )
}

export default function YuketangPage() {
  useTitle('雨课堂')
  const [tab, setTab] = useState<Tab>('courses')
  const [selectedLesson, setSelectedLesson] = useState<(YktActivity & { course_name?: string }) | null>(null)
  const [selectedCourseName, setSelectedCourseName] = useState<string | null>(null)
  const queryClient = useQueryClient()

  const statusQuery = useQuery({ queryKey: ['ykt-status'], queryFn: getYuketangStatus, refetchInterval: 5_000 })
  const overviewQuery = useQuery({
    queryKey: ['ykt-overview'],
    queryFn: () => getYuketangOverview(),
    enabled: statusQuery.data?.configured === true,
    refetchInterval: 5_000,
  })

  const syncMutation = useMutation({
    mutationFn: syncYuketang,
    onSuccess: (data) => {
      queryClient.setQueryData(['ykt-overview'], data)
      queryClient.invalidateQueries({ queryKey: ['ykt-status'] })
    },
  })

  const clearMutation = useMutation({
    mutationFn: clearYuketangSession,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['ykt-status'] })
      await queryClient.invalidateQueries({ queryKey: ['ykt-overview'] })
    },
  })

  const overview = overviewQuery.data
  const courses = overview?.courses ?? []
  const assignments = overview?.assignments ?? []
  const coursewareCourses = courses.filter((course: YktCourse) => course.lessons.length > 0)
  const totalLessons = courses.reduce((sum: number, course: YktCourse) => sum + course.lessons.length, 0)
  const coursewareGroups = (() => {
    const groups = new Map<string, { name: string; teacher: string; lessons: (YktActivity & { course_name: string })[] }>()
    for (const course of coursewareCourses) {
      const name = course.name || '未命名课程'
      const group = groups.get(name) || { name, teacher: course.teacher || '', lessons: [] }
      for (const lesson of course.lessons) {
        group.lessons.push({ ...lesson, course_name: name })
      }
      groups.set(name, group)
    }
    return [...groups.values()]
  })()
  const activeGroup = coursewareGroups.find((group) => group.name === selectedCourseName)
  const pending = assignments.filter((a) => a.pending).length

  if (statusQuery.isLoading) {
    return <div className="py-24 text-center text-sm text-muted-foreground">正在检查雨课堂连接…</div>
  }

  if (statusQuery.error) {
    return (
      <div className="rounded-2xl border border-red-200 bg-red-50 p-6 text-sm text-red-700">
        雨课堂状态读取失败：{statusQuery.error instanceof Error ? statusQuery.error.message : '未知错误'}
      </div>
    )
  }

  if (!statusQuery.data?.configured) {
    return (
      <div className="space-y-5 pb-8">
        <div>
          <h1 className="text-2xl font-bold">雨课堂</h1>
          <p className="mt-1 text-sm text-muted-foreground">长江雨课堂 · 只读同步课程、作业和课件</p>
        </div>
        <SetupCard onSaved={() => undefined} />
      </div>
    )
  }

  const tabs: { id: Tab; label: string; count?: number }[] = [
    { id: 'courses', label: '课程', count: courses.length },
    { id: 'assignments', label: '作业', count: pending },
    { id: 'courseware', label: '课件', count: coursewareGroups.length },
  ]

  return (
    <div className="space-y-5 pb-8">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <h1 className="text-2xl font-bold">雨课堂</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {overview?.account?.name ? `${overview.account.name}` : '长江雨课堂'} · 只读同步
            {' · '}
            上次同步 {fmtIso(overview?.last_sync || statusQuery.data.last_sync)}
          </p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => syncMutation.mutate()}
            disabled={syncMutation.isPending}
            className="rounded-lg border border-border bg-white px-3 py-2 text-sm font-medium hover:bg-secondary disabled:opacity-50"
          >
            {syncMutation.isPending ? '同步中…' : '立即同步'}
          </button>
          <button
            onClick={async () => {
              const ok = await confirm({
                title: '断开雨课堂？',
                message: '会清除本地 sessionid 和已同步缓存。',
                confirmLabel: '断开',
                danger: true,
              })
              if (ok) clearMutation.mutate()
            }}
            disabled={clearMutation.isPending}
            className="rounded-lg border border-border bg-white px-3 py-2 text-sm text-muted-foreground hover:bg-secondary disabled:opacity-50"
          >
            断开
          </button>
        </div>
      </div>

      {syncMutation.error && (
        <p className="rounded-lg border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
          {syncMutation.error instanceof Error ? syncMutation.error.message : '同步失败'}
        </p>
      )}
      {overview?.last_error && (
        <p className="rounded-lg border border-amber-200 bg-amber-50 px-3 py-2 text-sm text-amber-800">
          上次同步有问题：{overview.last_error}
        </p>
      )}

      <div className="grid gap-3 sm:grid-cols-3">
        <Stat label="课程" value={courses.length} />
        <Stat label="待完成作业" value={pending} tone={pending > 0 ? 'text-amber-600' : 'text-emerald-600'} />
        <Stat label="可看课件" value={totalLessons} />
      </div>

      <div className="flex gap-1 border-b border-border">
        {tabs.map((t) => (
          <button
            key={t.id}
            onClick={() => setTab(t.id)}
            className={`relative px-4 py-2.5 text-sm font-medium transition-colors ${
              tab === t.id ? 'text-primary' : 'text-muted-foreground hover:text-foreground'
            }`}
          >
            {t.label}
            {typeof t.count === 'number' && <span className="ml-1 text-xs opacity-60">{t.count}</span>}
            {tab === t.id && <span className="absolute inset-x-0 -bottom-px h-0.5 bg-primary" />}
          </button>
        ))}
      </div>

      {overview?.syncing && (
        <p className="rounded-lg border border-blue-200 bg-blue-50 px-3 py-2 text-sm text-blue-800">
          正在后台同步课程、作业和课件，页面会自动刷新。首次同步可能需要几十秒。
        </p>
      )}
      {overviewQuery.isLoading && <p className="py-12 text-center text-sm text-muted-foreground">正在同步雨课堂…</p>}

      {overviewQuery.error && (
        <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-700">
          同步失败：{overviewQuery.error instanceof Error ? overviewQuery.error.message : '未知错误'}
          <button onClick={() => overviewQuery.refetch()} className="ml-3 underline">重试</button>
        </div>
      )}

      {tab === 'courses' && (
        <div className="grid gap-3 md:grid-cols-2">
          {courses.map((course) => (
            <div key={course.classroom_id} className="rounded-xl border border-border bg-white p-4 shadow-sm">
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                  <h3 className="truncate font-semibold">{course.name || '未命名课程'}</h3>
                  <p className="mt-1 truncate text-xs text-muted-foreground">
                    {course.teacher || '教师未知'} · {course.term || '—'} · {course.class_name || ''}
                  </p>
                </div>
                {course.pending_count > 0 && (
                  <span className="shrink-0 rounded-full bg-amber-100 px-2 py-0.5 text-xs font-medium text-amber-700">
                    {course.pending_count} 个待完成
                  </span>
                )}
              </div>
              <div className="mt-3 flex gap-4 text-xs text-muted-foreground">
                <span>作业 {course.assignments.length}</span>
                <span>课件 {course.lessons.length}</span>
                <span>公告 {course.announcements.length}</span>
              </div>
              {course.deadlines.length > 0 && (
                <div className="mt-3 space-y-1 border-t border-border pt-2">
                  {course.deadlines.slice(0, 3).map((d) => (
                    <div key={d.leaf_id} className="flex justify-between gap-2 text-xs">
                      <span className="truncate text-muted-foreground">{d.name}</span>
                      <span className="shrink-0 text-foreground">{fmtTime(d.deadline)}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
          {courses.length === 0 && !overview?.syncing && <p className="py-8 text-sm text-muted-foreground">没有读到课程。</p>}
        </div>
      )}

      {tab === 'assignments' && (
        <div className="overflow-hidden rounded-xl border border-border bg-white">
          {assignments.length === 0 ? (
            <p className="p-6 text-sm text-muted-foreground">{overview?.syncing ? '正在同步作业…' : '没有读到作业。'}</p>
          ) : (
            assignments.map((a) => (
              <div key={`${a.classroom_id}-${a.id}`} className="flex items-center gap-3 border-b border-border px-4 py-3 last:border-0">
                <span className={`h-2 w-2 shrink-0 rounded-full ${
                  a.pending ? 'bg-amber-500' : a.expired ? 'bg-slate-300' : 'bg-emerald-500'
                }`} />
                <div className="min-w-0 flex-1">
                  <p className="truncate text-sm font-medium">{a.title || a.type_name}</p>
                  <p className="mt-0.5 truncate text-xs text-muted-foreground">
                    {a.course_name} · {a.type_name} · {fmtTime(a.create_time)}
                    {a.deadline ? ` · 截止 ${fmtTime(a.deadline)}` : ''}
                  </p>
                </div>
                <span className={`shrink-0 text-xs ${
                  a.pending ? 'text-amber-600' : a.expired ? 'text-muted-foreground' : 'text-emerald-600'
                }`}>
                  {a.pending ? '待完成' : a.expired ? '已截止' : a.finished ? '已完成' : '未完成'}
                </span>
              </div>
            ))
          )}
        </div>
      )}

      {tab === 'courseware' && (
        selectedCourseName && activeGroup ? (
          <div className="space-y-3">
            <button
              onClick={() => setSelectedCourseName(null)}
              className="text-sm text-muted-foreground hover:text-foreground"
            >
              ← 全部课程
            </button>
            <div className="rounded-xl border border-border bg-white px-4 py-3">
              <h3 className="font-semibold">{activeGroup.name}</h3>
              <p className="mt-0.5 text-xs text-muted-foreground">
                {activeGroup.teacher || '教师未知'} · {activeGroup.lessons.length} 节课
              </p>
            </div>
            <div className="grid gap-3 md:grid-cols-2">
              {activeGroup.lessons.map((lesson) => (
                <button
                  key={`${lesson.course_name}-${lesson.id}`}
                  onClick={() => setSelectedLesson(lesson)}
                  className="rounded-xl border border-border bg-white p-4 text-left shadow-sm transition-shadow hover:shadow-md"
                >
                  <div className="flex items-center justify-between gap-3">
                    <h3 className="truncate text-sm font-semibold">{lesson.title || '上课记录'}</h3>
                    <span className="shrink-0 text-xs text-muted-foreground">{fmtTime(lesson.create_time)}</span>
                  </div>
                  <p className="mt-1 truncate text-xs text-muted-foreground">点击查看课件</p>
                </button>
              ))}
            </div>
          </div>
        ) : (
          <div className="grid gap-3 md:grid-cols-2">
            {coursewareGroups.map((group) => (
              <button
                key={group.name}
                onClick={() => setSelectedCourseName(group.name)}
                className="rounded-xl border border-border bg-white p-4 text-left shadow-sm transition-shadow hover:shadow-md"
              >
                <div className="flex items-center justify-between gap-3">
                  <h3 className="truncate text-sm font-semibold">{group.name}</h3>
                  <span className="shrink-0 rounded-full bg-secondary px-2 py-0.5 text-xs text-muted-foreground">
                    {group.lessons.length} 节课
                  </span>
                </div>
                <p className="mt-1 truncate text-xs text-muted-foreground">
                  {group.teacher || '教师未知'} · 点击按课程查看
                </p>
              </button>
            ))}
            {coursewareGroups.length === 0 && !overview?.syncing && (
              <p className="py-8 text-sm text-muted-foreground">没有读到带课件的课程。</p>
            )}
          </div>
        )
      )}

      {selectedLesson && <CoursewarePanel lesson={selectedLesson} onClose={() => setSelectedLesson(null)} />}
    </div>
  )
}
