# 🚀 START HERE｜PCB 课程闯关入口

> 如果你第一次打开这个仓库，**不要先在几十个 Markdown 文件之间跳转**。从本页开始，按 Gate 顺序做。每一关都只有五件事：**做什么 → 看什么 → 产出什么 → 通过标准 → 下一关**。

## 先选路线

### 路线 A｜MCU 主线（推荐）

```text
Gate 0  前置能力检查
  ↓
Gate 1  Part 0：二层 → 多层认知升级
  ↓
Gate 2  STM32F407 V1：第一块四层板
  ↓
Gate 3  Part 2/3/4：SI + PI + EMC
  ↓
Gate 4  STM32F407 V2：四层综合毕业板
  ↓
Gate 5  Part 6：四层 → 六层
  ↓
Gate 6  STM32H743 V3：六层高速综合
  ↓
Gate 7  Part 9：工程交付与量产化
```

### 路线 B｜FPGA 专项副线

先完成 MCU 路线的 Gate 0～5，至少具备多层 / SI / PI / EMC 基础，然后进入：

```text
Artix-7 V1：Bank → Power → BGA → DDR3 → GTP → Bring-up
  ↓
Part 9：工程交付
```

---

# Gate 0｜我能不能开始？

## 你要做什么

确认自己已经能独立完成一个二层板：

- 原理图；
- PCB；
- ERC / DRC；
- Gerber；
- 基本上电；
- 万用表测量；
- 能查 datasheet。

## 通过标准

下面全部能做到才通过：

- [ ] 能从零建立一个 KiCad 工程；
- [ ] 能正确处理基本电源、去耦、晶振、复位、调试接口；
- [ ] 能完成二层板布局布线并导出制造文件；
- [ ] 知道为什么要做 ERC / DRC，而不只是会点击按钮；
- [ ] 上电前会做短路/电阻检查，并使用限流电源。

### 没通过？

先复习：

- [01_零基础入门](01_零基础入门/)
- [02_原理图设计](02_原理图设计/)
- [03_二层板实战](03_二层板实战/)

### 通过以后

→ 进入 [Gate 1：Part 0](10_Part0_从二层到多层/00_本Part导读.md)

---

# Gate 1｜Part 0：先升级思维，不急着画四层板

## 你要做什么

按顺序完成 Part 0 的 5 章，建立：

- reference plane；
- return path；
- edge rate；
- propagation delay；
- datasheet → PCB constraint；
- KiCad 10 多层规则意识。

## 通过标准

不看答案，你能解释：

1. 为什么高速不能只看 MHz？
2. 一条信号的 return path 在哪里？
3. 换层为什么可能改变 reference？
4. 为什么 L2 solid GND 有价值？
5. 如何从 datasheet 找到 PCB requirement？

全部能回答，才进入下一关。

### 下一步

→ [Gate 2：STM32F407 V1 闯关入口](projects/stm32f407-mainline/v1/START_HERE.md)

---

# Gate 2｜STM32F407 V1：第一块四层板

不要直接打开 KiCad 开始摆器件。

从项目唯一入口开始：

→ **[STM32F407 V1 START HERE](projects/stm32f407-mainline/v1/START_HERE.md)**

完成标准：从需求冻结一路做到 schematic、stackup、placement、routing、release、bring-up，每一关都有工程文件作为证据。

---

# Gate 3｜SI + PI + EMC 理论升级

V1 完成后依次学习：

1. [Part 2｜Signal Integrity](12_Part2_信号完整性/00_本Part导读.md)
2. [Part 3｜Power Integrity](13_Part3_电源完整性/00_本Part导读.md)
3. [Part 4｜EMI / EMC](14_Part4_EMI_EMC/00_本Part导读.md)

## 通过标准

你必须能从同一条网络同时回答：

- SI：信号怎么传播、参考是什么、哪里会反射/串扰？
- PI：切换电流从哪里来、PDN/去耦/IR Drop 怎么验证？
- EMC：source、coupling path、antenna/common-mode path 在哪里？

### 下一步

→ [Gate 4：STM32F407 V2 闯关入口](projects/stm32f407-mainline/v2/START_HERE.md)

---

# Gate 4｜STM32F407 V2：四层综合毕业板

V2 把 USB FS、CAN、SDIO、SI、PI、EMC 放回同一块四层板。

唯一入口：

→ **[STM32F407 V2 START HERE](projects/stm32f407-mainline/v2/START_HERE.md)**

完成标准：不是“线布完”，而是 System Spec、Pin/Clock、Schematic Review、Placement、Rules、Routing、SI/PI/EMC Joint Review、DFM、Release、Bring-up、Final Review 全部过 Gate。

---

# Gate 5｜Part 6：决定为什么要六层

学习：

→ [Part 6｜四层到六层](16_Part6_四层到六层/00_本Part导读.md)

## 通过标准

你能用工程约束解释：

- 为什么 4 层不够；
- 为什么 6 层够；
- 什么情况下应该直接上 8 层；
- 每个 signal layer 的 reference；
- layer transition 怎么处理；
- stackup 如何与板厂冻结。

### 下一步

→ [Gate 6：STM32H743 V3](projects/stm32h7-mainline/v3/START_HERE.md)

---

# Gate 6｜STM32H743 V3：六层高速综合

唯一入口：

→ **[STM32H743 V3 START HERE](projects/stm32h7-mainline/v3/START_HERE.md)**

完成标准：SDRAM timing 从 ns → cycles → ps/mm → PCB route → stress test；Ethernet 从 PHY/RMII → magnetics/MDI → cable/chassis → bring-up，全链可解释。

---

# FPGA Gate｜Artix-7 V1

如果走 FPGA 副线：

→ **[Artix-7 V1 START HERE](projects/artix7-mainline/v1/START_HERE.md)**

不要直接从 DDR3 或 GTP 开始。顺序固定为 Device/Package → Bank → Power → Config/Clock → BGA → DDR3/MIG → GTP → Tool Sync → Bring-up。

---

# Gate 7｜工程交付

设计验证完成后进入：

→ [Part 9｜工程交付与量产化](19_Part9_工程交付与量产化/00_本Part导读.md)

最终要交付的不是一张 PCB，而是一套能复现的：

```text
source
+ exact BOM
+ fabrication package
+ assembly package
+ firmware/bitstream
+ test evidence
+ ECO/revision
+ release manifest
```

---

# 闯关规则

每一关都遵守：

> **没有产出物，不算做过；没有通过标准，不进入下一关。**

遇到 `TBD` 不等于失败。真正的失败是：不知道它为什么是 TBD，却继续往下做。
