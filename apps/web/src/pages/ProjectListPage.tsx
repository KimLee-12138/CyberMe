import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { fetchProjects, createProject, deleteProject } from '../api/projects'
import { fetchRepos, importRepo, saveRepoNote, checkHealth } from '../api/github'
import type { GitHubRepo } from '../api/github'
import { useTitle } from '../lib/useTitle'
import { toast } from '../stores/toastStore'
import LoadingState from '../components/ui/LoadingState'
import ErrorState from '../components/ui/ErrorState'

const statusColors: Record<string, string> = {
  active: 'bg-emerald-100 text-emerald-700',
  completed: 'bg-blue-100 text-blue-700',
  archived: 'bg-gray-100 text-gray-500',
}

const LANG_COLORS: Record<string, string> = {
  TypeScript: 'bg-blue-100 text-blue-700',
  JavaScript: 'bg-yellow-100 text-yellow-700',
  Python: 'bg-green-100 text-green-700',
  Rust: 'bg-orange-100 text-orange-700',
  Go: 'bg-cyan-100 text-cyan-700',
  Java: 'bg-red-100 text-red-700',
}

export default function ProjectListPage() {
  useTitle('项目')
  const navigate = useNavigate()
  const qc = useQueryClient()
  const [showCreate, setShowCreate] = useState(false)
  const [title, setTitle] = useState('')
  const [goal, setGoal] = useState('')
  const [showGitHub, setShowGitHub] = useState(false)
  const [noteMap, setNoteMap] = useState<Record<string, string>>({})

  const { data, isLoading, error, refetch } = useQuery({ queryKey: ['projects'], queryFn: fetchProjects })

  const { data: ghHealth } = useQuery({
    queryKey: ['github-health'],
    queryFn: checkHealth,
    enabled: showGitHub,
  })

  const { data: ghData, isLoading: ghLoading } = useQuery({
    queryKey: ['github-repos'],
    queryFn: () => fetchRepos(),
    enabled: showGitHub && !!ghHealth?.configured,
  })

  const createMut = useMutation({
    mutationFn: () => createProject({ title, goal }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['projects'] }); setShowCreate(false); setTitle(''); setGoal(''); toast.success('项目创建成功') },
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => deleteProject(id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['projects'] }); toast.success('项目已删除') },
  })

  const importMut = useMutation({
    mutationFn: (repo: GitHubRepo) => importRepo(repo.full_name, noteMap[repo.full_name] || ''),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['projects'] }); toast.success('GitHub 项目已导入') },
  })

  const noteMut = useMutation({
    mutationFn: ({ fullName, note }: { fullName: string; note: string }) => saveRepoNote(fullName, note),
    onSuccess: () => toast.success('备注已保存'),
  })

  return (
    <div className="mx-auto max-w-4xl space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">项目</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {data?.projects.length || 0} 个项目
          </p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => setShowGitHub(!showGitHub)}
            className={`rounded-xl px-4 py-2 text-sm font-medium transition-colors ${
              showGitHub ? 'bg-secondary text-foreground' : 'border border-border text-muted-foreground hover:bg-secondary'
            }`}
          >
            GitHub
          </button>
          <button onClick={() => setShowCreate(true)} className="rounded-xl bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground hover:bg-primary/90">
            + 新建项目
          </button>
        </div>
      </div>

      {/* GitHub section */}
      {showGitHub && (
        <div className="rounded-2xl border border-border bg-card p-5 shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-sm font-semibold">
              GitHub 仓库
              {ghHealth?.user && (
                <span className="ml-2 font-normal text-muted-foreground">
                  ({ghHealth.user})
                </span>
              )}
            </h2>
            {ghHealth && !ghHealth.configured && (
              <p className="text-xs text-red-500">
                请在 .env 中配置 GITHUB_TOKEN
              </p>
            )}
            {ghHealth?.error && (
              <p className="text-xs text-red-500">{ghHealth.error}</p>
            )}
          </div>

          {ghLoading && <LoadingState lines={2} />}

          {ghData && (
            <div className="space-y-2 max-h-96 overflow-y-auto">
              {ghData.repos.map((repo) => (
                <div
                  key={repo.id}
                  className="flex items-start gap-3 rounded-xl border border-border p-4 hover:bg-muted/50 transition-colors"
                >
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      <a
                        href={repo.html_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-sm font-medium text-primary hover:underline truncate"
                      >
                        {repo.full_name}
                      </a>
                      {repo.language && (
                        <span className={`shrink-0 rounded px-1.5 py-0.5 text-[10px] font-medium ${LANG_COLORS[repo.language] || 'bg-gray-100 text-gray-600'}`}>
                          {repo.language}
                        </span>
                      )}
                      {repo.stargazers_count > 0 && (
                        <span className="shrink-0 text-[10px] text-muted-foreground">★ {repo.stargazers_count}</span>
                      )}
                    </div>
                    {repo.description && (
                      <p className="mt-1 text-xs text-muted-foreground line-clamp-2">{repo.description}</p>
                    )}
                    <input
                      value={noteMap[repo.full_name] ?? repo.note}
                      onChange={(e) => setNoteMap((m) => ({ ...m, [repo.full_name]: e.target.value }))}
                      placeholder="添加备注..."
                      className="mt-2 w-full rounded-lg border border-border bg-muted px-3 py-1.5 text-xs text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none"
                    />
                  </div>
                  <div className="flex shrink-0 flex-col gap-1">
                    <button
                      onClick={() => noteMut.mutate({ fullName: repo.full_name, note: noteMap[repo.full_name] ?? repo.note })}
                      className="rounded-lg bg-muted px-3 py-1 text-[11px] text-muted-foreground hover:bg-secondary hover:text-foreground transition-colors"
                    >
                      保存备注
                    </button>
                    <button
                      onClick={() => importMut.mutate(repo)}
                      className="rounded-lg bg-primary px-3 py-1 text-[11px] font-medium text-primary-foreground hover:bg-primary/90 transition-colors"
                    >
                      导入
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Create modal */}
      {showCreate && (
        <div className="rounded-2xl border border-primary/30 bg-primary/5 p-5 space-y-3">
          <input value={title} onChange={e => setTitle(e.target.value)} placeholder="项目名称" className="w-full rounded-xl border px-4 py-2 text-sm" onKeyDown={e => { if (e.key === 'Enter' && title.trim()) createMut.mutate() }} />
          <textarea value={goal} onChange={e => setGoal(e.target.value)} placeholder="目标（可选）" rows={2} className="w-full rounded-xl border px-4 py-2 text-sm" />
          <div className="flex gap-2">
            <button onClick={() => createMut.mutate()} disabled={!title.trim()} className="rounded-lg bg-primary px-4 py-1.5 text-sm text-primary-foreground disabled:opacity-40">创建</button>
            <button onClick={() => setShowCreate(false)} className="rounded-lg px-4 py-1.5 text-sm text-muted-foreground hover:bg-secondary">取消</button>
          </div>
        </div>
      )}

      {isLoading && <LoadingState />}
      {error && <ErrorState message="加载项目失败" onRetry={() => refetch()} />}

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {data?.projects.map(p => (
          <div key={p.id} className="group rounded-2xl border border-border bg-white p-5 shadow-sm hover:shadow-md transition-all cursor-pointer"
            onClick={() => navigate(`/projects/${p.id}`)}>
            <div className="flex items-start justify-between">
              <h3 className="text-sm font-semibold group-hover:text-primary transition-colors truncate">{p.title}</h3>
              <span className={`shrink-0 ml-2 rounded-full px-2 py-0.5 text-xs ${statusColors[p.status] || ''}`}>{p.status === 'active' ? '进行中' : p.status === 'completed' ? '已完成' : '已归档'}</span>
            </div>
            {p.goal && <p className="mt-2 text-xs text-muted-foreground line-clamp-2">{p.goal}</p>}
            <div className="mt-3 flex items-center justify-between text-xs text-muted-foreground">
              <span>{p.deadline || '无截止日'}</span>
              <button onClick={e => { e.stopPropagation(); if (confirm(`确定要删除项目「${p.title}」吗？此操作不可恢复。`)) deleteMut.mutate(p.id) }}
                className="text-red-400 hover:text-red-600 opacity-0 group-hover:opacity-100 transition-opacity">删除</button>
            </div>
          </div>
        ))}
      </div>

      {data && data.projects.length === 0 && !showGitHub && (
        <div className="rounded-2xl border bg-white py-12 text-center shadow-sm">
          <span className="text-3xl">📁</span>
          <p className="mt-3 text-sm text-muted-foreground">暂无项目，点击「新建项目」开始，或点击「GitHub」导入仓库</p>
        </div>
      )}
    </div>
  )
}
