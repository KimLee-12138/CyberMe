import { useState, useRef, useMemo, useCallback, useEffect } from 'react'
import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import ForceGraph2D from 'react-force-graph-2d'
import { fetchGraph, fetchOrphans } from '../api/knowledge'
import { useTitle } from '../lib/useTitle'
import LoadingState from '../components/ui/LoadingState'

// ── Node colors ───────────────────────────────────────

const NODE_COLORS: Record<string, string> = {
  'course-moc': '#7C3AED',
  concept: '#2563EB',
  formula: '#D97706',
  example: '#059669',
  mistake: '#DC2626',
  extract: '#6B7280',
  source: '#0891B2',
  project: '#DB2777',
  'self-fact': '#4F46E5',
  inference: '#9333EA',
  chapter: '#475569',
}
const DEFAULT_NODE_COLOR = '#94A3B8'

const typeLabels: Record<string, string> = {
  'course-moc': '课程MOC', concept: '概念', formula: '公式', example: '例题',
  mistake: '错题', extract: '提取材料', source: '来源', project: '项目',
  'self-fact': '个人事实', inference: '推断', chapter: '章节',
}

const edgeLabels: Record<string, string> = {
  belongs_to: '所属', related_to: '关联', prerequisite_of: '前置',
  sourced_from: '来源', example_of: '举例', contrasts_with: '对比',
  applies_to: '应用', candidate_link: 'AI候选',
}

export default function GraphPage() {
  useTitle('知识图谱')
  const navigate = useNavigate()
  const containerRef = useRef<HTMLDivElement>(null)
  const fgRef = useRef<any>(null)
  const [filter, setFilter] = useState('all')
  const [showOrphans, setShowOrphans] = useState(false)
  const [dims, setDims] = useState({ w: 800, h: 500 })
  const [hoveredNode, setHoveredNode] = useState<any>(null)

  // ── Resize observer ──────────────────────────────────

  useEffect(() => {
    const el = containerRef.current
    if (!el) return
    const update = () => setDims({ w: el.clientWidth, h: el.clientHeight })
    update()
    const ro = new ResizeObserver(update)
    ro.observe(el)
    return () => ro.disconnect()
  }, [])

  // ── Data ─────────────────────────────────────────────

  const { data, isLoading } = useQuery({
    queryKey: ['graph'],
    queryFn: () => fetchGraph(),
  })

  const { data: orphanData } = useQuery({
    queryKey: ['orphans'],
    queryFn: fetchOrphans,
    enabled: showOrphans,
  })

  // ── Filtered graph data ──────────────────────────────

  const dataKey = useMemo(
    () => JSON.stringify({ n: (data?.nodes || []).map((n) => n.id).sort(), e: (data?.edges || []).map((e) => e.id).sort() }),
    [data],
  )

  const graphData = useMemo(() => {
    const filteredNodes = (data?.nodes || []).filter(
      (n) => filter === 'all' || n.node_type === filter,
    )
    const filteredIds = new Set(filteredNodes.map((n) => n.id))
    const filteredEdges = (data?.edges || []).filter(
      (e) => filteredIds.has(e.source) && filteredIds.has(e.target),
    )
    return {
      nodes: filteredNodes.map((n) => ({
        id: n.id,
        label: n.label,
        node_type: n.node_type,
        document_id: n.document_id,
        color: NODE_COLORS[n.node_type] || DEFAULT_NODE_COLOR,
        val: n.node_type === 'course-moc' ? 8 : 4,
      })),
      links: filteredEdges.map((e) => ({
        source: e.source,
        target: e.target,
        edge_type: e.edge_type,
      })),
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dataKey, filter])

  // ── Handlers ─────────────────────────────────────────

  const handleNodeClick = useCallback((node: any) => {
    if (node.document_id) navigate(`/knowledge/${node.document_id}`)
  }, [navigate])

  // ── Node paint ───────────────────────────────────────

  const paintNode = useCallback((node: any, ctx: CanvasRenderingContext2D, _globalScale: number) => {
    const isHovered = hoveredNode?.id === node.id
    const baseR = node.val ?? 4

    // Breathing pulse — subtle radius oscillation
    const t = Date.now() / 1000
    const breathe = 1 + Math.sin(t * 1.8 + node.x! * 0.01) * 0.12

    const r = isHovered ? baseR * 1.8 : baseR * breathe
    const glowR = r + (isHovered ? 5 : 2)
    const label = (node.label || '').slice(0, 10)

    // Glow ring
    ctx.beginPath()
    ctx.arc(node.x!, node.y!, glowR, 0, 2 * Math.PI)
    ctx.fillStyle = node.color + (isHovered ? '28' : '12')
    ctx.fill()

    // Node circle
    ctx.beginPath()
    ctx.arc(node.x!, node.y!, r, 0, 2 * Math.PI)
    ctx.fillStyle = node.color
    ctx.fill()
    ctx.strokeStyle = isHovered ? '#fff' : 'rgba(255,255,255,0.5)'
    ctx.lineWidth = isHovered ? 2 : 1
    ctx.stroke()

    // Label — always visible
    if (label) {
      ctx.font = isHovered ? 'bold 5px system-ui, sans-serif' : '4.5px system-ui, sans-serif'
      ctx.fillStyle = isHovered ? '#0F172A' : '#475569'
      ctx.textAlign = 'center'
      ctx.fillText(label, node.x!, node.y! + r + 7)
    }
  }, [hoveredNode])

  const nodeTypes = [...new Set(data?.nodes.map((n) => n.node_type) || [])]

  return (
    <div className="flex flex-col h-[calc(100vh-7rem)] space-y-3">
      {/* Header */}
      <div className="flex shrink-0 items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">知识图谱</h1>
          <p className="text-sm text-muted-foreground">
            {data ? `${data.nodes.length} 节点 · ${data.edges.length} 边` : ''}
            <span className="ml-2 text-muted-foreground/60">拖拽节点 · 滚轮缩放 · 点击跳转</span>
          </p>
        </div>
      </div>

      {isLoading && <LoadingState />}

      {/* Filter bar */}
      <div className="flex shrink-0 flex-wrap items-center gap-2">
        <button
          onClick={() => { setFilter('all'); if (fgRef.current) setTimeout(() => fgRef.current.zoomToFit(400, 60), 400) }}
          className={`rounded-lg px-3 py-1.5 text-xs font-medium transition-colors ${
            filter === 'all' ? 'bg-primary text-primary-foreground' : 'bg-muted text-muted-foreground hover:text-foreground'
          }`}
        >
          全部 ({data?.nodes.length || 0})
        </button>
        {nodeTypes.map((t) => (
          <button
            key={t}
            onClick={() => { setFilter(t); if (fgRef.current) setTimeout(() => fgRef.current.zoomToFit(400, 60), 400) }}
            className={`rounded-lg px-3 py-1.5 text-xs font-medium transition-colors ${
              filter === t ? 'bg-primary text-primary-foreground' : 'bg-muted text-muted-foreground hover:text-foreground'
            }`}
          >
            {typeLabels[t] || t} ({data?.nodes.filter((n) => n.node_type === t).length || 0})
          </button>
        ))}
        <button
          onClick={() => setShowOrphans(!showOrphans)}
          className={`ml-auto rounded-lg px-3 py-1.5 text-xs font-medium transition-colors ${
            showOrphans ? 'bg-red-100 text-red-700' : 'bg-muted text-muted-foreground'
          }`}
        >
          孤岛节点 {orphanData ? `(${orphanData.total})` : ''}
        </button>
      </div>

      {/* Orphan nodes */}
      {showOrphans && orphanData && orphanData.orphans.length > 0 && (
        <div className="shrink-0 rounded-xl border border-red-200 bg-red-50/50 p-3">
          <div className="flex flex-wrap gap-1.5">
            {orphanData.orphans.map((n) => (
              <button
                key={n.id}
                onClick={() => navigate(`/knowledge/${n.id}`)}
                className="rounded-md border border-red-200 bg-white px-2 py-0.5 text-xs text-red-700 hover:bg-red-100 transition-colors"
              >
                {n.label.slice(0, 25)}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Graph canvas */}
      <div ref={containerRef} className="flex-1 rounded-xl border border-border bg-card overflow-hidden">
        {data && graphData.nodes.length > 0 && (
          <ForceGraph2D
            ref={fgRef}
            graphData={graphData}
            width={dims.w}
            height={dims.h}
            nodeCanvasObject={paintNode}
            onNodeClick={handleNodeClick}
            linkColor={() => 'rgba(148,163,184,0.25)'}
            linkDirectionalArrowLength={4}
            linkDirectionalArrowRelPos={1}
            linkWidth={1}
            nodeLabel={(n: any) => `${n.label}\n${typeLabels[n.node_type] || n.node_type}`}
            cooldownTicks={Infinity}
            d3AlphaDecay={0.02}
            d3VelocityDecay={0.85}
            warmupTicks={30}
            onNodeHover={(n: any) => { setHoveredNode(n); document.body.style.cursor = n ? 'pointer' : '' }}
            enableNodeDrag
            enableZoomInteraction
          />
        )}
        {(!data || graphData.nodes.length === 0) && !isLoading && (
          <div className="flex h-full items-center justify-center">
            <div className="text-center py-16">
              <span className="text-4xl">🔗</span>
              <p className="mt-3 text-sm text-muted-foreground">暂无图谱数据</p>
            </div>
          </div>
        )}
      </div>

      {/* Edge legend */}
      <div className="flex shrink-0 flex-wrap gap-1.5 text-[11px] text-muted-foreground">
        {Object.entries(edgeLabels).map(([key, label]) => (
          <span key={key} className="rounded-full bg-muted px-2 py-0.5">{label}</span>
        ))}
      </div>
    </div>
  )
}
