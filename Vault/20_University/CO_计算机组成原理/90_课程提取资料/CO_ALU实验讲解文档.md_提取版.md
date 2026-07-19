---
id: extract-co-7cf3e7cb
type: extract
status: extracted
course: CO
source:
  - "[[91_Raw-Archive/DOC/CO_ALU实验讲解文档.md_笔记_未知日期_7cf3e7cb.md]]"
source_pages: all
source_hash: "7cf3e7cbda8ca8202a7ab89c28193829e33641eddf6bab7fec8839c3c07a1092"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# ALU实验讲解文档.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# DE1-SoC 32 位 ALU 实验讲解文档

本文档面向两类使用者：

- 助教：可以按照本文档组织课堂讲解、实验演示和答疑。
- 学生：可以按照本文档完成工程打开、编译、下载、SignalTap 采样和结果分析。

本文档只基于当前仓库已有文件编写，不新增仿真主线、不修改 Verilog 源码、不修改 Quartus 工程配置。

## 1. 实验目标

本实验围绕一个 32 位 ALU（Arithmetic Logic Unit，算术逻辑单元）展开。学生需要理解 ALU 的基本数据通路、控制信号含义，以及如何在 FPGA 开发板上通过 SignalTap 观察内部组合逻辑信号。

完成本实验后，应达到以下目标：

1. 能打开并识别一个 DE1-SoC Quartus 工程。
2. 能说明顶层模块如何产生 ALU 的两个测试输入 `a` 和 `b`。
3. 能说明 `SW[3:0]` 如何作为 ALU 控制码 `aluc`。
4. 能理解 ALU 内部的四类结果通路：
   - 加法/减法通路。
   - 与/或逻辑通路。
   - 异或/LUI 通路。
   - 移位通路。
5. 能解释 `z = ~|r` 零标志的含义。
6. 能使用 SignalTap 观察 `a`、`b`、`aluc`、`r`、`z` 和中间信号。
7. 能根据给定输入手工计算 ALU 输出，并与 SignalTap 结果对照。

## 2. 工程文件总览

当前仓库是一个 Quartus 工程，顶层工程名为 `DE1_SOC_golden_top`。

| 文件或目录 | 作用 |
| --- | --- |
| `DE1_SOC_golden_top.qpf` | Quartus Project File，Quartus 工程入口文件之一。 |
| `DE1_SOC_golden_top.qsf` | Quartus Settings File，包含器件型号、顶层实体、引脚约束、源文件列表和 SignalTap 配置。 |
| `DE1_SOC_golden_top.qws` | Quartus workspace 文件，保存部分工作区状态。 |
| `DE1_SOC_golden_top.sdc` | 时序约束文件，定义时钟等时序约束。 |
| `DE1_SOC_golden_top.v` | 工程顶层 Verilog 文件，连接板上时钟、按键、开关，并例化 ALU。 |
| `alu/` | ALU 相关 Verilog 模块目录。 |
| `stp1.stp` | SignalTap 配置文件，用于采样 FPGA 内部信号。 |
| `output_files/` | Quartus 生成的综合、布局布线、时序报告和 `.sof` 下载文件。 |

`alu/` 目录中的主要文件如下：

| 文件 | 模块 | 作用 |
| --- | --- | --- |
| `alu/alu.v` | `alu` | 实验实际例化的 ALU 模块。 |
| `alu/alu_main.v` | `alu_main` | 与 `alu.v` 基本同构，但没有 `synthesis keep` 标记；当前顶层没有例化它。 |
| `alu/addsub32.v` | `addsub32` | 32 位加减法封装模块。 |
| `alu/cla32.v` | `cla32` | 32 位超前进位加法器顶层封装。 |
| `alu/cla_32.v`、`cla_16.v`、`cla_8.v`、`cla_4.v`、`cla_2.v` | `cla_*` | 分层构造超前进位加法器。 |
| `alu/g_p.v` | `g_p` | 根据组产生信号和组传递信号计算组进位。 |
| `alu/add.v` | `add` | 1 位加法单元，产生 `g`、`p` 和 `s`。 |
| `alu/shift.v` | `shift` | 左移、逻辑右移、算术右移。 |
| `alu/mux4x32.v` | `mux4x32` | 4 选 1 的 32 位多路选择器，用于选择 ALU 最终输出。 |
| `alu/mux2x32.v`、`alu/mux2x5.v` | `mux2x32`、`mux2x5` | 2 选 1 多路选择器；当前 ALU 主通路中没有直接使用。 |

## 3. 顶层模块与板上控制

顶层文件是 `DE1_SOC_golden_top.v`。该文件保留了 DE1-SoC 模板中的大量板级端口，但本实验真正用到的端口主要是：

| 端口 | 方向 | 实验中的作用 |
| --- | --- | --- |
| `CLOCK_50` | 输入 | 驱动 `pattern_a` 和 `pattern_b` 寄存器更新，也是 SignalTap 采样时钟。 |
| `KEY[0]` | 输入 | 低有效复位。按下时把测试数据初始化为固定值。 |
| `SW[3:0]` | 输入 | 作为 ALU 控制信号 `aluc`。 |
| `SW[4]` | 输入 | 控制测试数据是否自动递增。 |
| `LEDR`、`HEX0` 到 `HEX5` | 输出 | 顶层声明了这些端口，但当前实验代码没有驱动它们显示 ALU 结果。 |

### 3.1 测试数据寄存器

顶层中定义了两个 32 位寄存器：

```verilog
reg [31:0] pattern_a;
reg [31:0] pattern_b;
```

它们就是送入 ALU 的两个操作数。后面例化 ALU 时：

```verilog
.a(pattern_a),
.b(pattern_b),
.aluc(SW[3:0])
```

因此：

- ALU 的 `a` 来自 `pattern_a`。
- ALU 的 `b` 来自 `pattern_b`。
- ALU 的 `aluc` 来自板上开关 `SW[3:0]`。

### 3.2 复位行为

顶层的核心时序逻辑如下：

```verilog
always @ (posedge CLOCK_50)
begin
   if(!KEY[0])
      begin
        pattern_a <= 32'h000_000a;
        pattern_b <= 32'h000_000b;
      end
   else
      begin
        if(SW[4])
           begin
             pattern_a <= pattern_a + 32'h1;
             pattern_b <= pattern_b + 32'h3;
           end
        else
           begin
             pattern_a <= pattern_a;
             pattern_b <= pattern_b;
           end
      end
end
```

讲解要点：

- `always @ (posedge CLOCK_50)` 表示这是同步时序逻辑，只有在 `CLOCK_50` 上升沿才更新寄存器。
- `if(!KEY[0])` 表示 `KEY[0]` 是低有效复位：按键按下时通常读到逻辑 0。
- 复位时：
  - `pattern_a <= 32'h000_000a`，也就是十六进制 `0x0000000A`，十进制 10。
  - `pattern_b <= 32'h000_000b`，也就是十六进制 `0x0000000B`，十进制 11。
- 松开复位后：
  - 如果 `SW[4]=1`，`pattern_a` 每个时钟加 1，`pattern_b` 每个时钟加 3。
  - 如果 `SW[4]=0`，两个寄存器保持原值。

课堂演示建议：

1. 先让 `SW[4]=0`。
2. 按下并松开 `KEY[0]`。
3. 此时 SignalTap 中应看到 `a=0x0000000A`，`b=0x0000000B`。
4. 再切换 `SW[3:0]`，观察不同 `aluc` 下 `r` 的变化。
5. 最后把 `SW[4]=1`，观察 `a` 和 `b` 随时钟持续变化。

### 3.3 ALU 例化

顶层中例化的是 `alu`，不是 `alu_main`：

```verilog
alu alu_inst(
    .a(pattern_a),
    .b(pattern_b),
    .aluc(SW[3:0]),
    .r(),
    .z()
);
```

这里有一个非常重要的观察点：

- `r()` 和 `z()` 没有连接到顶层输出端口。
- 因此 ALU 结果不会显示到 LED 或数码管。
- 但 SignalTap 仍然可以观察 `alu_inst` 内部的 `r`、`z` 以及中间信号。

助教可以借这个设计讲清楚：FPGA 内部信号即使没有接到外部引脚，也可以通过片上逻辑分析仪 SignalTap 采样观察。

## 4. ALU 控制码与功能表

ALU 模块端口如下：

```verilog
module alu(a,b,aluc,r,z);
    input  [31:0] a,b;
    input  [3:0] aluc;
    output [31:0] r;
    output z;
```

其中：

- `a`、`b` 是两个 32 位操作数。
- `aluc` 是 4 位控制码。
- `r` 是 32 位运算结果。
- `z` 是零标志，当 `r` 全 0 时为 1。

ALU 的核心选择逻辑是：

```verilog
mux4x32 select (d_as,d_and_or,d_xor_lui,d_sh,aluc[1:0],r);
```

这说明最终输出 `r` 由 `aluc[1:0]` 决定：

| `aluc[1:0]` | 选择通路 | 含义 |
| --- | --- | --- |
| `00` | `d_as` | 加法或减法。 |
| `01` | `d_and_or` | AND 或 OR。 |
| `10` | `d_xor_lui` | XOR 或 LUI。 |
| `11` | `d_sh` | 移位。 |

`aluc[2]` 在不同通路里有不同含义：

| 通路 | `aluc[2]=0` | `aluc[2]=1` |
| --- | --- | --- |
| `d_as` | `a + b` | `a - b` |
| `d_and_or` | `a & b` | `a | b` |
| `d_xor_lui` | `a ^ b` | `{b[15:0], 16'h0}` |
| `d_sh` | 左移 | 右移 |

`aluc[3]` 只在右移时有意义：

- 当 `aluc[1:0]=11` 且 `aluc[2]=1` 时，表示右移。
- 此时 `aluc[3]=0` 是逻辑右移。
- 此时 `aluc[3]=1` 是算术右移。
- 对加法、减法、AND、OR、XOR、LUI 来说，`aluc[3]` 不改变结果。
- 对左移来说，`arith` 虽然传入了移位模块，但代码先判断 `!right`，所以左移时 `aluc[3]` 也不改变结果。

完整控制码表如下：

| `aluc` | `aluc[3]` | `aluc[2]` | `aluc[1:0]` | 运算 | 结果表达式 |
| --- | --- | --- | --- | --- | --- |
| `0000` | 0 | 0 | 00 | ADD | `a + b` |
| `0001` | 0 | 0 | 01 | AND | `a & b` |
| `0010` | 0 | 0 | 10 | XOR | `a ^ b` |
| `0011` | 0 | 0 | 11 | SLL | `b << a[4:0]` |
| `0100` | 0 | 1 | 00 | SUB | `a - b` |
| `0101` | 0 | 1 | 01 | OR | `a | b` |
| `0110` | 0 | 1 | 10 | LUI | `{b[15:0], 16'h0}` |
| `0111` | 0 | 1 | 11 | SRL | `b >> a[4:0]` |
| `1000` | 1 | 0 | 00 | ADD | `a + b` |
| `1001` | 1 | 0 | 01 | AND | `a & b` |
| `1010` | 1 | 0 | 10 | XOR | `a ^ b` |
| `1011` | 1 | 0 | 11 | SLL | `b << a[4:0]` |
| `1100` | 1 | 1 | 00 | SUB | `a - b` |
| `1101` | 1 | 1 | 01 | OR | `a | b` |
| `1110` | 1 | 1 | 10 | LUI | `{b[15:0], 16'h0}` |
| `1111` | 1 | 1 | 11 | SRA | `$signed(b) >>> a[4:0]` |

## 5. ALU 主模块代码讲解

`alu/alu.v` 是当前顶层实际使用的 ALU 模块。

### 5.1 逻辑运算通路

```verilog
wire [31:0] d_and = a & b;
wire [31:0] d_or  = a | b;
wire [31:0] d_xor = a ^ b;
wire [31:0] d_lui = {b[15:0],16'h0};
```

这四个信号是纯组合逻辑：

- `d_and`：按位与。
- `d_or`：按位或。
- `d_xor`：按位异或。
- `d_lui`：把 `b` 的低 16 位放到结果高 16 位，低 16 位补 0。

`d_lui` 对应类似 MIPS 中的 LUI（Load Upper Immediate）思想。例如：

- 若 `b = 32'h0000_000b`。
- `b[15:0] = 16'h000b`。
- `{b[15:0], 16'h0} = 32'h000b_0000`。

### 5.2 二级选择信号

```verilog
wire [31:0] d_and_or  = aluc[2]? d_or  : d_and;
wire [31:0] d_xor_lui = aluc[2]? d_lui : d_xor;
```

这是两个 2 选 1 选择器的写法：

- `aluc[2]=0` 时，`d_and_or=d_and`，`d_xor_lui=d_xor`。
- `aluc[2]=1` 时，`d_and_or=d_or`，`d_xor_lui=d_lui`。

这里可以提醒学生：同一个控制位 `aluc[2]` 在不同通路里被复用，是否表示减法、OR、LUI 或右移，要结合 `aluc[1:0]` 所选通路一起判断。

### 5.3 加减法和移位中间结果

```verilog
wire [31:0] d_as /*synthesis keep*/;
wire [31:0] d_sh /*synthesis keep*/;
addsub32 as32 (a,b,aluc[2],d_as);
shift shifter (b,a[4:0],aluc[2],aluc[3],d_sh);
```

`d_as` 是加减法结果：

- `aluc[2]=0`：加法。
- `aluc[2]=1`：减法。

`d_sh` 是移位结果：

- 被移位的数据是 `b`。
- 移位位数是 `a[4:0]`，也就是 `a` 的低 5 位。
- 32 位数据最多需要移动 0 到 31 位，所以低 5 位足够表示移位量。
- `aluc[2]` 传给 `right`，决定左移还是右移。
- `aluc[3]` 传给 `arith`，决定右移时是否算术右移。

`/*synthesis keep*/` 是综合属性，告诉综合器尽量保留这些中间信号。这样做的好处是方便 SignalTap 找到并观察 `d_as` 和 `d_sh`。如果没有这个属性，综合器可能认为某些中间信号可以被优化、合并或改名，导致调试时不容易找到。

### 5.4 最终结果选择

```verilog
mux4x32 select (d_as,d_and_or,d_xor_lui,d_sh,aluc[1:0],r);
```

这行是 ALU 主数据通路的核心：

- `aluc[1:0]=00`：输出 `d_as`。
- `aluc[1:0]=01`：输出 `d_and_or`。
- `aluc[1:0]=10`：输出 `d_xor_lui`。
- `aluc[1:0]=11`：输出 `d_sh`。

因此，ALU 可以理解为先并行算出多个候选结果，再用多路选择器挑一个作为最终结果。硬件中这些组合逻辑通常是并行存在的，不是像软件那样一条一条顺序执行。

### 5.5 零标志

```verilog
assign z = ~|r;
```

这是一个很典型的 Verilog 写法。

- `|r` 是归约或运算，只要 `r` 的任意一位是 1，结果就是 1。
- `~|r` 表示对归约或结果取反。
- 所以：
  - 当 `r = 32'h0000_0000` 时，`|r = 0`，`z = 1`。
  - 当 `r` 非 0 时，`|r = 1`，`z = 0`。

在 CPU 里，零标志常用于相等判断、条件分支等控制逻辑。

## 6. 加减法通路讲解

加减法从 `addsub32` 开始：

```verilog
module addsub32 (a, b, sub, s);
    input  [31:0] a, b;
    input         sub;
    output [31:0] s;
    cla32 as32 (a, b^{32{sub}}, sub, s);
endmodule
```

这里用一个加法器同时实现加法和减法。

### 6.1 加法

当 `sub=0` 时：

```verilog
b^{32{sub}} = b^{32{1'b0}} = b
ci = sub = 0
```

因此加法器实际计算：

```text
a + b + 0
```

也就是普通加法。

### 6.2 减法

当 `sub=1` 时：

```verilog
b^{32{sub}} = b^{32{1'b1}} = ~b
ci = sub = 1
```

因此加法器实际计算：

```text
a + ~b + 1
```

这正是补码减法：

```text
a - b = a + (~b + 1)
```

这是本实验中非常值得讲清楚的计算机组成原理知识点：硬件中不需要单独设计一个减法器，只要把 `b` 取反并让初始进位为 1，就可以用加法器完成减法。

## 7. 超前进位加法器 CLA 讲解

本工程没有直接使用 Verilog 的 `+` 来写完整 32 位加法器，而是分层构造了一个 CLA（Carry Lookahead Adder，超前进位加法器）。

### 7.1 一位加法单元 `add`

`alu/add.v`：

```verilog
module add (a,b,c,g,p,s);
    input  a,b,c;
    output g,p,s;
    assign s = a ^ b ^ c;
    assign g = a & b;
    assign p = a | b;
endmodule
```

含义：

- `s = a ^ b ^ c`：当前位的和。
- `g = a & b`：产生进位 generate。只要 `a` 和 `b` 都是 1，本位一定向高位产生进位。
- `p = a | b`：传递进位 propagate。只要 `a` 或 `b` 有一个是 1，低位来的进位就有可能传到高位。

注意：有些教材把传递信号定义为 `a ^ b`，这里代码使用的是 `a | b`。在配套的进位公式中，这种写法仍然可以工作，因为当 `g=1` 时本位已经必然产生进位，`p` 是否也为 1 不会破坏 `c_out = g | p & c_in` 的结果。

### 7.2 两位 CLA `cla_2`

`alu/cla_2.v` 中例化了两个一位加法单元：

```verilog
add add0 (a[0],b[0],c_in,g[0],p[0],s[0]);
add add1 (a[1],b[1],c_out,g[1],p[1],s[1]);
g_p g_p0 (g,p,c_in,g_out,p_out,c_out);
```

数据含义：

- `add0` 计算第 0 位。
- `g_p` 根据第 0 位的 `g[0]`、`p[0]` 和 `c_in` 计算第 1 位需要的进位 `c_out`。
- `add1` 使用 `c_out` 计算第 1 位。
- 同时，`g_p` 还会给整个 2 位小组生成组产生信号 `g_out` 和组传递信号 `p_out`。

### 7.3 组进位模块 `g_p`

`alu/g_p.v`：

```verilog
assign g_out = g[1] | p[1] & g[0];
assign p_out = p[1] & p[0];
assign c_out = g[0] | p[0] & c_in;
```

这三行是 CLA 的核心：

- `c_out`：低半组向高半组提供的进位。
- `g_out`：整个 2 组是否不依赖输入进位就能产生进位。
- `p_out`：整个 2 组是否能把输入进位一路传出去。

助教可以从 `c_out` 讲起：

```text
c_out = g[0] | (p[0] & c_in)
```

含义是：

- 如果低位自己产生进位 `g[0]=1`，则高位进位为 1。
- 如果低位能传递进位 `p[0]=1`，且输入进位 `c_in=1`，则高位进位也为 1。

### 7.4 分层构造 32 位加法器

后续模块按 2 倍宽度层层拼接：

```text
add -> cla_2 -> cla_4 -> cla_8 -> cla_16 -> cla_32 -> cla32
```

每一级的结构都很相似。例如 `cla_8`：

```verilog
cla_4 cla0 (a[3:0],b[3:0],c_in,g[0],p[0],s[3:0]);
cla_4 cla1 (a[7:4],b[7:4],c_out,g[1],p[1],s[7:4]);
g_p g_p0 (g,p,c_in,g_out,p_out,c_out);
```

它的思路是：

- 用低 4 位 CLA 计算 `s[3:0]`。
- 用 `g_p` 计算高 4 位需要的进位 `c_out`。
- 用高 4 位 CLA 计算 `s[7:4]`。
- 再输出整个 8 位组的 `g_out` 和 `p_out`。

`cla32.v` 是最外层封装：

```verilog
cla_32 cla (a,b,ci,g_out,p_out,s);
assign co = g_out | p_out & ci;
```

其中 `co` 是 32 位加法器的最终进位输出。当前 `addsub32` 例化 `cla32` 时没有使用 `co`，因为 ALU 当前只关心 32 位结果 `s`，没有把溢出或进位标志输出到顶层。

### 7.5 为什么要讲 CLA

如果用普通串行进位加法器，低位进位要一级一级传到高位，延迟较大。CLA 的思想是预先计算组产生和组传递信号，让进位更快地被推导出来。

本实验中，学生不一定要手推完整 32 位 CLA 公式，但至少要理解：

- `g` 表示本位或本组能否产生进位。
- `p` 表示本位或本组能否传递进位。
- 多级 `cla_*` 是用小加法器搭出大加法器。
- `addsub32` 使用同一个 CLA 同时支持加法和减法。

## 8. 移位通路讲解

`alu/shift.v`：

```verilog
module shift (d,sa,right,arith,sh);
     input [31:0] d;
     input [4:0] sa;
     input       right,arith;
     output [31:0] sh;
     reg [31:0]    sh;
     always @* begin
          if (!right) begin
              sh = d << sa;
          end else if (!arith) begin
              sh = d >> sa;
          end else begin
              sh = $signed(d) >>> sa;
          end
     end
endmodule
```

端口说明：

| 端口 | 作用 |
| --- | --- |
| `d` | 被移位的数据。ALU 中连接的是 `b`。 |
| `sa` | shift amount，移位位数。ALU 中连接的是 `a[4:0]`。 |
| `right` | 是否右移。0 表示左移，1 表示右移。 |
| `arith` | 右移时是否算术右移。 |
| `sh` | 移位结果。 |

三种情况：

1. `right=0`：执行逻辑左移 `d << sa`。
2. `right=1` 且 `arith=0`：执行逻辑右移 `d >> sa`，高位补 0。
3. `right=1` 且 `arith=1`：执行算术右移 `$signed(d) >>> sa`，高位补符号位。

特别注意：

- 算术右移只有在最高位为 1 的负数补码数据上，才明显区别于逻辑右移。
- 复位样例中 `b=0x0000000B` 是正数，所以逻辑右移和算术右移的结果都为 0。
- 如果要课堂演示两者差异，可以让学生思考 `b=0x80000000` 右移时会发生什么，但不要把它作为当前工程的正式新增实验步骤。

## 9. 多路选择器讲解

### 9.1 `mux4x32`

`alu/mux4x32.v`：

```verilog
function  [31:0] select;
    input [31:0] a0,a1,a2,a3;
    input [1:0] s;
    case  (s)
        2'b00: select = a0;
        2'b01: select = a1;
        2'b10: select = a2;
        2'b11: select = a3;
    endcase
endfunction
assign y = select(a0,a1,a2,a3,s);
```

这是一个 4 选 1 组合逻辑模块。ALU 里把它用于最终结果选择：

```text
a0 = d_as
a1 = d_and_or
a2 = d_xor_lui
a3 = d_sh
s  = aluc[1:0]
y  = r
```

因此，`aluc[1:0]` 是 ALU 的一级大类选择信号。

### 9.2 `mux2x32` 和 `mux2x5`

这两个模块当前没有在 `alu.v` 主数据通路中直接使用：

```verilog
assign y = s? a1 : a0;
```

它们是常见的 2 选 1 多路选择器模板。可以在讲解时简单带过：工程中保留了这些通用模块，但当前 ALU 的核心选择主要由条件运算符和 `mux4x32` 完成。

## 10. SignalTap 实验流程

本实验的关键不是看 LED，而是用 SignalTap 观察 FPGA 内部信号。

### 10.1 打开工程

1. 启动 Quartus。
2. 选择 `File -> Open Project`。
3. 打开 `DE1_SOC_golden_top.qpf`。
4. 确认顶层实体是 `DE1_SOC_golden_top`。
5. 打开 `DE1_SOC_golden_top.v` 和 `alu/alu.v`，确认顶层例化的是 `alu alu_inst`。

### 10.2 检查器件和源文件

在 Quartus 中检查：

1. `Assignments -> Device`：
   - Family 应为 Cyclone V。
   - Device 应为 `5CSEMA5F31C6`。
2. `Project -> Add/Remove Files in Project`：
   - 确认 ALU 相关文件已经列入工程。
   - 如果看到 `alu/regfile.v` 和 `alu/dff32.v` 缺失，要向学生解释这是当前工程文件列表中的历史遗留引用。

如果只是使用已有 `output_files/DE1_SOC_golden_top.sof` 下载观察，可以先不重新编译。如果需要重新编译，则必须处理缺失文件引用问题。

### 10.3 编译工程

若工程文件完整，可执行：

1. 点击 `Processing -> Start Compilation`。
2. 编译成功后，在 `output_files/` 中应生成或更新：
   - `DE1_SOC_golden_top.sof`
   - `DE1_SOC_golden_top.flow.rpt`
   - `DE1_SOC_golden_top.fit.summary`
   - `DE1_SOC_golden_top.sta.summary`

当前仓库已有一次成功编译的输出文件。报告中显示：

- Flow Status：Successful。
- Logic utilization：`2,048 / 32,070 ALMs`。
- Total registers：`5581`。
- Total pins：`70 / 457`。
- SignalTap 使用文件：`stp1.stp`。
- SignalTap sample depth：`256`。

### 10.4 下载 `.sof`

1. 用 USB-Blaster 连接 DE1-SoC 开发板。
2. 打开 `Tools -> Programmer`。
3. Hardware Setup 中选择 USB-Blaster。
4. 添加或确认编程文件：
   - `output_files/DE1_SOC_golden_top.sof`
5. 勾选 `Program/Configure`。
6. 点击 `Start` 下载。

`.sof` 是 SRAM Object File，下载后配置会保存在 FPGA 的易失性配置存储中，开发板断电后配置会丢失。这适合实验调试。

### 10.5 打开 SignalTap

1. 打开 `Tools -> SignalTap II Logic Analyzer`。
2. 打开当前工程中的 `stp1.stp`。
3. 确认 JTAG Chain 能识别到 DE1-SoC。
4. 确认 `.sof` 文件指向：
   - `output_files/DE1_SOC_golden_top.sof`
5. 确认采样时钟：
   - `CLOCK_50`
   - 上升沿采样。
6. 确认采样深度：
   - 256。

`stp1.stp` 中已经配置了大量观测信号，包括：

- `KEY[0]`
- `SW[4]`
- `alu:alu_inst|a[31..0]`
- `alu:alu_inst|b[31..0]`
- `alu:alu_inst|aluc[3..0]`
- `alu:alu_inst|r[31..0]`
- `alu:alu_inst|z`
- `alu:alu_inst|d_and[31..0]`
- `alu:alu_inst|d_or[31..0]`
- `alu:alu_inst|d_xor[31..0]`
- `alu:alu_inst|d_and_or[31..0]`
- `alu:alu_inst|d_xor_lui[31..0]`
- `alu:alu_inst|d_as[31..0]`
- `alu:alu_inst|d_sh[31..0]`
- `alu:alu_inst|addsub32:as32|a[31..0]`
- `alu:alu_inst|addsub32:as32|b[31..0]`
- `alu:alu_inst|addsub32:as32|s[31..0]`

如果 SignalTap 显示节点无效，可能是重新综合后节点名变化、信号被优化、或者使用的 `.sof` 与 `.stp` 不匹配。应重新运行 SignalTap 的节点查找，或重新编译并确保 `.sof` 与当前工程一致。

### 10.6 推荐观察步骤

实验观察建议分为三轮。

第一轮：固定输入，观察不同运算。

1. 设置 `SW[4]=0`。
2. 按下 `KEY[0]`，保持一小段时间。
3. 松开 `KEY[0]`。
4. 在 SignalTap 中采样，确认：
   - `a = 0x0000000A`
   - `b = 0x0000000B`
5. 依次设置 `SW[3:0]` 为不同 `aluc`。
6. 每切换一次，重新采样或观察波形变化。
7. 记录 `r` 和 `z`。

第二轮：观察中间通路。

1. 保持 `SW[4]=0`，固定 `a` 和 `b`。
2. 对比 `d_as`、`d_and_or`、`d_xor_lui`、`d_sh`。
3. 改变 `aluc[1:0]`，观察最终 `r` 从哪个中间通路选出。
4. 改变 `aluc[2]`，观察：
   - `d_as` 从加法变为减法。
   - `d_and_or` 从 AND 变为 OR。
   - `d_xor_lui` 从 XOR 变为 LUI。
   - `d_sh` 从左移变为右移。

第三轮：动态输入观察。

1. 设置 `SW[4]=1`。
2. 观察 `a` 每个时钟加 1。
3. 观察 `b` 每个时钟加 3。
4. 固定一个 `aluc`，观察 `r` 随输入变化。
5. 如果数据变化太快，可以回到 `SW[4]=0`，重新复位后做静态观察。

## 11. 复位样例结果表

复位后：

```text
a = 0x0000000A = 10
b = 0x0000000B = 11
sa = a[4:0] = 10
```

此时各 `aluc` 的期望结果如下：

| `aluc` | 运算 | 手工计算 | 期望 `r` | 期望 `z` |
| --- | --- | --- | --- | --- |
| `0000` | ADD | `0xA + 0xB = 0x15` | `0x00000015` | 0 |
| `0001` | AND | `0xA & 0xB = 0xA` | `0x0000000A` | 0 |
| `0010` | XOR | `0xA ^ 0xB = 0x1` | `0x00000001` | 0 |
| `0011` | SLL | `0xB << 10 = 0x2C00` | `0x00002C00` | 0 |
| `0100` | SUB | `0xA - 0xB = -1` | `0xFFFFFFFF` | 0 |
| `0101` | OR | `0xA | 0xB = 0xB` | `0x0000000B` | 0 |
| `0110` | LUI | `{16'h000B, 16'h0000}` | `0x000B0000` | 0 |
| `0111` | SRL | `0xB >> 10 = 0` | `0x00000000` | 1 |
| `1000` | ADD | `aluc[3]` 对 ADD 无影响 | `0x00000015` | 0 |
| `1001` | AND | `aluc[3]` 对 AND 无影响 | `0x0000000A` | 0 |
| `1010` | XOR | `aluc[3]` 对 XOR 无影响 | `0x00000001` | 0 |
| `1011` | SLL | 左移时 `arith` 无影响 | `0x00002C00` | 0 |
| `1100` | SUB | `aluc[3]` 对 SUB 无影响 | `0xFFFFFFFF` | 0 |
| `1101` | OR | `aluc[3]` 对 OR 无影响 | `0x0000000B` | 0 |
| `1110` | LUI | `aluc[3]` 对 LUI 无影响 | `0x000B0000` | 0 |
| `1111` | SRA | `$signed(0xB) >>> 10 = 0` | `0x00000000` | 1 |

助教可以让学生先手工填这张表，再用 SignalTap 验证。这样学生会把 Verilog 代码、控制码、硬件波形和二进制运算联系起来。

## 12. 本实验与计算机组成原理的关系

本实验可以连接到课程中的多个知识点：

| 课程知识点 | 本实验对应位置 |
| --- | --- |
| 补码加减法 | `addsub32` 中 `b^{32{sub}}` 和初始进位 `sub`。 |
| 加法器设计 | `add`、`g_p`、`cla_*` 分层结构。 |
| 组合逻辑 | `alu.v` 中逻辑运算、移位、多路选择器。 |
| 控制信号 | `aluc[3:0]` 对不同数据通路的控制。 |
| 数据通路 | ALU 内部候选结果和最终选择。 |
| 标志位 | `z = ~|r`。 |
| FPGA 调试 | SignalTap 片上逻辑分析仪。 |

因此，本实验不是单纯写 Verilog，而是帮助学生把“课程里的 ALU 框图”对应到真实硬件工程。




## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_计算机组成原理_课程MOC|计算机组成原理 MOC]]
