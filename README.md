# PCB 设计教材｜从二层板到四层 / 六层高速板

> 面向**已经会画二层板**的学习者：通过一条持续升级的 MCU 项目主线，系统学习 4 层 / 6 层 PCB、Signal Integrity（SI）、Power Integrity（PI）、EMI/EMC、DFM、测量与 Design Review。

这套教材不以“背规则”为目标，而是训练你从**电流路径、电磁场、器件要求、接口规范和制造约束**解释每一个关键 PCB 决策。

```text
现象 → 建立直觉 → SVG / 互动实验 → 物理原因 → 必要公式
→ KiCad 实操 → 修改主线 PCB → Fault Lab → Design Review → 实测 / 验证
```

---

# 当前课程进度

| Part | 状态 | 主题 | 主线产出 |
|---|---|---|---|
| 0 | ✅ | 二层 → 多层认知跃迁 | 能分析 reference / return / edge rate |
| 1 | ✅ | 第一块四层板 | STM32F407 V1 |
| 2 | ✅ | Signal Integrity | V2 SI upgrade |
| 3 | ✅ | Power Integrity | V2 PI upgrade |
| 4 | ✅ | EMI / EMC | V2 interface / ESD / pre-compliance |
| 5 | ✅ | 四层综合 | STM32F407 V2：USB / CAN / SDIO 综合收口 |
| 6 | ✅ | 四层 → 六层 | Layer-count / stackup / reference / 多电源域 / H7 transition |
| 7 | ✅ | 六层高速 | STM32H743 V3 + SDRAM + Ethernet 工程闭环 |
| 8 | ⏭️ | FPGA 专项 | Bank / BGA fanout / clock / DDR / pin planning |
| 9 | ⏭️ | 工程交付 | DFM / 测量 / 调试 / BOM / 量产 |

---

## ✅ Part 0｜从二层板到多层板：认知升级

**[开始学习](10_Part0_从二层到多层/00_本Part导读.md)**

重点：PCB 互连不是理想导线、Return Path / Reference Plane、edge rate / flight time、从 Datasheet 提取 PCB 规则、KiCad 9 多层基础。

互动：[Edge Rate Lab](interactive/edge-rate-lab.html)

---

## ✅ Part 1｜第一块真正的四层板：STM32F407 V1

**[开始项目](11_Part1_STM32F407四层板/00_项目导读.md)**

```text
需求 → power tree / schematic → 四层 stackup → placement → routing
→ DRC + manual review → Gerber → bring-up
```

项目资产：[`projects/stm32f407-mainline/v1/`](projects/stm32f407-mainline/v1/)

---

## ✅ Part 2｜Signal Integrity：STM32F407 V1 → V2

**[开始学习 SI](12_Part2_信号完整性/00_本Part导读.md)**

```text
波传播 → transmission line / Z0 → reflection / termination
→ return path / layer transition → crosstalk → differential pair / USB FS
→ TDR / eye / oscilloscope → KiCad SI Review
```

互动：[Reflection Lab](interactive/reflection-lab.html) · [Return Path Lab](interactive/return-path-lab.html) · [Crosstalk Lab](interactive/crosstalk-lab.html)

V2 SI：[`projects/stm32f407-mainline/v2/si-review.md`](projects/stm32f407-mainline/v2/si-review.md)

---

## ✅ Part 3｜Power Integrity：从“有 3.3 V”到“PDN 可解释”

**[开始学习 PI](13_Part3_电源完整性/00_本Part导读.md)**

```text
瞬态电流 → local decoupling → C / ESR / ESL / SRF / DC Bias
→ mounting inductance → PDN / target impedance → anti-resonance
→ plane / ground bounce → Buck hot loop → measurement integrity → KiCad PI Review
```

互动：[Decoupling Impedance Lab](interactive/decoupling-impedance-lab.html) · [Target Impedance Lab](interactive/target-impedance-lab.html) · [Buck Hot Loop Lab](interactive/buck-hot-loop-lab.html)

---

## ✅ Part 4｜EMI / EMC：从板内电流到电缆、机壳与外部世界

**[开始学习 EMI / EMC](14_Part4_EMI_EMC/00_本Part导读.md)**

```text
Differential / Common Mode → loop / slot / cable
→ connector electromagnetic boundary → ESD / TVS current path
→ shield / chassis / system GND → USB / CAN EMC
→ near-field / cable A-B experiments → KiCad EMC Review
```

互动：[ESD Layout Lab](interactive/esd-layout-lab.html) · [Common-Mode Cable Lab](interactive/common-mode-cable-lab.html)

---

# ✅ Part 5｜STM32F407 V2 四层综合板

**[开始四层综合项目](15_Part5_四层综合/00_本Part导读.md)**

<p align="center"><img src="assets/svg/v2-part5-overview.svg" width="980" alt="Part 5 STM32F407 V2 四层综合项目总览"></p>

Part 5 把 **SI + PI + EMC** 压回同一块四层 PCB：

```text
System Specification → Pin / Clock Planning → Schematic Review
→ Placement / Board Zoning → Stackup / Rule Matrix → Routing Priority
→ SI + PI + EMC Joint Review → DFM / BOM / Testability
→ Gerber / Release Gate → Bring-up / Validation → Final Design Review
```

项目资产：[`projects/stm32f407-mainline/v2/`](projects/stm32f407-mainline/v2/)

互动：[V2 Layout Tradeoff Lab](interactive/v2-layout-tradeoff-lab.html) · [V2 Release Gate Lab](interactive/v2-release-gate-lab.html)

---

# ✅ Part 6｜从四层升级到六层：重新组织电磁结构

**[开始学习 Part 6](16_Part6_四层到六层/00_本Part导读.md)**

<p align="center"><img src="assets/svg/part6-four-vs-six.svg" width="980" alt="Part 6 四层到六层设计压力"></p>

Part 6 不用接口名字机械决定层数，而是完成一次完整 **Layer-Count / Stackup Architecture Review**：

```text
四层真实瓶颈
→ Layer-Count Gate
→ 六层 Stackup 邻接关系
→ Signal Layer / Reference Plane 配对
→ GND↔GND / GND↔PWR Reference Transition
→ Power Domain / Plane Split
→ Routing Density / Escape / Via Forest
→ KiCad 9 六层规则
→ 板厂阻抗与 Stackup Freeze
→ STM32H743 V3 Transition Gate
```

核心章节：

- [四层板什么时候真的不够](16_Part6_四层到六层/01_四层板什么时候真的不够.md)
- [六层 Stackup 工程设计](16_Part6_四层到六层/02_六层Stackup工程设计.md)
- [Signal Layer 与 Reference Plane](16_Part6_四层到六层/03_SignalLayer与ReferencePlane配对.md)
- [换层与 Reference Transition](16_Part6_四层到六层/04_换层与ReferenceTransition.md)
- [Power Domain 与 Plane Split](16_Part6_四层到六层/05_PowerDomain与PlaneSplit规划.md)
- [Routing Density / Escape 与层数](16_Part6_四层到六层/06_RoutingDensity_Escape与层数.md)
- [KiCad 六层 Stackup 与规则](16_Part6_四层到六层/07_KiCad六层Stackup与规则落地.md)
- [板厂阻抗与 Stackup Freeze](16_Part6_四层到六层/08_板厂阻抗与StackupFreeze.md)
- [STM32H7 V3 过渡设计](16_Part6_四层到六层/09_STM32H7_V3过渡设计.md)
- [参考资料与数据纪律](16_Part6_四层到六层/10_参考资料与数据纪律.md)

互动：

- [Six-Layer Stackup Lab](interactive/six-layer-stackup-lab.html)
- [Reference Transition Lab](interactive/reference-transition-lab.html)

V3 过渡工程资产：[`projects/stm32h7-mainline/v3/`](projects/stm32h7-mainline/v3/)

- [Layer-Count Decision](projects/stm32h7-mainline/v3/layer-count-decision.md)
- [Stackup Decision Record](projects/stm32h7-mainline/v3/stackup-decision-record.md)
- [Layer Role Map](projects/stm32h7-mainline/v3/layer-role-map.md)
- [Reference Transition Map](projects/stm32h7-mainline/v3/reference-transition-map.md)
- [KiCad Rule Plan](projects/stm32h7-mainline/v3/kicad-rule-plan.md)
- [Part 6 → 7 Transition Review](projects/stm32h7-mainline/v3/part6-transition-review.md)
- [Part 6 Fault Lab](projects/stm32h7-mainline/fault-lab/part6-stackup-faults.md)

Part 6 使用 JLCPCB 当前公开的六层 controlled-impedance stackup 作为真实制造案例，但所有板厂参数在实际下单前重新核对。

---

# ✅ Part 7｜STM32H743 V3 六层高速综合板

**[开始 Part 7](17_Part7_STM32H7六层高速/00_本Part导读.md)**

<p align="center"><img src="assets/svg/part7-system-architecture.svg" width="980" alt="Part 7 STM32H743 V3 六层高速系统架构"></p>

硬件基线：

- STM32H743ZIT6 / LQFP144
- Alliance AS4C4M16SA-6TIN，x16 8 MiB SDR SDRAM
- FMC_SDCLK = 100 MHz project baseline
- LAN8742A/Ai 10/100 Ethernet PHY
- RMII 50 MHz
- 六层 controlled-impedance PCB

完整工程链：

```text
System / Pin / Power / Clock Freeze
→ SDRAM selection → FMC ns-to-cycle timing
→ board skew / routing constraints
→ RMII / PHY / MDI / Magnetics / RJ45
→ six-layer floorplan
→ SI + PI + EMC joint review
→ KiCad constraints
→ bring-up / stress / evidence
→ Final Design Review / Source Freeze
```

核心章节：

- [系统规格与资源冻结](17_Part7_STM32H7六层高速/01_V3系统规格与资源冻结.md)
- [H743 电源、时钟与启动](17_Part7_STM32H7六层高速/02_H743电源时钟与启动架构.md)
- [SDRAM 选型与 FMC 架构](17_Part7_STM32H7六层高速/03_SDRAM选型与FMC架构.md)
- [FMC 时序：ns → cycles](17_Part7_STM32H7六层高速/04_FMC时序从ns到寄存器.md)
- [SDRAM 板级时序与等长](17_Part7_STM32H7六层高速/05_SDRAM板级时序与等长.md)
- [Ethernet PHY / RMII](17_Part7_STM32H7六层高速/06_Ethernet_PHY与RMII架构.md)
- [Magnetics / RJ45 / ESD](17_Part7_STM32H7六层高速/07_Magnetics_RJ45与ESD边界.md)
- [六层 Floorplan 与布线顺序](17_Part7_STM32H7六层高速/08_六层Floorplan与布线顺序.md)
- [SI / PI / EMC 联合 Review](17_Part7_STM32H7六层高速/09_SI_PI_EMC联合Review.md)
- [KiCad 高速约束](17_Part7_STM32H7六层高速/10_KiCad高速约束与Review.md)
- [Bring-up 与故障定位](17_Part7_STM32H7六层高速/11_Bringup内存网络与故障定位.md)
- [Final Design Review](17_Part7_STM32H7六层高速/12_FinalDesignReview与六层毕业门槛.md)
- [参考资料与 Source Freeze](17_Part7_STM32H7六层高速/13_参考资料与SourceFreeze.md)

互动：

- [FMC Timing Lab](interactive/fmc-timing-lab.html)
- [SDRAM Skew Lab](interactive/sdram-skew-lab.html)
- [Ethernet Boundary Lab](interactive/ethernet-boundary-lab.html)

工程资产：[`projects/stm32h7-mainline/v3/`](projects/stm32h7-mainline/v3/)

Fault Lab：[Part 7 H7 / SDRAM / Ethernet Faults](projects/stm32h7-mainline/fault-lab/part7-h7-sdram-ethernet-faults.md)

**六层毕业标准：**不是把几十根线“调成绿色”，而是能从 datasheet timing、PCB delay、reference/return、PDN、connector boundary 和实测 evidence 解释每个关键决策。

---

# 下一阶段：Part 8｜FPGA 板级设计专项

Part 8 将把重心从 MCU 转向 FPGA board-level engineering：

```text
FPGA architecture / Bank / I/O standard
→ power rails / sequencing
→ clock tree
→ BGA fanout / escape
→ pin planning ↔ PCB co-design
→ DDR interface concepts
→ high-speed differential I/O
→ decoupling / PDN
→ configuration / JTAG
→ FPGA board bring-up
```

重点仍然是**板级设计**，不会把课程变成 HDL 编程教程。

---

# 主线产品家族

```text
STM32F407 V1 — 四层基本功
      ↓
STM32F407 V2 — USB / CAN / SDIO + SI / PI / EMC
      ↓
STM32H743 V3 — 六层 + Ethernet / SDRAM
```

另有 FPGA 板级设计专项。

---

# Fault Lab：故意画错，然后亲手修

每个 Fault 都要求：

```text
Symptom → Why DRC misses it → Current path / field / parasitic
→ Root cause → PCB change → Side effect → A/B verification → Checklist
```

课程训练的是**诊断能力**，不是背答案。

---

# 数字与规则的写作纪律

课程明确区分：物理原理、工程经验、器件厂家要求、接口/认证标准要求、板厂制造限制、系统设计目标和教学数量级示例。

不会把 `3W`、`≤1 mm`、`100 nF`、`TVS <5 mm`、固定 MHz 门槛等跨场景写成无条件铁律。

---

# 一手资料原则

教材优先使用 STM32 Datasheet / Reference Manual / Errata / Hardware Guide、接口规范、器件官方 Application Note、KiCad 官方文档和板厂实际 stackup / capability。

标准、器件、软件和板厂工艺会变化；**实际设计冻结前重新核对当前版本。**

---

# 最终学习目标

> **一块你能解释每个重要设计决策的六层板。**

别人问你为什么这样叠层、为什么这个电容放这里、为什么这根线换层、为什么接口这样保护、为什么 shield 这样接，你能从电流路径、电磁场、器件要求、系统结构和制造约束解释，而不是回答“网上都这么画”。