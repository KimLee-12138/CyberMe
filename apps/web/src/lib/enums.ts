/** 枚举值到中文的映射表，所有页面统一使用。 */

export const MASTERY = {
  unknown: '未标记',
  learning: '学习中',
  reviewing: '复习中',
  mastered: '已掌握',
} as const
export type MasteryKey = keyof typeof MASTERY
export const masteryLabel = (k: string) => MASTERY[k as MasteryKey] || k

export const IMPORTANCE = {
  low: '低',
  medium: '中',
  high: '高',
  critical: '紧急',
} as const
export type ImportanceKey = keyof typeof IMPORTANCE
export const importanceLabel = (k: string) => IMPORTANCE[k as ImportanceKey] || k

export const DOC_STATUS = {
  extracted: '已提取',
  cleaned: '已清洗',
  active: '活跃',
  resolved: '已解决',
  archived: '已归档',
} as const
export type DocStatusKey = keyof typeof DOC_STATUS
export const docStatusLabel = (k: string) => DOC_STATUS[k as DocStatusKey] || k

export const DOC_TYPE = {
  concept: '概念',
  extract: '摘录',
  formula: '公式',
  procedure: '流程',
  reflection: '反思',
} as const
export type DocTypeKey = keyof typeof DOC_TYPE
export const docTypeLabel = (k: string) => DOC_TYPE[k as DocTypeKey] || k

export const PLATFORM = {
  windows: 'Windows',
  macos: 'macOS',
  linux: 'Linux',
  android: 'Android',
  ios: 'iOS',
} as const
export type PlatformKey = keyof typeof PLATFORM
export const platformLabel = (k: string) => PLATFORM[k as PlatformKey] || k

export const REVIEW_RATING = {
  Again: '重来',
  Hard: '困难',
  Good: '良好',
  Easy: '简单',
} as const
export type ReviewRatingKey = keyof typeof REVIEW_RATING
export const reviewRatingLabel = (k: string) => REVIEW_RATING[k as ReviewRatingKey] || k

export const PROJECT_STATUS = {
  active: '进行中',
  completed: '已完成',
  archived: '已归档',
} as const
export type ProjectStatusKey = keyof typeof PROJECT_STATUS
export const projectStatusLabel = (k: string) => PROJECT_STATUS[k as ProjectStatusKey] || k

export const IMPACT = {
  low: '低',
  medium: '中',
  high: '高',
  critical: '紧急',
} as const
export type ImpactKey = keyof typeof IMPACT
export const impactLabel = (k: string) => IMPACT[k as ImpactKey] || k
