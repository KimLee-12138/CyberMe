import { api } from './client'

export interface NoteSource {
  source_id: string
  rel: string
  doc_type: string
  source_pages: number[]
  section_id: string
  section_title: string
}

export interface NoteSummary {
  note_id: string
  topic_id: string
  course: string
  course_name: string
  title: string
  chapter: string
  aliases: string[]
  tags: string[]
  confidence: number
  verification: string
  unit_count: number
  key_points: number
  formulas: number
  conflicts: number
  source_count: number
  flags: string[]
  path: string
  summary: string
  snippet: string
}

export interface NoteDetail extends NoteSummary {
  body: string
  frontmatter: Record<string, unknown>
  sources: NoteSource[]
  topic: Record<string, any>
}

export interface NoteCourseFacet {
  course: string
  name: string
  count: number
}

export interface NoteFlagFacet {
  flag: string
  label: string
  count: number
}

export interface NoteListResponse {
  items: NoteSummary[]
  total: number
  offset: number
  limit: number
  stats: {
    all_notes: number
    filtered: number
    courses: number
    formula_missing: number
    conflicts: number
    no_definition: number
  }
  courses: NoteCourseFacet[]
  flags: NoteFlagFacet[]
}

export async function fetchNotes(params: {
  q?: string
  course?: string
  flag?: string
  limit?: number
  offset?: number
}): Promise<NoteListResponse> {
  return api.get('/notes', {
    params: {
      q: params.q || undefined,
      course: params.course || undefined,
      flag: params.flag || undefined,
      limit: String(params.limit ?? 500),
      offset: String(params.offset ?? 0),
    },
  })
}

export async function fetchNote(noteId: string): Promise<NoteDetail> {
  return api.get(`/notes/${encodeURIComponent(noteId)}`)
}
