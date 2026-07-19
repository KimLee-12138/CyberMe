import { useState, useCallback } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import Markdown from '../components/ui/Markdown'
import { useTitle } from '../lib/useTitle'
import { fetchDueReviews, gradeCard, fetchReviewStats } from '../api/learning'

// ── Rating config ───────────────────────────────────────

const RATINGS = [
  { value: 1, label: '完全忘了', key: '重来', color: 'bg-red-500 hover:bg-red-600', emoji: '🔴' },
  { value: 2, label: '勉强记得', key: '困难', color: 'bg-amber-500 hover:bg-amber-600', emoji: '🟠' },
  { value: 3, label: '正确回忆', key: '良好', color: 'bg-emerald-500 hover:bg-emerald-600', emoji: '🟢' },
  { value: 4, label: '非常轻松', key: '简单', color: 'bg-blue-500 hover:bg-blue-600', emoji: '🔵' },
]

// ── Skeleton ────────────────────────────────────────────

function SkeletonCard() {
  return (
    <div className="mx-auto w-full max-w-lg animate-pulse">
      <div className="mb-4 h-3 w-24 rounded bg-muted" />
      <div className="rounded-2xl border border-border bg-white p-8 shadow-sm">
        <div className="mb-4 h-4 w-2/3 rounded bg-muted" />
        <div className="mb-2 h-3 w-full rounded bg-muted" />
        <div className="h-12 rounded-xl bg-muted" />
      </div>
    </div>
  )
}

// ── Main component ──────────────────────────────────────

export default function ReviewPage() {
  useTitle('复习')
  const queryClient = useQueryClient()
  const [showAnswer, setShowAnswer] = useState(false)
  const [feedback, setFeedback] = useState<string | null>(null)

  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['due-reviews'],
    queryFn: fetchDueReviews,
  })

  const { data: stats } = useQuery({
    queryKey: ['review-stats'],
    queryFn: fetchReviewStats,
    staleTime: 30_000,
  })

  const cards = data?.cards || []
  const activeCard = cards.length > 0 ? cards[0] : null

  const gradeMutation = useMutation({
    mutationFn: ({ cardId, rating }: { cardId: string; rating: number }) =>
      gradeCard(cardId, rating),
    onSuccess: (_data, variables) => {
      const rating = RATINGS.find((r) => r.value === variables.rating)
      setFeedback(rating?.label || '已记录')
      queryClient.invalidateQueries({ queryKey: ['due-reviews'] })

      setTimeout(() => {
        setFeedback(null)
        setShowAnswer(false)
        refetch()
      }, 800)
    },
  })

  const handleRate = useCallback(
    (rating: number) => {
      if (!activeCard || gradeMutation.isPending) return
      gradeMutation.mutate({ cardId: activeCard.id, rating })
    },
    [activeCard, gradeMutation.isPending],
  )

  // ── Loading ────────────────────────────────────────
  if (isLoading) {
    return (
      <div className="space-y-6">
        <h1 className="text-2xl font-bold">复习</h1>
        <SkeletonCard />
      </div>
    )
  }

  // ── Error ──────────────────────────────────────────
  if (error) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="text-center max-w-sm">
          <span className="text-4xl">⚠️</span>
          <h2 className="mt-3 text-lg font-semibold">加载复习数据失败</h2>
          <button
            onClick={() => refetch()}
            className="mt-4 rounded-lg bg-primary px-5 py-2 text-sm font-medium text-primary-foreground"
          >
            重试
          </button>
        </div>
      </div>
    )
  }

  // ── Empty ──────────────────────────────────────────
  if (!activeCard) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="text-center max-w-md">
          <span className="text-5xl">🎉</span>
          <h2 className="mt-4 text-xl font-bold">暂无待复习卡片</h2>
          <p className="mt-2 text-sm text-muted-foreground">
            新卡片将在你浏览知识时自动生成，或稍后刷新页面获取
          </p>
          <button
            onClick={() => refetch()}
            className="mt-4 rounded-lg bg-primary px-5 py-2 text-sm font-medium text-primary-foreground"
          >
            刷新
          </button>
        </div>
      </div>
    )
  }

  // ── Feedback overlay ───────────────────────────────
  if (feedback) {
    const emojiMap: Record<string, string> = {
      '完全忘了': '💪',
      '勉强记得': '👍',
      '正确回忆': '✅',
      '非常轻松': '🌟',
    }
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="text-center">
          <span className="text-4xl">{emojiMap[feedback] || '✅'}</span>
          <p className="mt-2 text-lg font-semibold">{feedback}</p>
        </div>
      </div>
    )
  }

  // ── Review card ────────────────────────────────────
  return (
    <div className="mx-auto max-w-lg space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">复习</h1>
        <span className="text-sm text-muted-foreground">
          {cards.length} 张待复习
        </span>
      </div>

      {/* Stats ribbon */}
      {stats && (
        <div className="grid grid-cols-4 gap-3">
          <div className="rounded-xl border border-border bg-card p-3 text-center">
            <p className="text-xs text-muted-foreground">记忆保持率</p>
            <p className="mt-1 text-lg font-bold text-emerald-600">{stats.retention_rate}%</p>
          </div>
          <div className="rounded-xl border border-border bg-card p-3 text-center">
            <p className="text-xs text-muted-foreground">今日复习</p>
            <p className="mt-1 text-lg font-bold text-primary">{stats.reviews_today}</p>
          </div>
          <div className="rounded-xl border border-border bg-card p-3 text-center">
            <p className="text-xs text-muted-foreground">平均稳定性</p>
            <p className="mt-1 text-lg font-bold text-amber-600">{stats.avg_stability.toFixed(1)}</p>
          </div>
          <div className="rounded-xl border border-border bg-card p-3 text-center">
            <p className="text-xs text-muted-foreground">卡片总数</p>
            <p className="mt-1 text-lg font-bold">{stats.total_cards}</p>
          </div>
        </div>
      )}

      <div className="rounded-2xl border border-border bg-white p-6 shadow-sm">
        {/* Card type badge */}
        <span className="mb-3 inline-block rounded-full bg-primary/10 px-2.5 py-0.5 text-xs font-medium text-primary">
          {activeCard.card_type === 'recall' ? '回忆' :
           activeCard.card_type === 'concept' ? '概念' :
           activeCard.card_type === 'problem' ? '题目' : '应用'}
          {activeCard.reps > 0 && ` · 第${activeCard.reps}次`}
        </span>

        {/* Front side */}
        <Markdown>{activeCard.front}</Markdown>

        {/* Show answer button */}
        {!showAnswer && (
          <button
            onClick={() => setShowAnswer(true)}
            className="mt-4 w-full rounded-xl border-2 border-dashed border-primary/30 bg-primary/5 py-3 text-sm font-medium text-primary hover:bg-primary/10 transition-colors"
          >
            点击显示答案
          </button>
        )}

        {/* Back side (answer) */}
        {showAnswer && (
          <div className="mt-4 border-t border-border pt-4">
            <p className="mb-2 text-xs font-medium text-muted-foreground uppercase tracking-wider">
              答案
            </p>
            <div className="max-h-60 overflow-y-auto">
              <Markdown>{activeCard.back}</Markdown>
            </div>
          </div>
        )}
      </div>

      {/* Rating buttons */}
      {showAnswer && (
        <div className="grid grid-cols-4 gap-2">
          {RATINGS.map((r) => (
            <button
              key={r.value}
              onClick={() => handleRate(r.value)}
              disabled={gradeMutation.isPending}
              className={`flex flex-col items-center rounded-xl py-3 text-white text-sm font-semibold transition-all active:scale-95 disabled:opacity-50 ${r.color}`}
            >
              <span className="text-lg">{r.emoji}</span>
              <span className="text-xs mt-0.5">{r.label}</span>
              <span className="text-[10px] opacity-70">{r.key}</span>
            </button>
          ))}
        </div>
      )}
    </div>
  )
}
