import { useCallback, useEffect, useRef, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { BrainCircuit, CheckCircle2, HelpCircle, Layers, Loader2, RotateCcw, Sparkles, XCircle } from 'lucide-react'
import Markdown from '../components/ui/Markdown'
import Select from '../components/ui/Select'
import { useTitle } from '../lib/useTitle'
import type { QuizQuestion, RagAskResponse, RagEvidence } from '../api/chat'
import * as chatApi from '../api/chat'

function fixMarkdown(text: string): string {
  text = text.replace(
    /^(\|(?:[^|\n]+)\|)\s*(\|(?:\s*:?-{2,}:?\s*)\|)/gm,
    '$1\n$2'
  )
  text = text.replace(
    /^(\|(?:\s*:?-{2,}:?\s*)+)\|\s*(\|[^|\n]+\|)/gm,
    '$1\n$2'
  )
  return text
}

function pagesLabel(pages: number[][] | undefined): string {
  if (!pages || pages.length === 0) return ''
  return pages.map(([a, b]) => (a === b ? `p.${a}` : `p.${a}-${b}`)).join(', ')
}

function locator(e: RagEvidence): string {
  const pages = pagesLabel(e.pages)
  return pages || '本地知识库'
}

function evidenceNo(e: RagEvidence, index: number): string {
  const raw = (e.evidence_id || '').replace(/^E/i, '')
  return raw || String(index + 1)
}

function EvidenceCards({
  result,
  selected,
  onSelect,
}: {
  result: RagAskResponse
  selected: RagEvidence | null
  onSelect: (e: RagEvidence) => void
}) {
  return (
    <>
      {result.evidence.map((e, index) => {
        const isSelected = selected?.evidence_id === e.evidence_id
        return (
          <button
            key={e.evidence_id}
            onClick={() => onSelect(e)}
            className={`w-full rounded-xl border p-3 text-left transition-colors ${
              isSelected
                ? 'border-primary bg-primary/5'
                : 'border-border bg-background hover:bg-secondary/50'
            }`}
          >
            <div className="flex items-center justify-between gap-2">
              <span className="rounded-full bg-[#eef4ff] px-2 py-0.5 text-[10px] font-semibold text-[#2563eb]">
                来源 {evidenceNo(e, index)}
              </span>
              <span className="text-[10px] text-muted-foreground">
                {e.kind === 'note' ? '笔记' : '原文'} · {e.course}
              </span>
            </div>
            <p className="mt-1 line-clamp-1 text-xs font-medium text-foreground">{e.title}</p>
            <p className="text-[11px] text-muted-foreground">§ {e.heading}</p>
            <p className="mt-0.5 text-[10px] text-muted-foreground/80">{locator(e)}</p>
            <p className="mt-1 line-clamp-3 text-[11px] leading-relaxed text-muted-foreground">
              {e.snippet.replace(/\n+/g, ' ')}
            </p>
          </button>
        )
      })}

      {selected && (
        <div className="rounded-xl border border-border bg-background p-3">
          <p className="text-[11px] font-medium text-muted-foreground">当前证据全文</p>
          <p className="mt-1 font-mono text-[10px] text-muted-foreground/80">{locator(selected)}</p>
          <div className="mt-2 max-h-56 overflow-y-auto whitespace-pre-wrap text-[11px] leading-relaxed text-foreground">
            {selected.snippet}
          </div>
        </div>
      )}
    </>
  )
}

interface Turn {
  id: string
  question: string
  result: RagAskResponse
}

interface QuizState {
  loading: boolean
  questions: QuizQuestion[]
  selected: Record<string, number>
  submitted: boolean
  error: string
}

const COURSES = [
  { value: '', label: '全部课程' },
  { value: 'DB', label: '数据库' },
  { value: 'ALGO', label: '算法' },
  { value: 'DS', label: '数据结构' },
  { value: 'CO', label: '计组' },
  { value: 'SE', label: '软件工程' },
  { value: 'PROB', label: '概率论' },
  { value: 'CALCULUS', label: '微积分' },
  { value: 'MAYUAN', label: '马原' },
  { value: 'XIGAI', label: '习概' },
  { value: 'HISTORY', label: '近代史' },
  { value: 'MAOGAI', label: '毛概' },
  { value: 'ASM', label: '汇编' },
  { value: 'EDA', label: 'EDA' },
  { value: 'JAVA', label: 'Java' },
  { value: 'JUNLI', label: '军理' },
  { value: 'RLMATH', label: '强化学习数学' },
  { value: 'PHYSICS', label: '大学物理' },
  { value: 'DISCRETE', label: '离散数学' },
  { value: 'CPP', label: 'C++' },
]

const EXAMPLES = [
  { q: '什么是函数依赖？', course: 'DB' },
  { q: '2NF 和 3NF 的区别是什么？', course: 'DB' },
  { q: '0/1 背包为什么容量要逆序？', course: 'ALGO' },
  { q: '栈和队列的区别是什么？', course: 'DS' },
  { q: '数据库索引的原理是什么？', course: 'DB' },
]

export default function ChatPage() {
  useTitle('问答')
  const [searchParams] = useSearchParams()
  const [turns, setTurns] = useState<Turn[]>([])
  const [input, setInput] = useState(searchParams.get('q') || '')
  const [course, setCourse] = useState('')
  const [sending, setSending] = useState(false)
  const [error, setError] = useState('')
  const [activeTurnId, setActiveTurnId] = useState<string | null>(null)
  const [selected, setSelected] = useState<RagEvidence | null>(null)
  const [evidenceOpen, setEvidenceOpen] = useState(false)
  const [quizzes, setQuizzes] = useState<Record<string, QuizState>>({})
  const [stats, setStats] = useState<{ chunks?: number; notes?: number; sources?: number } | null>(null)
  const endRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const q = searchParams.get('q')
    if (q) setInput(q)
  }, [searchParams])

  useEffect(() => {
    fetch('/api/v1/rag/health', { credentials: 'include' })
      .then(r => r.json())
      .then(setStats)
      .catch(() => {})
  }, [])

  useEffect(() => {
    if (!turns.length && !sending) return
    endRef.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
  }, [turns, sending])

  const activeTurn = turns.find(t => t.id === activeTurnId) || turns[turns.length - 1]
  const activeResult = activeTurn?.result

  const openEvidence = (turnId: string, evidence?: RagEvidence) => {
    setActiveTurnId(turnId)
    if (evidence) setSelected(evidence)
    setEvidenceOpen(true)
  }

  const runQuery = useCallback(async (question: string, courseCode?: string) => {
    const q = question.trim()
    if (!q || sending) return
    setSending(true)
    setError('')
    setInput('')
    try {
      const result = await chatApi.askRag(q, courseCode || undefined, 8)
      const turn: Turn = {
        id: `t_${Date.now()}`,
        question: q,
        result,
      }
      setTurns(prev => [...prev, turn])
      setActiveTurnId(turn.id)
      setSelected(result.citations?.[0] || result.evidence?.[0] || null)
    } catch (e) {
      setError(e instanceof Error ? e.message : '请求失败，请稍后再试')
    } finally {
      setSending(false)
    }
  }, [sending])

  const handleSend = useCallback(() => {
    runQuery(input, course)
  }, [input, course, runQuery])

  const startQuiz = async (turn: Turn) => {
    setQuizzes(prev => ({
      ...prev,
      [turn.id]: { loading: true, questions: [], selected: {}, submitted: false, error: '' },
    }))
    try {
      const data = await chatApi.askRagQuiz(turn.question, turn.result.answer, 3)
      setQuizzes(prev => ({
        ...prev,
        [turn.id]: {
          loading: false,
          questions: data.questions,
          selected: {},
          submitted: false,
          error: '',
        },
      }))
    } catch (e) {
      setQuizzes(prev => ({
        ...prev,
        [turn.id]: {
          loading: false,
          questions: [],
          selected: {},
          submitted: false,
          error: e instanceof Error ? e.message : '出题失败，请稍后再试',
        },
      }))
    }
  }

  const chooseQuizOption = (turnId: string, questionId: string, optionIndex: number) => {
    setQuizzes(prev => {
      const current = prev[turnId]
      if (!current || current.submitted) return prev
      return {
        ...prev,
        [turnId]: { ...current, selected: { ...current.selected, [questionId]: optionIndex } },
      }
    })
  }

  const submitQuiz = (turnId: string) => {
    setQuizzes(prev => {
      const current = prev[turnId]
      if (!current) return prev
      return { ...prev, [turnId]: { ...current, submitted: true } }
    })
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  const reset = () => {
    setTurns([])
    setSelected(null)
    setActiveTurnId(null)
    setError('')
    setInput('')
  }

  return (
    <div className="flex h-[calc(100dvh-9rem)] min-h-[560px] overflow-hidden rounded-[24px] border border-[#e3eaf3] bg-white shadow-[0_24px_70px_-40px_rgba(15,31,58,0.4)]">
      {/* Left: examples */}
      <aside className="hidden w-[236px] shrink-0 flex-col border-r border-[#edf1f7] bg-[#f8fafc] lg:flex">
        <div className="border-b border-[#edf1f7] px-4 py-4">
          <div className="flex items-center gap-2">
            <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-[#eef4ff] text-[#2563eb]"><Sparkles size={14} /></span>
            <p className="text-[12px] font-bold">示例问题</p>
          </div>
          <p className="mt-1.5 text-[10px] text-muted-foreground">基于语料 v1 · 本地会话</p>
        </div>
        <div className="flex-1 space-y-1 overflow-y-auto p-2">
          {EXAMPLES.map((example) => (
            <button
              key={example.q}
              onClick={() => {
                setCourse(example.course)
                runQuery(example.q, example.course)
              }}
              className="w-full rounded-xl px-3 py-2.5 text-left transition-colors hover:bg-white hover:shadow-sm"
            >
              <span className="line-clamp-2 text-[11px] font-medium leading-5 text-foreground">{example.q}</span>
              <span className="mt-1 block text-[9px] font-semibold tracking-wide text-muted-foreground">{example.course}</span>
            </button>
          ))}
        </div>
        <div className="border-t border-[#edf1f7] p-3">
          <button onClick={reset} className="app-button app-button-secondary w-full !min-h-9 !text-[11px]">
            <RotateCcw size={13} /> 清空对话
          </button>
        </div>
      </aside>

      {/* Center */}
      <section className="flex min-w-0 flex-1 flex-col bg-white">
        <header className="flex flex-wrap items-center gap-2 border-b border-[#edf1f7] px-4 py-3 sm:px-5">
          <div className="mr-auto flex items-center gap-2.5">
            <span className="flex h-8 w-8 items-center justify-center rounded-xl bg-[#071a33] text-white"><BrainCircuit size={16} /></span>
            <div>
              <h1 className="text-[13px] font-bold tracking-tight">知识问答</h1>
              <p className="mt-0.5 text-[10px] text-muted-foreground">
                RAG v1{stats?.chunks ? ` · ${stats.chunks.toLocaleString()} chunks` : ''}{stats?.notes ? ` · ${stats.notes} notes` : ''}
              </p>
            </div>
          </div>
          <Select value={course} options={COURSES} onChange={setCourse} ariaLabel="课程筛选" size="sm" className="w-36" />
          <button onClick={reset} className="app-button app-button-ghost !min-h-9 !px-2.5 !text-[11px]">
            新对话
          </button>
        </header>

        <div className="flex-1 space-y-5 overflow-y-auto bg-[#fbfcfe] px-4 py-5 sm:px-6">
          {turns.length === 0 && !sending && (
            <div className="flex min-h-full items-center justify-center py-8">
              <div className="w-full max-w-md text-center">
                <span className="mx-auto flex h-16 w-16 items-center justify-center rounded-[22px] bg-gradient-to-br from-[#eef4ff] to-[#dce9ff] text-[#2563eb] shadow-[0_12px_30px_-16px_rgba(37,99,235,0.6)]">
                  <BrainCircuit size={28} />
                </span>
                <h2 className="mt-4 text-[20px] font-[750] tracking-[-0.04em]">问你的课程知识库</h2>
                <p className="mx-auto mt-2 max-w-sm text-[12px] leading-6 text-muted-foreground">
                  回答只使用 433 篇笔记与 414 个来源 section；证据不足会明确拒答。
                </p>
                <div className="mt-5 flex flex-wrap justify-center gap-2">
                  {EXAMPLES.slice(0, 3).map((example) => (
                    <button
                      key={example.q}
                      onClick={() => {
                        setCourse(example.course)
                        runQuery(example.q, example.course)
                      }}
                      className="rounded-full border border-[#e3eaf3] bg-white px-3 py-2 text-[10px] font-medium text-[#506785] shadow-sm transition-all hover:border-[#8bb3ff] hover:text-[#2563eb]"
                    >
                      {example.q}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {turns.map((turn) => {
            const result = turn.result
            const quiz = quizzes[turn.id]
            return (
              <div key={turn.id} className="space-y-2.5">
                <div className="flex justify-end">
                  <div className="max-w-[82%] rounded-[18px] rounded-br-md bg-gradient-to-br from-[#0b1f3a] to-[#153b70] px-4 py-2.5 text-[12px] leading-6 text-white shadow-[0_10px_24px_-16px_rgba(11,31,58,0.7)]">
                    {turn.question}
                  </div>
                </div>

                <div className="flex justify-start">
                  <div className="max-w-[92%] rounded-[18px] rounded-bl-md border border-[#e8edf5] bg-white px-4 py-3.5 text-[12px] leading-6 text-foreground shadow-[0_8px_20px_-18px_rgba(15,31,58,0.35)]">
                    {result.degraded && (
                      <div className="mb-2 rounded-xl border border-[#fde2af] bg-[#fffdf5] px-3 py-2 text-[11px] leading-5 text-[#92400e]">
                        <span className="font-semibold">未检索到足够的本地资料</span>
                        <span className="text-[#a16207]">，已降级使用 DeepSeek 模型知识回答；以下内容不是你的课程资料。</span>
                      </div>
                    )}
                    {result.refused && !result.degraded && (
                      <div className="mb-2 rounded-xl border border-[#fecaca] bg-[#fff8f8] px-3 py-2 text-[11px] text-[#b42318]">
                        证据不足：{result.refusal_reason || '没有找到足够依据'}
                      </div>
                    )}
                    <Markdown>{fixMarkdown(result.answer)}</Markdown>

                    {result.citations?.length > 0 && (
                      <div className="mt-3 border-t border-[#edf1f7] pt-2">
                        <p className="mb-1.5 text-[10px] font-semibold text-muted-foreground">参考来源</p>
                        <div className="flex flex-wrap gap-1.5">
                          {result.citations.map((citation, index) => (
                            <button
                              key={citation.evidence_id}
                              onClick={() => openEvidence(turn.id, citation)}
                              className="inline-flex max-w-full items-center gap-1.5 rounded-full bg-[#eef4ff] px-2.5 py-1 text-[9px] font-medium text-[#2563eb] transition-colors hover:bg-[#dce9ff]"
                              title={locator(citation)}
                            >
                              <span className="flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-[#2563eb] text-[8px] font-bold text-white">{index + 1}</span>
                              <span className="truncate">{citation.title} · {citation.heading}</span>
                              {locator(citation) && <span className="shrink-0 text-[#6b8dc9]">{locator(citation)}</span>}
                            </button>
                          ))}
                        </div>
                      </div>
                    )}

                    <button
                      onClick={() => openEvidence(turn.id)}
                      className="mt-2.5 w-full rounded-xl border border-[#dce9ff] bg-[#f7faff] px-3 py-2 text-[11px] font-semibold text-[#2563eb] hover:bg-[#eef4ff] xl:hidden"
                    >
                      查看证据（{result.evidence.length}）
                    </button>

                    {/* Quiz card: offer → option cards → explanation */}
                    <div className="mt-3 rounded-2xl border border-[#e3eaf3] bg-[#f8fafc] p-3">
                      <div className="flex items-center justify-between gap-2">
                        <div className="flex items-center gap-2">
                          <span className="flex h-6 w-6 items-center justify-center rounded-lg bg-[#eef4ff] text-[#2563eb]"><HelpCircle size={14} /></span>
                          <div>
                            <p className="text-[11px] font-bold text-foreground">检验一下</p>
                            <p className="text-[9px] text-muted-foreground">3 道单选题 · 由刚才的讲解生成</p>
                          </div>
                        </div>
                        {!quiz && (
                          <button onClick={() => startQuiz(turn)} className="app-button app-button-secondary !min-h-8 !px-2.5 !text-[10px]">
                            出 3 道题
                          </button>
                        )}
                      </div>

                      {quiz?.loading && (
                        <div className="mt-3 flex items-center gap-2 text-[10px] text-muted-foreground">
                          <Loader2 size={13} className="animate-spin" /> 正在出题…
                        </div>
                      )}

                      {quiz?.error && (
                        <div className="mt-2 rounded-xl border border-[#fecaca] bg-[#fff8f8] px-3 py-2 text-[10px] text-[#b42318]">
                          {quiz.error}
                          <button onClick={() => startQuiz(turn)} className="ml-2 font-semibold underline">重试</button>
                        </div>
                      )}

                      {quiz && !quiz.loading && quiz.questions.length > 0 && (
                        <div className="mt-3 space-y-3">
                          {quiz.questions.map((q, qi) => {
                            const picked = quiz.selected[q.id]
                            return (
                              <div key={q.id} className="rounded-xl border border-[#e8edf5] bg-white p-3">
                                <p className="text-[11px] font-semibold leading-5 text-foreground">{qi + 1}. {q.question}</p>
                                <div className="mt-2 grid gap-1.5">
                                  {q.options.map((option, oi) => {
                                    const isPicked = picked === oi
                                    const isCorrect = q.answer_index === oi
                                    let cls = 'border-[#e3eaf3] bg-white hover:border-[#8bb3ff]'
                                    if (!quiz.submitted && isPicked) cls = 'border-[#2563eb] bg-[#eef4ff]'
                                    if (quiz.submitted && isCorrect) cls = 'border-emerald-400 bg-emerald-50'
                                    if (quiz.submitted && isPicked && !isCorrect) cls = 'border-red-300 bg-red-50'
                                    return (
                                      <button
                                        key={`${q.id}-${oi}`}
                                        disabled={quiz.submitted}
                                        onClick={() => chooseQuizOption(turn.id, q.id, oi)}
                                        className={`flex w-full items-start gap-2 rounded-lg border px-2.5 py-2 text-left text-[10px] leading-5 transition-colors disabled:cursor-default ${cls}`}
                                      >
                                        <span className={`flex h-4 w-4 shrink-0 items-center justify-center rounded-full text-[8px] font-bold ${isPicked ? 'bg-[#2563eb] text-white' : 'bg-[#f1f5f9] text-[#64748b]'}`}>
                                          {String.fromCharCode(65 + oi)}
                                        </span>
                                        <span className="flex-1 text-foreground">{option}</span>
                                        {quiz.submitted && isCorrect && <CheckCircle2 size={13} className="shrink-0 text-emerald-600" />}
                                        {quiz.submitted && isPicked && !isCorrect && <XCircle size={13} className="shrink-0 text-red-500" />}
                                      </button>
                                    )
                                  })}
                                </div>
                                {quiz.submitted && q.explanation && (
                                  <p className="mt-2 rounded-lg bg-[#f8fafc] px-2.5 py-2 text-[9px] leading-5 text-muted-foreground">{q.explanation}</p>
                                )}
                              </div>
                            )
                          })}

                          {!quiz.submitted ? (
                            <button
                              onClick={() => submitQuiz(turn.id)}
                              disabled={quiz.questions.some((q) => quiz.selected[q.id] === undefined)}
                              className="app-button app-button-primary w-full !min-h-9 !text-[11px]"
                            >
                              提交答案
                            </button>
                          ) : (
                            <div className="flex flex-wrap items-center justify-between gap-2">
                              <p className="text-[11px] font-bold text-foreground">
                                得分 {quiz.questions.filter((q) => quiz.selected[q.id] === q.answer_index).length} / {quiz.questions.length}
                              </p>
                              <button onClick={() => startQuiz(turn)} className="app-button app-button-secondary !min-h-8 !px-2.5 !text-[10px]">
                                再出一组
                              </button>
                            </div>
                          )}
                        </div>
                      )}
                    </div>

                    <div className="mt-2.5 flex flex-wrap gap-2 text-[9px] text-muted-foreground/70">
                      {result.model && <span>{result.model}</span>}
                      {result.latency_ms != null && <span>{(result.latency_ms / 1000).toFixed(1)}s</span>}
                      {result.coverage != null && <span>coverage {result.coverage.toFixed(2)}</span>}
                      {result.usage?.prompt_tokens != null && <span>{result.usage.prompt_tokens}+{result.usage.completion_tokens} tokens</span>}
                    </div>
                  </div>
                </div>
              </div>
            )
          })}

          {sending && (
            <div className="flex justify-start">
              <div className="flex items-center gap-2 rounded-[18px] border border-[#e8edf5] bg-white px-4 py-3 text-[11px] text-muted-foreground shadow-sm">
                <span className="flex gap-1">
                  <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-[#2563eb] [animation-delay:-0.2s]" />
                  <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-[#2563eb] [animation-delay:-0.1s]" />
                  <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-[#2563eb]" />
                </span>
                正在检索并生成回答，约 15–20 秒…
              </div>
            </div>
          )}

          {error && (
            <div className="rounded-xl border border-[#fecaca] bg-[#fff8f8] px-4 py-3 text-[11px] text-[#b42318]">{error}</div>
          )}
          <div ref={endRef} />
        </div>

        <div className="border-t border-[#edf1f7] bg-white px-3 py-3 sm:px-5">
          <div className="flex items-end gap-2 rounded-2xl border border-[#e3eaf3] bg-[#fbfcfe] p-1.5 transition-all focus-within:border-[#8bb3ff] focus-within:bg-white focus-within:shadow-[0_0_0_4px_rgba(37,99,235,0.08)]">
            <textarea
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="输入问题，Enter 发送，Shift+Enter 换行"
              rows={1}
              className="max-h-32 min-h-10 flex-1 resize-none bg-transparent px-2.5 py-2 text-[12px] leading-5 text-foreground outline-none placeholder:text-[#94a3b8]"
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || sending}
              className="app-button app-button-accent !min-h-9 !rounded-xl !px-3.5 !text-[11px]"
            >
              {sending ? '生成中' : '发送'}
            </button>
          </div>
        </div>
      </section>

      {/* Right: evidence */}
      <aside className="hidden w-[350px] shrink-0 flex-col border-l border-[#edf1f7] bg-[#f8fafc] xl:flex">
        <div className="flex items-center justify-between border-b border-[#edf1f7] px-4 py-4">
          <div>
            <h3 className="text-[12px] font-bold">证据面板</h3>
            <p className="mt-0.5 text-[10px] text-muted-foreground">
              {activeResult ? `${activeResult.evidence.length} 条证据 · coverage ${activeResult.coverage?.toFixed(2) ?? '-'}` : '提问后显示检索证据'}
            </p>
          </div>
          {activeResult?.refused && <span className="app-chip app-chip-amber">证据不足</span>}
        </div>
        <div className="flex-1 space-y-2 overflow-y-auto p-3">
          {!activeResult && (
            <div className="rounded-2xl border border-dashed border-[#dbe3ef] bg-white/70 px-4 py-10 text-center">
              <Layers size={22} className="mx-auto text-[#b3c1d4]" />
              <p className="mt-2 text-[10px] leading-5 text-muted-foreground">证据会显示在这里：标题、章节、页码、片段、分数。</p>
            </div>
          )}
          {activeResult && <EvidenceCards result={activeResult} selected={selected} onSelect={setSelected} />}
        </div>
      </aside>

      {/* Mobile evidence sheet */}
      {evidenceOpen && activeResult && (
        <div className="fixed inset-0 z-50 flex items-end bg-[#071a33]/40 backdrop-blur-sm xl:hidden" onClick={() => setEvidenceOpen(false)}>
          <div className="app-pop-in relative flex max-h-[78vh] w-full flex-col rounded-t-[24px] border-t border-[#e3eaf3] bg-white shadow-2xl" onClick={(event) => event.stopPropagation()}>
            <div className="flex items-start justify-between border-b border-[#edf1f7] px-4 py-3">
              <div>
                <h3 className="text-[12px] font-bold">证据面板</h3>
                <p className="mt-0.5 text-[10px] text-muted-foreground">{activeResult.evidence.length} 条证据 · coverage {activeResult.coverage?.toFixed(2) ?? '-'}</p>
              </div>
              <button onClick={() => setEvidenceOpen(false)} className="app-button app-button-secondary !min-h-8 !px-2.5 !text-[10px]">关闭</button>
            </div>
            <div className="flex-1 space-y-2 overflow-y-auto p-3">
              <EvidenceCards result={activeResult} selected={selected} onSelect={setSelected} />
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
