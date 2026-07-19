import { useEffect } from 'react'

export function useTitle(title: string) {
  useEffect(() => {
    const prev = document.title
    document.title = title ? `${title} — CyberMe OS` : 'CyberMe OS — 个人学习操作系统'
    return () => {
      document.title = prev
    }
  }, [title])
}
