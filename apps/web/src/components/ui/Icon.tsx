import {
  House,
  ChatCircleText,
  BookOpenText,
  ArrowsCounterClockwise,
  GraduationCap,
  Graph,
  RocketLaunch,
  PenNib,
  Scales,
  User,
  ChartBar,
  ArrowsClockwise,
  Gear,
  List,
  Brain,
  X,
  MagnifyingGlass,
  SignOut,
} from '@phosphor-icons/react'

const icons = {
  house: House,
  chat: ChatCircleText,
  learn: BookOpenText,
  review: ArrowsCounterClockwise,
  courses: GraduationCap,
  graph: Graph,
  projects: RocketLaunch,
  write: PenNib,
  decisions: Scales,
  self: User,
  evaluations: ChartBar,
  sync: ArrowsClockwise,
  settings: Gear,
  list: List,
  brain: Brain,
  x: X,
  search: MagnifyingGlass,
  logout: SignOut,
} as const

type IconName = keyof typeof icons

interface Props {
  name: IconName
  size?: number
  weight?: 'thin' | 'light' | 'regular' | 'bold' | 'fill' | 'duotone'
  className?: string
}

export default function Icon({ name, size = 20, weight = 'regular', className }: Props) {
  const Component = icons[name]
  return <Component size={size} weight={weight} className={className} />
}
