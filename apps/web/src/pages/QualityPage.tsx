import { useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import { useQuery } from '@tanstack/react-query'
import { AlertTriangle } from 'lucide-react'
import { useTitle } from '../lib/useTitle'
import {
  fetchCorpusCourses,
  fetchCorpusIssues,
  fetchCorpusStats,
} from '../api/corpus'
import type {
  CorpusCourse,
  CorpusIssues,
  CorpusStats,
  QualityStatus,
} from '../api/corpus'
import LoadingState from '../components/ui/LoadingState'

const QUALITY_ORDER: QualityStatus[] = ['official', 'review', 'candidate', 'duplicate', 'quarantine']

const STATUS_META: Record<QualityStatus, {
  label: string
  bar: string
  soft: string
  text: string
  dot: string
}> = {
  official: {
    label: '官方',
    bar: 'bg-emerald-500',
    soft: 'border-emerald-200 bg-emerald-50',
    text: 'text-emerald-700',
    dot: 'bg-emerald-500',
  },
  review: {
    label: '待复核',
    bar: 'bg-amber-400',
    soft: 'border-amber-200 bg-amber-50',
    text: 'text-amber-700',
    dot: 'bg-amber-400',
  },
  candidate: {
    label: '候选',
    bar: 'bg-sky-400',
    soft: 'border-sky-200 bg-sky-50',
    text: 'text-sky-700',
    dot: 'bg-sky-400',
  },
  duplicate: {
    label: '重复',
    bar: 'bg-slate-400',
    soft: 'border-slate-200 bg-slate-50',
    text: 'text-slate-600',
    dot: 'bg-slate-400',
  },
  quarantine: {
    label: '隔离',
    bar: 'bg-red-500',
    soft: 'border-red-200 bg-red-50',
    text: 'text-red-700',
    dot: 'bg-red-500',
  },
}

const STAGE_ACCENTS = [
  'from-slate-500 to-slate-400',
  'from-sky-500 to-sky-400',
  'from-violet-500 to-violet-400',
  'from-amber-500 to-amber-400',
  'from-emerald-500 to-emerald-400',
  'from-primary to-blue-400',
]

const RELATION_META: Record<string, { label: string; cls: string }> = {
  duplicate: { label: '重复', cls: 'bg-red-50 text-red-700 border-red-200' },
  parallel: { label: '并行版本', cls: 'bg-sky-50 text-sky-700 border-sky-200' },
  candidate: { label: '候选重复', cls: 'bg-amber-50 text-amber-700 border-amber-200' },
}

const fmt = (n: number | undefined | null) => Number(n ?? 0).toLocaleString('zh-CN')
const pct = (n: number, d: number) => (d > 0 ? `${((n / d) * 100).toFixed(1)}%` : '—')

function Section({
  title,
  desc,
  right,
  children,
  className = '',
}: {
  title: string
  desc?: string
  right?: ReactNode
  children: ReactNode
  className?: string
}) {
  return (
    <section className={`rounded-2xl border border-border bg-white p-5 shadow-sm ${className}`}>
      <div className="mb-4 flex flex-wrap items-start justify-between gap-2">
        <div>
          <h2 className="text-sm font-semibold text-foreground">{title}</h2>
          {desc && <p className="mt-0.5 text-xs text-muted-foreground">{desc}</p>}
        </div>
        {right}
      </div>
      {children}
    </section>
  )
}

function KpiCard({
  label,
  value,
  sub,
  accent,
}: {
  label: string
  value: string
  sub: string
  accent: string
}) {
  return (
    <div className="relative overflow-hidden rounded-2xl border border-border bg-white p-4 shadow-sm">
      <div className={`absolute inset-x-0 top-0 h-1 bg-gradient-to-r ${accent}`} />
      <p className="text-xs text-muted-foreground">{label}</p>
      <p className="mt-1 text-2xl font-bold tracking-tight text-foreground">{value}</p>
      <p className="mt-1 text-[11px] leading-relaxed text-muted-foreground">{sub}</p>
    </div>
  )
}

function StatusBar({
  quality,
  total,
  height = 'h-2.5',
  showTitle = true,
}: {
  quality: Record<QualityStatus, number>
  total: number
  height?: string
  showTitle?: boolean
}) {
  if (total <= 0) return <div className={`${height} rounded-full bg-muted`} />
  return (
    <div className={`flex overflow-hidden rounded-full bg-muted ${height}`}>
      {QUALITY_ORDER.map(s => {
        const n = quality[s] ?? 0
        if (!n) return null
        return (
          <div
            key={s}
            className={STATUS_META[s].bar}
            style={{ width: `${(n / total) * 100}%` }}
            title={showTitle ? `${STATUS_META[s].label} ${n}（${pct(n, total)}）` : undefined}
          />
        )
      })}
    </div>
  )
}

function FunnelCard({ stage, index }: { stage: CorpusStats['funnel'][number]; index: number }) {
  const kindLabel = stage.kind === 'files' ? '文件' : stage.kind === 'parts' ? '分节' : stage.kind === 'units' ? '单元' : '主题'
  return (
    <div className="flex flex-1 items-stretch gap-2">
      <div className="relative flex-1 overflow-hidden rounded-xl border border-border bg-secondary/20 p-3">
        <div className={`absolute inset-x-0 top-0 h-0.5 bg-gradient-to-r ${STAGE_ACCENTS[index] || STAGE_ACCENTS[0]}`} />
        <div className="flex items-center justify-between gap-1">
          <span className="text-[10px] font-medium text-muted-foreground">{kindLabel}</span>
          <span className="rounded bg-white/70 px-1 text-[9px] text-muted-foreground">{String(index + 1).padStart(2, '0')}</span>
        </div>
        <p className="mt-1 text-xl font-bold tabular-nums text-foreground">{fmt(stage.count)}</p>
        <p className="mt-0.5 text-[11px] font-medium text-foreground">{stage.label}</p>
        <p className="mt-1 min-h-[28px] text-[10px] leading-relaxed text-muted-foreground">{stage.note}</p>
      </div>
      {index < 5 && <span className="hidden shrink-0 items-center text-muted-foreground/50 xl:flex">→</span>}
    </div>
  )
}

function IssueTabs({ issues }: { issues: CorpusIssues }) {
  type Tab = 'conflicts' | 'quarantine' | 'formula' | 'duplicates' | 'writeback'
  const [tab, setTab] = useState<Tab>('conflicts')
  const [dupFilter, setDupFilter] = useState('all')

  const c = issues.counts
  const tabs: Array<{ key: Tab; label: string; count: number; tone: string }> = [
    { key: 'conflicts', label: '冲突', count: c.conflicts, tone: 'bg-red-500' },
    { key: 'quarantine', label: '隔离', count: c.quarantine, tone: 'bg-orange-500' },
    { key: 'formula', label: '公式缺失', count: c.formula_missing_notes, tone: 'bg-amber-500' },
    { key: 'duplicates', label: '近重复', count: c.near_duplicate_pairs, tone: 'bg-sky-500' },
    { key: 'writeback', label: '写回提案', count: c.writeback_total, tone: 'bg-violet-500' },
  ]

  const duplicates = useMemo(
    () => (dupFilter === 'all' ? issues.near_duplicates : issues.near_duplicates.filter(x => x.relation === dupFilter)),
    [issues.near_duplicates, dupFilter],
  )

  return (
    <Section
      title="问题清单"
      desc="冲突、隔离、公式缺失、近重复与写回提案；所有条目都可追到文件或笔记。"
      right={<span className="rounded-full bg-secondary px-2 py-1 text-[10px] text-muted-foreground">只读 · 不修改 Vault</span>}
    >
      <div className="mb-3 flex flex-wrap gap-1.5">
        {tabs.map(t => (
          <button
            key={t.key}
            onClick={() => setTab(t.key)}
            className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-xs transition-colors ${
              tab === t.key
                ? 'border-primary bg-primary/10 text-primary'
                : 'border-border text-muted-foreground hover:bg-secondary'
            }`}
          >
            <span className={`h-1.5 w-1.5 rounded-full ${t.tone}`} />
            {t.label}
            <span className="tabular-nums opacity-70">{fmt(t.count)}</span>
          </button>
        ))}
      </div>

      {tab === 'conflicts' && (
        <div className="space-y-2">
          {issues.conflicts.map((x, i) => (
            <div key={`${x.topic_id}-${i}`} className="rounded-xl border border-red-100 bg-red-50/40 p-3">
              <div className="flex flex-wrap items-center gap-2">
                <span className="rounded bg-white px-1.5 py-0.5 text-[10px] font-medium text-red-700">{x.course_name}</span>
                <span className="text-xs font-semibold text-foreground">{x.title}</span>
                <span className="font-mono text-[10px] text-muted-foreground">{x.topic_id}</span>
              </div>
              <p className="mt-1.5 text-xs leading-relaxed text-foreground/80">{x.conflict}</p>
              <p className="mt-1 break-all font-mono text-[10px] text-muted-foreground">{x.note_path}</p>
            </div>
          ))}
          {issues.conflicts.length === 0 && <p className="py-8 text-center text-xs text-muted-foreground">没有冲突</p>}
        </div>
      )}

      {tab === 'quarantine' && (
        <div className="overflow-x-auto">
          <table className="w-full min-w-[720px] text-left text-xs">
            <thead className="border-b border-border text-[10px] uppercase text-muted-foreground">
              <tr>
                <th className="py-2 pr-3">课程</th>
                <th className="py-2 pr-3">文件</th>
                <th className="py-2 pr-3 text-right">字符</th>
                <th className="py-2 pr-3 text-right">质量分</th>
                <th className="py-2">原因</th>
              </tr>
            </thead>
            <tbody>
              {issues.quarantine.map(x => (
                <tr key={x.source_id} className="border-b border-border/60 last:border-0">
                  <td className="py-2 pr-3 whitespace-nowrap">{x.course_name}</td>
                  <td className="max-w-[420px] py-2 pr-3">
                    <p className="truncate">{x.rel}</p>
                    <p className="font-mono text-[10px] text-muted-foreground">{x.source_id}</p>
                  </td>
                  <td className="py-2 pr-3 text-right tabular-nums">{fmt(x.chars)}</td>
                  <td className="py-2 pr-3 text-right tabular-nums">{x.quality_score.toFixed(0)}</td>
                  <td className="py-2">
                    <span className="rounded bg-red-50 px-1.5 py-0.5 text-[10px] text-red-700">{x.reasons || 'low_content'}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {tab === 'formula' && (
        <div className="max-h-[420px] overflow-auto">
          <table className="w-full min-w-[720px] text-left text-xs">
            <thead className="sticky top-0 border-b border-border bg-white text-[10px] uppercase text-muted-foreground">
              <tr>
                <th className="py-2 pr-3">笔记</th>
                <th className="py-2 pr-3">课程</th>
                <th className="py-2 pr-3">来源</th>
                <th className="py-2">标记</th>
              </tr>
            </thead>
            <tbody>
              {issues.formula_missing.map(x => (
                <tr key={x.note_id} className="border-b border-border/60 last:border-0">
                  <td className="max-w-[380px] py-2 pr-3">
                    <p className="truncate font-medium text-foreground">{x.title}</p>
                    <p className="font-mono text-[10px] text-muted-foreground">{x.note_id}</p>
                  </td>
                  <td className="py-2 pr-3 whitespace-nowrap">{x.course_name}</td>
                  <td className="py-2 pr-3 text-muted-foreground">{x.source_count} 个来源</td>
                  <td className="py-2">
                    <span className="rounded bg-amber-50 px-1.5 py-0.5 text-[10px] text-amber-700">formula_missing</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {tab === 'duplicates' && (
        <div>
          <div className="mb-2 flex flex-wrap gap-1">
            {[
              { key: 'all', label: '全部', count: issues.near_duplicates.length },
              { key: 'duplicate', label: '重复', count: c.near_duplicate_duplicate },
              { key: 'parallel', label: '并行版本', count: c.near_duplicate_parallel },
              { key: 'candidate', label: '候选重复', count: c.near_duplicate_candidate },
            ].map(f => (
              <button
                key={f.key}
                onClick={() => setDupFilter(f.key)}
                className={`rounded-full px-2.5 py-1 text-[10px] ${
                  dupFilter === f.key ? 'bg-primary text-primary-foreground' : 'bg-secondary text-muted-foreground'
                }`}
              >
                {f.label} {f.count}
              </button>
            ))}
          </div>
          <div className="max-h-[420px] overflow-auto">
            <table className="w-full min-w-[760px] text-left text-xs">
              <thead className="sticky top-0 border-b border-border bg-white text-[10px] uppercase text-muted-foreground">
                <tr>
                  <th className="py-2 pr-3">类型</th>
                  <th className="py-2 pr-3">文件 A</th>
                  <th className="py-2 pr-3">文件 B</th>
                  <th className="py-2 pr-3 text-right">Jaccard</th>
                </tr>
              </thead>
              <tbody>
                {duplicates.slice(0, 120).map((x, i) => {
                  const meta = RELATION_META[x.relation] || { label: x.relation, cls: 'bg-secondary text-muted-foreground border-border' }
                  return (
                    <tr key={`${x.source_a}-${x.source_b}-${i}`} className="border-b border-border/60 last:border-0">
                      <td className="py-2 pr-3">
                        <span className={`rounded border px-1.5 py-0.5 text-[10px] ${meta.cls}`}>{meta.label}</span>
                      </td>
                      <td className="max-w-[280px] py-2 pr-3">
                        <p className="truncate">{x.rel_a}</p>
                        <p className="font-mono text-[10px] text-muted-foreground">{x.source_a}</p>
                      </td>
                      <td className="max-w-[280px] py-2 pr-3">
                        <p className="truncate">{x.rel_b}</p>
                        <p className="font-mono text-[10px] text-muted-foreground">{x.source_b}</p>
                      </td>
                      <td className="py-2 pr-3 text-right tabular-nums">{(x.jaccard * 100).toFixed(1)}%</td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
          {duplicates.length > 120 && (
            <p className="mt-2 text-[10px] text-muted-foreground">只显示前 120 条；完整数据见 `/api/v1/corpus/issues`。</p>
          )}
        </div>
      )}

      {tab === 'writeback' && (
        <div className="space-y-3">
          <div className="grid gap-2 sm:grid-cols-3">
            <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-3">
              <p className="text-[11px] text-emerald-700">新建笔记</p>
              <p className="text-xl font-bold text-emerald-800">{fmt(issues.writeback.create)}</p>
            </div>
            <div className="rounded-xl border border-sky-200 bg-sky-50 p-3">
              <p className="text-[11px] text-sky-700">追加补充</p>
              <p className="text-xl font-bold text-sky-800">{fmt(issues.writeback.append_supplement)}</p>
            </div>
            <div className="rounded-xl border border-slate-200 bg-slate-50 p-3">
              <p className="text-[11px] text-slate-600">跳过重复</p>
              <p className="text-xl font-bold text-slate-700">{fmt(issues.writeback.skip_duplicate)}</p>
            </div>
          </div>
          <div className="rounded-xl border border-amber-200 bg-amber-50 px-3 py-2 text-xs text-amber-800">
            Vault 未修改：{fmt(issues.writeback.total)} 条都是 proposal，需要人工审批。
          </div>
          <div className="space-y-1.5">
            {issues.writeback.sample.map(item => (
              <div key={item.note_id} className="flex flex-wrap items-center gap-2 rounded-lg bg-secondary/30 px-2.5 py-1.5 text-[11px]">
                <span className="rounded bg-white px-1.5 py-0.5 text-[10px] text-muted-foreground">{item.action}</span>
                <span className="font-medium text-foreground">{item.title}</span>
                <span className="break-all font-mono text-[10px] text-muted-foreground">{item.target_path}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </Section>
  )
}

function CourseTable({ courses }: { courses: CorpusCourse[] }) {
  const totals = courses.reduce(
    (acc, c) => {
      acc.included += c.included
      acc.distill += c.distill
      acc.sections += c.sections
      acc.units += c.units
      acc.topics += c.topics
      acc.formula_missing += c.formula_missing
      acc.conflicts += c.conflicts
      acc.official += c.quality.official
      acc.review += c.quality.review
      return acc
    },
    { included: 0, distill: 0, sections: 0, units: 0, topics: 0, formula_missing: 0, conflicts: 0, official: 0, review: 0 },
  )

  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-[980px] text-left text-xs">
        <thead className="border-b border-border text-[10px] uppercase text-muted-foreground">
          <tr>
            <th className="py-2 pr-3">课程</th>
            <th className="py-2 pr-3 text-right">纳入</th>
            <th className="py-2 pr-3 text-right">蒸馏</th>
            <th className="py-2 pr-3 text-right">章节</th>
            <th className="py-2 pr-3 text-right">单元</th>
            <th className="py-2 pr-3 text-right">主题/笔记</th>
            <th className="min-w-[150px] py-2 pr-3">质量分级</th>
            <th className="py-2 pr-3 text-right">公式缺失</th>
            <th className="py-2 text-right">冲突</th>
          </tr>
        </thead>
        <tbody>
          {courses.map(c => {
            const total = c.included || 1
            return (
              <tr key={c.course} className="border-b border-border/60 last:border-0 hover:bg-secondary/20">
                <td className="py-2 pr-3">
                  <span className="font-medium text-foreground">{c.name}</span>
                  <span className="ml-1 font-mono text-[10px] text-muted-foreground">{c.course}</span>
                </td>
                <td className="py-2 pr-3 text-right tabular-nums">{c.included}</td>
                <td className="py-2 pr-3 text-right tabular-nums">{c.distill}</td>
                <td className="py-2 pr-3 text-right tabular-nums">{c.sections}</td>
                <td className="py-2 pr-3 text-right tabular-nums">{fmt(c.units)}</td>
                <td className="py-2 pr-3 text-right tabular-nums">{c.topics}</td>
                <td className="py-2 pr-3">
                  <StatusBar quality={c.quality} total={total} height="h-2" />
                  <div className="mt-0.5 flex justify-between text-[9px] text-muted-foreground">
                    <span>{pct(c.quality.official, total)} 官方</span>
                    <span>{pct(c.quality.review, total)} 复核</span>
                  </div>
                </td>
                <td className={`py-2 pr-3 text-right tabular-nums ${c.formula_missing ? 'text-amber-700' : 'text-muted-foreground'}`}>
                  {c.formula_missing || '—'}
                </td>
                <td className={`py-2 text-right tabular-nums ${c.conflicts ? 'text-red-600' : 'text-muted-foreground'}`}>
                  {c.conflicts || '—'}
                </td>
              </tr>
            )
          })}
        </tbody>
        <tfoot className="border-t border-border bg-secondary/30 font-medium">
          <tr>
            <td className="py-2 pr-3">合计</td>
            <td className="py-2 pr-3 text-right tabular-nums">{totals.included}</td>
            <td className="py-2 pr-3 text-right tabular-nums">{totals.distill}</td>
            <td className="py-2 pr-3 text-right tabular-nums">{totals.sections}</td>
            <td className="py-2 pr-3 text-right tabular-nums">{fmt(totals.units)}</td>
            <td className="py-2 pr-3 text-right tabular-nums">{totals.topics}</td>
            <td className="py-2 pr-3 text-[10px] text-muted-foreground">{totals.official} 官方 / {totals.review} 复核</td>
            <td className="py-2 pr-3 text-right tabular-nums">{totals.formula_missing}</td>
            <td className="py-2 text-right tabular-nums">{totals.conflicts}</td>
          </tr>
        </tfoot>
      </table>
    </div>
  )
}

export default function QualityPage() {
  useTitle('数据质量')
  const statsQ = useQuery({ queryKey: ['corpus-stats'], queryFn: fetchCorpusStats })
  const coursesQ = useQuery({ queryKey: ['corpus-courses'], queryFn: fetchCorpusCourses })
  const issuesQ = useQuery({ queryKey: ['corpus-issues'], queryFn: fetchCorpusIssues })

  const isLoading = statsQ.isLoading || coursesQ.isLoading || issuesQ.isLoading
  const error = statsQ.error || coursesQ.error || issuesQ.error

  if (isLoading) {
    return (
      <div className="space-y-4">
        <h1 className="text-2xl font-bold">数据质量</h1>
        <LoadingState />
      </div>
    )
  }

  if (error || !statsQ.data || !coursesQ.data || !issuesQ.data) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="max-w-sm text-center">
          <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-[#fff8e8] text-[#b45309]"><AlertTriangle size={22} /></span>
          <h2 className="mt-3 text-lg font-semibold">加载语料质量数据失败</h2>
          <p className="mt-2 text-sm text-muted-foreground">请确认后端 `/api/v1/corpus/stats` 可用。</p>
          <button
            onClick={() => {
              statsQ.refetch()
              coursesQ.refetch()
              issuesQ.refetch()
            }}
            className="mt-4 rounded-lg bg-primary px-5 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90"
          >
            重新加载
          </button>
        </div>
      </div>
    )
  }

  const stats = statsQ.data
  const courses = coursesQ.data
  const issues = issuesQ.data
  const q = stats.quality
  const statusTotal = QUALITY_ORDER.reduce((sum, s) => sum + (q[s] ?? 0), 0)
  const qualityPct = {
    official: pct(q.official, statusTotal),
    review: pct(q.review, statusTotal),
    candidate: pct(q.candidate, statusTotal),
    duplicate: pct(q.duplicate, statusTotal),
    quarantine: pct(q.quarantine, statusTotal),
  }
  const exclusionMax = stats.exclusions.reasons[0]?.count || 1
  const docTypeMax = stats.doc_types[0]?.count || 1

  return (
    <div className="space-y-5 pb-10">
      <header className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-2xl font-bold">数据质量</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            语料 {stats.version} · 868 原始文件 → 433 篇可追溯笔记 · {stats.generated_at?.slice(0, 10)}
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2 text-[11px]">
          <span className="rounded-full border border-emerald-200 bg-emerald-50 px-2.5 py-1 text-emerald-700">v1 已冻结</span>
          <span className="rounded-full border border-amber-200 bg-amber-50 px-2.5 py-1 text-amber-700">Vault 未修改</span>
          <span className="rounded-full border border-border bg-white px-2.5 py-1 text-muted-foreground">只读看板</span>
        </div>
      </header>

      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-5">
        <KpiCard
          label="原始文件"
          value={fmt(stats.raw.pdf + stats.raw.md)}
          sub={`${fmt(stats.raw.pdf)} PDF + ${fmt(stats.raw.md)} MD · ${fmt(stats.raw.pages)} 页`}
          accent="from-slate-500 to-slate-400"
        />
        <KpiCard
          label="纳入语料"
          value={fmt(stats.funnel[1]?.count)}
          sub={`排除 ${fmt(stats.exclusions.total)} · 纳入率 ${pct(stats.funnel[1]?.count ?? 0, stats.funnel[0]?.count ?? 0)}`}
          accent="from-sky-500 to-sky-400"
        />
        <KpiCard
          label="进入蒸馏"
          value={fmt(stats.funnel[2]?.count)}
          sub={`${pct(stats.funnel[2]?.count ?? 0, stats.funnel[1]?.count ?? 0)} 的纳入文件 · 未蒸馏 ${fmt((stats.funnel[1]?.count || 0) - (stats.funnel[2]?.count || 0))}`}
          accent="from-violet-500 to-violet-400"
        />
        <KpiCard
          label="知识单元"
          value={fmt(stats.funnel[4]?.count)}
          sub={`${fmt(stats.funnel[3]?.count)} 个 section part · ${fmt(stats.coverage.sections)} 个 section`}
          accent="from-amber-500 to-amber-400"
        />
        <KpiCard
          label="主题 / 笔记"
          value={fmt(stats.funnel[5]?.count)}
          sub={`100% 带 source_id 和页码 · 可索引 ${fmt(q.indexable)}`}
          accent="from-emerald-500 to-emerald-400"
        />
      </div>

      {stats.resolution && (
        <Section
          title="清洗结果"
          desc="夜间 AI enrichment：公式、定义、冲突、来源去噪。原始 notes 与 Vault 均未覆盖。"
          right={<span className="rounded-full bg-emerald-50 px-2 py-1 text-[10px] font-medium text-emerald-700">enriched {stats.resolution.enriched_notes}</span>}
        >
          <div className="grid gap-2 sm:grid-cols-2 xl:grid-cols-4">
            {[
              { label: '公式缺失', value: stats.resolution.formula_missing_remaining, sub: `${fmt(stats.resolution.source_supported_formulas)} 条公式有原文/笔记依据`, tone: 'text-emerald-700' },
              { label: '未解决冲突', value: stats.resolution.conflicts_unresolved, sub: '已解决/非冲突不再显示', tone: stats.resolution.conflicts_unresolved ? 'text-amber-700' : 'text-emerald-700' },
              { label: '隔离来源', value: stats.resolution.quarantine_excluded, sub: 'low_content，未进入索引', tone: 'text-muted-foreground' },
              { label: 'raw source chunks', value: stats.resolution.raw_source_chunks_indexed, sub: `${fmt(stats.resolution.near_duplicate_sources)} 组来源重复不参与检索`, tone: 'text-emerald-700' },
            ].map((item) => (
              <div key={item.label} className="rounded-xl border border-border bg-secondary/20 px-3 py-2.5">
                <p className="text-[10px] text-muted-foreground">{item.label}</p>
                <p className={`mt-0.5 text-lg font-bold tabular-nums ${item.tone}`}>{fmt(item.value)}</p>
                <p className="mt-0.5 text-[9px] leading-4 text-muted-foreground">{item.sub}</p>
              </div>
            ))}
          </div>
        </Section>
      )}

      <Section
        title="语料漏斗"
        desc="文件级先筛，再分节蒸馏；section part 与知识单元会放大，不能按文件数直接比较。"
        right={<span className="rounded-full bg-secondary px-2 py-1 text-[10px] text-muted-foreground">868 → 410 → 309 → 414 → 4,523 → 433</span>}
      >
        <div className="flex flex-col gap-2 xl:flex-row xl:items-stretch">
          {stats.funnel.map((s, i) => <FunnelCard key={s.key} stage={s} index={i} />)}
        </div>
        <div className="mt-3 grid gap-2 text-[11px] text-muted-foreground sm:grid-cols-3">
          <div className="rounded-lg bg-secondary/30 px-3 py-2">
            <span className="font-medium text-foreground">文件级：</span> 868 原始 → 410 纳入 → 309 蒸馏
          </div>
          <div className="rounded-lg bg-secondary/30 px-3 py-2">
            <span className="font-medium text-foreground">内容级：</span> 309 文件 → 414 part → 4,523 unit
          </div>
          <div className="rounded-lg bg-secondary/30 px-3 py-2">
            <span className="font-medium text-foreground">知识级：</span> 4,523 unit → 433 topic → 433 note
          </div>
        </div>
      </Section>

      <div className="grid gap-4 lg:grid-cols-3">
        <Section
          title="质量分级"
          desc={`${fmt(statusTotal)} 个纳入文件 · 可索引 ${fmt(q.indexable)} · 蒸馏 ${fmt(q.distill)}`}
          className="lg:col-span-2"
          right={
            <span className="rounded-full bg-emerald-50 px-2 py-1 text-[10px] text-emerald-700">
              {pct(q.indexable, statusTotal)} 可索引
            </span>
          }
        >
          <div className="mb-4">
            <StatusBar quality={{ official: q.official, review: q.review, candidate: q.candidate, duplicate: q.duplicate, quarantine: q.quarantine }} total={statusTotal} height="h-5" />
          </div>
          <div className="grid gap-2 sm:grid-cols-2 xl:grid-cols-5">
            {QUALITY_ORDER.map(s => {
              const meta = STATUS_META[s]
              return (
                <div key={s} className={`rounded-xl border p-3 ${meta.soft}`}>
                  <div className="flex items-center gap-1.5">
                    <span className={`h-2 w-2 rounded-full ${meta.dot}`} />
                    <span className={`text-[11px] font-medium ${meta.text}`}>{meta.label}</span>
                  </div>
                  <p className="mt-1 text-lg font-bold tabular-nums text-foreground">{fmt(q[s])}</p>
                  <p className="text-[10px] text-muted-foreground">{qualityPct[s]} of {fmt(statusTotal)}</p>
                </div>
              )
            })}
          </div>
          <div className="mt-3 grid gap-2 sm:grid-cols-3">
            <div className="rounded-lg border border-border px-3 py-2">
              <p className="text-[10px] text-muted-foreground">可索引</p>
              <p className="text-sm font-semibold">{fmt(q.indexable)} <span className="text-[10px] font-normal text-muted-foreground">/ {fmt(statusTotal)}</span></p>
            </div>
            <div className="rounded-lg border border-border px-3 py-2">
              <p className="text-[10px] text-muted-foreground">进入蒸馏</p>
              <p className="text-sm font-semibold">{fmt(q.distill)} <span className="text-[10px] font-normal text-muted-foreground">/ {fmt(stats.funnel[1]?.count)}</span></p>
            </div>
            <div className="rounded-lg border border-border px-3 py-2">
              <p className="text-[10px] text-muted-foreground">人工抽查</p>
              <p className="text-sm font-semibold">{fmt(issues.counts.review_sample)} <span className="text-[10px] font-normal text-muted-foreground">篇</span></p>
            </div>
          </div>
        </Section>

        <Section
          title="质量结论"
          desc="看板只呈现事实；不改 Vault，不替人做合并决定。"
        >
          <div className="space-y-2.5 text-xs">
            <div className="flex items-start gap-2 rounded-lg bg-emerald-50 p-2.5 text-emerald-800">
              <span className="mt-0.5">●</span>
              <p>{fmt(q.official)} 个官方文件 + {fmt(q.review)} 个待复核文件；{fmt(q.indexable)} 个可索引。</p>
            </div>
            <div className="flex items-start gap-2 rounded-lg bg-amber-50 p-2.5 text-amber-800">
              <span className="mt-0.5">●</span>
              <p>{fmt(issues.counts.conflicts)} 条冲突（{fmt(issues.counts.conflict_notes)} 篇笔记）、{fmt(q.formula_missing_notes)} 篇公式缺失，均已标记。</p>
            </div>
            <div className="flex items-start gap-2 rounded-lg bg-red-50 p-2.5 text-red-800">
              <span className="mt-0.5">●</span>
              <p>{fmt(issues.counts.quarantine)} 个隔离文件（low_content），不进入检索/图谱。</p>
            </div>
            <div className="flex items-start gap-2 rounded-lg bg-sky-50 p-2.5 text-sky-800">
              <span className="mt-0.5">●</span>
              <p>{fmt(issues.counts.near_duplicate_pairs)} 组近重复：{fmt(issues.counts.near_duplicate_duplicate)} 重复 / {fmt(issues.counts.near_duplicate_parallel)} 并行 / {fmt(issues.counts.near_duplicate_candidate)} 候选。</p>
            </div>
            <div className="mt-2 rounded-lg border border-border bg-secondary/30 p-2.5 text-[11px] text-muted-foreground">
              section 覆盖率 <span className="font-semibold text-foreground">{pct(stats.coverage.coverage * 100, 100)}</span>，
              {fmt(stats.coverage.files)} 个蒸馏文件、{fmt(stats.coverage.sections)} 个 section、{fmt(stats.coverage.parts)} 个 part，gaps {fmt(stats.coverage.gaps)}。
            </div>
          </div>
        </Section>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <Section
          title="排除原因"
          desc={`${fmt(stats.exclusions.total)} 个文件被排除；同一文件可能命中多个原因。`}
          right={<span className="rounded-full bg-secondary px-2 py-1 text-[10px] text-muted-foreground">可多重计数</span>}
        >
          <div className="space-y-2">
            {stats.exclusions.reasons.slice(0, 9).map(r => (
              <div key={r.reason}>
                <div className="flex items-center justify-between text-[11px]">
                  <span className="text-foreground/80">{r.label}</span>
                  <span className="tabular-nums text-muted-foreground">{fmt(r.count)}</span>
                </div>
                <div className="mt-0.5 h-1.5 overflow-hidden rounded-full bg-secondary">
                  <div className="h-full rounded-full bg-gradient-to-r from-slate-500 to-slate-400" style={{ width: `${(r.count / exclusionMax) * 100}%` }} />
                </div>
              </div>
            ))}
          </div>
        </Section>

        <div className="grid gap-4 sm:grid-cols-2">
          <Section title="文件类型" desc="纳入后的 410 个文件">
            <div className="space-y-2">
              {stats.doc_types.map(t => (
                <div key={t.type}>
                  <div className="flex items-center justify-between text-[11px]">
                    <span className="text-foreground/80">{t.label}</span>
                    <span className="tabular-nums text-muted-foreground">{fmt(t.count)}</span>
                  </div>
                  <div className="mt-0.5 h-1.5 overflow-hidden rounded-full bg-secondary">
                    <div className="h-full rounded-full bg-gradient-to-r from-sky-500 to-sky-400" style={{ width: `${(t.count / docTypeMax) * 100}%` }} />
                  </div>
                </div>
              ))}
            </div>
          </Section>

          <Section title="写回与成本" desc="提案，不自动写 Vault">
            <div className="space-y-2 text-xs">
              <div className="flex items-center justify-between">
                <span className="text-muted-foreground">写回提案</span>
                <span className="font-semibold">{fmt(stats.writeback.total)}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-muted-foreground">新建 / 补充 / 跳过</span>
                <span className="font-mono text-[11px]">{stats.writeback.create} / {stats.writeback.append_supplement} / {stats.writeback.skip_duplicate}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-muted-foreground">总 token</span>
                <span className="font-semibold">{fmt(stats.cost.total_tokens)}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-muted-foreground">Flash 成本</span>
                <span className="text-[11px]">${(stats.cost.flash_offpeak_usd ?? 0).toFixed(2)} – ${(stats.cost.flash_peak_usd ?? 0).toFixed(2)}</span>
              </div>
              <div className="mt-1 rounded bg-emerald-50 px-2 py-1.5 text-[10px] text-emerald-700">
                Vault 未修改 · 433 条 proposal 等人工审批
              </div>
            </div>
          </Section>
        </div>
      </div>

      <Section
        title="按课程分布"
        desc={`${courses.total} 门有内容的课程；另有 ${courses.empty_courses.length} 门暂无蒸馏内容（${courses.empty_courses.join(' / ')}）。`}
        right={<span className="rounded-full bg-secondary px-2 py-1 text-[10px] text-muted-foreground">纳入 {fmt(courses.totals.included)} · 笔记 {fmt(courses.totals.topics)}</span>}
      >
        <CourseTable courses={courses.courses} />
      </Section>

      <IssueTabs issues={issues} />

      <footer className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-3 text-[10px] text-muted-foreground">
        <span>数据源：data/manifest_v1.json · data/registry/*.csv · data/notes/_manifest.csv · data/sections/*.jsonl</span>
        <span>只读 · 不修改 Vault · 数字由后端实时计算</span>
      </footer>
    </div>
  )
}
