import type { LucideIcon } from 'lucide-react'
import {
  Home,
  MessageCircle,
  BookOpen,
  BookOpenCheck,
  FlaskConical,
  RotateCcw,
  GraduationCap,
  Network,
  Rocket,
  PenLine,
  Scale,
  User,
  BarChart3,
  RefreshCw,
  Settings,
  List,
  Brain,
  X,
  Search,
  LogOut,
  CheckCircle2,
} from 'lucide-react'

const icons: Record<string, LucideIcon> = {
  house: Home,
  chat: MessageCircle,
  learn: BookOpen,
  review: RotateCcw,
  courses: GraduationCap,
  notes: BookOpen,
  yuketang: BookOpenCheck,
  graph: Network,
  projects: Rocket,
  write: PenLine,
  decisions: Scale,
  self: User,
  evaluations: BarChart3,
  distill: FlaskConical,
  sync: RefreshCw,
  settings: Settings,
  list: List,
  brain: Brain,
  x: X,
  search: Search,
  logout: LogOut,
  quality: CheckCircle2,
} as const

type IconName = keyof typeof icons

interface Props {
  name: IconName
  size?: number
  weight?: 'thin' | 'light' | 'regular' | 'bold' | 'fill' | 'duotone'
  className?: string
}

export default function Icon({ name, size = 20, className }: Props) {
  const Component = icons[name] || Search
  return <Component size={size} strokeWidth={1.8} className={className} />
}
