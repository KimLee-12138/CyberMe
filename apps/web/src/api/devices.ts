import { api } from './client'

interface DeviceInfo {
  id: string
  name: string
  platform: string
  last_seen_at: string | null
}

export async function listDevices(): Promise<{ devices: DeviceInfo[] }> {
  return api.get('/devices')
}

export async function createPairingCode(): Promise<{
  pairing_code: string
  expires_in: number
}> {
  return api.post('/devices/pairing-codes')
}

export async function revokeDevice(deviceId: string): Promise<void> {
  return api.delete(`/devices/${deviceId}`)
}
