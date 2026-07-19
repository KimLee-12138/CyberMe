import { api } from './client'

export interface ProjectInfo {
  id: string
  title: string
  goal: string | null
  status: string
  deadline: string | null
  created_at: string | null
  updated_at: string | null
}

export interface HypothesisInfo {
  id: string
  statement: string
  verification_criteria: string | null
  status: string
  evidence_for: string | null
  evidence_against: string | null
}

export interface ExperimentInfo {
  id: string
  design: string | null
  environment: string | null
  code_version: string | null
  parameters: Record<string, unknown>
  metrics: Record<string, unknown>
  result: Record<string, unknown>
  failed: boolean
  lessons_learned: string | null
}

export interface RiskInfo {
  id: string
  description: string
  probability: number
  impact: string
  trigger_signals: string | null
  mitigation: string | null
  status: string
}

export interface ProjectDetail extends ProjectInfo {
  success_criteria: string | null
  constraints: string | null
  hypotheses: HypothesisInfo[]
  experiments: ExperimentInfo[]
  risks: RiskInfo[]
}

// ── Projects ──────────────────────────────────────────

export async function fetchProjects(): Promise<{ projects: ProjectInfo[] }> {
  return api.get('/projects')
}
export async function fetchProject(id: string): Promise<ProjectDetail> {
  return api.get(`/projects/${id}`)
}
export async function createProject(data: { title: string; goal?: string; deadline?: string }): Promise<{ id: string }> {
  return api.post('/projects', data)
}
export async function updateProject(id: string, data: Record<string, unknown>): Promise<{ id: string; status: string }> {
  return api.patch(`/projects/${id}`, data)
}
export async function deleteProject(id: string): Promise<{ status: string }> {
  return api.delete(`/projects/${id}`)
}

// ── Hypotheses ────────────────────────────────────────

export async function createHypothesis(projectId: string, data: { statement: string; verification_criteria?: string }): Promise<{ id: string }> {
  return api.post(`/projects/${projectId}/hypotheses`, data)
}
export async function updateHypothesis(projectId: string, id: string, data: Record<string, unknown>): Promise<{ id: string; status: string }> {
  return api.patch(`/projects/${projectId}/hypotheses/${id}`, data)
}

// ── Experiments ───────────────────────────────────────

export async function createExperiment(projectId: string, data: Record<string, unknown>): Promise<{ id: string }> {
  return api.post(`/projects/${projectId}/experiments`, data)
}

// ── Risks ─────────────────────────────────────────────

export async function createRisk(projectId: string, data: { description: string; probability?: number; impact?: string; mitigation?: string }): Promise<{ id: string }> {
  return api.post(`/projects/${projectId}/risks`, data)
}
export async function updateRisk(projectId: string, id: string, data: Record<string, unknown>): Promise<{ id: string; status: string }> {
  return api.patch(`/projects/${projectId}/risks/${id}`, data)
}
