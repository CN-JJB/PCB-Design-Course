# 第三章 层次化原理图与 ERC：组织大设计与质量把关

> 本章目标：掌握层次图设计法，让几十页的原理图井井有条；吃透 ERC 每类警告的含义与处理策略；完成标注、BOM 输出等收尾工作。

---

## 3.1 为什么需要层次化

单页原理图的舒适上限约 50~80 个元件。超过之后：

- 连线像意大利面，改一处牵全身
- 找元件靠 Ctrl+F 碰运气
- 多人协作无法分工

解决方案就是软件工程里的老思想——**分而治之**：

```
根图 Root Sheet
┌──────────────────────────────┐
│  [电源模块]──[主控模块]        │   ← 每个模块是一个"黑盒"
│      │          │            │     (Sheet Symbol)
│      ▼          ▼            │
│  [存储模块]  [接口模块]        │
└──────────────────────────────┘
    │双击黑盒展开子图
    ▼
┌────────────┐
│ 子图: 电源  │  内部是完整电路细节
│ AMS1117... │
└────────────┘
```

三层结构对应三种规模：

| 规模 | 做法 |
|------|------|
| 小 (<60 元件) | 单页即可 |
| 中 (60~300) | 一层层次：根图+若干子图 |
| 大 (>300) | 多层嵌套或每功能域一页平铺+全局标签 |

---

## 3.2 层次图核心操作（KiCad 9）

### 创建子图

```
① 根图中：Place → Add Sheet(放置→图纸符号)，快捷键 S
② 拖出矩形框 → 弹窗输入子图文件名 power.kicad_sch 和显示名 "电源"
③ 双击该 Sheet Symbol → 进入子图编辑（自动新建）
④ 在子图里照常画电路
```

### 三种连接标签——必须彻底分清

| 标签 | 快捷键 | 作用范围 | 典型用途 |
|------|--------|---------|---------|
| Local Label 本地标签 | L | 仅当前页面 | 页内远距离连接 |
| Hierarchical Label 层次标签 | H | 穿透 Sheet 边界 | **父子图之间的信号口** |
| Global Label 全局标签 | Ctrl+L? （Place→Global Label） | 所有同名跨全工程 | 电源轨、I2C 总线等全局信号 |

层次标签的工作机制：

```
父图 Sheet Symbol 的边界上放 "Sheet Pin"(自动从子图的H标签生成)
                │
子图内部对应位置必须有同名的 Hierarchical Label
                │
两者配对成功 = 这条信号穿过图纸边界连通
```

操作流：

```
① 子图里画好电路，在需要对外连接的网络上按 H 放置层次标签，
   如 "+5V"、"USB_DP"
② 回到根图，右键 Sheet Symbol → Import Sheet Pin / 
   或 Place → Add Sheet Pin 手动放置——标签会出现在框边上
③ 从 Sheet Pin 拉线连接其他模块
```

> 【选择原则】能用层次标签就不用全局标签。全局标签虽然省事，但破坏了模块的封装性——你永远不知道哪个角落的页面还有一根同名线。只有真正全局性的东西（电源轨、总线、时钟）才用 Global Label。

### 实战改造：把 STM32 最小系统改成层次结构

```
root.kicad_sch（根图）
 ├── power.kicad_sch      USB→AMS1117→3V3
 │     对外: +5V, +3V3 (用 Global Label 因为全工程共享)
 ├── mcu.kicad_sch        F103 本体+去耦阵
 │     对外: NRST, OSC_IN/OUT, SWDIO, SWCLK (Hierarchical Label)
 ├── clock_reset.kicad_sch 8MHz晶振+复位RC
 └── debug_boot.kicad_sch  SWD排针+BOOT下拉
```

改造完成后跑 ERC 验证连通性无损。

---

## 3.3 跨页连接的其他技巧

### 直接连接 Direct Connection

KiCad 支持 Off-page connector 风格——不同页之间直接用同名网络标号连接（默认行为：Local Label 不跨页！必须用 Global Label 或层次结构）。

> 【易错点】很多从 Altium 转来的同学习惯"网络标号全局生效"。KiCad 里普通 Label 是页内作用域，跨页必须 Global 或层次。这是两软件最大的心智差异之一。

### 电源符号的特殊性

power 库符号（GND/+3V3 等）本质上是预定义的全局标签，天然跨页连通。这就是为什么电源从来不用画长线。

---

## 3.4 总线的完整用法

以 8 位数据总线为例：

```
① 画总线：Place → Add Bus（快捷键 B），画一条粗斜线段
② 分支：每个成员网络处 Place → Bus Entry（总线入口），
        形成斜向短线接入总线
③ 命名：总线上放标签 "D[0..7]"（方括号区间语法）
④ 成员：每个入口处的单线上放本地标签 D0、D1…D7
⑤ 跨页传总线：Sheet Pin + Hierarchical Label 同名 D[0..7]
```

注意：**真正决定电气连接的是成员网络名（D0~D7），总线只是视觉容器**。忘放成员标签=断路且不报错，是总线最阴险的坑。

---

## 3.5 ERC 完全指南

Inspect → Electrical Rules Checker。ERC 是你的免费质检员，态度应该是：**每条警告都要能解释清楚为什么放过它**。

### 主要检查项分类解读

| 错误类型 | 含义 | 处理策略 |
|---------|------|---------|
| pin not connected | 引脚悬空无标记 | 真不用→加 no-connect(Q)；要用→连线 |
| Input Power not driven | 电源输入脚没有源 | 确认供电逻辑后降级为忽略；否则补电源 |
| pin to pin conflict | 引脚类型冲突(如 out-out) | 99% 是真错误，逐个查 |
| similar labels | 标签名相似易混(+3V3 vs +3V33) | 统一命名规范 |
| unannotated | 未标注位号 | 跑 Annotate |
| footprint missing | 符号没分配封装 | 第四章解决 |
| units conflict | 多单元符号使用不一致 | 检查 U1A/U1B 用法 |

### Severity（严重性）调级的原则

File → Board Setup？不对——原理图侧路径：Inspect → ERC → Violation Severities 标签页。

| 该升为 Error 的 | 可以降为 Ignore 的 |
|---------------|-------------------|
| 未连接引脚（配合 no-connect 使用）| 已确认的 power drive 结构性提示 |
| 引脚类型冲突 | 特定厂商符号的固有类型问题 |

红线原则：**Ignore 只允许用于"我理解并接受"的情况**，禁止为了图清净把所有警告一键静音——那等于拆掉烟雾报警器。

### 一个真实的排查案例

```
现象：ERC 报 PA13 "pin not driven"
分析：PA13 是 MCU 的双向 IO(SWDIO)，
     连到排针。Input 类型悬空误报？
处理：把排针引脚类型改为 Passive，
     或给该网络加 no-connect 变通……
正解：这类 MCU IO 口接连接器的场景，
     将连接器符号引脚类型改为 Passive 后警告消失。
```

经验：ERC 报警时先看引脚两端类型，再判断是电路真错还是符号类型定义不当。

---

## 3.6 收尾三件套：Annotate、BOM、网表状态

### 标注复查

Tools → Annotate：即使新版自动标注，大改动后手动重跑一遍保证连续性。选项 Keep existing 保持已有序号，只补新洞。

### BOM 导出

File → Export → BOM（文件→导出→物料清单）：

- KiCad 9 提供 BOM 编辑器模板（xsl/csv 配置）
- 推荐输出列：Reference, Value, Footprint, Quantity
- 中文采购场景建议加一列备注（立创商城编号 LCSC Part#）

BOM 的职业写法示例：

```
Ref     Value        Footprint              Qty  备注
C1-C4   100nF        C_0603_1608Metric       4   X7R 50V 立创C14663
C5      10μF         C_0805_2012Metric       1   X5R 16V
R1,R2   10kΩ         R_0603_1608Metric       2   1%
U1      STM32F103C8T6 LQFP-48               1   ST原装
Y1      8MHz         Crystal_SMD_3225        1   CL=20pF
```

### 网表去哪了？

KiCad 新版不再需要显式导出网表文件——PCB 编辑器的 Tools → Update PCB from Schematic 直接读取原理图同步。老教程里的 netlist 文件流程已过时。

---

## 3.7 设计评审自查清单

提交 PCB 阶段前，原理图应通过以下检查：

```
[ ] 电源树清晰：每路电压来源、去向、电流估算都明确
[ ] 每个 IC 的 datasheet 应用电路核对过一遍
[ ] 所有 VDD/VDDA 都有去耦电容
[ ] 复位/BOOT/EN 等配置脚都有确定电平
[ ] 晶振负载电容值与 CL 匹配
[ ] 所有未用引脚有 no-connect 或确定接法
[ ] 网络名语义化且无拼写不一致(如 GND/gnd)
[ ] ERC 无未解释的警告
[ ] 位号连续无重复
[ ] BOM 导出正常，关键器件有采购渠道确认
[ ] 图纸分区注释完整，三个月后的自己能看懂
```

---

## 3.8 自检与实践

自检：

1. Local/Hierarchical/Global 三种标签的作用范围和适用场景？
2. 总线里真正决定连接的是什么？最常见的总线翻车是什么？
3. KiCad 与 Altium 在网络标号作用域上的最大差异？
4. 哪些 ERC 项可以合理忽略？哪些绝对不行？
5. BOM 至少要包含哪几列？

实践作业：

1. 把 STM32 最小系统重构为 4 个子图的层次结构
2. 故意制造三个错误（拔掉一颗去耦电容的地线、两个 output 对接、漏一个 no-connect），观察 ERC 如何捕获它们，再修复
3. 导出一份带立创编号列的 BOM

下一章《封装分配与检查清单》完成后，原理图阶段毕业。
