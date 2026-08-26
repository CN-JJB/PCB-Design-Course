# PCB 设计教材｜从二层板到四层 / 六层高速板

> 面向**已经会画二层板**的学习者：通过一条持续升级的 MCU 项目主线，系统学习 4 层 / 6 层 PCB、Signal Integrity（SI）、Power Integrity（PI）、EMI/EMC、DFM、测量与 Design Review。

这套教材不以“背规则”为目标，而是训练你从**电流路径、电磁场、器件要求、接口规范和制造约束**解释每一个关键 PCB 决策。

```text
现象
→ 建立直觉
→ SVG / 互动实验
→ 物理原因
→ 必要公式
→ KiCad 实操
→ 修改主线 PCB
→ Fault Lab
→ Design Review
→ 实测 / 验证
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
| 6 | ⏭️ | 四层 → 六层 | Stackup / reference / 多电源域 |
| 7 | ⏭️ | 六层高速 | STM32H7 + Ethernet + SDRAM |
| 8 | ⏭️ | FPGA 专项 | Bank / BGA fanout / clock / DDR / pin planning |
| 9 | ⏭️ | 工程交付 | DFM / 测量 / 调试 / BOM / 量产 |

---

## ✅ Part 0｜从二层板到多层板：认知升级

**[开始学习 Part 0](10_Part0_从二层到多层/00_本Part导读.md)**

重点：

- PCB 互连为什么不是理想导线
- Return Path / Reference Plane
- edge rate / flight time
- 从 Datasheet / Hardware Guide 提取 PCB 规则
- KiCad 9 多层设计必备操作

互动： [Edge Rate Lab](interactive/edge-rate-lab.html)

---

## ✅ Part 1｜第一块真正的四层板：STM32F407 V1

**[开始项目 Part 1](11_Part1_STM32F407四层板/00_项目导读.md)**

```text
需求 → power tree / schematic → 四层 stackup
→ placement → routing → DRC + manual review
→ Gerber → bring-up
```

项目资产：[`projects/stm32f407-mainline/v1/`](projects/stm32f407-mainline/v1/)

---

## ✅ Part 2｜Signal Integrity：STM32F407 V1 → V2

**[开始学习 SI](12_Part2_信号完整性/00_本Part导读.md)**

```text
波传播
→ transmission line / Z0
→ reflection / termination
→ return path / layer transition
→ crosstalk
→ differential pair / USB FS
→ TDR / eye / oscilloscope
→ KiCad SI Review
```

互动：

- [Reflection Lab](interactive/reflection-lab.html)
- [Return Path Lab](interactive/return-path-lab.html)
- [Crosstalk Lab](interactive/crosstalk-lab.html)

V2 SI：

- [SI Upgrade Plan](projects/stm32f407-mainline/v2/si-upgrade-plan.md)
- [SI Routing Constraints](projects/stm32f407-mainline/v2/si-routing-constraints.md)
- [SI Review](projects/stm32f407-mainline/v2/si-review.md)
- [SI Fault Lab](projects/stm32f407-mainline/fault-lab/part2-si-faults.md)

---

## ✅ Part 3｜Power Integrity：从“有 3.3 V”到“PDN 可解释”

**[开始学习 PI](13_Part3_电源完整性/00_本Part导读.md)**

```text
瞬态电流 → local decoupling
→ C / ESR / ESL / SRF / DC Bias
→ mounting inductance
→ PDN / target impedance
→ anti-resonance
→ plane / ground bounce
→ Buck hot loop
→ measurement integrity
→ KiCad PI Review
```

互动：

- [Decoupling Impedance Lab](interactive/decoupling-impedance-lab.html)
- [Target Impedance Lab](interactive/target-impedance-lab.html)
- [Buck Hot Loop Lab](interactive/buck-hot-loop-lab.html)

V2 PI：

- [PI Upgrade Plan](projects/stm32f407-mainline/v2/pi-upgrade-plan.md)
- [PI Rail Budget](projects/stm32f407-mainline/v2/pi-rail-budget.md)
- [PI Review](projects/stm32f407-mainline/v2/pi-review.md)
- [PI Fault Lab](projects/stm32f407-mainline/fault-lab/part3-pi-faults.md)

---

## ✅ Part 4｜EMI / EMC：从板内电流到电缆、机壳与外部世界

**[开始学习 EMI / EMC](14_Part4_EMI_EMC/00_本Part导读.md)**

```text
Differential / Common Mode
→ loop / slot / cable antenna structure
→ connector electromagnetic boundary
→ ESD / TVS current path
→ shield / chassis / system GND
→ USB / CAN interface EMC
→ near-field / cable A-B experiments
→ KiCad EMC Review
```

互动：

- [ESD Layout Lab](interactive/esd-layout-lab.html)
- [Common-Mode Cable Lab](interactive/common-mode-cable-lab.html)

V2 EMC：

- [EMC Upgrade Plan](projects/stm32f407-mainline/v2/emc-upgrade-plan.md)
- [EMC Review](projects/stm32f407-mainline/v2/emc-review.md)
- [Pre-compliance Plan](projects/stm32f407-mainline/v2/emc-precompliance-plan.md)
- [EMC Fault Lab](projects/stm32f407-mainline/fault-lab/part4-emc-faults.md)

---

# ✅ Part 5｜STM32F407 V2 四层综合板

**[开始四层综合项目](15_Part5_四层综合/00_本Part导读.md)**

<p align="center">
  <img src="assets/images/part5-overview.jpg" width="980" alt="Part 5 STM32F407 V2 四层综合项目总览">
</p>

Part 5 不再新增孤立理论，而是把前面的 **SI + PI + EMC** 压回同一块真实四层板：

```text
System Specification
→ Pin / Clock / Peripheral Planning
→ Schematic Review
→ Placement / Board Zoning
→ Stackup / Net Class / Rule Matrix
→ Routing Priority
→ SI + PI + EMC Joint Review
→ DFM / BOM / Testability
→ Gerber / Assembly Release Gate
→ Bring-up / Validation
→ Final Design Review
```

综合接口：

- STM32F407VGT6 / LQFP100
- USB 2.0 Full-Speed / USB-C device
- CAN 2.0B
- microSD / 4-bit SDIO
- SWD
- 四层板完整 GND reference

项目资产：[`projects/stm32f407-mainline/v2/`](projects/stm32f407-mainline/v2/)

其中包括：

- [System Specification](projects/stm32f407-mainline/v2/system-spec.md)
- [Pin / Clock Plan](projects/stm32f407-mainline/v2/pin-clock-plan.md)
- [Placement Zoning Plan](projects/stm32f407-mainline/v2/placement-zoning-plan.md)
- [Integration Rule Matrix](projects/stm32f407-mainline/v2/integration-rule-matrix.md)
- [Routing Execution Plan](projects/stm32f407-mainline/v2/routing-execution-plan.md)
- [Integration Review](projects/stm32f407-mainline/v2/integration-review.md)
- [DFM Checklist](projects/stm32f407-mainline/v2/dfm-checklist.md)
- [BOM Risk Register](projects/stm32f407-mainline/v2/bom-risk-register.md)
- [Testpoint Plan](projects/stm32f407-mainline/v2/testpoint-plan.md)
- [Release Gate](projects/stm32f407-mainline/v2/release-gate.md)
- [Bring-up Test Plan](projects/stm32f407-mainline/v2/bringup-test-plan.md)
- [Validation Matrix](projects/stm32f407-mainline/v2/validation-matrix.md)
- [Final Design Review](projects/stm32f407-mainline/v2/final-design-review.md)
- [Source Freeze](projects/stm32f407-mainline/v2/source-freeze.md)
- [Part 5 Integration Fault Lab](projects/stm32f407-mainline/fault-lab/part5-integration-faults.md)

互动：

- [V2 Layout Tradeoff Lab](interactive/v2-layout-tradeoff-lab.html)
- [V2 Release Gate Lab](interactive/v2-release-gate-lab.html)

**四层板毕业标准：**不是“DRC 通过”，而是你能解释关键电流路径、参考平面、约束来源、接口保护、制造选择和验证方法。

---

# 下一阶段：Part 6｜为什么从四层升级到六层

Part 6 会从 STM32F407 V2 的真实限制出发，而不是先给一个六层模板：

```text
四层板哪里开始难受？
→ layer congestion
→ reference transition
→ power-domain pressure
→ more high-speed interfaces
→ six-layer stackup alternatives
→ signal / reference pairing
→ via / return transition
→ power distribution
→ STM32H7 V3 architecture
```

目标是理解：**什么时候四层已经足够，什么时候六层是真正的工程需求。**

---

# 主线产品家族

```text
STM32F407 V1 — 四层基本功
      ↓
STM32F407 V2 — USB / CAN / SDIO + SI / PI / EMC
      ↓
STM32H7 V3 — 六层 + Ethernet / SDRAM
```

另有 FPGA 板级设计专项。

---

# Fault Lab：故意画错，然后亲手修

每个 Fault 都要求走完整诊断链：

```text
Symptom
→ Why DRC misses it
→ Current path / field / parasitic
→ Root cause
→ Proposed PCB change
→ Side effect
→ A/B verification
→ Checklist
```

课程训练的是**诊断能力**，不是背答案。

---

# 数字与规则的写作纪律

课程明确区分：

1. 物理原理
2. 工程经验
3. 器件厂家要求
4. 接口 / 认证标准要求
5. 板厂制造限制
6. 系统设计目标
7. 教学数量级示例

不会把 `3W`、`≤1 mm`、`100 nF`、`TVS <5 mm` 等数字跨场景写成无条件铁律。

---

# 一手资料基线

教材优先使用：

- STM32 Datasheet / Reference Manual / Errata / Hardware Guide
- USB-IF 等接口规范
- 芯片/接口器件官方 Application Note
- KiCad 官方文档
- 板厂实际 stackup / manufacturing capability
- 测量与 EMC/PI/SI 厂商技术资料

标准、器件、软件和板厂工艺会变化；**实际设计冻结前重新核对当前版本。**

---

# 关于旧版目录

`01_零基础入门`、`03_二层板实战`、`04_多层板理论`、`05_KiCad多层板操作`、`06_实战项目` 等仍是重构前素材来源。

最终不会保留两套平行教材：好的解释迁移，重复内容合并，误导规则修正；对应 Part 稳定后逐步删除旧章节。Git 历史本身保留旧版本。

---

# 最终学习目标

最终毕业作品不是“一块看起来很复杂的六层板”，而是：

> **一块你能解释每个重要设计决策的六层板。**

别人问你为什么这样叠层、为什么这个电容放这里、为什么这根线换层、为什么接口这样保护、为什么 shield 这样接，你能从电流路径、电磁场、器件要求、系统结构和制造约束解释，而不是回答“网上都这么画”。