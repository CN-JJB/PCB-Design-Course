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

### ✅ Part 2｜Signal Integrity：STM32F407 V1 → V2

从这里开始：

**[12_Part2_信号完整性/00_本Part导读.md](12_Part2_信号完整性/00_本Part导读.md)**

这部分不把 SI 写成“高速玄学”，而是围绕同一块 V2 PCB 依次解决：

```text
传播
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
- [KiCad 中的 SI 落地与 Review](12_Part2_信号完整性/08_KiCad中的SI落地与Review.md)

互动实验：

- [Reflection Lab](interactive/reflection-lab.html)
- [Return Path Lab](interactive/return-path-lab.html)
- [Crosstalk Lab](interactive/crosstalk-lab.html)
- [Edge Rate Lab](interactive/edge-rate-lab.html)

V2 工程资产：

- [SI Upgrade Plan](projects/stm32f407-mainline/v2/si-upgrade-plan.md)
- [SI Net Inventory](projects/stm32f407-mainline/v2/si-net-inventory.md)
- [SI Routing Constraints](projects/stm32f407-mainline/v2/si-routing-constraints.md)
- [SI Review](projects/stm32f407-mainline/v2/si-review.md)
- [Part 2 Fault Lab](projects/stm32f407-mainline/fault-lab/part2-si-faults.md)

Part 2 已明确修正旧稿中的几类问题：

- 不再用固定 MHz 作为“高速”的物理分界；
- 修正旧稿 `1 ns × 15 cm/ns = 1.5 cm` 的数量级错误；
- 不把 `22/33 Ω` source resistor 写成固定答案；
- 不把 `3W/3H/5H/1 mm` 跨场景写成铁律；
- 不把“差分等长”当成差分设计全部；
- 不假设“两根单端线”自动等于正确 differential impedance。

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

Part 1 已定义基础布局/电源/制造错误；Part 2 继续加入：

- 同频率不同 edge-rate 风险；
- impedance discontinuity；
- source resistor 放错位置；
- 跨 reference slot；
- layer transition 缺少回流分析；
- 长距离平行串扰；
- differential geometry 不对称；
- 过度 meander；
- USB ESD 位置错误；
- 示波器长地线制造伪振铃。

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
- ST AN4879 USB hardware guide：https://www.st.com/resource/en/application_note/an4879-usb-hardware-design-guidelines-for-stm32-microcontrollers-stmicroelectronics.pdf
- USB-IF USB 2.0 documents：https://www.usb.org/documents?search=usb%202.0
- TI transmission-line / high-speed design application reports：https://www.ti.com/
- JLCPCB controlled-impedance stackup：https://jlcpcb.com/impedance
- AP2112：https://www.diodes.com/part/view/AP2112

板厂、接口规范和软件参数可能变化，课程会记录查询日期；实际下单/使用前重新核对。

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