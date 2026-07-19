import { api } from './client'

export interface GitHubRepo {
  id: number
  full_name: string
  name: string
  description: string | null
  html_url: string
  language: string | null
  stargazers_count: number
  updated_at: string | null
  topics: string[]
  note: string
}

export interface GitHubHealth {
  configured: boolean
  message?: string
  user?: string
  avatar?: string
  error?: string
}

export async function fetchRepos(page = 1): Promise<{ repos: GitHubRepo[] }> {
  return api.get('/github/repos', { params: { page, per_page: 50 } })
}

export async function saveRepoNote(repoFullName: string, note: string): Promise<{ status: string }> {
  return api.post('/github/notes', { repo_full_name: repoFullName, note })
}

export async function importRepo(repoFullName: string, note?: string): Promise<{ id: string; title: string }> {
  return api.post('/github/import', { repo_full_name: repoFullName, note: note || '' })
}

export async function checkHealth(): Promise<GitHubHealth> {
  return api.get('/github/health')
}
