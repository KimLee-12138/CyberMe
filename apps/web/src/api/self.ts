import { api } from './client'

export interface SelfFact {
  id: string
  type: string
  title?: string | null
  label?: string
  course_code?: string | null
  verification?: string | null
  node_type?: string
  path?: string
  properties?: Record<string, unknown>
}

export interface SelfInference {
  id: string
  source_label: string
  target_label: string
  edge_type: string
  confidence: number | null
  evidence: Record<string, unknown>
}

export interface StyleSample {
  id: string
  content: string
  sample_type: 'approved' | 'rejected'
  note: string | null
  created_at: string
}

export interface SelfModelData {
  facts: SelfFact[]
  facts_count: number
  inferences: SelfInference[]
  inferences_count: number
  style_samples: StyleSample[]
}

export async function fetchSelfModel(): Promise<SelfModelData> {
  return api.get('/self')
}

export async function addStyleSample(data: {
  content: string
  sample_type: 'approved' | 'rejected'
  note?: string
}): Promise<StyleSample> {
  return api.post('/self/style-samples', data)
}

export async function removeStyleSample(id: string): Promise<{ status: string }> {
  return api.delete(`/self/style-samples/${id}`)
}
