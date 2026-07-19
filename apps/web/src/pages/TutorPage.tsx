import { useState, useRef, useEffect } from 'react'
import { useMutation } from '@tanstack/react-query'
import Markdown from '../components/ui/Markdown'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'
import { createSession, submitResponse } from '../api/learning'
import type { TutorMode, SessionResponse } from '../api/learning'

// ── Mode definitions ─────────────────────────────────────

interface ModeInfo {
  key: TutorMode
  label: string
  desc: string
  icon: string
  color: string
}

const MODES: ModeInfo[] = [
  { key: 'concept', label: '概念讲解', desc: '一句话→原理→公式→例子→易错点', icon: '💡', color: 'border-blue-500' },
  { key: 'socratic', label: '苏格拉底', desc: '一次一问，逐步深入', icon: '🎓', color: 'border-purple-500' },
  { key: 'closed_book', label: '闭卷回忆', desc: '不看笔记，主动回忆', icon: '🧠', color: 'border-amber-500' },
  { key: 'step_by_step', label: '分步做题', desc: '逐步解题，记录每一步', icon: '📝', color: 'border-emerald-500' },
  { key: 'mock_exam', label: '模拟考试', desc: '限时答题，自动批改', icon: '⏱️', color: 'border-red-500' },
  { key: 'mistake_retrain', label: '错题复训', desc: '从错误中学习，生成变体', icon: '🔄', color: 'border-pink-500' },
]

// ── Main component ───────────────────────────────────────

export default function TutorPage() {
  useTitle('AI 导师')
  const [mode, setMode] = useState<TutorMode>('concept')
  const [topic, setTopic] = useState('')
  const [sessionId, setSessionId] = useState<string | null>(null)
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([])
  const [input, setInput] = useState('')
  const [complete, setComplete] = useState(false)
  const [correctAnswer, setCorrectAnswer] = useState('')
  const bottomRef = useRef<HTMLDivElement>(null)

  const startMutation = useMutation({
    mutationFn: () => createSession(mode, topic, mode === 'mock_exam' ? 3 : undefined),
    onSuccess: (data: SessionResponse) => {
      setSessionId(data.session_id)
      setMessages([{ role: 'assistant', content: data.content }])
      setComplete(data.complete || false)
      if (data.correct_answer) setCorrectAnswer(data.correct_answer)
      toast.success('导师已就绪')
    },
  })

  const replyMutation = useMutation({
    mutationFn: (answer: string) => submitResponse(sessionId!, answer),
    onSuccess: (data: SessionResponse) => {
      setMessages((prev) => [
        ...prev,
        ...(data.content
          ? [{ role: 'assistant' as const, content: data.content }]
          : []),
      ])
      setComplete(data.complete || false)
      if (data.correct_answer) setCorrectAnswer(data.correct_answer)
    },
  })

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const handleStart = () => {
    if (!topic.trim()) return
    setMessages([])
    setComplete(false)
    setCorrectAnswer('')
    startMutation.mutate()
  }

  const handleSend = () => {
    if (!input.trim() || !sessionId || replyMutation.isPending) return
    const answer = input.trim()
    setMessages((prev) => [...prev, { role: 'user', content: answer }])
    setInput('')
    replyMutation.mutate(answer)
  }

  const handleReset = () => {
    setSessionId(null)
    setMessages([])
    setComplete(false)
    setCorrectAnswer('')
    setTopic('')
  }

  const modeInfo = MODES.find((m) => m.key === mode)!

  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <h1 className="text-2xl font-bold">自适应导师</h1>

      {/* Mode selector */}
      <div className="grid grid-cols-3 gap-2 sm:grid-cols-6">
        {MODES.map((m) => (
          <button
            key={m.key}
            onClick={() => { setMode(m.key); handleReset() }}
            className={`flex flex-col items-center rounded-xl border-2 p-3 text-center transition-all ${
              mode === m.key
                ? `${m.color} bg-white shadow-sm`
                : 'border-transparent bg-secondary/50 text-muted-foreground hover:bg-secondary'
            }`}
          >
            <span className="text-xl">{m.icon}</span>
            <span className="mt-1 text-xs font-medium">{m.label}</span>
          </button>
        ))}
        <p className="col-span-full text-center text-xs text-muted-foreground mt-1">
          {modeInfo.desc}
        </p>
      </div>

      {/* Topic input */}
      {!sessionId && (
        <div className="flex gap-2">
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleStart()}
            placeholder={mode === 'concept' ? '输入要学习的知识点，如：事务隔离级别' :
                          mode === 'mock_exam' ? '输入考试范围，如：数据库系统概论' :
                          '输入学习主题...'}
            className="flex-1 rounded-xl border border-border bg-white px-4 py-2.5 text-sm placeholder:text-muted-foreground focus:border-primary focus:outline-none"
          />
          <button
            onClick={handleStart}
            disabled={!topic.trim() || startMutation.isPending}
            className="rounded-xl bg-primary px-6 py-2.5 text-sm font-semibold text-primary-foreground hover:bg-primary/90 disabled:opacity-40"
          >
            {startMutation.isPending ? '准备中...' : '开始学习'}
          </button>
        </div>
      )}

      {/* Loading / Generating */}
      {(startMutation.isPending || replyMutation.isPending) && (
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <span className="inline-block h-3 w-3 animate-spin rounded-full border-2 border-primary border-t-transparent" />
          {startMutation.isPending ? '正在准备学习内容...' : '正在思考...'}
        </div>
      )}

      {/* Chat / Interaction area */}
      {messages.length > 0 && (
        <div className="space-y-4 rounded-2xl border border-border bg-white p-5 shadow-sm">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`rounded-xl px-4 py-3 ${
                msg.role === 'user'
                  ? 'ml-8 bg-primary text-primary-foreground'
                  : 'mr-8 bg-secondary/60 text-foreground'
              }`}
            >
              <Markdown>{msg.content}</Markdown>
            </div>
          ))}
          <div ref={bottomRef} />
        </div>
      )}

      {/* Correct answer reveal (closed book mode) */}
      {correctAnswer && complete && (
        <div className="rounded-2xl border border-amber-200 bg-amber-50 p-5">
          <h3 className="text-sm font-semibold text-amber-800">📋 标准答案</h3>
          <div className="mt-2 text-amber-900">
            <Markdown>{correctAnswer}</Markdown>
          </div>
        </div>
      )}

      {/* Input area (for interactive modes) */}
      {sessionId && !complete && (
        <div className="flex gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault()
                handleSend()
              }
            }}
            placeholder={
              mode === 'socratic' ? '输入你的思考和回答...' :
              mode === 'step_by_step' ? '输入这一步的答案...' :
              '输入你的答案...'
            }
            rows={2}
            className="flex-1 resize-none rounded-xl border border-border bg-white px-4 py-2.5 text-sm placeholder:text-muted-foreground focus:border-primary focus:outline-none"
          />
          <button
            onClick={handleSend}
            disabled={!input.trim() || replyMutation.isPending}
            className="shrink-0 rounded-xl bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground hover:bg-primary/90 disabled:opacity-40"
          >
            发送
          </button>
        </div>
      )}

      {/* Complete / Reset */}
      {complete && (
        <div className="flex gap-2">
          <button
            onClick={handleReset}
            className="rounded-xl bg-primary px-6 py-2.5 text-sm font-semibold text-primary-foreground hover:bg-primary/90"
          >
            重新开始
          </button>
          <span className="flex items-center text-sm text-muted-foreground">
            ✅ 本轮学习完成
          </span>
        </div>
      )}
    </div>
  )
}
