import { useState, useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import Icon from '../ui/Icon'
import { searchDocuments, type SearchResult } from '../../api/knowledge'

export default function TopBar({ onMenuToggle }: { onMenuToggle: () => void }) {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<SearchResult['results']>([])
  const [showResults, setShowResults] = useState(false)
  const navigate = useNavigate()
  const inputRef = useRef<HTMLInputElement>(null)
  const debounceRef = useRef<ReturnType<typeof setTimeout>>()

  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current)
    if (query.trim().length < 2) {
      setResults([])
      setShowResults(false)
      return
    }
    debounceRef.current = setTimeout(async () => {
      try {
        const data = await searchDocuments(query.trim())
        setResults(data.results.slice(0, 8))
        setShowResults(true)
      } catch {
        setResults([])
      }
    }, 200)
    return () => { if (debounceRef.current) clearTimeout(debounceRef.current) }
  }, [query])

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    if (query.trim()) {
      setShowResults(false)
      navigate(`/ask?q=${encodeURIComponent(query.trim())}`)
    }
  }

  const goToDoc = (docId: string) => {
    setShowResults(false)
    setQuery('')
    navigate(`/knowledge/${docId}`)
  }

  return (
    <header className="flex h-14 items-center gap-4 border-b border-border bg-card px-6">
      <button onClick={onMenuToggle} className="rounded-lg p-1.5 text-muted-foreground hover:bg-muted hover:text-foreground transition-colors md:hidden">
        <Icon name="list" size={22} />
      </button>

      {/* Search with dropdown */}
      <form onSubmit={handleSearch} className="relative flex-1 max-w-md">
        <div className="relative">
          <Icon name="search" size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onFocus={() => { if (results.length > 0) setShowResults(true) }}
            onBlur={() => setTimeout(() => setShowResults(false), 200)}
            placeholder="搜索知识点、课程、笔记..."
            className="w-full rounded-lg border border-border bg-muted py-2 pl-10 pr-4 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20"
          />
        </div>

        {/* Search results dropdown */}
        {showResults && results.length > 0 && (
          <div className="absolute top-full mt-1 w-full rounded-xl border border-border bg-card shadow-lg z-50 max-h-80 overflow-y-auto">
            {results.map((r) => (
              <button
                key={r.id}
                type="button"
                onMouseDown={() => goToDoc(r.id)}
                className="flex w-full items-start gap-3 px-4 py-2.5 text-left hover:bg-muted/50 transition-colors border-b border-border/50 last:border-b-0"
              >
                <span className="shrink-0 mt-0.5 text-xs text-muted-foreground">
                  {r.course_code || '-'}
                </span>
                <div className="min-w-0 flex-1">
                  <p className="text-sm font-medium truncate">{r.title || r.relative_path.split('/').pop()}</p>
                  {r.snippet && (
                    <p className="text-xs text-muted-foreground line-clamp-1 mt-0.5">{r.snippet.slice(0, 80)}</p>
                  )}
                </div>
              </button>
            ))}
            <div className="px-4 py-2 border-t border-border bg-muted/30">
              <span className="text-xs text-muted-foreground">
                {results.length} 条结果 · 按 Enter 进入 AI 问答
              </span>
            </div>
          </div>
        )}
      </form>

      {/* Right side */}
      <div className="flex items-center gap-3">
        <button className="flex items-center gap-1.5 rounded-lg px-2 py-1 text-xs text-muted-foreground hover:bg-muted transition-colors" onClick={() => navigate('/sync')}>
          <span className="h-1.5 w-1.5 rounded-full bg-emerald-500" />
          <span className="hidden sm:inline">已同步</span>
        </button>
        <button onClick={() => navigate('/ask')} className="rounded-lg bg-primary px-4 py-1.5 text-xs font-medium text-primary-foreground hover:bg-primary/90 transition-all hover:shadow-sm">
          快速提问
        </button>
      </div>
    </header>
  )
}
