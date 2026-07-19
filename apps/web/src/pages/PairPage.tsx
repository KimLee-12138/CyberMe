import { useState, useEffect } from 'react'
import { createPairingCode } from '../api/devices'

export default function PairPage() {
  const [code, setCode] = useState<string | null>(null)
  const [expiresIn, setExpiresIn] = useState(0)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const generate = async () => {
    setLoading(true)
    setError('')
    try {
      const result = await createPairingCode()
      setCode(result.pairing_code)
      setExpiresIn(result.expires_in)
    } catch {
      setError('生成配对码失败，请检查网络连接')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    if (expiresIn <= 0) return
    const timer = setInterval(() => {
      setExpiresIn((prev) => {
        if (prev <= 1) {
          setCode(null)
          return 0
        }
        return prev - 1
      })
    }, 1000)
    return () => clearInterval(timer)
  }, [expiresIn])

  const minutes = Math.floor(expiresIn / 60)
  const seconds = expiresIn % 60

  return (
    <div className="mx-auto max-w-lg space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">设备配对</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          生成一次性配对码，在本地同步代理中输入即可连接
        </p>
      </div>

      <div className="rounded-2xl border border-border bg-white p-8 shadow-sm">
        {!code ? (
          <div className="text-center space-y-5">
            <span className="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-primary/10 text-2xl">
              🔗
            </span>
            <p className="text-sm text-muted-foreground">
              点击下方按钮生成 6 位配对码，有效期为 10 分钟
            </p>
            <button
              onClick={generate}
              disabled={loading}
              className="rounded-lg bg-primary px-6 py-2.5 text-sm font-semibold text-primary-foreground transition-all hover:bg-primary/90 active:scale-[0.98] disabled:opacity-50"
            >
              {loading ? '生成中...' : '生成配对码'}
            </button>
            {error && (
              <p className="text-sm text-red-600">{error}</p>
            )}
          </div>
        ) : (
          <div className="text-center space-y-5">
            <span className="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-emerald-50 text-2xl">
              ✅
            </span>
            <div>
              <p className="text-sm text-muted-foreground">配对码</p>
              <p className="mt-2 text-5xl font-mono font-bold tracking-[0.15em] text-foreground">
                {code}
              </p>
            </div>
            <div className="inline-flex items-center gap-2 rounded-full bg-secondary px-4 py-1.5 text-xs font-medium text-muted-foreground">
              <span className="h-1.5 w-1.5 rounded-full animate-pulse bg-amber-500" />
              {minutes > 0
                ? `${minutes} 分 ${seconds} 秒后过期`
                : `${seconds} 秒后过期`}
            </div>
            <p className="text-xs text-muted-foreground">
              在本地终端运行{' '}
              <code className="rounded bg-secondary px-1.5 py-0.5 text-xs font-mono">
                cyberme-sync pair
              </code>{' '}
              并输入此配对码
            </p>
          </div>
        )}
      </div>

      <div className="rounded-xl border border-border bg-secondary/50 px-5 py-4">
        <h3 className="text-sm font-semibold text-foreground">使用说明</h3>
        <ol className="mt-2 list-inside list-decimal space-y-1 text-xs text-muted-foreground">
          <li>确保本地同步代理已安装</li>
          <li>在此页面生成配对码</li>
          <li>在终端运行 <code className="rounded bg-muted px-1 py-0.5 font-mono">cyberme-sync pair</code></li>
          <li>输入 6 位配对码完成配对</li>
          <li>配对后设备将自动开始同步 Obsidian Vault</li>
        </ol>
      </div>
    </div>
  )
}
