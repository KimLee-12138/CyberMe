import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'
import { listDevices, revokeDevice } from '../api/devices'
import { platformLabel } from '../lib/enums'
import { useTitle } from '../lib/useTitle'
import { fetchDashboard } from '../api/learning'
import { useQuery } from '@tanstack/react-query'

interface Device {
  id: string
  name: string
  platform: string
  last_seen_at: string | null
}

export default function SettingsPage() {
  useTitle('设置')
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()
  const [devices, setDevices] = useState<Device[]>([])
  const [loading, setLoading] = useState(true)
  const [revoking, setRevoking] = useState<string | null>(null)

  const { data: health } = useQuery({
    queryKey: ['dashboard'],
    queryFn: fetchDashboard,
    staleTime: 60_000,
  })

  const loadDevices = async () => {
    try {
      const result = await listDevices()
      setDevices(result.devices)
    } catch {
      // Ignore
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadDevices()
  }, [])

  const handleRevoke = async (deviceId: string, deviceName: string) => {
    if (!confirm(`确认撤销设备 "${deviceName}" 的访问权限？该设备将无法再同步数据。`)) {
      return
    }
    setRevoking(deviceId)
    try {
      await revokeDevice(deviceId)
      setDevices((prev) => prev.filter((d) => d.id !== deviceId))
    } catch {
      alert('撤销失败，请重试')
    } finally {
      setRevoking(null)
    }
  }

  const handleLogout = async () => {
    await logout()
    navigate('/login', { replace: true })
  }

  return (
    <div className="mx-auto max-w-2xl space-y-8">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">设置</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          管理账号、设备和系统配置
        </p>
      </div>

      {/* Account */}
      <div className="rounded-2xl border border-border bg-white shadow-sm">
        <div className="border-b border-border px-6 py-4">
          <h2 className="text-sm font-semibold text-foreground">账号信息</h2>
        </div>
        <div className="px-6 py-4 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">用户名</span>
            <span className="text-sm font-medium text-foreground">
              {user?.username}
            </span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">密码</span>
            <span className="text-sm text-muted-foreground">••••••••</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">两步验证</span>
            <span className="inline-flex items-center gap-1.5 rounded-full bg-secondary px-2.5 py-0.5 text-xs font-medium text-muted-foreground">
              未启用
            </span>
          </div>
        </div>
      </div>

      {/* Devices */}
      <div className="rounded-2xl border border-border bg-white shadow-sm">
        <div className="flex items-center justify-between border-b border-border px-6 py-4">
          <h2 className="text-sm font-semibold text-foreground">已配对设备</h2>
          <button
            onClick={() => navigate('/pair')}
            className="rounded-lg bg-primary px-3 py-1.5 text-xs font-medium text-primary-foreground transition-colors hover:bg-primary/90"
          >
            配对新设备
          </button>
        </div>
        <div className="px-6 py-4">
          {loading ? (
            <p className="text-sm text-muted-foreground">加载中...</p>
          ) : devices.length === 0 ? (
            <div className="py-6 text-center">
              <span className="text-2xl">📱</span>
              <p className="mt-2 text-sm text-muted-foreground">
                暂无已配对设备
              </p>
              <p className="mt-1 text-xs text-muted-foreground">
                点击"配对新设备"将本地同步代理连接到云端
              </p>
            </div>
          ) : (
            <div className="space-y-3">
              {devices.map((device) => (
                <div
                  key={device.id}
                  className="flex items-center justify-between rounded-lg border border-border bg-background px-4 py-3"
                >
                  <div className="flex items-center gap-3">
                    <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-secondary text-sm">
                      {device.platform === 'windows'
                        ? '🖥️'
                        : device.platform === 'macos'
                          ? '💻'
                          : '🐧'}
                    </span>
                    <div>
                      <p className="text-sm font-medium text-foreground">
                        {device.name}
                      </p>
                      <p className="text-xs text-muted-foreground">
                        {platformLabel(device.platform)}
                        {device.last_seen_at &&
                          ` · 最后在线: ${new Date(device.last_seen_at).toLocaleString('zh-CN')}`}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => handleRevoke(device.id, device.name)}
                    disabled={revoking === device.id}
                    className="rounded-md px-3 py-1.5 text-xs font-medium text-red-600 transition-colors hover:bg-red-50 disabled:opacity-50"
                  >
                    {revoking === device.id ? '撤销中...' : '撤销'}
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* System Health */}
      <div className="rounded-2xl border border-border bg-white shadow-sm">
        <div className="border-b border-border px-6 py-4">
          <h2 className="text-sm font-semibold text-foreground">系统状态</h2>
        </div>
        <div className="px-6 py-4 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">数据库</span>
            <span className={`inline-flex items-center gap-1.5 text-xs ${health ? 'text-emerald-600' : 'text-muted-foreground'}`}>
              <span className={`h-1.5 w-1.5 rounded-full ${health ? 'bg-emerald-500' : 'bg-gray-300'}`} />
              {health ? '正常' : '加载中...'}
            </span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">节点数</span>
            <span className="text-xs text-muted-foreground">
              {health?.system_health?.knowledge_graph?.nodes?.toLocaleString() ?? '-'}
            </span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">月预算</span>
            <span className="text-xs text-muted-foreground">
              {health?.system_health?.budget ? `$${health.system_health.budget.monthly_cost_estimate?.toFixed(2)} / $${health.system_health.budget.budget_limit?.toFixed(0)}` : '-'}
            </span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-sm text-muted-foreground">同步设备</span>
            <span className="text-xs text-muted-foreground">
              {devices.length > 0 ? `${devices.length} 台设备` : '暂无设备连接'}
            </span>
          </div>
        </div>
      </div>

      {/* Logout */}
      <div className="rounded-2xl border border-border bg-white shadow-sm">
        <div className="px-6 py-4">
          <button
            onClick={handleLogout}
            className="w-full rounded-lg border border-red-200 px-4 py-2.5 text-sm font-medium text-red-600 transition-colors hover:bg-red-50"
          >
            退出登录
          </button>
        </div>
      </div>
    </div>
  )
}
