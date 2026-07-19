import { useState, useRef, useEffect, useCallback } from 'react'
import Markdown from '../components/ui/Markdown'
import { useTitle } from '../lib/useTitle'
import type { Conversation, Message, Citation } from '../api/chat'
import * as chatApi from '../api/chat'

/** Preprocess markdown to fix common model-generated formatting issues. */
function fixMarkdown(text: string): string {
  // Fix: tables where the separator row is on the same line as header
  // Pattern: | col1 | col2 | | :--- | :--- |
  // Repaired: split into two rows
  text = text.replace(
    /^(\|(?:[^|\n]+)\|)\s*(\|(?:\s*:?-{2,}:?\s*)\|)/gm,
    '$1\n$2'
  )

  // Fix: data rows joined right after separator row on same line
  // Pattern: | :--- | :--- | | data1 | data2 |
  text = text.replace(
    /^(\|(?:\s*:?-{2,}:?\s*)+)\|\s*(\|[^|\n]+\|)/gm,
    '$1\n$2'
  )

  return text
}

type AnswerMode = 'normal' | 'evidence_only' | 'deep_research'

const MODE_LABELS: Record<AnswerMode, { label: string; desc: string }> = {
  normal: { label: '知识问答', desc: '优先使用知识库证据' },
  evidence_only: { label: '只查资料', desc: '仅使用 Vault 证据' },
  deep_research: { label: '深度研究', desc: '多轮检索，全面分析' },
}

export default function ChatPage() {
  useTitle('问答')
  const [conversations, setConversations] = useState<Conversation[]>([])
  const [activeConvId, setActiveConvId] = useState<string | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [mode, setMode] = useState<AnswerMode>('normal')
  const [sending, setSending] = useState(false)
  const [streamingText, setStreamingText] = useState('')
  const [streamingCitations, setStreamingCitations] = useState<Citation[]>([])
  const [selectedCitation, setSelectedCitation] = useState<Citation | null>(null)
  const [showEvidence, setShowEvidence] = useState(false)

  const messagesEndRef = useRef<HTMLDivElement>(null)
  const eventSourceRef = useRef<EventSource | null>(null)

  // Load conversations
  useEffect(() => {
    chatApi.listConversations()
      .then(res => setConversations(res.conversations))
      .catch(() => {})
  }, [])

  // Scroll to bottom on new messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, streamingText])

  // Clean up SSE on unmount
  useEffect(() => {
    return () => {
      eventSourceRef.current?.close()
    }
  }, [])

  const handleCreateConv = async () => {
    try {
      const conv = await chatApi.createConversation()
      setConversations(prev => [conv, ...prev])
      setActiveConvId(conv.id)
      setMessages([])
      setStreamingText('')
    } catch {
      // ignore
    }
  }

  const handleSelectConv = async (convId: string) => {
    eventSourceRef.current?.close()
    setActiveConvId(convId)
    setStreamingText('')
    setStreamingCitations([])
    try {
      const conv = await chatApi.getConversation(convId)
      setMessages(conv.messages || [])
    } catch {
      // ignore
    }
  }

  const handleSend = useCallback(async () => {
    const trimmed = input.trim()
    if (!trimmed || sending) return

    // Ensure we have a conversation
    let convId = activeConvId
    if (!convId) {
      try {
        const conv = await chatApi.createConversation()
        setConversations(prev => [conv, ...prev])
        convId = conv.id
        setActiveConvId(convId)
      } catch {
        return
      }
    }

    setInput('')
    setSending(true)
    setStreamingText('')
    setStreamingCitations([])

    // Add user message optimistically
    const userMsg: Message = {
      id: `temp_user_${Date.now()}`,
      role: 'user',
      content: trimmed,
      created_at: new Date().toISOString(),
    }
    setMessages(prev => [...prev, userMsg])

    // Use SSE streaming
    const url = chatApi.getStreamUrl(convId, trimmed, mode)
    const es = new EventSource(url, { withCredentials: true })
    eventSourceRef.current = es

    let fullAnswer = ''

    es.addEventListener('token', (e) => {
      try {
        const data = JSON.parse(e.data)
        fullAnswer += data.text
        setStreamingText(fullAnswer)
      } catch { /* ignore */ }
    })

    es.addEventListener('citations', (e) => {
      try {
        const data = JSON.parse((e as MessageEvent).data)
        if (data.citations) setStreamingCitations((prev) => [...prev, ...data.citations])
      } catch { /* ignore */ }
    })

    es.addEventListener('error', () => {
      es.close()
      setSending(false)
      if (fullAnswer) {
        const assistantMsg: Message = {
          id: `assistant_${Date.now()}`,
          role: 'assistant',
          content: fullAnswer,
          created_at: new Date().toISOString(),
        }
        setMessages(prev => [...prev, assistantMsg])
      }
      setStreamingText('')
      setStreamingCitations([])
    })

    es.addEventListener('done', () => {
      es.close()
      setSending(false)
      const assistantMsg: Message = {
        id: `assistant_${Date.now()}`,
        role: 'assistant',
        content: fullAnswer,
        created_at: new Date().toISOString(),
      }
      setMessages(prev => [...prev, assistantMsg])
      setStreamingText('')
      setStreamingCitations([])

      // Refresh conversation list
      chatApi.listConversations()
        .then(res => setConversations(res.conversations))
        .catch(() => {})
    })
  }, [input, sending, activeConvId, mode])

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="flex h-full gap-0">
      {/* Left: Conversation list */}
      <div className="hidden w-56 shrink-0 border-r border-border bg-secondary/30 lg:flex lg:flex-col">
        <div className="flex items-center justify-between border-b border-border px-3 py-3">
          <span className="text-sm font-semibold text-foreground">对话</span>
          <button
            onClick={handleCreateConv}
            className="flex h-7 w-7 items-center justify-center rounded-lg bg-primary text-primary-foreground text-lg leading-none hover:bg-primary/90 transition-colors"
            title="新建对话"
          >
            +
          </button>
        </div>
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {conversations.length === 0 && (
            <p className="px-2 py-4 text-center text-xs text-muted-foreground">
              还没有对话
            </p>
          )}
          {conversations.map(conv => (
            <button
              key={conv.id}
              onClick={() => handleSelectConv(conv.id)}
              className={`w-full rounded-lg px-3 py-2 text-left text-sm transition-colors ${
                activeConvId === conv.id
                  ? 'bg-primary/10 text-primary font-medium'
                  : 'text-foreground hover:bg-secondary'
              }`}
            >
              <span className="line-clamp-1">{conv.title}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Center: Chat area */}
      <div className="flex flex-1 flex-col min-w-0">
        {/* Mode selector + mobile create button */}
        <div className="flex items-center gap-2 border-b border-border px-4 py-2">
          <button
            onClick={handleCreateConv}
            className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground text-lg lg:hidden"
          >
            +
          </button>
          <div className="flex gap-1">
            {(Object.keys(MODE_LABELS) as AnswerMode[]).map(m => (
              <button
                key={m}
                onClick={() => setMode(m)}
                className={`rounded-full px-3 py-1 text-xs font-medium transition-colors ${
                  mode === m
                    ? 'bg-primary text-primary-foreground'
                    : 'bg-secondary text-muted-foreground hover:bg-secondary/80'
                }`}
                title={MODE_LABELS[m].desc}
              >
                {MODE_LABELS[m].label}
              </button>
            ))}
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto px-4 py-4 space-y-4">
          {messages.length === 0 && !streamingText && (
            <div className="flex h-full items-center justify-center">
              <div className="text-center max-w-md">
                <span className="text-4xl">🧠</span>
                <h2 className="mt-3 text-lg font-semibold text-foreground">
                  知识问答
                </h2>
                <p className="mt-2 text-sm text-muted-foreground">
                  基于你的个人知识库提问。当前模式：{MODE_LABELS[mode].label}
                </p>
                <div className="mt-4 flex flex-wrap justify-center gap-2">
                  {['数据库事务隔离级别', '什么是 FSRS 算法', '操作系统进程调度方式'].map(hint => (
                    <button
                      key={hint}
                      onClick={() => { setInput(hint); /* focus handled by ref */ }}
                      className="rounded-full border border-border px-3 py-1.5 text-xs text-muted-foreground hover:bg-secondary transition-colors"
                    >
                      {hint}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {messages.map(msg => (
            <div
              key={msg.id}
              className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                  msg.role === 'user'
                    ? 'bg-primary text-primary-foreground'
                    : 'bg-secondary text-foreground'
                }`}
              >
                <Markdown>{fixMarkdown(msg.content)}</Markdown>
                {msg.citations && msg.citations.length > 0 && (
                  <div className="mt-2 border-t border-border/50 pt-2">
                    <p className="text-xs font-medium text-muted-foreground mb-1">引用来源：</p>
                    <div className="flex flex-wrap gap-1">
                      {msg.citations.map(c => (
                        <button
                          key={c.citation_id}
                          onClick={() => { setSelectedCitation(c); setShowEvidence(true) }}
                          className="rounded-full bg-primary/10 px-2 py-0.5 text-xs text-primary hover:bg-primary/20 transition-colors"
                        >
                          [{c.citation_id}] {c.heading?.slice(0, 20) || c.path}
                        </button>
                      ))}
                    </div>
                  </div>
                )}
                {msg.model && (
                  <p className="mt-1 text-xs text-muted-foreground/70">
                    {msg.model} · {msg.latency_ms ? `${(msg.latency_ms / 1000).toFixed(1)}s` : ''}
                  </p>
                )}
              </div>
            </div>
          ))}

          {/* Streaming indicator */}
          {streamingText && (
            <div className="flex justify-start">
              <div className="max-w-[80%] rounded-2xl bg-secondary px-4 py-3">
                <Markdown>{fixMarkdown(streamingText)}</Markdown>
                <span className="inline-block w-1.5 h-4 bg-primary animate-pulse ml-0.5 align-text-bottom" />
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <div className="border-t border-border px-4 py-3">
          <div className="flex gap-2">
            <textarea
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={
                mode === 'evidence_only'
                  ? '仅基于知识库资料回答...'
                  : mode === 'deep_research'
                  ? '深度研究模式...'
                  : '输入问题，Enter 发送，Shift+Enter 换行'
              }
              rows={1}
              className="flex-1 resize-none rounded-xl border border-border bg-background px-4 py-2.5 text-sm placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || sending}
              className="shrink-0 rounded-xl bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground hover:bg-primary/90 disabled:opacity-40 transition-all"
            >
              {sending ? '...' : '发送'}
            </button>
          </div>
        </div>
      </div>

      {/* Right: Evidence panel */}
      {showEvidence && selectedCitation && (
        <div className="hidden w-80 shrink-0 border-l border-border bg-secondary/10 xl:flex xl:flex-col">
          <div className="flex items-center justify-between border-b border-border px-4 py-3">
            <h3 className="text-sm font-semibold text-foreground">证据详情</h3>
            <button
              onClick={() => setShowEvidence(false)}
              className="rounded-lg p-1 text-muted-foreground hover:bg-secondary transition-colors"
            >
              ✕
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-4 space-y-3">
            <div>
              <p className="text-xs font-medium text-muted-foreground">来源文件</p>
              <p className="text-sm text-foreground font-mono break-all">{selectedCitation.path}</p>
            </div>
            <div>
              <p className="text-xs font-medium text-muted-foreground">标题</p>
              <p className="text-sm text-foreground">{selectedCitation.heading}</p>
            </div>
            {selectedCitation.source && (
              <div>
                <p className="text-xs font-medium text-muted-foreground">原始来源</p>
                <p className="text-sm text-foreground">{selectedCitation.source}</p>
                {selectedCitation.source_pages && (
                  <p className="text-xs text-muted-foreground">页码：{selectedCitation.source_pages}</p>
                )}
              </div>
            )}
            <div>
              <p className="text-xs font-medium text-muted-foreground">可信度</p>
              <span className={`inline-block rounded-full px-2 py-0.5 text-xs font-medium ${
                selectedCitation.verification === 'explicit'
                  ? 'bg-green-100 text-green-700'
                  : 'bg-yellow-100 text-yellow-700'
              }`}>
                {selectedCitation.verification === 'explicit' ? 'A · 已确认' : 'C · 待验证'}
              </span>
            </div>
            <div>
              <p className="text-xs font-medium text-muted-foreground">内容片段</p>
              <div className="mt-1 rounded-lg border border-border bg-background p-3 text-sm text-foreground max-h-60 overflow-y-auto whitespace-pre-wrap">
                {selectedCitation.content_snippet}
              </div>
            </div>
            <div>
              <p className="text-xs font-medium text-muted-foreground">相关度评分</p>
              <div className="mt-1 h-1.5 rounded-full bg-secondary">
                <div
                  className="h-full rounded-full bg-primary transition-all"
                  style={{ width: `${(selectedCitation.score * 100).toFixed(0)}%` }}
                />
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
