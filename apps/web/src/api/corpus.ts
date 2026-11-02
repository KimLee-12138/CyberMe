import { api } from './client'

export type QualityStatus = 'official' | 'review' | 'candidate' | 'duplicate' | 'quarantine'

export interface FunnelStage {
  key: string
  label: string
  count: number
  note: string
  kind: 'files' | 'parts' | 'units' | 'topics' | string
}

export interface CorpusQuality {
  official: number
  review: number
  candidate: number
  duplicate: number
  quarantine: number
  indexable: number
  distill: number
  conflicts: number
  formula_missing_notes: number
  merge_duplicate: number
  merge_supplement: number
  merge_new: number
}

export interface CorpusIssuesCounts {
  quality_status: Record<QualityStatus, number>
  indexable: number
  distill: number
  quarantine: number
  duplicate_status: number
  candidate_status: number
  near_duplicate_pairs: number
  near_duplicate_duplicate: number
  near_duplicate_parallel: number
  near_duplicate_candidate: number
  conflicts: number
  conflict_notes: number
  formula_missing_notes: number
  review_sample: number
  writeback_total: number
}

export interface CorpusStats {
  version: string
  generated_at: string
  vault_unchanged: boolean
  funnel: FunnelStage[]
  raw: { pdf: number; md: number; pages: number; chars: number }
  included: { pdf: number; md: number; pages: number; chars: number }
  quality: CorpusQuality
  coverage: {
    files: number
    sections: number
    parts: number
    covered_files: number
    coverage: number
    gaps: number
  }
  issues: CorpusIssuesCounts
  resolution?: {
    enriched_notes: number
    source_supported_formulas: number
    quarantine_excluded: number
    near_duplicate_sources: number
    raw_source_chunks_indexed: number
    formula_missing_remaining: number
    conflicts_unresolved: number
  }
  exclusions: {
    total: number
    reasons: Array<{ reason: string; label: string; count: number }>
  }
  doc_types: Array<{ type: string; label: string; count: number }>
  writeback: {
    total: number
    create: number
    append_supplement: number
    skip_duplicate: number
    vault_modified: boolean
  }
  cost: Record<string, number>
  empty_courses: string[]
}

export interface CorpusCourse {
  course: string
  name: string
  included: number
  distill: number
  indexable: number
  sections: number
  parts: number
  units: number
  topics: number
  notes: number
  quality: Record<QualityStatus, number>
  formula_missing: number
  conflicts: number
  coverage: number
  raw_files: number
  raw_pages: number
  raw_chars: number
}

export interface CorpusCourses {
  courses: CorpusCourse[]
  total: number
  empty_courses: string[]
  totals: {
    included: number
    distill: number
    sections: number
    units: number
    topics: number
    formula_missing: number
    conflicts: number
  }
}

export interface CorpusConflict {
  course: string
  course_name: string
  topic_id: string
  title: string
  note_id: string
  note_path: string
  conflict: string
}

export interface CorpusQuarantine {
  source_id: string
  course: string
  course_name: string
  rel: string
  pages: number
  chars: number
  quality_score: number
  reasons: string
}

export interface CorpusFormulaMissing {
  note_id: string
  course: string
  course_name: string
  title: string
  path: string
  flags: string
  source_count: number
}

export interface CorpusNearDuplicate {
  relation: string
  course: string
  course_name: string
  source_a: string
  source_b: string
  rel_a: string
  rel_b: string
  jaccard: number
  hamming: number
}

export interface CorpusIssues {
  counts: CorpusIssuesCounts
  conflicts: CorpusConflict[]
  quarantine: CorpusQuarantine[]
  formula_missing: CorpusFormulaMissing[]
  near_duplicates: CorpusNearDuplicate[]
  writeback: {
    total: number
    create: number
    append_supplement: number
    skip_duplicate: number
    vault_modified: boolean
    sample: Array<{
      note_id: string
      course: string
      title: string
      source_note: string
      action: string
      target_path: string
      requires_approval: boolean
    }>
  }
}

export async function fetchCorpusStats(): Promise<CorpusStats> {
  return api.get('/corpus/stats')
}

export async function fetchCorpusCourses(): Promise<CorpusCourses> {
  return api.get('/corpus/courses')
}

export async function fetchCorpusIssues(): Promise<CorpusIssues> {
  return api.get('/corpus/issues')
}
