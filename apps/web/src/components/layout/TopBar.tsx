import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowUpRight, Search, X } from 'lucide-react'
import Icon from '../ui/Icon'
import { fetchNotes, type NoteSummary } from '../../api/notes'

export default function TopBar({ onMenuToggle }: { onMenuToggle: () => void }) {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<NoteSummary[]>([])
  const [showResults, setShowResults] = useState(false)
  const [mobileSearchOpen, setMobileSearchOpen] = useState(false)
  const navigate = useNavigate()
  const inputRef = useRef<HTMLInputElement>(null)
  const mobileInputRef = useRef<HTMLInputElement>(null)
  const debounceRef = useRef<ReturnType<typeof setTimeout> | undefined>(undefined)

  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current)
    if (query.trim().length < 2) {
      setResults([])
      setShowResults(false)
      return
    }
    debounceRef.current = setTimeout(async () => {
      try {
        const data = await fetchNotes({ q: query.trim(), limit: 8 })
        setResults(data.items)
        setShowResults(true)
      } catch {
        setResults([])
      }
    }, 220)
    return () => {
      if (debounceRef.current) clearTimeout(debounceRef.current)
    }
  }, [query])

  useEffect(() => {
    if (mobileSearchOpen) {
      window.setTimeout(() => mobileInputRef.current?.focus(), 60)
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
    return () => {
      document.body.style.overflow = ''
    }
  }, [mobileSearchOpen])

  const handleSearch = (event?: { preventDefault?: () => void }) => {
    event?.preventDefault?.()
    if (!query.trim()) return
    setShowResults(false)
    setMobileSearchOpen(false)
    navigate(`/ask?q=${encodeURIComponent(query.trim())}`)
  }

  const goToNote = (noteId: string) => {
    setShowResults(false)
    setQuery('')
    setMobileSearchOpen(false)
    navigate(`/notes?note=${encodeURIComponent(noteId)}`)
  }

  const searchBox = (
    <form onSubmit={handleSearch} className="relative w-full">
      <div className="relative">
        <Search size={16} className="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[#7b8da5]" />
        <input
          ref={inputRef}
          type="text"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          onFocus={() => {
            if (results.length > 0) setShowResults(true)
          }}
          placeholder="搜索知识点、课程、笔记…"
          className="h-10 w-full rounded-xl border border-[#e3eaf3] bg-white/75 pl-10 pr-16 text-[13px] text-foreground outline-none transition-all placeholder:text-[#94a3b8] focus:border-[#8bb3ff] focus:bg-white focus:ring-4 focus:ring-[#2563eb]/8"
        />
        <span className="pointer-events-none absolute right-3 top-1/2 hidden -translate-y-1/2 items-center gap-1 rounded-md border border-[#e3eaf3] bg-[#f8fafc] px-1.5 py-0.5 text-[9px] font-semibold text-[#94a3b8] lg:flex">
          ENTER
        </span>
      </div>

      {showResults && results.length > 0 && (
        <div className="app-pop-in absolute left-0 right-0 top-[calc(100%+8px)] z-[90] max-h-80 overflow-y-auto rounded-2xl border border-[#e3eaf3] bg-white p-1.5 shadow-[0_24px_60px_-24px_rgba(15,31,58,0.45)]">
          {results.map((result) => (
            <button
              key={result.note_id}
              type="button"
              onMouseDown={() => goToNote(result.note_id)}
              className="flex w-full items-start gap-3 rounded-xl px-3 py-2.5 text-left transition-colors hover:bg-[#f5f8ff]"
            >
              <span className="mt-1 flex h-5 shrink-0 items-center rounded-md bg-[#eef4ff] px-1.5 text-[9px] font-semibold text-[#2563eb]">
                {result.course_name || 'NOTE'}
              </span>
              <div className="min-w-0 flex-1">
                <p className="truncate text-[13px] font-semibold text-foreground">{result.title}</p>
                {result.snippet && (
                  <p className="mt-0.5 line-clamp-1 text-[11px] text-muted-foreground">{result.snippet.slice(0, 80)}</p>
                )}
              </div>
              <ArrowUpRight size={14} className="mt-1 shrink-0 text-[#b3c1d4]" />
            </button>
          ))}
          <div className="flex items-center justify-between px-3 py-2 text-[10px] text-muted-foreground">
            <span>{results.length} 条结果</span>
            <span>Enter 进入 AI 问答</span>
          </div>
        </div>
      )}
    </form>
  )

  return (
    <>
      <header className="sticky top-0 z-40 flex h-16 shrink-0 items-center gap-3 border-b border-[#e8edf5]/80 bg-[#f4f7fb]/80 px-4 backdrop-blur-xl md:px-7">
        <button
          onClick={onMenuToggle}
          className="flex h-10 w-10 items-center justify-center rounded-xl text-muted-foreground transition-colors hover:bg-[#eef4ff] hover:text-foreground md:hidden"
          aria-label="打开菜单"
        >
          <Icon name="list" size={21} />
        </button>

        <button onClick={() => navigate('/')} className="flex items-center gap-2 md:hidden" aria-label="回到驾驶舱">
          <img src="/app-icon.png" alt="" className="h-8 w-8 rounded-[10px] object-cover ring-1 ring-[#e3eaf3]" />
          <span className="text-[14px] font-bold tracking-[-0.03em]">CyberMe</span>
        </button>

        <div className="hidden w-full max-w-[520px] md:block">{searchBox}</div>
        <div className="flex-1 md:hidden" />

        <div className="flex items-center gap-2">
          <button
            onClick={() => setMobileSearchOpen(true)}
            className="flex h-10 w-10 items-center justify-center rounded-xl text-muted-foreground transition-colors hover:bg-[#eef4ff] hover:text-foreground md:hidden"
            aria-label="搜索"
          >
            <Search size={19} />
          </button>

          <button
            onClick={() => navigate('/sync')}
            className="hidden items-center gap-1.5 rounded-full border border-[#e3eaf3] bg-white/70 px-2.5 py-1 text-[10px] font-medium text-[#64748b] transition-colors hover:bg-white sm:flex"
          >
            <span className="h-1.5 w-1.5 rounded-full bg-emerald-500 shadow-[0_0_0_3px_rgba(16,185,129,0.12)]" />
            已同步
          </button>

          <button
            onClick={() => navigate('/ask')}
            className="app-button app-button-accent !min-h-9 !rounded-full !px-3.5 !text-[11px]"
          >
            <span className="hidden sm:inline">快速提问</span>
            <span className="sm:hidden">提问</span>
            <ArrowUpRight size={14} />
          </button>
        </div>
      </header>

      {mobileSearchOpen && (
        <div className="fixed inset-0 z-[100] bg-[#071a33]/35 p-3 backdrop-blur-sm md:hidden" onClick={() => setMobileSearchOpen(false)}>
          <div
            className="app-pop-in mx-auto mt-3 w-full max-w-lg rounded-2xl border border-[#e3eaf3] bg-white p-3 shadow-2xl"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="mb-2 flex items-center justify-between px-1">
              <p className="text-xs font-semibold text-foreground">全局搜索</p>
              <button onClick={() => setMobileSearchOpen(false)} className="rounded-lg p-1 text-muted-foreground hover:bg-muted" aria-label="关闭搜索">
                <X size={18} />
              </button>
            </div>
            <input
              ref={mobileInputRef}
              type="text"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === 'Enter') {
                  event.preventDefault()
                  handleSearch(event)
                }
              }}
              placeholder="搜索知识点、课程、笔记…"
              className="app-input h-12 text-[15px]"
            />
            <div className="mt-2 max-h-[50vh] overflow-y-auto">
              {results.map((result) => (
                <button
                  key={result.note_id}
                  onClick={() => goToNote(result.note_id)}
                  className="flex w-full items-start gap-3 rounded-xl px-3 py-3 text-left transition-colors hover:bg-[#f5f8ff]"
                >
                  <span className="mt-1 rounded-md bg-[#eef4ff] px-1.5 py-0.5 text-[9px] font-semibold text-[#2563eb]">
                    {result.course_name || 'NOTE'}
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="block truncate text-sm font-semibold">{result.title}</span>
                    {result.snippet && <span className="mt-0.5 line-clamp-1 block text-[11px] text-muted-foreground">{result.snippet}</span>}
                  </span>
                </button>
              ))}
              {query.trim().length >= 2 && results.length === 0 && (
                <p className="px-3 py-6 text-center text-sm text-muted-foreground">没有找到匹配笔记</p>
              )}
            </div>
            <button onClick={handleSearch} className="app-button app-button-primary mt-2 w-full">
              进入 AI 问答
            </button>
          </div>
        </div>
      )}
    </>
  )
}
