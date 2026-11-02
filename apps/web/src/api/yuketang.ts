import { api, download } from './client'

export interface YktStatus {
  configured: boolean
  region: string
  region_name: string
  account: { name: string; school: string; user_id: string } | null
  last_sync: string | null
  last_error: string | null
  refreshing: boolean
  syncing?: boolean
}

export interface YktActivity {
  id: string
  type: number
  type_name: string
  title: string
  courseware_id: string
  create_time: number
  deadline: number
  status: number
  unfinished: number
  progress: number
  score: number | null
  finished: boolean
  expired?: boolean
  pending?: boolean
}

export interface YktDeadline {
  name: string
  leaf_id: string
  leaf_type: number
  status: string
  deadline: number
  score?: number
  total_score?: number
}

export interface YktCourse {
  classroom_id: string
  course_id: string
  name: string
  class_name: string
  teacher: string
  term: number
  activities: YktActivity[]
  assignments: YktActivity[]
  lessons: YktActivity[]
  announcements: YktActivity[]
  pending_count: number
  deadlines: YktDeadline[]
  activity_error?: string
}

export interface YktAssignment extends YktActivity {
  course_name: string
  classroom_id: string
}

export interface YktOverview {
  configured: boolean
  region: string
  region_name: string
  account: { name: string; school: string; user_id: string } | null
  last_sync: string | null
  last_error: string | null
  syncing?: boolean
  courses: YktCourse[]
  assignments: YktAssignment[]
  error?: string
}

export interface YktSlide {
  index: number
  image: string
}

export interface YktPresentation {
  id: string
  title: string
  cover: string
  slides_count: number
  slides: YktSlide[]
}

export interface YktCourseware {
  lesson_id: string
  title: string
  course_name: string
  teacher: string
  presentations: YktPresentation[]
  fetched_at: string
}

export const getYuketangStatus = () =>
  api.get<YktStatus>('/integrations/yuketang/status')

export const getYuketangOverview = (force = false) =>
  api.get<YktOverview>(`/integrations/yuketang/overview?force=${force}`)

export const saveYuketangSession = (sessionid: string) =>
  api.post<{ ok: boolean; account: YktStatus['account']; overview: YktOverview }>(
    '/integrations/yuketang/session',
    { sessionid },
  )

export const clearYuketangSession = () =>
  api.delete<{ ok: boolean }>('/integrations/yuketang/session')

export const syncYuketang = () =>
  api.post<YktOverview>('/integrations/yuketang/sync')

export const getYuketangCourseware = (lessonId: string, force = false) =>
  api.get<YktCourseware>(
    `/integrations/yuketang/courseware/${encodeURIComponent(lessonId)}?force=${force}`,
  )

export async function downloadYuketangCoursewarePdf(lessonId: string, title: string) {
  const safe = (title || 'courseware').replace(/[\\/:*?"<>|]+/g, '_').slice(0, 80)
  await download(
    `/integrations/yuketang/courseware/${encodeURIComponent(lessonId)}/pdf`,
    `${safe}.pdf`,
  )
}
