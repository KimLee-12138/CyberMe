import { api } from './client'

export interface CourseInfo {
  id: string
  code: string
  name: string
  knowledge_count: number
  extract_count: number
  last_indexed_at: string | null
}

export interface DocumentInfo {
  id: string
  title: string | null
  relative_path: string
  document_type: string | null
  status: string | null
  mastery: string | null
  importance: string | null
}

export interface CourseDetail {
  id: string
  code: string
  name: string
  knowledge_count: number
  documents: DocumentInfo[]
}

export interface DocumentDetail {
  id: string
  title: string | null
  relative_path: string
  document_type: string | null
  course_code: string | null
  status: string | null
  mastery: string | null
  importance: string | null
  needs_review: boolean
  frontmatter: Record<string, string | number | null>
  markdown_body: string | null
  content_hash: string
  indexed_at: string | null
  edges: Array<{
    edge_type: string
    origin: string
    target_label: string
    target_node_id: string
  }>
}

export interface SearchResult {
  query: string
  results: Array<{
    id: string
    title: string | null
    relative_path: string
    document_type: string | null
    course_code: string | null
    snippet: string
  }>
  total: number
}

export interface GraphData {
  nodes: Array<{
    id: string
    node_type: string
    label: string
    document_id: string | null
    properties: Record<string, string | number | null>
  }>
  edges: Array<{
    id: string
    source: string
    target: string
    edge_type: string
    origin: string
    confidence: number | null
  }>
}

export async function fetchCourses(): Promise<{ courses: CourseInfo[] }> {
  return api.get('/courses')
}

export async function fetchCourse(courseId: string): Promise<CourseDetail> {
  return api.get(`/courses/${courseId}`)
}

export async function fetchDocument(documentId: string): Promise<DocumentDetail> {
  return api.get(`/documents/${documentId}`)
}

export async function searchDocuments(
  q: string,
  courseCode?: string,
  docType?: string,
): Promise<SearchResult> {
  return api.get('/search', {
    params: { q, course_code: courseCode, document_type: docType },
  })
}

export async function fetchGraph(
  nodeType?: string,
  courseCode?: string,
): Promise<GraphData> {
  return api.get('/graph', {
    params: { node_type: nodeType, course_code: courseCode, limit: '500' },
  })
}

// ── New types ─────────────────────────────────────────

export interface VersionInfo {
  id: string
  content_hash: string
  created_at: string | null
  source_device_id: string | null
}

export interface WikiLinkResult {
  document_id: string
  title: string | null
  path: string
}

export interface OrphanNode {
  id: string
  node_type: string
  label: string
}

export interface NeighborhoodData {
  center: { id: string; node_type: string; label: string }
  nodes: Array<{ id: string; node_type: string; label: string }>
  edges: Array<{
    id: string
    source: string
    target: string
    edge_type: string
    origin: string
  }>
}

// ── New API functions ──────────────────────────────────

export async function updateDocument(
  documentId: string,
  data: { status?: string; mastery?: string; importance?: string },
): Promise<{ id: string; status: string | null; mastery: string | null; importance: string | null }> {
  return api.patch(`/documents/${documentId}`, data)
}

export async function fetchVersions(documentId: string): Promise<{ versions: VersionInfo[] }> {
  return api.get(`/documents/${documentId}/versions`)
}

export async function resolveWikiLink(wikilink: string): Promise<WikiLinkResult> {
  return api.post('/documents/resolve-wikilink', { wikilink })
}

export async function fetchOrphans(): Promise<{ orphans: OrphanNode[]; total: number }> {
  return api.get('/graph/orphans')
}

export async function fetchNeighborhood(
  nodeId: string,
  depth: number = 1,
): Promise<NeighborhoodData> {
  return api.get(`/graph/neighborhood/${nodeId}`, { params: { depth: String(depth) } })
}
