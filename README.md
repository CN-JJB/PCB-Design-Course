# PCB 设计教材｜从二层板到四层 / 六层高速板

> 面向**已经会画二层板**的学习者：通过一条持续升级的 MCU 项目主线，系统学习 4 层 / 6 层 PCB、Signal Integrity（SI）、Power Integrity（PI）、EMI/EMC、DFM、测量与 Design Review。

本教材不以“记规则”为目标。核心教学顺序是：

```text
现象
→ 建立直觉
→ 教材插图 / 互动实验
→ 物理原因
→ 必要公式
→ KiCad 实操
→ 修改主线 PCB
→ 故障板案例
→ Design Review
→ 本章任务
```

---

## 当前重构阶段

### ✅ Part 0｜从二层板到多层板：认知升级

从这里开始：

**[10_Part0_从二层到多层/00_本Part导读.md](10_Part0_从二层到多层/00_本Part导读.md)**

你会先补齐真正需要的地基：

- PCB 走线为什么不是理想导线；
- 电流回路与 Return Path；
- Reference Plane；
- 为什么高速主要看 edge rate / flight time，而不是固定 MHz；
- 如何从 Datasheet / Hardware Guide 提取 PCB 规则；
- KiCad 9 的 Physical Stackup / Net Classes / Custom Rules 思维。

配套：

- [Edge Rate Lab](interactive/edge-rate-lab.html)
- [二层 vs 四层 SVG](assets/svg/part0-two-vs-four-layer.svg)
- [Signal / Return Path SVG](assets/svg/part0-current-loop.svg)

### ✅ Part 1｜第一块真正的四层板：STM32F407 V1

从这里开始：

**[11_Part1_STM32F407四层板/00_项目导读.md](11_Part1_STM32F407四层板/00_项目导读.md)**

主控：`STM32F407VGT6 / LQFP100`

流程：

```text
需求
→ power tree / schematic
→ 真实四层 stackup
→ placement
→ routing rules
→ DRC + manual review
→ Gerber
→ bring-up
```

项目资产：

- [STM32F407 mainline](projects/stm32f407-mainline/README.md)
- [Hardware Constraints](projects/stm32f407-mainline/v1/hardware-constraints.md)
- [Design Decisions](projects/stm32f407-mainline/v1/design-decisions.md)
- [Design Review Checklist](projects/stm32f407-mainline/review/design-review-checklist.md)
- [Fault Lab](projects/stm32f407-mainline/fault-lab/README.md)

---

## 整本教材路线

| Part | 主题 | 主线产出 |
|---|---|---|
| 0 | 二层 → 多层认知跃迁 | 能分析 reference / return / edge rate |
| 1 | STM32F407 四层 V1 | 第一块可 Review 的四层 MCU 板 |
| 2 | Signal Integrity | V1 → V2：传输线/反射/端接/回流/串扰/差分 |
| 3 | Power Integrity | 去耦/PDN/ESL/安装电感/Ground Bounce/Buck |
| 4 | EMI / EMC | 回路面积/共模/接口/ESD/电缆/预兼容测试 |
| 5 | 四层综合 | STM32F407 V2：USB/CAN/SDIO |
| 6 | 四层 → 六层 | Stackup / reference / 多电源域 |
| 7 | 六层高速 | STM32H7 + Ethernet + SDRAM |
| 8 | FPGA 专项 | Bank / BGA fanout / clock / DDR / pin planning |
| 9 | 工程交付 | DFM / 测量 / 调试 / Gerber / BOM / 量产 |

---

## 主线不是六块互不相干的 Demo

新版课程使用一个产品家族持续升级：

```text
STM32F407 V1 — 四层基本功
      ↓
STM32F407 V2 — USB / CAN / SDIO + SI/PI/EMC
      ↓
STM32H7 V3 — 六层 + Ethernet / SDRAM
```

另有 FPGA 板级设计专项。

这样每学一个理论，你都会立刻回到“正在画的那块板”验证。

---

## Fault Lab：故意画错，然后亲手修

课程会保留第二条暗线：**故障板实验**。

不是只展示正确答案，而是让你分析：

```text
What is the symptom?
→ DRC 为什么可能看不见？
→ signal/power current 怎么走？
→ reference / return 在哪里断？
→ root cause
→ Before / After
→ 新增 Checklist
```

当前已定义：

- 去耦电容排队但离 MCU 太远；
- VCAP 长线；
- HSE 跨板；
- 拿 L2 GND 当救火布线层；
- Bottom 跨 L3 Power split；
- LDO 热预算错误；
- SWD 物理不可访问；
- Gerber 最终输出与编辑器预期不一致。

---

## 教材可视化约定

技术图优先使用 SVG：可缩放、可审阅、可版本控制。

统一视觉语言：

- **红色**：signal / outgoing current；
- **蓝色**：return current；
- **深灰**：GND reference；
- **铜色**：signal/power copper；
- **紫色**：field / sensitive electromagnetic relationship；
- **红色警示**：错误结构；
- **绿色**：改进结构。

静态图不够时使用 HTML/JS 互动实验；KiCad 操作使用真实软件流程；外部图片优先使用官方/明确开放许可来源。

---

## 数字与规则的写作纪律

本课程会区分：

1. **物理原理**；
2. **工程经验**；
3. **器件厂家要求**；
4. **接口标准要求**；
5. **板厂制造限制**。

例如不会再把：

```text
高速 = 超过 50 MHz
换层地孔必须 ≤1 mm
去耦必须 ≤2 mm
板边每 10 mm 一个地孔
```

写成无条件“铁律”。

关键数字尽量就近给出一手资料来源和适用条件。

---

## 当前一手资料基线

- KiCad 9 PCB Editor：https://docs.kicad.org/9.0/zh/pcbnew/pcbnew.html
- STM32F407VG：https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html
- STM32F407 Datasheet：https://www.st.com/resource/en/datasheet/stm32f407vg.pdf
- ST AN4488：https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf
- JLCPCB controlled-impedance stackup：https://jlcpcb.com/impedance
- AP2112：https://www.diodes.com/part/view/AP2112

板厂和软件参数可能变化，课程会记录查询日期；实际下单/使用前重新核对。

---

## 关于旧版目录

仓库中的 `01_零基础入门`、`03_二层板实战`、`04_多层板理论`、`05_KiCad多层板操作`、`06_实战项目` 等是本次重构前的内容来源。

**不会长期保留两套平行教材。**

迁移原则：

- 好的解释 → 合并到新主线；
- 好的案例 → 重写并保留；
- 重复内容 → 合并；
- 过度绝对/误导规则 → 修正；
- 已完成迁移的旧章节 → 在对应 Part 完成后逐步删除。

Git 历史本身会保存旧版本，因此最终仓库只保留一条清晰学习路径。

---

## 学习目标

最终毕业作品不是“一块看起来很复杂的六层板”，而是：

> **一块你能解释每个重要设计决策的六层板。**

别人问你为什么这样叠层、为什么这个电容放这里、为什么这根线换层、为什么这个接口需要这样做，你能从电流路径、电磁场、器件要求和制造约束解释，而不是回答“网上都这么画”。