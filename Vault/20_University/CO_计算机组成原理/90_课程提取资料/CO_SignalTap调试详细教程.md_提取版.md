---
id: extract-co-b1df9301
type: extract
status: extracted
course: CO
source:
  - "[[91_Raw-Archive/DOC/CO_SignalTap调试详细教程.md_笔记_未知日期_b1df9301.md]]"
source_pages: all
source_hash: "b1df9301b3a5eb67e382b9224fd5e88640cf761ed81972fcc054e536ea867fcc"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# SignalTap调试详细教程.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# SignalTap 调试详细教程

本文档是 `DE1_SOC_golden_top` 工程的 SignalTap 傻瓜式调试教程。它只讲如何用 SignalTap 观察本实验 ALU 的内部信号，不重新讲完整 ALU 原理。

如果你第一次使用 SignalTap，可以直接从第 1 节开始照做；如果你已经会打开 SignalTap，可以跳到第 7 节开始做 ALU 观察实验。

## 1. 先弄清楚 SignalTap 是什么

SignalTap II Logic Analyzer 是 Quartus 自带的片上逻辑分析仪。

普通示波器只能测 FPGA 引脚上的信号；SignalTap 可以把 FPGA 内部信号抓出来看，例如本实验里的：

- `alu:alu_inst|a[31..0]`
- `alu:alu_inst|b[31..0]`
- `alu:alu_inst|aluc[3..0]`
- `alu:alu_inst|r[31..0]`
- `alu:alu_inst|z`
- `alu:alu_inst|d_as[31..0]`
- `alu:alu_inst|d_sh[31..0]`

本实验顶层代码中 ALU 输出没有接到 LED 或数码管，所以看不到板上显示是正常的。观察 ALU 结果主要靠 SignalTap。

三个文件要分清：

| 文件 | 作用 |
| --- | --- |
| `DE1_SOC_golden_top.qpf` | Quartus 工程文件，用来打开工程。 |
| `output_files/DE1_SOC_golden_top.sof` | 下载到 FPGA 的配置文件。 |
| `stp1.stp` | SignalTap 配置文件，里面保存要观察哪些内部信号、用哪个时钟采样、采样深度是多少。 |

最容易混淆的是 `.sof` 和 `.stp`：

- `.sof` 是真正下载到 FPGA 里的硬件电路。
- `.stp` 是 SignalTap 的观察窗口配置。
- 两者必须匹配。换了工程、重新综合、改了节点后，旧 `.stp` 可能找不到信号。

## 2. 本工程中 SignalTap 已经配置好的内容

当前 `stp1.stp` 已经配置：

| 配置项 | 当前值 |
| --- | --- |
| 采样时钟 | `CLOCK_50` |
| 采样边沿 | 上升沿 |
| 采样深度 | 256 |
| `.sof` 路径 | `output_files/DE1_SOC_golden_top.sof` |
| 主要观察对象 | `KEY[0]`、`SW[4]`、ALU 输入、输出和内部中间结果 |

已配置的重点信号如下：

| 信号 | 含义 | 推荐显示进制 |
| --- | --- | --- |
| `KEY[0]` | 低有效复位按键 | Binary |
| `SW[4]` | 测试数据自动递增使能 | Binary |
| `alu:alu_inst|a[31..0]` | ALU 输入 `a`，来自 `pattern_a` | Hexadecimal |
| `alu:alu_inst|b[31..0]` | ALU 输入 `b`，来自 `pattern_b` | Hexadecimal |
| `alu:alu_inst|aluc[3..0]` | ALU 控制码，来自 `SW[3:0]` | Binary 或 Hexadecimal |
| `alu:alu_inst|r[31..0]` | ALU 最终结果 | Hexadecimal |
| `alu:alu_inst|z` | 零标志，`r` 全 0 时为 1 | Binary |
| `alu:alu_inst|d_and[31..0]` | `a & b` | Hexadecimal |
| `alu:alu_inst|d_or[31..0]` | `a | b` | Hexadecimal |
| `alu:alu_inst|d_xor[31..0]` | `a ^ b` | Hexadecimal |
| `alu:alu_inst|d_and_or[31..0]` | AND/OR 二选一后的结果 | Hexadecimal |
| `alu:alu_inst|d_xor_lui[31..0]` | XOR/LUI 二选一后的结果 | Hexadecimal |
| `alu:alu_inst|d_as[31..0]` | 加法或减法结果 | Hexadecimal |
| `alu:alu_inst|d_sh[31..0]` | 移位结果 | Hexadecimal |
| `alu:alu_inst|addsub32:as32|a[31..0]` | 加减法器输入 `a` | Hexadecimal |
| `alu:alu_inst|addsub32:as32|b[31..0]` | 加减法器实际输入 `b`，减法时会变成 `~b` | Hexadecimal |
| `alu:alu_inst|addsub32:as32|s[31..0]` | 加减法器输出 | Hexadecimal |

## 3. 上板前检查清单

开始调试前，先按下面清单检查。这个清单可以直接给学生照着打勾。

| 检查项 | 正确状态 |
| --- | --- |
| 开发板电源 | 已打开，板子电源灯亮。 |
| USB-Blaster | 已连接电脑和 DE1-SoC。 |
| Quartus 工程 | 已打开 `DE1_SOC_golden_top.qpf`。 |
| `.sof` 文件 | `output_files/DE1_SOC_golden_top.sof` 存在。 |
| SignalTap 文件 | `stp1.stp` 存在。 |
| 目标器件 | Quartus 能看到 DE1-SoC 的 Cyclone V 器件。 |
| 板上开关 | 初始建议 `SW[4]=0`，`SW[3:0]=0000`。 |

本实验推荐先使用已有的 `.sof` 下载观察。因为当前工程的 `.qsf` 中引用了两个当前文件夹里不存在的文件：`alu/regfile.v` 和 `alu/dff32.v`。如果重新完整编译，可能需要先处理这两个缺失文件引用。

## 4. 第一次打开工程

1. 启动 Quartus。
2. 点击菜单 `File -> Open Project...`。
3. 进入工程目录：
   - `C:\Users\22067\Desktop\DE1_SOC_experiment2`
4. 选择：
   - `DE1_SOC_golden_top.qpf`
5. 点击 `Open`。
6. 打开后，在 Quartus 左侧或标题栏确认工程名是：
   - `DE1_SOC_golden_top`

如果 Quartus 提示工程版本较旧，通常可以选择打开或迁移，但助教演示时建议使用和实验室环境一致的 Quartus 版本，避免版本差异导致 SignalTap 节点变化。

## 5. 下载 `.sof` 到 FPGA

这一步的目标是把已经编译好的硬件电路下载到 DE1-SoC。

### 5.1 打开 Programmer

1. 在 Quartus 中点击：
   - `Tools -> Programmer`
2. 弹出 Programmer 窗口。
3. 点击 `Hardware Setup...`。
4. 在硬件列表中选择 USB-Blaster。
5. 点击 `Close`。

如果这里没有 USB-Blaster：

- 检查 USB 线是否插好。
- 检查开发板是否上电。
- 检查驱动是否安装。
- 重新插拔 USB-Blaster。
- 必要时重启 Quartus。

### 5.2 添加或确认 `.sof`

在 Programmer 窗口中确认文件列表里有：

```text
output_files/DE1_SOC_golden_top.sof
```

如果没有：

1. 点击 `Add File...`。
2. 进入工程目录下的 `output_files`。
3. 选择 `DE1_SOC_golden_top.sof`。
4. 点击 `Open`。

### 5.3 开始下载

1. 勾选 `.sof` 那一行的 `Program/Configure`。
2. 点击 `Start`。
3. 等进度条到 100%。
4. 如果显示成功，说明 FPGA 已经配置完成。

下载成功后，板上不一定会有明显 LED 变化。因为本工程没有把 ALU 结果连到 LED，这不是错误。

## 6. 打开 SignalTap

### 6.1 打开工具

1. 在 Quartus 中点击：
   - `Tools -> SignalTap II Logic Analyzer`
2. 如果自动打开了 `stp1.stp`，直接继续。
3. 如果没有自动打开：
   - 在 SignalTap 窗口中点击 `File -> Open...`
   - 选择工程目录下的 `stp1.stp`
   - 点击 `Open`

### 6.2 认识 SignalTap 界面

SignalTap 窗口一般可以分成几块：

| 区域 | 作用 |
| --- | --- |
| JTAG Chain 或 Hardware 区域 | 选择连接的开发板和 FPGA 器件。 |
| Instance Manager | 显示 SignalTap 实例，本工程通常是 `auto_signaltap_0`。 |
| Setup 视图 | 配置采样时钟、采样深度、触发条件、观测信号。 |
| Data 视图 | 显示采样后的波形或数据。 |
| Signal 列表 | 左侧列出所有被采样的信号。 |
| 波形区 | 右侧显示每个采样点上信号的值。 |

如果学生看到界面很多按钮，不要慌。做本实验主要只用这几个功能：

- 选择硬件。
- 选择 `.sof`。
- 确认采样时钟。
- 点击运行采样。
- 查看 `a`、`b`、`aluc`、`r`、`z`。

## 7. SignalTap 基本设置确认

### 7.1 确认 JTAG Chain

在 SignalTap 界面中找到 JTAG Chain 或 Hardware 相关区域。

正确情况应该能看到类似：

```text
DE-SoC [USB-1]
```

并且器件类似：

```text
5CSE...
```

如果看不到：

1. 检查 Programmer 能不能下载 `.sof`。
2. 检查 USB-Blaster 是否被选中。
3. 检查板子电源。
4. 关闭 SignalTap 再重新打开。
5. 必要时回到 Programmer 重新执行一次下载。

### 7.2 确认 `.sof` 文件

在 SignalTap 中找到 `.sof` 文件设置位置，确认它指向：

```text
output_files/DE1_SOC_golden_top.sof
```

如果路径不对：

1. 点击选择 `.sof` 的按钮。
2. 找到工程目录：
   - `C:\Users\22067\Desktop\DE1_SOC_experiment2`
3. 进入：
   - `output_files`
4. 选择：
   - `DE1_SOC_golden_top.sof`
5. 确认。

注意：SignalTap 使用的 `.sof` 必须和 FPGA 里下载的 `.sof` 是同一个版本。否则可能出现节点无效、采样不到、数据不对等问题。

### 7.3 确认采样时钟

在 `Setup` 页面中找到 Clock 设置。

本工程应为：

```text
CLOCK_50
```

采样边沿为：

```text
posedge
```

意思是 SignalTap 每遇到一次 `CLOCK_50` 上升沿，就采一个样本。

为什么用 `CLOCK_50`：

- 顶层中 `pattern_a` 和 `pattern_b` 就是在 `CLOCK_50` 上升沿更新。
- 用同一个时钟采样，观察到的数据最容易解释。

### 7.4 确认采样深度

本工程 `stp1.stp` 中采样深度为：

```text
256
```

含义是一次采样会保存 256 个采样点。

在 50 MHz 时钟下：

```text
1 个周期 = 20 ns
256 个周期 = 5120 ns = 5.12 us
```

这说明 SignalTap 抓到的是一小段非常短的高速波形。对于观察 `SW[4]=1` 时 `a` 和 `b` 每个时钟变化很有用；对于手动拨开关这种慢动作，则通常每次拨完开关后重新采样。

## 8. 第一次采样：确认工具能正常工作

这一节只做最简单的确认：能不能采到 `KEY[0]`、`SW[4]`、`a`、`b`。

### 8.1 板上开关先这样放

先把板子设置成静态输入：

| 开关或按键 | 状态 |
| --- | --- |
| `SW[4]` | 0 |
| `SW[3]` | 0 |
| `SW[2]` | 0 |
| `SW[1]` | 0 |
| `SW[0]` | 0 |
| `KEY[0]` | 先不按 |

说明：

- `SW[4]=0` 表示 `pattern_a` 和 `pattern_b` 保持不变。
- `SW[3:0]=0000` 表示 ALU 做 ADD。

不同实验室板子的开关方向可能会让新同学困惑。一般拨到 ON 或上方表示 1，拨到下方表示 0；如果不确定，以 SignalTap 里看到的 `aluc[3..0]` 和 `SW[4]` 为准。

### 8.2 复位一次

1. 按下 `KEY[0]`。
2. 保持大约 1 秒。
3. 松开 `KEY[0]`。

复位后，顶层代码会把：

```text
pattern_a = 0x0000000A
pattern_b = 0x0000000B
```

因此 SignalTap 中应看到：

```text
alu:alu_inst|a[31..0] = 0x0000000A
alu:alu_inst|b[31..0] = 0x0000000B
```

### 8.3 点击运行采样

在 SignalTap 窗口中点击运行按钮。不同 Quartus 版本按钮名字可能略有不同，常见叫法包括：

- `Run Analysis`
- `Run`
- 工具栏上的播放按钮

如果弹出提示要求重新下载 `.sof`，确认当前 `.sof` 是 `output_files/DE1_SOC_golden_top.sof` 后继续。

采样结束后，Data 页面会出现波形或数据。

### 8.4 第一次采样应该看到什么

找到以下信号：

```text
alu:alu_inst|a[31..0]
alu:alu_inst|b[31..0]
alu:alu_inst|aluc[3..0]
alu:alu_inst|r[31..0]
alu:alu_inst|z
```

如果当前 `SW[3:0]=0000`，那么：

```text
a = 0x0000000A
b = 0x0000000B
aluc = 0000
r = 0x00000015
z = 0
```

因为：

```text
0xA + 0xB = 0x15
```

如果 `a` 和 `b` 不是 `0xA` 和 `0xB`：

1. 确认 `SW[4]=0`。
2. 再按一次 `KEY[0]` 复位。
3. 松开后重新采样。

如果 `r` 不等于 `0x15`：

1. 看 `aluc[3..0]` 是不是 `0000`。
2. 如果不是，检查 `SW[3:0]` 是否拨对。
3. 注意 `SW[0]` 是最低位，`SW[3]` 是最高位。

## 9. 设置显示进制

SignalTap 默认可能用 Binary 显示 32 位总线，读起来非常痛苦。建议把 32 位总线改成十六进制显示。

推荐设置：

| 信号 | 推荐显示方式 |
| --- | --- |
| `a[31..0]` | Hexadecimal |
| `b[31..0]` | Hexadecimal |
| `r[31..0]` | Hexadecimal |
| `d_as[31..0]` | Hexadecimal |
| `d_sh[31..0]` | Hexadecimal |
| `d_and[31..0]` | Hexadecimal |
| `d_or[31..0]` | Hexadecimal |
| `d_xor[31..0]` | Hexadecimal |
| `aluc[3..0]` | Binary |
| `z` | Binary |
| `KEY[0]` | Binary |
| `SW[4]` | Binary |

常见操作方式：

1. 在信号列表里右键某个信号。
2. 找到 `Radix` 或 `Bus Display Format`。
3. 选择 `Hexadecimal`。

如果要讲给学生听，建议这样说：

```text
32 位数据看十六进制，控制信号看二进制。
```

这样最清楚。

## 10. 固定输入下验证全部 ALU 功能

这一节是本实验最重要的 SignalTap 操作。

### 10.1 固定输入

先把输入固定在复位值：

1. 设置 `SW[4]=0`。
2. 按下 `KEY[0]`。
3. 松开 `KEY[0]`。
4. 采样确认：

```text
a = 0x0000000A
b = 0x0000000B
```

之后只改变 `SW[3:0]`，不要动 `SW[4]`。

### 10.2 逐个拨控制码

`SW[3:0]` 对应 `aluc[3:0]`：

| 开关 | 控制码位 |
| --- | --- |
| `SW[3]` | `aluc[3]` |
| `SW[2]` | `aluc[2]` |
| `SW[1]` | `aluc[1]` |
| `SW[0]` | `aluc[0]` |

例如：

| 想设置的 `aluc` | 开关状态 |
| --- | --- |
| `0000` | `SW[3]=0, SW[2]=0, SW[1]=0, SW[0]=0` |
| `0100` | `SW[3]=0, SW[2]=1, SW[1]=0, SW[0]=0` |
| `1111` | `SW[3]=1, SW[2]=1, SW[1]=1, SW[0]=1` |

每次拨完一个控制码后：

1. 点击 `Run Analysis`。
2. 等采样完成。
3. 看 `aluc[3..0]` 是否等于你想设置的值。
4. 看 `r[31..0]` 和 `z`。
5. 填表记录。

### 10.3 固定输入期望结果表

复位后：

```text
a = 0x0000000A
b = 0x0000000B
a[4:0] = 10
```

应得到：

| `aluc` | 运算 | 期望 `r` | 期望 `z` | SignalTap 实测 `r` | SignalTap 实测 `z` |
| --- | --- | --- | --- | --- | --- |
| `0000` | ADD | `0x00000015` | 0 |  |  |
| `0001` | AND | `0x0000000A` | 0 |  |  |
| `0010` | XOR | `0x00000001` | 0 |  |  |
| `0011` | SLL | `0x00002C00` | 0 |  |  |
| `0100` | SUB | `0xFFFFFFFF` | 0 |  |  |
| `0101` | OR | `0x0000000B` | 0 |  |  |
| `0110` | LUI | `0x000B0000` | 0 |  |  |
| `0111` | SRL | `0x00000000` | 1 |  |  |
| `1000` | ADD | `0x00000015` | 0 |  |  |
| `1001` | AND | `0x0000000A` | 0 |  |  |
| `1010` | XOR | `0x00000001` | 0 |  |  |
| `1011` | SLL | `0x00002C00` | 0 |  |  |
| `1100` | SUB | `0xFFFFFFFF` | 0 |  |  |
| `1101` | OR | `0x0000000B` | 0 |  |  |
| `1110` | LUI | `0x000B0000` | 0 |  |  |
| `1111` | SRA | `0x00000000` | 1 |  |  |

### 10.4 看懂几个重点例子

#### 例 1：`aluc=0000`

```text
aluc[1:0] = 00 -> 选择 d_as
aluc[2] = 0 -> d_as 做加法
r = a + b = 0xA + 0xB = 0x15
z = 0
```

SignalTap 中重点看：

```text
d_as = 0x00000015
r    = 0x00000015
z    = 0
```

#### 例 2：`aluc=0100`

```text
aluc[1:0] = 00 -> 选择 d_as
aluc[2] = 1 -> d_as 做减法
r = a - b = 0xA - 0xB = -1 = 0xFFFFFFFF
z = 0
```

SignalTap 中重点看：

```text
d_as = 0xFFFFFFFF
r    = 0xFFFFFFFF
z    = 0
```

同时可以看加减法器内部：

```text
addsub32:as32|a = 0x0000000A
addsub32:as32|b = 0xFFFFFFF4
addsub32:as32|s = 0xFFFFFFFF
```

这里 `0xFFFFFFF4` 是 `0x0000000B` 按位取反后的结果。再加上初始进位 1，就实现了 `a - b`。

#### 例 3：`aluc=0110`

```text
aluc[1:0] = 10 -> 选择 d_xor_lui
aluc[2] = 1 -> d_xor_lui 选择 LUI
r = {b[15:0], 16'h0}
  = {16'h000B, 16'h0000}
  = 0x000B0000
```

SignalTap 中重点看：

```text
d_xor_lui = 0x000B0000
r         = 0x000B0000
```

#### 例 4：`aluc=0011`

```text
aluc[1:0] = 11 -> 选择 d_sh
aluc[2] = 0 -> 左移
d = b = 0x0000000B
sa = a[4:0] = 10
r = b << 10 = 0x00002C00
```

SignalTap 中重点看：

```text
d_sh = 0x00002C00
r    = 0x00002C00
```

#### 例 5：`aluc=0111`

```text
aluc[1:0] = 11 -> 选择 d_sh
aluc[2] = 1 -> 右移
aluc[3] = 0 -> 逻辑右移
r = 0x0000000B >> 10 = 0x00000000
z = 1
```

SignalTap 中重点看：

```text
d_sh = 0x00000000
r    = 0x00000000
z    = 1
```

## 11. 观察中间信号：证明 ALU 是“先算候选结果，再选择”

很多学生会把 Verilog 当成软件顺序执行。SignalTap 可以帮助他们看到：ALU 内部很多结果是同时存在的，最后只是选择一个作为 `r`。

### 11.1 推荐观察组合

固定：

```text
a = 0x0000000A
b = 0x0000000B
SW[4] = 0
```

同时观察：

```text
d_as
d_and
d_or
d_xor
d_and_or
d_xor_lui
d_sh
r
aluc
```

### 11.2 操作步骤

1. 复位，让 `a=0xA`，`b=0xB`。
2. 设置 `aluc=0000`。
3. 采样并记录：
   - `d_as`
   - `d_and`
   - `d_or`
   - `d_xor`
   - `d_sh`
   - `r`
4. 改成 `aluc=0001`。
5. 再采样并记录。
6. 改成 `aluc=0010`。
7. 再采样并记录。
8. 改成 `aluc=0011`。
9. 再采样并记录。

你会发现：

- 中间信号一直都能算出对应候选结果。
- `r` 会随着 `aluc[1:0]` 选择不同通路。
- `aluc[2]` 会改变某些中间信号的含义。

### 11.3 给学生的解释话术

可以这样讲：

```text
ALU 不是先判断要做什么再临时生成一块硬件，而是加减法、逻辑、移位这些组合逻辑都已经在电路里。控制码 aluc 的作用，是选择哪个候选结果送到最终输出 r。
```

## 12. 动态输入观察：打开 `SW[4]`

前面都是固定输入。现在观察 `SW[4]=1` 时，测试数据自动递增。

### 12.1 先理解代码行为

顶层代码中：

```verilog
if(SW[4])
begin
    pattern_a <= pattern_a + 32'h1;
    pattern_b <= pattern_b + 32'h3;
end
```

因此当 `SW[4]=1`：

```text
a 每个 CLOCK_50 上升沿加 1
b 每个 CLOCK_50 上升沿加 3
```

由于 `CLOCK_50` 是 50 MHz，所以变化非常快，肉眼无法观察，只能用 SignalTap 抓一小段。

### 12.2 操作步骤

1. 先设置 `SW[4]=0`。
2. 按下并松开 `KEY[0]`，让：

```text
a = 0x0000000A
b = 0x0000000B
```

3. 设置一个简单控制码，例如：

```text
SW[3:0] = 0000
```

也就是 ADD。

4. 将 `SW[4]` 拨到 1。
5. 立刻点击 `Run Analysis`。
6. 观察 `a`、`b`、`r`。

### 12.3 期望看到什么

如果采样区间内数据连续变化，理想情况下会看到：

```text
a: 0x0000000A, 0x0000000B, 0x0000000C, 0x0000000D, ...
b: 0x0000000B, 0x0000000E, 0x00000011, 0x00000014, ...
r: a + b
```

由于手动拨动 `SW[4]` 和点击采样之间有时间差，实际第一帧不一定从 `0xA`、`0xB` 开始。这是正常的。重点是看变化规律：

```text
a 每个采样点大约 +1
b 每个采样点大约 +3
```

如果你只想观察固定值，不要开 `SW[4]`，保持 `SW[4]=0`。

## 13. 触发条件怎么用

刚开始可以直接点击 `Run Analysis` 抓一段数据。但如果想抓“按下复位的瞬间”或“打开 SW[4] 的瞬间”，可以设置触发条件。

### 13.1 什么是触发

触发就是告诉 SignalTap：

```text
等某个条件发生时，再开始保存波形。
```

例如：

- `KEY[0]` 从 1 变成 0：按下复位。
- `KEY[0]` 从 0 变成 1：松开复位。
- `SW[4]` 从 0 变成 1：开始自动递增。
- `aluc[3..0] = 0100`：观察减法。

### 13.2 最简单的触发：不设复杂条件

对学生第一次实验，推荐不设置复杂触发。原因是：

- 当前采样深度只有 256。
- ALU 是组合逻辑，拨完开关后直接采样就能看到稳定结果。
- 复杂触发容易让初学者卡在工具操作上。

最简单流程：

```text
拨开关 -> Run Analysis -> 看结果 -> 记录
```

### 13.3 进阶触发：抓复位后数据

如果想抓松开 `KEY[0]` 后 `a`、`b` 变成复位值的过程：

1. 在 SignalTap 的触发列找到 `KEY[0]`。
2. 设置触发条件为 `KEY[0] = 1` 或上升沿。
3. 点击 `Run Analysis`。
4. 按下 `KEY[0]`。
5. 松开 `KEY[0]`。
6. SignalTap 捕获波形。

不同 Quartus 版本里，边沿触发图标可能显示为上升箭头或文字。如果学生不会设置边沿，直接设置电平触发也可以：

```text
KEY[0] = 1
```

然后在松开按键后触发。

### 13.4 进阶触发：抓 `SW[4]=1` 后自动递增

如果想观察 `a` 和 `b` 连续变化：

1. 设置 `SW[4]=0`。
2. 复位一次。
3. 在触发条件中设置：

```text
SW[4] = 1
```

4. 点击 `Run Analysis`。
5. 把 `SW[4]` 拨到 1。
6. 等采样结束。
7. 查看 `a`、`b` 是否连续变化。

如果没有触发：

- 确认 `SW[4]` 在 SignalTap 中真的从 0 变成 1。
- 确认板上开关方向。
- 确认 JTAG 和 `.sof` 没问题。

## 14. SignalTap 中如何重新添加节点

如果 `stp1.stp` 里的节点变红、显示 invalid、或找不到信号，可以重新添加节点。

### 14.1 打开 Node Finder

1. 在 SignalTap 的信号列表区域右键。
2. 选择 `Add Nodes...` 或 `Insert Node or Bus...`。
3. 打开 Node Finder。

不同版本菜单名称可能略有不同，但关键词一般是：

- `Node Finder`
- `Add Nodes`
- `Insert Node`
- `SignalTap II: pre-synthesis`
- `post-fitting`

### 14.2 设置过滤器

在 Node Finder 中：

1. Filter 选择类似：

```text
SignalTap II: post-fitting
```

或：

```text
SignalTap II: pre-synthesis
```

2. 点击 `List`。
3. 等待节点列表生成。

如果列表为空：

- 工程可能没有编译。
- `.sof` 和工程不匹配。
- SignalTap 未启用。
- 选择的过滤器不对。

### 14.3 搜索本实验重点信号

建议搜索关键词：

| 想找的信号 | 搜索关键词 |
| --- | --- |
| ALU 输入 `a` | `alu_inst` 或 `a[` |
| ALU 输入 `b` | `alu_inst` 或 `b[` |
| 控制码 | `aluc` |
| 输出结果 | `r[` |
| 零标志 | `z` |
| 加减法结果 | `d_as` |
| 移位结果 | `d_sh` |
| AND 结果 | `d_and` |
| OR 结果 | `d_or` |
| XOR 结果 | `d_xor` |

本工程常见完整节点名：

```text
alu:alu_inst|a[31..0]
alu:alu_inst|b[31..0]
alu:alu_inst|aluc[3..0]
alu:alu_inst|r[31..0]
alu:alu_inst|z
alu:alu_inst|d_as[31..0]
alu:alu_inst|d_sh[31..0]
```

### 14.4 添加到 SignalTap

1. 选中要添加的节点。
2. 点击 `>` 或 `Add`，加入右侧 Selected Nodes。
3. 点击 `OK`。
4. 回到 SignalTap 主界面。
5. 确认新信号出现在列表里。

如果添加了新节点，通常需要重新编译工程，让 SignalTap 逻辑被综合进 FPGA。当前实验建议优先使用已配置好的 `stp1.stp`，不要随意改动节点，除非原节点无效。

## 15. 如果改了 SignalTap 配置，要不要重新编译

简单判断：

| 操作 | 通常是否需要重新编译 |
| --- | --- |
| 只改显示进制 | 不需要 |
| 只缩放波形 | 不需要 |
| 只重新运行采样 | 不需要 |
| 改触发条件 | 通常不需要重新完整编译 |
| 添加新的内部信号节点 | 通常需要重新编译 |
| 删除节点 | 通常需要重新编译 |
| 改采样深度 | 通常需要重新编译 |
| 改采样时钟 | 需要重新编译 |

对于本实验，建议学生不要修改采样深度、采样时钟和节点列表。只需要：

```text
打开 stp1.stp -> 下载已有 sof -> Run Analysis -> 看结果
```

这样最稳。

## 16. 常见错误现象与解决办法

### 16.1 找不到 USB-Blaster

现象：

```text
Hardware Setup 中没有 USB-Blaster
```

解决：

1. 检查 USB 线。
2. 检查板子电源。
3. 检查驱动。
4. 换 USB 口。
5. 重启 Quartus。
6. 先在 Programmer 中确认能否看到硬件。

### 16.2 Programmer 下载失败

可能原因：

- 没有选中正确硬件。
- `.sof` 路径不对。
- 板子没上电。
- USB-Blaster 驱动异常。

解决：

1. 重新选择 Hardware Setup。
2. 重新添加 `DE1_SOC_golden_top.sof`。
3. 勾选 `Program/Configure`。
4. 再点击 `Start`。

### 16.3 SignalTap 显示节点无效

常见显示：

```text
invalid node
node not found
```

可能原因：

- `.stp` 和 `.sof` 不是同一次工程生成的。
- 重新综合后节点名变了。
- 中间信号被综合优化。
- 当前打开的工程不是这个工程。

解决顺序：

1. 确认 Quartus 打开的是 `DE1_SOC_golden_top.qpf`。
2. 确认 SignalTap 打开的是 `stp1.stp`。
3. 确认 `.sof` 是 `output_files/DE1_SOC_golden_top.sof`。
4. 重新下载 `.sof`。
5. 关闭并重新打开 SignalTap。
6. 仍不行时，用 Node Finder 重新找信号。

### 16.4 采样后没有波形

可能原因：

- 没有点击 `Run Analysis`。
- 触发条件一直没有满足。
- JTAG 连接断开。
- FPGA 没有下载正确 `.sof`。

解决：

1. 先取消复杂触发，改成直接运行采样。
2. 重新下载 `.sof`。
3. 确认 JTAG Chain 能看到器件。
4. 点击 `Run Analysis`。

### 16.5 `a` 和 `b` 不是 `0xA`、`0xB`

可能原因：

- 没有按 `KEY[0]` 复位。
- `SW[4]=1`，导致数据已经快速变化。
- 采样时机在复位之前或动态变化之后。

解决：

1. 设置 `SW[4]=0`。
2. 按下 `KEY[0]`。
3. 松开 `KEY[0]`。
4. 重新采样。

### 16.6 `r` 和表格对不上

按顺序排查：

1. 看 `a` 是不是 `0x0000000A`。
2. 看 `b` 是不是 `0x0000000B`。
3. 看 `aluc[3..0]` 是不是你以为的值。
4. 看显示进制是不是 Hexadecimal。
5. 看 `SW[4]` 是否为 0。
6. 看是否下载了正确 `.sof`。

最常见错误是把开关位顺序弄反。记住：

```text
SW[3] SW[2] SW[1] SW[0]
  |     |     |     |
aluc3 aluc2 aluc1 aluc0
```

### 16.7 `z` 不知道怎么看

`z` 是 1 位信号：

```text
z = 1 表示 r 全 0
z = 0 表示 r 非 0
```

复位样例中，只有这些操作结果为 0：

```text
aluc = 0111，SRL
aluc = 1111，SRA
```

所以这两行 `z` 应该为 1。

### 16.8 为什么有些 `aluc` 结果重复

因为 `aluc[3]` 只对算术右移有影响。

例如：

```text
0000 和 1000 都是 ADD
0001 和 1001 都是 AND
0010 和 1010 都是 XOR
```

这是正常现象。

## 17. 助教演示流程建议

如果课堂时间有限，建议助教按这个顺序演示：

1. 打开 Quartus 工程。
2. 展示顶层代码中 `KEY[0]`、`SW[4]`、`SW[3:0]` 的作用。
3. 下载 `DE1_SOC_golden_top.sof`。
4. 打开 `stp1.stp`。
5. 确认 `CLOCK_50` 和采样深度 256。
6. 设置 `SW[4]=0`，按 `KEY[0]` 复位。
7. 设置 `aluc=0000`，采样，看 ADD 结果 `0x15`。
8. 设置 `aluc=0100`，采样，看 SUB 结果 `0xFFFFFFFF`。
9. 设置 `aluc=0110`，采样，看 LUI 结果 `0x000B0000`。
10. 设置 `aluc=0011`，采样，看 SLL 结果 `0x00002C00`。
11. 设置 `aluc=0111`，采样，看 `r=0`、`z=1`。
12. 打开 `SW[4]=1`，采样，看 `a`、`b` 动态递增。
13. 解释为什么 LED 没变化：ALU 输出没有接到 LED。
14. 解释节点无效时如何处理。

这一套演示基本能覆盖本实验最核心的 SignalTap 使用方法。

## 18. 学生实验记录模板

学生可以按下面模板记录。

### 18.1 工具设置

| 项目 | 记录 |
| --- | --- |
| 工程名 | `DE1_SOC_golden_top` |
| SignalTap 文件 | `stp1.stp` |
| 下载文件 | `output_files/DE1_SOC_golden_top.sof` |
| 采样时钟 | `CLOCK_50` |
| 采样深度 | 256 |
| 是否成功识别 USB-Blaster |  |
| 是否成功下载 `.sof` |  |

### 18.2 固定输入记录

| 项目 | SignalTap 观测值 |
| --- | --- |
| `SW[4]` |  |
| `KEY[0]` |  |
| `a[31..0]` |  |
| `b[31..0]` |  |

### 18.3 ALU 结果记录

| `aluc` | 运算 | 理论 `r` | 实测 `r` | 理论 `z` | 实测 `z` | 是否一致 |
| --- | --- | --- | --- | --- | --- | --- |
| `0000` | ADD | `0x00000015` |  | 0 |  |  |
| `0001` | AND | `0x0000000A` |  | 0 |  |  |
| `0010` | XOR | `0x00000001` |  | 0 |  |  |
| `0011` | SLL | `0x00002C00` |  | 0 |  |  |
| `0100` | SUB | `0xFFFFFFFF` |  | 0 |  |  |
| `0101` | OR | `0x0000000B` |  | 0 |  |  |
| `0110` | LUI | `0x000B0000` |  | 0 |  |  |
| `0111` | SRL | `0x00000000` |  | 1 |  |  |
| `1111` | SRA | `0x00000000` |  | 1 |  |  |

### 18.4 动态输入记录

打开 `SW[4]=1` 后，记录连续几个采样点：

| 采样点 | `a` | `b` | 当前运算 | `r` |
| --- | --- | --- | --- | --- |
| 0 |  |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |

观察结论：

```text
a 是否每个采样点加 1：
b 是否每个采样点加 3：
r 是否符合当前 aluc 对应运算：
```

## 19. 最短操作版

如果学生已经完成一次配置，只想快速复现实验，可以照这个最短流程：

1. 打开 `DE1_SOC_golden_top.qpf`。
2. 打开 Programmer。
3. 下载 `output_files/DE1_SOC_golden_top.sof`。
4. 打开 `Tools -> SignalTap II Logic Analyzer`。
5. 打开 `stp1.stp`。
6. 确认硬件是 USB-Blaster，`.sof` 路径正确。
7. 设置 `SW[4]=0`。
8. 按下并松开 `KEY[0]`。
9. 设置 `SW[3:0]=0000`。
10. 点击 `Run Analysis`。
11. 看：

```text
a = 0x0000000A
b = 0x0000000B
aluc = 0000
r = 0x00000015
z = 0
```

12. 改 `SW[3:0]`。
13. 再点 `Run Analysis`。
14. 对照结果表记录。

## 20. 一句话总结

本实验中 SignalTap 的核心用法就是：

```text
下载正确的 .sof，打开匹配的 .stp，用 CLOCK_50 采样，固定 SW[4]=0 后复位，再通过 SW[3:0] 改变 aluc，观察 ALU 内部信号和最终结果 r、z。
```



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_计算机组成原理_课程MOC|计算机组成原理 MOC]]
