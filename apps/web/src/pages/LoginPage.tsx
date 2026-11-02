import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowRight, Eye, EyeOff, ShieldCheck, Sparkles } from 'lucide-react'
import { useAuthStore } from '../stores/authStore'
import { useTitle } from '../lib/useTitle'

export default function LoginPage() {
  useTitle('登录')
  const navigate = useNavigate()
  const { login, verifyTotp } = useAuthStore()

  const [step, setStep] = useState<'credentials' | 'totp'>('credentials')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [totpCode, setTotpCode] = useState('')
  const [tempToken, setTempToken] = useState('')
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  const handleCredentials = async (event: React.FormEvent) => {
    event.preventDefault()
    setError('')
    setSubmitting(true)
    try {
      const result = await login(username, password)
      if (result.status === 'authenticated') navigate('/', { replace: true })
      else if (result.status === 'totp_required' && result.tempToken) {
        setTempToken(result.tempToken)
        setStep('totp')
      }
    } catch {
      setError('用户名或密码错误')
    } finally {
      setSubmitting(false)
    }
  }

  const handleTotp = async (event: React.FormEvent) => {
    event.preventDefault()
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
    <div className="relative flex min-h-dvh bg-[#f4f7fb]">
      {/* Brand panel */}
      <section className="relative hidden w-[46%] max-w-[720px] overflow-hidden bg-[#071a33] p-10 text-white lg:flex lg:flex-col xl:p-14">
        <div className="pointer-events-none absolute -right-32 -top-24 h-[420px] w-[420px] rounded-full bg-[#2563eb]/25 blur-3xl" />
        <div className="pointer-events-none absolute -bottom-44 -left-24 h-[420px] w-[420px] rounded-full bg-[#4f8bff]/15 blur-3xl" />
        <div className="pointer-events-none absolute inset-0 opacity-[0.04]" style={{ backgroundImage: 'linear-gradient(#fff 1px, transparent 1px), linear-gradient(90deg, #fff 1px, transparent 1px)', backgroundSize: '44px 44px' }} />

        <div className="relative flex items-center gap-3">
          <img src="/app-icon.png" alt="CyberMe" className="h-11 w-11 rounded-[14px] object-cover ring-1 ring-white/25" />
          <div>
            <p className="text-[17px] font-bold tracking-[-0.03em]">CyberMe</p>
            <p className="mt-0.5 text-[9px] font-semibold tracking-[0.22em] text-white/40">LEARNING OPERATING SYSTEM</p>
          </div>
        </div>

        <div className="relative my-auto max-w-md py-16">
          <p className="app-eyebrow !text-[#8bb3ff]">Private · Local-first</p>
          <h1 className="mt-5 text-[clamp(2.5rem,4.5vw,4.5rem)] font-[750] leading-[0.98] tracking-[-0.06em]">
            把学习，
            <br />
            变成一个<span className="text-[#6ea0ff]">系统</span>。
          </h1>
          <p className="mt-6 max-w-sm text-[14px] leading-7 text-white/50">
            课程、笔记、图谱、雨课堂与 AI 问答，聚合在你的个人知识空间里。
          </p>

          <div className="mt-10 grid max-w-sm grid-cols-2 gap-2.5">
            {[
              { icon: Sparkles, label: 'RAG 引用问答', sub: '433 notes' },
              { icon: ShieldCheck, label: '数据本地优先', sub: 'private by default' },
            ].map((item) => (
              <div key={item.label} className="rounded-2xl border border-white/10 bg-white/[0.05] p-3.5 backdrop-blur-sm">
                <item.icon size={16} className="text-[#8bb3ff]" />
                <p className="mt-3 text-[12px] font-semibold">{item.label}</p>
                <p className="mt-0.5 text-[10px] text-white/35">{item.sub}</p>
              </div>
            ))}
          </div>
        </div>

        <p className="relative text-[10px] tracking-[0.12em] text-white/25">CYBERME OS · PERSONAL KNOWLEDGE INFRASTRUCTURE</p>
      </section>

      {/* Form panel */}
      <section className="flex flex-1 items-center justify-center px-5 py-10 sm:px-8">
        <div className="w-full max-w-[400px]">
          <div className="mb-8 flex items-center gap-3 lg:hidden">
            <img src="/app-icon.png" alt="CyberMe" className="h-11 w-11 rounded-[14px] object-cover shadow-sm ring-1 ring-[#e3eaf3]" />
            <div>
              <p className="text-[17px] font-bold tracking-[-0.03em]">CyberMe</p>
              <p className="mt-0.5 text-[9px] font-semibold tracking-[0.18em] text-muted-foreground">LEARNING OS</p>
            </div>
          </div>

          <div className="app-card p-6 sm:p-8">
            {step === 'credentials' ? (
              <form onSubmit={handleCredentials} className="space-y-5">
                <div>
                  <p className="app-eyebrow">Welcome back</p>
                  <h2 className="mt-2 text-[26px] font-[750] tracking-[-0.045em]">登录你的空间</h2>
                  <p className="mt-2 text-[13px] leading-6 text-muted-foreground">输入账号密码，继续今天的学习。</p>
                </div>

                {error && (
                  <div role="alert" className="rounded-xl border border-[#fecaca] bg-[#fff5f5] px-3.5 py-2.5 text-[12px] font-medium text-[#b42318]">
                    {error}
                  </div>
                )}

                <label className="block">
                  <span className="mb-1.5 block text-[11px] font-semibold text-[#506785]">用户名</span>
                  <input
                    id="username"
                    type="text"
                    autoComplete="username"
                    required
                    value={username}
                    onChange={(event) => setUsername(event.target.value)}
                    placeholder="demo"
                    className="app-input"
                  />
                </label>

                <label className="block">
                  <span className="mb-1.5 block text-[11px] font-semibold text-[#506785]">密码</span>
                  <div className="relative">
                    <input
                      id="password"
                      type={showPassword ? 'text' : 'password'}
                      autoComplete="current-password"
                      required
                      value={password}
                      onChange={(event) => setPassword(event.target.value)}
                      placeholder="输入密码"
                      className="app-input pr-12"
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword((value) => !value)}
                      className="absolute right-1.5 top-1/2 flex h-9 w-9 -translate-y-1/2 items-center justify-center rounded-lg text-[#8a9bb0] hover:bg-[#f1f5f9] hover:text-foreground"
                      aria-label={showPassword ? '隐藏密码' : '显示密码'}
                    >
                      {showPassword ? <EyeOff size={17} /> : <Eye size={17} />}
                    </button>
                  </div>
                </label>

                <button
                  type="submit"
                  disabled={submitting || !username || !password}
                  className="app-button app-button-primary !min-h-11 w-full !rounded-xl"
                >
                  {submitting ? '验证中…' : '进入 CyberMe'}
                  {!submitting && <ArrowRight size={16} />}
                </button>

                <div className="flex items-center gap-2 rounded-xl bg-[#f8fafc] px-3 py-2.5 text-[10px] leading-4 text-muted-foreground">
                  <ShieldCheck size={13} className="shrink-0 text-emerald-600" />
                  私有部署 · 单用户 · 数据只在本机
                </div>
              </form>
            ) : (
              <form onSubmit={handleTotp} className="space-y-5">
                <div>
                  <p className="app-eyebrow">Two-factor</p>
                  <h2 className="mt-2 text-[26px] font-[750] tracking-[-0.045em]">两步验证</h2>
                  <p className="mt-2 text-[13px] leading-6 text-muted-foreground">输入认证应用中的 6 位验证码。</p>
                </div>

                {error && (
                  <div role="alert" className="rounded-xl border border-[#fecaca] bg-[#fff5f5] px-3.5 py-2.5 text-[12px] font-medium text-[#b42318]">
                    {error}
                  </div>
                )}

                <label className="block">
                  <span className="mb-1.5 block text-[11px] font-semibold text-[#506785]">验证码</span>
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
                    onChange={(event) => setTotpCode(event.target.value.replace(/\D/g, '').slice(0, 6))}
                    placeholder="000000"
                    className="app-input h-14 text-center text-2xl font-semibold tracking-[0.4em]"
                  />
                </label>

                <div className="flex gap-2">
                  <button type="button" onClick={handleBack} disabled={submitting} className="app-button app-button-secondary flex-1">
                    返回
                  </button>
                  <button type="submit" disabled={submitting || totpCode.length !== 6} className="app-button app-button-primary flex-1">
                    {submitting ? '验证中…' : '确认'}
                  </button>
                </div>
              </form>
            )}
          </div>

          <p className="mt-5 text-center text-[10px] tracking-[0.02em] text-muted-foreground">
            私有部署 · 单用户系统 · 所有数据由你掌控
          </p>
        </div>
      </section>
    </div>
  )
}
