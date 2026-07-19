import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'
import rehypeKatex from 'rehype-katex'
import type { Components } from 'react-markdown'
import './Markdown.css'

function slugify(text: string): string {
  return text.toLowerCase().replace(/[^\w\u4e00-\u9fff\s-]/g, '').replace(/\s+/g, '-')
}

const headingComponents: Components = {
  h2: ({ children, ...props }) => {
    const text = String(children)
    return <h2 id={slugify(text)} {...props}>{children}</h2>
  },
  h3: ({ children, ...props }) => {
    const text = String(children)
    return <h3 id={slugify(text)} {...props}>{children}</h3>
  },
  h4: ({ children, ...props }) => {
    const text = String(children)
    return <h4 id={slugify(text)} {...props}>{children}</h4>
  },
}

interface MarkdownProps {
  children: string
  math?: boolean
  extraComponents?: Components
}

export default function Markdown({ children, math = false, extraComponents }: MarkdownProps) {
  return (
    <div className="markdown-body">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, ...(math ? [remarkMath] : [])]}
        rehypePlugins={math ? [rehypeKatex] : []}
        components={extraComponents ? { ...headingComponents, ...extraComponents } : headingComponents}
      >
        {children}
      </ReactMarkdown>
    </div>
  )
}
