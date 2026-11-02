export type NavIcon =
  | 'house'
  | 'chat'
  | 'learn'
  | 'review'
  | 'courses'
  | 'notes'
  | 'graph'
  | 'yuketang'
  | 'quality'
  | 'projects'
  | 'write'
  | 'decisions'
  | 'self'
  | 'evaluations'
  | 'distill'
  | 'sync'
  | 'settings'

export interface NavItem {
  to: string
  label: string
  icon: NavIcon
}

export const NAV_GROUPS: { label: string; items: NavItem[] }[] = [
  {
    label: 'Overview',
    items: [
      { to: '/', label: '驾驶舱', icon: 'house' },
      { to: '/ask', label: '问答', icon: 'chat' },
      { to: '/notes', label: '笔记', icon: 'notes' },
      { to: '/graph', label: '图谱', icon: 'graph' },
      { to: '/yuketang', label: '雨课堂', icon: 'yuketang' },
    ],
  },
  {
    label: 'Study',
    items: [
      { to: '/courses', label: '课程', icon: 'courses' },
      { to: '/learn', label: '学习', icon: 'learn' },
      { to: '/review', label: '复习', icon: 'review' },
      { to: '/quality', label: '数据质量', icon: 'quality' },
    ],
  },
  {
    label: 'Workspace',
    items: [
      { to: '/projects', label: '项目', icon: 'projects' },
      { to: '/write', label: '写作', icon: 'write' },
      { to: '/decisions', label: '决策', icon: 'decisions' },
      { to: '/self', label: '个人模型', icon: 'self' },
      { to: '/evaluations', label: '评测', icon: 'evaluations' },
      { to: '/distill', label: 'AI 蒸馏', icon: 'distill' },
    ],
  },
  {
    label: 'System',
    items: [
      { to: '/sync', label: '同步', icon: 'sync' },
      { to: '/settings', label: '设置', icon: 'settings' },
    ],
  },
]

export const MOBILE_NAV_ITEMS: NavItem[] = [
  { to: '/', label: '驾驶舱', icon: 'house' },
  { to: '/ask', label: '问答', icon: 'chat' },
  { to: '/notes', label: '笔记', icon: 'notes' },
  { to: '/graph', label: '图谱', icon: 'graph' },
]
