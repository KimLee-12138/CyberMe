---
id: asm-interrupts
type: concept
status: active
course: ASM
source: ["课件-中断", "课件-功能调用"]
created: 2026-07-18
updated: 2026-07-18
mastery: reviewing
importance: critical
confidence: high
---

# 中断与DOS功能调用

> 一句话：中断让 CPU 能响应突发事件。中断向量表是"应急通讯录"，int 21H 是写 DOS 程序的瑞士军刀。

## 一、中断的分类

```
中断
├─ 内中断（软中断）
│  ├─ INT 指令（主动调用）
│  ├─ CPU 错误（除法溢出、单步调试）
│  └─ 断点中断
└─ 外中断（硬中断）
   ├─ 可屏蔽中断（键盘、鼠标）— 可用 CLI 屏蔽
   └─ 非屏蔽中断（电源掉电、内存校验错）— 必须响应
```

## 二、中断向量表

位于内存最底部 `0000:0000 ~ 0000:03FF`，共 1024 字节。存储 256 个中断处理程序的入口地址。

**每个中断占 4 字节**：
- 低字（字节 0-1）：偏移地址 IP
- 高字（字节 2-3）：段地址 CS

```
中断 N 的入口地址所在位置：
IP = 内存 [N × 4] 字
CS = 内存 [N × 4 + 2] 字
```

**0000:0200 ~ 0000:02FF** 这 256 字节是空的——**考试重点：自己编写的中断处理程序可以复制到这段空白区域**。

## 三、CPU 响应中断的 6 步

当 CPU 响应中断时，硬件自动执行：

| 步骤 | 操作 | 说明 |
|------|------|------|
| 1 | 获取中断类型码 N | 从 INTA 总线周期或 INT 指令 |
| 2 | 标志寄存器入栈 | pushf |
| 3 | TF=0, IF=0 | 禁止单步和其他可屏蔽中断 |
| 4 | CS 入栈 | 保存返回段地址 |
| 5 | IP 入栈 | 保存返回偏移 |
| 6 | 设置 CS:IP | 从中断向量表 N×4 处加载 |

完成后 CPU 跳转到中断处理程序。**这是考试最爱考的流程**。

## 四、IRET 指令

中断程序结束时执行 `iret`，相当于：

```
pop IP    ; 恢复指令指针
pop CS    ; 恢复代码段
popf      ; 恢复标志寄存器
```

CPU 自动回到被打断的位置继续执行。

## 五、编写自定义中断程序（考试重点）

完整步骤：

```asm
; 1. 将中断处理程序代码复制到 0000:0200H 处
mov ax, cs
mov ds, ax
mov ax, 0
mov es, ax
mov si, offset do0      ; 源地址（我们的程序）
mov di, 0200H           ; 目的地址（中断向量表空白区）
mov cx, offset do0_end - offset do0  ; 程序长度
cld
rep movsb               ; 复制！

; 2. 修改中断向量表，让 0 号中断指向我们的程序
mov ax, 0
mov es, ax
mov word ptr es:[0*4], 0200H    ; IP
mov word ptr es:[0*4+2], 0      ; CS

; 3. 触发中断
int 0

; 4. 中断处理程序
do0:
    ; 显示 "overflow!" 等处理逻辑
    ; ...
    iret
do0_end: nop
```

## 六、DOS 功能调用（INT 21H）

| AH | 功能 | 入口参数 | 示例 |
|----|------|---------|------|
| 4CH | 程序退出 | AL=返回码 | `mov ah,4CH; int 21H` |
| 09H | 显示字符串 | DS:DX=字符串(以'$'结尾) | `mov ah,9; int 21H` |
| 02H | 显示单个字符 | DL=字符 | `mov ah,2; int 21H` |
| 01H | 键盘输入(回显) | — | 返回 AL=ASCII 码 |
| 0AH | 字符串输入 | DS:DX=缓冲区 | 略 |

### 6.1 显示字符串标准模板

```asm
data segment
    msg db 'Hello World!$'    ; 以 $ 结尾！
data ends

code segment
    assume cs:code, ds:data
start:
    mov ax, data
    mov ds, ax
    mov ah, 9
    mov dx, offset msg
    int 21H
    mov ah, 4CH
    int 21H
code ends
end start
```

### 6.2 显示单个字符

```asm
mov ah, 2
mov dl, 'A'         ; 或 mov dl, 41H
int 21H
```

## 七、完整程序框架

```asm
assume cs:code, ds:data

data segment
    ; 数据定义放这里
data ends

code segment
start:
    mov ax, data
    mov ds, ax

    ; 你的代码

    mov ah, 4CH
    int 21H
code ends
end start
```

## 八、易错点

1. **中断向量表每个表项 4 字节**：IP(低字) + CS(高字)
2. **int 指令的保存顺序**：先 pushf，再 CS，再 IP（iret 恢复时刚好反向）
3. **自定义中断必须先复制程序到 0000:0200H**，再改中断向量表
4. **DOS 功能调用的字符串必须 `$` 结尾**

---

## 相关链接
- [[标志寄存器与条件转移]] — 条件跳转
- [[汇编程序设计模板]] — 完整程序示例
