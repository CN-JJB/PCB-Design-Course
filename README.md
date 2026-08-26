# PCB 设计教材｜从二层板到四层 / 六层高速板

> 面向**已经会画二层板**的学习者：通过一条持续升级的 MCU 项目主线，系统学习 4 层 / 6 层 PCB、Signal Integrity（SI）、Power Integrity（PI）、EMI/EMC、DFM、测量与 Design Review。

这套教材不以“背规则”为目标。核心学习顺序是：

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

## ✅ Part 0｜从二层板到多层板：认知升级

**[开始学习](10_Part0_从二层到多层/00_本Part导读.md)**

重点：

- PCB 互连不是理想导线
- Return Path / Reference Plane
- edge rate / flight time
- 从 Datasheet / Hardware Guide 提取 PCB 规则
- KiCad 9 多层必备操作

互动：

- [Edge Rate Lab](interactive/edge-rate-lab.html)

---

## ✅ Part 1｜第一块真正的四层板：STM32F407 V1

**[开始项目](11_Part1_STM32F407四层板/00_项目导读.md)**

主控：`STM32F407VGT6 / LQFP100`

```text
需求
→ power tree / schematic
→ 真实四层 stackup
→ placement
→ routing
→ DRC + manual review
→ Gerber
→ bring-up
```

项目资产：

- [STM32F407 mainline](projects/stm32f407-mainline/README.md)
- [Hardware Constraints](projects/stm32f407-mainline/v1/hardware-constraints.md)
- [Design Decisions](projects/stm32f407-mainline/v1/design-decisions.md)
- [Design Review Checklist](projects/stm32f407-mainline/review/design-review-checklist.md)

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

核心章节：

- [波在 PCB 上怎么传播](12_Part2_信号完整性/01_波在PCB上怎么传播.md)
- [传输线与特性阻抗](12_Part2_信号完整性/02_传输线与特性阻抗.md)
- [反射与终端匹配](12_Part2_信号完整性/03_反射与终端匹配.md)
- [回流路径与换层](12_Part2_信号完整性/04_回流路径与换层.md)
- [串扰与几何隔离](12_Part2_信号完整性/05_串扰与几何隔离.md)
- [差分对与 USB 实战](12_Part2_信号完整性/06_差分对与USB实战.md)
- [TDR、眼图与示波器判读](12_Part2_信号完整性/07_TDR眼图与示波器判读.md)
- [KiCad SI Review](12_Part2_信号完整性/08_KiCad中的SI落地与Review.md)

互动：

- [Reflection Lab](interactive/reflection-lab.html)
- [Return Path Lab](interactive/return-path-lab.html)
- [Crosstalk Lab](interactive/crosstalk-lab.html)

V2 SI：

- [SI Upgrade Plan](projects/stm32f407-mainline/v2/si-upgrade-plan.md)
- [SI Net Inventory](projects/stm32f407-mainline/v2/si-net-inventory.md)
- [SI Routing Constraints](projects/stm32f407-mainline/v2/si-routing-constraints.md)
- [SI Review](projects/stm32f407-mainline/v2/si-review.md)
- [SI Fault Lab](projects/stm32f407-mainline/fault-lab/part2-si-faults.md)

---

## ✅ Part 3｜Power Integrity：从“有 3.3 V”到“PDN 可解释”

**[开始学习 PI](13_Part3_电源完整性/00_本Part导读.md)**

```text
瞬态电流
→ local decoupling
→ C / ESR / ESL / SRF / DC Bias
→ mounting inductance
→ PDN / target impedance
→ anti-resonance
→ plane / ground bounce
→ Buck hot loop
→ measurement integrity
→ KiCad PI Review
```

核心章节：

- [瞬态电流与去耦](13_Part3_电源完整性/01_瞬态电流与去耦.md)
- [真实电容：ESR / ESL / SRF](13_Part3_电源完整性/02_真实电容_ESR_ESL与自谐振.md)
- [安装电感与布局](13_Part3_电源完整性/03_安装电感与布局.md)
- [PDN 与目标阻抗](13_Part3_电源完整性/04_PDN与目标阻抗.md)
- [多电容与反谐振](13_Part3_电源完整性/05_多电容与反谐振.md)
- [电源地平面与地弹](13_Part3_电源完整性/06_电源地平面与地弹.md)
- [Buck 热环路与布局](13_Part3_电源完整性/07_Buck热环路与布局.md)
- [示波器测电源噪声](13_Part3_电源完整性/08_示波器测电源噪声.md)
- [KiCad PI Review](13_Part3_电源完整性/09_KiCad中的PI落地与Review.md)

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

核心章节：

- [差模、共模与辐射源](14_Part4_EMI_EMC/01_差模共模与辐射源.md)
- [回路、槽缝与天线结构](14_Part4_EMI_EMC/02_回路槽缝与天线结构.md)
- [连接器、电缆与共模转换](14_Part4_EMI_EMC/03_连接器电缆与共模转换.md)
- [ESD 与 TVS 布局](14_Part4_EMI_EMC/04_ESD与TVS布局.md)
- [Shield / Chassis / System GND](14_Part4_EMI_EMC/05_Shield_Chassis与系统地.md)
- [USB / CAN 接口 EMC 实战](14_Part4_EMI_EMC/06_USB_CAN接口EMC实战.md)
- [近场探头与预兼容测试](14_Part4_EMI_EMC/07_近场探头与预兼容测试.md)
- [KiCad EMC Review](14_Part4_EMI_EMC/08_KiCad中的EMC落地与Review.md)
- [参考资料与数据纪律](14_Part4_EMI_EMC/09_参考资料与数据纪律.md)

互动：

- [ESD Layout Lab](interactive/esd-layout-lab.html)
- [Common-Mode Cable Lab](interactive/common-mode-cable-lab.html)

V2 EMC：

- [EMC Upgrade Plan](projects/stm32f407-mainline/v2/emc-upgrade-plan.md)
- [EMC Interface Inventory](projects/stm32f407-mainline/v2/emc-interface-inventory.md)
- [EMC Review](projects/stm32f407-mainline/v2/emc-review.md)
- [Pre-compliance Plan](projects/stm32f407-mainline/v2/emc-precompliance-plan.md)
- [Part 4 Fault Lab](projects/stm32f407-mainline/fault-lab/part4-emc-faults.md)

Part 4 特别避免这些“EMC 口诀化”误导：

- 不把 TVS `<5 mm` 当通用通过条件；
- 不把板边 via fence `≤10 mm` 当所有板通用要求；
- 不把 shield 永远直接接 GND / 永远 RC 接地写成统一答案；
- 不把 CMC / ferrite 当万能整改件；
- 不把 near-field hotspot 直接等同于正式远场主因；
- 不把“拔掉电缆后峰值下降”直接等同于 PHY 根因；
- 不把 DRC PASS 当 EMC PASS。

---

# 整本教材路线

| Part | 主题 | 主线产出 |
|---|---|---|
| 0 | 二层 → 多层认知跃迁 | 能分析 reference / return / edge rate |
| 1 | 四层入门 | STM32F407 V1 |
| 2 | Signal Integrity | V2 SI upgrade |
| 3 | Power Integrity | V2 PI upgrade |
| 4 | EMI / EMC | V2 interface / ESD / pre-compliance |
| 5 | 四层综合 | STM32F407 V2：USB / CAN / SDIO 综合收口 |
| 6 | 四层 → 六层 | Stackup / reference / 多电源域 |
| 7 | 六层高速 | STM32H7 + Ethernet + SDRAM |
| 8 | FPGA 专项 | Bank / BGA fanout / clock / DDR / pin planning |
| 9 | 工程交付 | DFM / 测量 / 调试 / BOM / 量产 |

主线产品家族：

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

每个 Fault 要求：

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

课程希望训练的不是“看见错误答案”，而是**诊断能力**。

---

# 教材可视化约定

技术图优先使用 SVG：可缩放、可审阅、可版本控制。

统一视觉语言：

- **红色**：signal / outgoing current / high-di/dt path
- **蓝色**：return / discharge current
- **深灰**：GND reference
- **铜色**：signal / power copper
- **紫色**：field / coupling / impedance relationship
- **红色警示**：错误结构
- **绿色**：改进结构

静态图不够时使用 HTML/JS 互动实验；KiCad 操作使用真实软件流程。

---

# 数字与规则的写作纪律

课程明确区分：

1. 物理原理
2. 工程经验
3. 器件厂家要求
4. 接口/认证标准要求
5. 板厂制造限制
6. 系统设计目标
7. 教学数量级示例

关键数字尽量给出来源和适用条件。

---

# 当前一手资料基线

- KiCad 9 PCB Editor：https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html
- STM32F407：https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html
- ST AN4488：https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf
- ST AN4879 USB hardware / PCB guide：https://www.st.com/resource/en/application_note/an4879-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf
- USB-IF：https://www.usb.org/documents
- TI ESD Protection Layout Guide (SLVA680A)：https://www.ti.com/lit/an/slva680a/slva680a.pdf
- TI CAN transient reference design TIDA-00629：https://www.ti.com/tool/TIDA-00629
- TI PDN Analysis：https://www.ti.com/lit/an/swpa222a/swpa222a.pdf
- TI Buck Layout：https://www.ti.com/lit/pdf/slva494
- JLCPCB controlled impedance：https://jlcpcb.com/impedance

标准、软件、板厂与器件资料会变化；实际设计冻结前重新核对。

---

# 关于旧版目录

`01_零基础入门`、`03_二层板实战`、`04_多层板理论`、`05_KiCad多层板操作`、`06_实战项目` 等仍是重构前素材来源。

**最终不会保留两套平行教材。**

好的解释迁移、重复内容合并、误导规则修正；对应 Part 稳定后逐步删除旧章节。Git 历史本身保留旧版本。

---

# 最终学习目标

最终毕业作品不是“一块看起来很复杂的六层板”，而是：

> **一块你能解释每个重要设计决策的六层板。**

别人问你为什么这样叠层、为什么这个电容放这里、为什么这根线换层、为什么接口这样保护、为什么 shield 这样接，你能从电流路径、电磁场、器件要求、系统结构和制造约束解释，而不是回答“网上都这么画”。