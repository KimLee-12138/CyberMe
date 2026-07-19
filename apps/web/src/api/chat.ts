import { api } from './client'

export interface Conversation {
  id: string
  title: string
  created_at: string
  updated_at: string
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  citations?: Citation[]
  evidence?: EvidenceBundle
  model?: string
  latency_ms?: number
  created_at: string
}

export interface Citation {
  citation_id: string
  evidence_id: string
  document_id: string
  path: string
  heading: string
  source: string
  source_pages: string
  content_snippet: string
  verification: string
  score: number
}

export interface EvidenceItem {
  evidence_id: string
  document_id: string
  path: string
  heading: string
  content: string
  source: string
  source_pages: string
  verification: string
  score: number
}

export interface EvidenceBundle {
  query: string
  scope: string[]
  items: EvidenceItem[]
  conflicts: Array<{ evidence_a: string; evidence_b: string; topic: string }>
  coverage: number
}

export interface SendMessageResponse {
  id: string
  role: string
  content: string
  citations: Citation[]
  evidence: EvidenceBundle
  usage?: { prompt_tokens: number; completion_tokens: number }
  model?: string
  latency_ms?: number
  created_at: string
}

export async function createConversation(title?: string) {
  return api.post<Conversation>('/conversations', { title })
}

export async function listConversations() {
  return api.get<{ conversations: Conversation[] }>('/conversations')
}

export async function getConversation(convId: string) {
  return api.get<Conversation & { messages: Message[] }>(`/conversations/${convId}`)
}

export async function sendMessage(
  convId: string,
  content: string,
  mode: string = 'normal',
  scope?: Record<string, string[]>,
) {
  return api.post<SendMessageResponse>(`/conversations/${convId}/messages`, {
    content,
    mode,
    scope,
  })
}

export function getStreamUrl(convId: string, query: string, mode: string = 'normal'): string {
  return `/api/v1/conversations/${convId}/stream?q=${encodeURIComponent(query)}&mode=${mode}`
}

export async function quickAsk(
  content: string,
  mode: string = 'normal',
  scope?: Record<string, string[]>,
) {
  return api.post<SendMessageResponse>('/ask', { content, mode, scope })
}
