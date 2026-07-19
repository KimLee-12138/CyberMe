import { api } from './client'

// ── Types ─────────────────────────────────────────────

export interface TopAction {
  type: 'review' | 'debt' | 'orphan' | 'inference' | 'project_risk'
  title: string
  description: string
  priority: 'critical' | 'warning' | 'info'
  link?: string
}

export interface DueDocument {
  id: string
  title: string | null
  mastery: string
  importance: string
  course_code: string | null
}

export interface DueReviews {
  count: number
  documents: DueDocument[]
}

export interface DebtDocuments {
  count: number
  documents: Array<{
    id: string
    title: string | null
    importance: string | null
    mastery: string
  }>
}

export interface KnowledgeDebt {
  high_importance_low_mastery: DebtDocuments
  missing_verification: {
    count: number
    sample: Array<{ id: string; title: string | null }>
  }
  orphaned_nodes: { count: number }
  needs_review_total: number
}

export interface SystemHealth {
  document_count: number
  chunk_count: number
  course_count: number
  sync: {
    status: 'connected' | 'no_devices'
    last_seen: string | null
  }
  budget: {
    daily_cost_estimate: number
    monthly_cost_estimate: number
    monthly_budget_limit: number
    daily_tokens: number
    monthly_tokens: number
  }
  database: 'connected' | 'disconnected'
  redis: 'connected' | 'disconnected'
}

export interface DashboardData {
  top_actions: TopAction[]
  due_reviews: DueReviews
  knowledge_debt: KnowledgeDebt
  project_risks: {
    stub: boolean
    total_projects?: number
    total_hypotheses?: number
    total_open_risks?: number
    recent_projects?: { id: string; title: string; status: string; deadline: string | null }[]
    open_risks?: { id: string; description: string; impact: string; probability: number }[]
  }
  digital_twin: {
    ai_candidate_edges: number
    recent_audit_count: number
  }
  system_health: SystemHealth
  generated_at: string
}

// ── Review Types ──────────────────────────────────────

export interface ReviewCard {
  id: string
  card_type: 'recall' | 'concept' | 'problem' | 'application'
  front: string
  back: string
  state: 'new' | 'learning' | 'review' | 'relearning'
  due_at: string
  stability: number
  difficulty: number
  reps: number
  lapses: number
}

export interface DueReviewsResponse {
  cards: ReviewCard[]
  total_due: number
}

export interface GradeResponse extends ReviewCard {
  scheduled_interval: number
}

// ── API ────────────────────────────────────────────────

// Review stats
export interface ReviewStats {
  total_cards: number
  cards_due_today: number
  reviews_today: number
  total_reviews_30d: number
  avg_stability: number
  avg_difficulty: number
  retention_rate: number
  state_distribution: Record<string, number>
  rating_distribution_30d: Record<string, number>
}

export async function fetchReviewStats(): Promise<ReviewStats> {
  return api.get('/reviews/stats')
}

export async function fetchDashboard(): Promise<DashboardData> {
  return api.get('/learning/dashboard')
}

export async function fetchDueReviews(): Promise<DueReviewsResponse> {
  return api.get('/reviews/due')
}

export async function gradeCard(cardId: string, rating: number): Promise<GradeResponse> {
  return api.post(`/reviews/${cardId}/grade`, { rating })
}

// ── Tutor Types ────────────────────────────────────────

export type TutorMode = 'concept' | 'socratic' | 'closed_book' | 'step_by_step' | 'mock_exam' | 'mistake_retrain'

export interface SessionResponse {
  session_id: string
  mode: string
  content: string
  complete: boolean
  step?: number
  num_questions?: number
  correct_answer?: string
}

// ── Tutor API ───────────────────────────────────────────

export async function createSession(
  mode: TutorMode,
  topic: string,
  numQuestions?: number,
): Promise<SessionResponse> {
  return api.post('/learning/sessions', {
    mode,
    topic,
    num_questions: numQuestions || 3,
  })
}

export async function submitResponse(
  sessionId: string,
  answer: string,
): Promise<SessionResponse> {
  return api.post(`/learning/sessions/${sessionId}/responses`, { answer })
}

export async function completeSession(
  sessionId: string,
): Promise<{ session_id: string; mode: string; topic: string; rounds: number }> {
  return api.post(`/learning/sessions/${sessionId}/complete`)
}

// ── Writing Types ───────────────────────────────────────

export interface FactBinding {
  ref: string
  path: string
  verification: string
}

export interface WritingGenerateResponse {
  draft: string
  fact_bindings: FactBinding[]
  evidence_count: number
  model: string
}

export interface AuditParagraph {
  text: string
  type: 'direct_fact' | 'rewrite' | 'inference' | 'gap' | 'model_knowledge'
  note: string
}

export interface WritingAuditResponse {
  paragraphs: AuditParagraph[]
}

// ── Writing API ─────────────────────────────────────────

export async function generateWriting(
  topic: string,
  outputType: string = 'report',
  courseCode?: string,
): Promise<WritingGenerateResponse> {
  return api.post('/writing/generate', { topic, output_type: outputType, course_code: courseCode })
}

export async function auditWriting(text: string): Promise<WritingAuditResponse> {
  return api.post('/writing/audit', { text })
}

// ── Decision Types ──────────────────────────────────────

export interface DecisionAnalysis {
  role: string
  label: string
  icon: string
  content: string
}

export interface Decision {
  id: string
  topic: string
  context: string
  analyses: DecisionAnalysis[]
  created_at: string
}

// ── Decision API ────────────────────────────────────────

export async function createDecision(topic: string, context?: string): Promise<Decision> {
  return api.post('/decisions', { topic, context: context || '' })
}

export async function listDecisions(): Promise<{ decisions: Decision[] }> {
  return api.get('/decisions')
}

export async function getDecision(id: string): Promise<Decision> {
  return api.get(`/decisions/${id}`)
}

// ── Evaluation Types ────────────────────────────────────

export interface EvalCase {
  id: string
  question: string
  reference_answer: string
  scope_courses: string[]
  expected_document_ids: string[]
}

export interface EvalSuite {
  id: string
  name: string
  description: string
  cases: EvalCase[]
  case_count: number
  created_at: string
}

export interface EvalCaseResult {
  case_id: string
  question: string
  pass: boolean
  has_evidence?: boolean
  recall?: number
  citation_count?: number
  latency_ms?: number
  model?: string
  error?: string
}

export interface EvalRun {
  id: string
  suite_id: string
  suite_name: string
  total: number
  passed: number
  pass_rate: number
  avg_recall: number
  avg_latency_ms: number
  case_results: EvalCaseResult[]
  run_at: string
}

// ── Evaluation API ──────────────────────────────────────

export async function listSuites(): Promise<{ suites: EvalSuite[] }> {
  return api.get('/evaluations/suites')
}
export async function createSuite(data: { name: string; description?: string; cases: Array<{ question: string; reference_answer?: string; scope_courses?: string[]; expected_document_ids?: string[] }> }): Promise<EvalSuite> {
  return api.post('/evaluations/suites', data)
}
export async function deleteSuite(id: string): Promise<{ status: string }> {
  return api.delete(`/evaluations/suites/${id}`)
}
export async function runEvaluation(suiteId: string): Promise<EvalRun> {
  return api.post(`/evaluations/suites/${suiteId}/run`)
}
export async function listRuns(): Promise<{ runs: EvalRun[] }> {
  return api.get('/evaluations/runs')
}

// ── Writeback Types ─────────────────────────────────────

export interface DiffLine {
  type: 'changed' | 'added' | 'removed'
  line: number
  old?: string
  new?: string
}

export interface WritebackProposal {
  id: string
  document_id: string
  document_title: string | null
  document_path: string
  old_content: string
  new_content: string
  reason: string
  status: 'draft' | 'validating' | 'ready' | 'approved' | 'rejected' | 'applied'
  created_by: string
  created_at: string
  diff?: DiffLine[]
}

// ── Writeback API ───────────────────────────────────────

export async function listProposals(): Promise<{ proposals: WritebackProposal[] }> {
  return api.get('/writebacks')
}
export async function getProposal(id: string): Promise<WritebackProposal> {
  return api.get(`/writebacks/${id}`)
}
export async function createProposal(data: { document_id: string; new_content: string; reason?: string }): Promise<WritebackProposal> {
  return api.post('/writebacks', data)
}
export async function approveProposal(id: string): Promise<WritebackProposal> {
  return api.post(`/writebacks/${id}/approve`)
}
export async function rejectProposal(id: string): Promise<WritebackProposal> {
  return api.post(`/writebacks/${id}/reject`)
}
export async function applyProposal(id: string): Promise<WritebackProposal> {
  return api.post(`/writebacks/${id}/apply`)
}
export async function generateProposal(documentId: string, instruction: string): Promise<WritebackProposal> {
  return api.post('/writebacks/generate', { document_id: documentId, instruction })
}
