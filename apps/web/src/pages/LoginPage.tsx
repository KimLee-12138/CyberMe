import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'
import { useTitle } from '../lib/useTitle'

export default function LoginPage() {
  useTitle('登录')
  const navigate = useNavigate()
  const { login, verifyTotp } = useAuthStore()

  const [step, setStep] = useState<'credentials' | 'totp'>('credentials')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [totpCode, setTotpCode] = useState('')
  const [tempToken, setTempToken] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  const handleCredentials = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setSubmitting(true)

    try {
      const result = await login(username, password)
      if (result.status === 'authenticated') {
        navigate('/', { replace: true })
      } else if (result.status === 'totp_required' && result.tempToken) {
        setTempToken(result.tempToken)
        setStep('totp')
      }
    } catch {
      setError('用户名或密码错误')
    } finally {
      setSubmitting(false)
    }
  }

  const handleTotp = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setSubmitting(true)

    try {
      await verifyTotp(tempToken, totpCode)
      navigate('/', { replace: true })
    } catch {
      setError('验证码无效或已过期，请重新登录')
      setStep('credentials')
      setTotpCode('')
    } finally {
      setSubmitting(false)
    }
  }

  const handleBack = () => {
    setStep('credentials')
    setTotpCode('')
    setError('')
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-slate-50 to-blue-50 px-4">
      <div className="w-full max-w-md">
        {/* Logo / Brand */}
        <div className="mb-8 text-center">
          <span className="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-primary/10 text-3xl shadow-inner">
            🧠
          </span>
          <h1 className="mt-4 text-2xl font-bold tracking-tight text-foreground">
            CyberMe OS
          </h1>
          <p className="mt-1.5 text-sm text-muted-foreground">
            个人学习操作系统
          </p>
        </div>

        {/* Card */}
        <div className="rounded-2xl border border-border bg-white p-8 shadow-lg">
          {step === 'credentials' ? (
            <form onSubmit={handleCredentials} className="space-y-5">
              <div>
                <h2 className="text-lg font-semibold text-foreground">登录</h2>
                <p className="mt-1 text-sm text-muted-foreground">
                  输入账号密码进入你的知识空间
                </p>
              </div>

              {error && (
                <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
                  {error}
                </div>
              )}

              <div className="space-y-4">
                <div>
                  <label
                    htmlFor="username"
                    className="mb-1.5 block text-sm font-medium text-foreground"
                  >
                    用户名
                  </label>
                  <input
                    id="username"
                    type="text"
                    autoComplete="username"
                    required
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="请输入用户名"
                    className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 transition-colors"
                  />
                </div>

                <div>
                  <label
                    htmlFor="password"
                    className="mb-1.5 block text-sm font-medium text-foreground"
                  >
                    密码
                  </label>
                  <input
                    id="password"
                    type="password"
                    autoComplete="current-password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="请输入密码"
                    className="w-full rounded-lg border border-border bg-background px-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 transition-colors"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={submitting || !username || !password}
                className="w-full rounded-lg bg-primary py-2.5 text-sm font-semibold text-primary-foreground transition-all hover:bg-primary/90 active:scale-[0.98] disabled:cursor-not-allowed disabled:opacity-50"
              >
                {submitting ? '验证中...' : '登录'}
              </button>
            </form>
          ) : (
            <form onSubmit={handleTotp} className="space-y-5">
              <div>
                <h2 className="text-lg font-semibold text-foreground">
                  两步验证
                </h2>
                <p className="mt-1 text-sm text-muted-foreground">
                  请输入你的认证应用中的 6 位验证码
                </p>
              </div>

              {error && (
                <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
                  {error}
                </div>
              )}

              <div>
                <label
                  htmlFor="totp"
                  className="mb-1.5 block text-sm font-medium text-foreground"
                >
                  验证码
                </label>
                <input
                  id="totp"
                  type="text"
                  inputMode="numeric"
                  autoComplete="one-time-code"
                  required
                  maxLength={6}
                  minLength={6}
                  pattern="[0-9]{6}"
                  value={totpCode}
                  onChange={(e) => setTotpCode(e.target.value.replace(/\D/g, '').slice(0, 6))}
                  placeholder="000000"
                  className="w-full rounded-lg border border-border bg-background px-4 py-3 text-center text-2xl tracking-[0.3em] font-mono text-foreground placeholder:text-muted-foreground/40 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 transition-colors"
                />
              </div>

              <div className="flex gap-3">
                <button
                  type="button"
                  onClick={handleBack}
                  disabled={submitting}
                  className="rounded-lg border border-border bg-background px-4 py-2.5 text-sm font-medium text-foreground transition-colors hover:bg-secondary disabled:opacity-50"
                >
                  返回
                </button>
                <button
                  type="submit"
                  disabled={submitting || totpCode.length !== 6}
                  className="flex-1 rounded-lg bg-primary py-2.5 text-sm font-semibold text-primary-foreground transition-all hover:bg-primary/90 active:scale-[0.98] disabled:cursor-not-allowed disabled:opacity-50"
                >
                  {submitting ? '验证中...' : '确认'}
                </button>
              </div>
            </form>
          )}
        </div>

        <p className="mt-6 text-center text-xs text-muted-foreground">
          私有部署 · 单用户系统 · 所有数据由你掌控
        </p>
      </div>
    </div>
  )
}
