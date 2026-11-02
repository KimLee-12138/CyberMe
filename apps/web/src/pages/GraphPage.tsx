import { useState, useRef, useMemo, useCallback, useEffect } from 'react'
import { useQuery } from '@tanstack/react-query'
import { useNavigate, useSearchParams } from 'react-router-dom'
import ForceGraph2D from 'react-force-graph-2d'
import { fetchKgGraph, fetchKgNode, fetchKgValidate } from '../api/knowledge'
import { useTitle } from '../lib/useTitle'
import LoadingState from '../components/ui/LoadingState'
import Select from '../components/ui/Select'
import Checkbox from '../components/ui/Checkbox'

const NODE_COLORS: Record<string, string> = {
  course: '#0B1F3A',
  section: '#2563EB',
  topic: '#4F8BFF',
  source: '#0E7490',
}
const DEFAULT_COLOR = '#94A3B8'

const TYPE_LABELS: Record<string, string> = {
  course: '课程',
  section: '章节',
  topic: '主题',
  source: '来源',
}

const EDGE_LABELS: Record<string, string> = {
  prerequisite_of: '课程前置',
  belongs_to: '所属课程',
  part_of: '属于章节',
  derived_from: '来源',
  candidate_link: 'AI候选（虚线）',
}

const EDGE_COLORS: Record<string, string> = {
  prerequisite_of: 'rgba(234,88,12,0.8)',
  belongs_to: 'rgba(37,99,235,0.35)',
  part_of: 'rgba(148,163,184,0.25)',
  derived_from: 'rgba(14,116,144,0.25)',
  candidate_link: 'rgba(148,163,184,0.6)',
}

function pagesLabel(pages: any): string {
  if (!Array.isArray(pages) || pages.length === 0) return ''
  return pages.map((p: any) => {
    if (Array.isArray(p)) return p[0] === p[1] ? `p.${p[0]}` : `p.${p[0]}-${p[1]}`
    return String(p)
  }).join(', ')
}

export default function GraphPage() {
  useTitle('知识图谱')
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()
  const containerRef = useRef<HTMLDivElement>(null)
  const fgRef = useRef<any>(null)
  const [course, setCourse] = useState((searchParams.get('course') || '').toUpperCase())
  const [selectedId, setSelectedId] = useState<string | null>(
    searchParams.get('course') ? `course:${searchParams.get('course')!.toUpperCase()}` : null,
  )
  const [showCandidates, setShowCandidates] = useState(false)
  const [copied, setCopied] = useState('')
  const [hovered, setHovered] = useState<any>(null)
  const [dims, setDims] = useState({ w: 900, h: 560 })

  useEffect(() => {
    const code = (searchParams.get('course') || '').toUpperCase()
    if (!code) return
    setCourse(code)
    setSelectedId(`course:${code}`)
  }, [searchParams])

  useEffect(() => {
    const el = containerRef.current
    if (!el) return
    const update = () => setDims({ w: el.clientWidth, h: el.clientHeight })
    update()
    const ro = new ResizeObserver(update)
    ro.observe(el)
    return () => ro.disconnect()
  }, [])

  const { data, isLoading, isFetching, isError, refetch } = useQuery({
    queryKey: ['kg-graph', course, showCandidates],
    queryFn: () => fetchKgGraph(course || undefined, showCandidates),
  })

  const { data: validation } = useQuery({
    queryKey: ['kg-validate'],
    queryFn: fetchKgValidate,
  })

  const { data: detail, isFetching: detailLoading } = useQuery({
    queryKey: ['kg-node', selectedId],
    queryFn: () => fetchKgNode(selectedId!),
    enabled: !!selectedId,
  })

  const graphData = useMemo(() => {
    const nodes = (data?.nodes || []).map((n: any) => ({
      ...n,
      color: NODE_COLORS[n.node_type] || DEFAULT_COLOR,
      val: n.node_type === 'course' ? 9 : n.node_type === 'section' ? 5 : n.node_type === 'topic' ? 4 : 3,
    }))
    const ids = new Set(nodes.map((n: any) => n.id))
    const links: any[] = (data?.edges || [])
      .filter((e: any) => ids.has(e.source) && ids.has(e.target))
      .map((e: any) => ({ ...e }))
    if (showCandidates) {
      const candidates = (data?.candidate_edges || [])
        .filter((e: any) => ids.has(e.source) && ids.has(e.target))
        .map((e: any) => ({ ...e, origin: 'ai_candidate' }))
      links.push(...candidates)
    }
    return { nodes, links }
  }, [data, showCandidates])

  useEffect(() => {
    if (!data || !fgRef.current) return
    const t = setTimeout(() => fgRef.current?.zoomToFit?.(500, 70), 350)
    return () => clearTimeout(t)
  }, [data])

  const handleNodeClick = useCallback((node: any) => {
    setSelectedId(node.id)
    if (node.node_type === 'course' && node.properties?.code && node.properties.code !== course) {
      setCourse(node.properties.code)
    }
  }, [course])

  const paintNode = useCallback((node: any, ctx: CanvasRenderingContext2D) => {
    if (!node.x || !node.y) return
    const isHovered = hovered?.id === node.id
    const isSelected = selectedId === node.id
    const baseR = node.val ?? 4
    const r = isHovered || isSelected ? baseR * 1.5 : baseR
    const label = (node.label || '').slice(0, node.node_type === 'topic' ? 10 : 8)

    ctx.beginPath()
    ctx.arc(node.x, node.y, r + (isSelected ? 4 : 2), 0, 2 * Math.PI)
    ctx.fillStyle = node.color + (isSelected ? '40' : '18')
    ctx.fill()

    ctx.beginPath()
    ctx.arc(node.x, node.y, r, 0, 2 * Math.PI)
    ctx.fillStyle = node.color
    ctx.fill()
    ctx.strokeStyle = isSelected ? '#0F172A' : 'rgba(255,255,255,0.65)'
    ctx.lineWidth = isSelected ? 2 : 1
    ctx.stroke()

    if (label) {
      ctx.font = `${isSelected ? 'bold ' : ''}4.5px system-ui, sans-serif`
      ctx.fillStyle = isSelected ? '#0F172A' : '#475569'
      ctx.textAlign = 'center'
      ctx.fillText(label, node.x, node.y + r + 7)
    }
  }, [hovered, selectedId])

  const courseNames = useMemo(() => data?.course_names || {}, [data])
  const courseOptions = useMemo(
    () => Object.entries(courseNames).sort((a, b) => String(a[1]).localeCompare(String(b[1]), 'zh-CN')),
    [courseNames],
  )

  const selectedNode = detail?.node || graphData.nodes.find((n: any) => n.id === selectedId)
  const props = selectedNode?.properties || {}

  const selectCourse = (code: string) => {
    setCourse(code)
    setSelectedId(code ? `course:${code}` : null)
  }

  return (
    <div className="flex h-[calc(100vh-7rem)] min-h-0 flex-col gap-3">
      <header className="flex shrink-0 flex-wrap items-end justify-between gap-2">
        <div>
          <h1 className="text-2xl font-bold">知识图谱</h1>
          <p className="text-sm text-muted-foreground">
            {data ? `${data.stats.nodes} 节点 · ${data.stats.edges} 边` : '加载中…'}
            <span className="ml-2 text-muted-foreground/60">
              {course ? `已展开 ${courseNames[course] || course}` : '点击课程展开章节/主题/来源'}
            </span>
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {validation && (
            <span
              className={`rounded-full px-2 py-1 text-[10px] ${
                validation.ok
                  ? 'bg-emerald-100 text-emerald-700'
                  : 'bg-red-100 text-red-700'
              }`}
              title={`孤立节点 ${validation.counts.orphan_nodes} · 断边 ${validation.counts.dangling_edges} · 重复 label ${validation.counts.duplicate_label_groups} · 缺页码 ${validation.counts.missing_pages}`}
            >
              {validation.ok ? '校验通过' : '校验异常'}
            </span>
          )}
          <Checkbox
            checked={showCandidates}
            onChange={setShowCandidates}
            label="AI 候选边"
            className="rounded-lg border border-border bg-white px-2.5 py-1"
          />
          <Select
            value={course}
            onChange={selectCourse}
            ariaLabel="课程筛选"
            size="sm"
            className="w-52"
            options={[
              { value: '', label: `全部课程（${Object.keys(courseNames).length}）` },
              ...courseOptions.map(([code, name]) => ({ value: code, label: `${name}（${code}）` })),
            ]}
          />
          <button
            onClick={() => selectCourse('')}
            className="rounded-lg border border-border px-3 py-1.5 text-xs text-muted-foreground hover:bg-secondary"
          >
            返回总览
          </button>
          {isFetching && <span className="text-[11px] text-muted-foreground">加载…</span>}
        </div>
      </header>

      <div className="flex min-h-0 flex-1 gap-3">
        <div className="flex min-w-0 flex-1 flex-col gap-2">
          <div ref={containerRef} className="relative flex-1 overflow-hidden rounded-xl border border-border bg-card">
            {isLoading && (
              <div className="absolute inset-0 z-10 flex items-center justify-center bg-background/60">
                <LoadingState />
              </div>
            )}
            {data && graphData.nodes.length > 0 && (
              <ForceGraph2D
                ref={fgRef}
                graphData={graphData}
                width={dims.w}
                height={dims.h}
                nodeCanvasObject={paintNode}
                onNodeClick={handleNodeClick}
                linkColor={(l: any) => (l.origin === 'ai_candidate' ? EDGE_COLORS.candidate_link : (EDGE_COLORS[l.edge_type] || 'rgba(148,163,184,0.25)'))}
                linkWidth={(l: any) => (l.origin === 'ai_candidate' ? 0.7 : l.edge_type === 'prerequisite_of' ? 1.8 : 0.8)}
                linkLineDash={(l: any) => (l.origin === 'ai_candidate' ? [3, 3] : null)}
                linkDirectionalArrowLength={(l: any) => (l.edge_type === 'prerequisite_of' ? 5 : 3)}
                linkDirectionalArrowRelPos={1}
                linkDirectionalParticles={(l: any) => (l.edge_type === 'prerequisite_of' && l.origin !== 'ai_candidate' ? 2 : 0)}
                linkDirectionalParticleWidth={2}
                nodeLabel={(n: any) => `${n.label}\n${TYPE_LABELS[n.node_type] || n.node_type}`}
                cooldownTicks={Infinity}
                d3AlphaDecay={0.02}
                d3VelocityDecay={0.85}
                warmupTicks={30}
                onNodeHover={(n: any) => {
                  setHovered(n)
                  document.body.style.cursor = n ? 'pointer' : ''
                }}
                enableNodeDrag
                enableZoomInteraction
              />
            )}
            {isError && !isLoading && (
              <div className="flex h-full items-center justify-center">
                <div className="text-center">
                  <p className="text-sm text-muted-foreground">图谱数据加载失败</p>
                  <button onClick={() => refetch()} className="mt-2 text-xs text-primary hover:underline">
                    重试
                  </button>
                </div>
              </div>
            )}
            {(!data || graphData.nodes.length === 0) && !isLoading && !isError && (
              <div className="flex h-full items-center justify-center">
                <p className="text-sm text-muted-foreground">暂无图谱数据</p>
              </div>
            )}
          </div>

          <div className="flex shrink-0 flex-wrap gap-2 text-[11px] text-muted-foreground">
            {Object.entries(EDGE_LABELS).map(([key, label]) => (
              <span key={key} className="inline-flex items-center gap-1 rounded-full bg-muted px-2 py-0.5">
                <span className="h-1.5 w-4 rounded-full" style={{ background: EDGE_COLORS[key] }} />
                {label}
              </span>
            ))}
            <span className="ml-auto text-muted-foreground/60">拖拽 · 滚轮缩放 · 点击展开</span>
          </div>
        </div>

        <aside className="hidden w-80 shrink-0 flex-col overflow-hidden rounded-xl border border-border bg-card xl:flex">
          <div className="border-b border-border px-4 py-3">
            <h2 className="text-sm font-semibold">节点详情</h2>
            <p className="text-[11px] text-muted-foreground">
              {selectedNode ? TYPE_LABELS[selectedNode.node_type] || selectedNode.node_type : '点击节点查看'}
            </p>
          </div>
          <div className="flex-1 overflow-y-auto p-4">
            {!selectedNode && (
              <div className="space-y-4">
                <p className="text-xs text-muted-foreground">
                  默认显示 24 门课程和课程前置边。点击课程节点展开该课程的章节、主题和来源。
                </p>
                {data && Object.keys(data.course_prerequisites || {}).length > 0 && (
                  <div>
                    <p className="mb-2 text-[11px] font-medium text-muted-foreground">课程前置（示例）</p>
                    <div className="space-y-1.5">
                      {Object.entries(data.course_prerequisites).slice(0, 10).map(([target, prereqs]) => (
                        <div key={target} className="rounded-lg bg-secondary/40 px-2 py-1.5 text-[11px]">
                          <span className="font-medium text-foreground">{courseNames[target] || target}</span>
                          <span className="text-muted-foreground"> ← {prereqs.map(p => courseNames[p] || p).join(' / ')}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {selectedNode && (
              <div className="space-y-3">
                <div>
                  <div className="mb-1 flex items-center gap-2">
                    <span
                      className="inline-block h-2.5 w-2.5 rounded-full"
                      style={{ background: NODE_COLORS[selectedNode.node_type] || DEFAULT_COLOR }}
                    />
                    <span className="text-[11px] text-muted-foreground">
                      {TYPE_LABELS[selectedNode.node_type] || selectedNode.node_type}
                    </span>
                  </div>
                  <h3 className="text-sm font-semibold leading-snug">{selectedNode.label}</h3>
                </div>

                {selectedNode.node_type === 'course' && (
                  <div className="space-y-2 text-xs">
                    <div className="grid grid-cols-3 gap-1">
                      <div className="rounded-lg bg-secondary/50 p-2 text-center">
                        <div className="text-sm font-semibold">{props.topic_count ?? 0}</div>
                        <div className="text-[10px] text-muted-foreground">主题</div>
                      </div>
                      <div className="rounded-lg bg-secondary/50 p-2 text-center">
                        <div className="text-sm font-semibold">{props.section_count ?? 0}</div>
                        <div className="text-[10px] text-muted-foreground">章节</div>
                      </div>
                      <div className="rounded-lg bg-secondary/50 p-2 text-center">
                        <div className="text-sm font-semibold">{props.source_count ?? 0}</div>
                        <div className="text-[10px] text-muted-foreground">来源</div>
                      </div>
                    </div>
                    {!!props.prerequisites?.length && (
                      <div className="flex flex-wrap items-center gap-1 text-[11px] text-muted-foreground">
                        <span>前置：</span>
                        {props.prerequisites.map((c: string) => (
                          <button
                            key={c}
                            onClick={() => selectCourse(c)}
                            className="rounded bg-secondary px-1.5 py-0.5 text-foreground hover:bg-secondary/70"
                          >
                            {courseNames[c] || c}
                          </button>
                        ))}
                      </div>
                    )}
                    {!!props.unlocks?.length && (
                      <div className="flex flex-wrap items-center gap-1 text-[11px] text-muted-foreground">
                        <span>后续：</span>
                        {props.unlocks.map((c: string) => (
                          <button
                            key={c}
                            onClick={() => selectCourse(c)}
                            className="rounded bg-secondary px-1.5 py-0.5 text-foreground hover:bg-secondary/70"
                          >
                            {courseNames[c] || c}
                          </button>
                        ))}
                      </div>
                    )}
                    <button
                      onClick={() => selectCourse(props.code)}
                      className="w-full rounded-lg bg-primary/10 px-3 py-1.5 text-xs text-primary hover:bg-primary/20"
                    >
                      展开这门课
                    </button>
                  </div>
                )}

                {selectedNode.node_type === 'topic' && (
                  <div className="space-y-2 text-xs">
                    <p className="text-[11px] text-muted-foreground">
                      {courseNames[props.course] || props.course} · {props.unit_count ?? 0} units · 置信度 {Number(props.confidence ?? 0).toFixed(2)}
                    </p>
                    <div className="flex flex-wrap gap-1 text-[10px]">
                      <span className="rounded bg-secondary px-1.5 py-0.5">关键点 {props.key_points ?? 0}</span>
                      <span className="rounded bg-secondary px-1.5 py-0.5">公式 {props.formulas ?? 0}</span>
                      {!!props.conflicts && <span className="rounded bg-amber-100 px-1.5 py-0.5 text-amber-700">冲突 {props.conflicts}</span>}
                    </div>
                    {Array.isArray(props.sources) && props.sources.length > 0 && (
                      <div>
                        <p className="mb-1 text-[10px] font-medium text-muted-foreground">来源</p>
                        <div className="space-y-1">
                          {props.sources.map((s: any) => (
                            <div key={s.source_id + (s.page_start || '')} className="rounded bg-secondary/40 px-2 py-1 text-[10px] text-muted-foreground">
                              {s.source_id} {pagesLabel([[s.page_start, s.page_end]])}
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                    {props.note_path && (
                      <div className="flex items-start gap-1">
                        <p className="min-w-0 flex-1 break-all rounded bg-secondary/40 px-2 py-1 font-mono text-[10px] text-muted-foreground">
                          {props.note_path}
                        </p>
                        <button
                          onClick={() => {
                            navigator.clipboard?.writeText(props.note_path)
                            setCopied(props.note_path)
                          }}
                          className="shrink-0 rounded border border-border px-1.5 py-1 text-[10px] text-muted-foreground hover:bg-secondary"
                        >
                          {copied === props.note_path ? '已复制' : '复制'}
                        </button>
                      </div>
                    )}
                    {props.note_id && (
                      <button
                        onClick={() => navigate(`/notes?note=${encodeURIComponent(props.note_id)}`)}
                        className="w-full rounded-lg bg-primary/10 px-3 py-1.5 text-xs text-primary hover:bg-primary/20"
                      >
                        打开笔记浏览器
                      </button>
                    )}
                    <p className="text-[11px] text-muted-foreground">
                      章节：{props.section_id || '—'}
                    </p>
                  </div>
                )}

                {selectedNode.node_type === 'section' && (
                  <div className="space-y-2 text-xs text-muted-foreground">
                    <p>课程：{courseNames[props.course] || props.course}</p>
                    <p>路径：{(props.heading_path || []).join(' > ')}</p>
                    <p>页码：{pagesLabel([[props.page_start, props.page_end]]) || '—'}</p>
                    <p>字符：{props.chars ?? 0}</p>
                  </div>
                )}

                {selectedNode.node_type === 'source' && (
                  <div className="space-y-2 text-xs text-muted-foreground">
                    <p className="break-all">{props.rel}</p>
                    <p>类型：{props.doc_type} · 页数：{props.pages ?? '—'}</p>
                    <p>质量：{props.quality_status || '—'}</p>
                  </div>
                )}

                {!!detail?.neighbors?.length && (
                  <div>
                    <p className="mb-1 text-[10px] font-medium text-muted-foreground">邻居（{detail.neighbor_count}）</p>
                    <div className="space-y-1">
                      {detail.neighbors.slice(0, 20).map((n: any) => (
                        <button
                          key={n.id}
                          onClick={() => setSelectedId(n.id)}
                          className="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-[11px] hover:bg-secondary"
                        >
                          <span
                            className="h-2 w-2 shrink-0 rounded-full"
                            style={{ background: NODE_COLORS[n.node_type] || DEFAULT_COLOR }}
                          />
                          <span className="truncate">{n.label}</span>
                        </button>
                      ))}
                    </div>
                  </div>
                )}

                {detailLoading && <p className="text-[11px] text-muted-foreground">加载详情…</p>}
              </div>
            )}
          </div>
        </aside>
      </div>

      {/* Small-screen detail drawer */}
      {selectedNode && (
        <div className="fixed inset-x-0 bottom-0 z-40 max-h-[60vh] overflow-y-auto rounded-t-2xl border-t border-border bg-card p-4 shadow-2xl xl:hidden">
          <div className="mb-2 flex items-start justify-between gap-2">
            <div>
              <p className="text-[10px] text-muted-foreground">
                {TYPE_LABELS[selectedNode.node_type] || selectedNode.node_type}
              </p>
              <h3 className="text-sm font-semibold">{selectedNode.label}</h3>
            </div>
            <button
              onClick={() => setSelectedId(null)}
              className="rounded-lg border border-border px-2 py-1 text-[11px] text-muted-foreground"
            >
              关闭
            </button>
          </div>

          {selectedNode.node_type === 'course' && (
            <p className="text-xs text-muted-foreground">
              {props.topic_count ?? 0} 主题 · {props.section_count ?? 0} 章节 · {props.source_count ?? 0} 来源
            </p>
          )}

          {selectedNode.node_type === 'topic' && (
            <div className="space-y-1 text-xs text-muted-foreground">
              <p>{courseNames[props.course] || props.course} · {props.unit_count ?? 0} units</p>
              {Array.isArray(props.sources) && props.sources.map((s: any) => (
                <p key={s.source_id} className="text-[11px]">
                  {s.source_id} {pagesLabel([[s.page_start, s.page_end]])}
                </p>
              ))}
              {props.note_path && <p className="break-all font-mono text-[10px]">{props.note_path}</p>}
            </div>
          )}

          {selectedNode.node_type === 'section' && (
            <p className="text-xs text-muted-foreground">
              {courseNames[props.course] || props.course} · {pagesLabel([[props.page_start, props.page_end]]) || '页码缺失'}
            </p>
          )}

          {selectedNode.node_type === 'source' && (
            <p className="break-all text-xs text-muted-foreground">{props.rel}</p>
          )}
        </div>
      )}
    </div>
  )
}
