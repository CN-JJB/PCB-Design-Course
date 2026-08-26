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

重点：PCB 互连不是理想导线、Return Path / Reference Plane、edge rate / flight time、从 Datasheet 提取 PCB 规则、KiCad 9 多层必备操作。

配套：

- [Edge Rate Lab](interactive/edge-rate-lab.html)
- [二层 vs 四层 SVG](assets/svg/part0-two-vs-four-layer.svg)
- [Signal / Return Path SVG](assets/svg/part0-current-loop.svg)

### ✅ Part 1｜第一块真正的四层板：STM32F407 V1

从这里开始：

**[11_Part1_STM32F407四层板/00_项目导读.md](11_Part1_STM32F407四层板/00_项目导读.md)**

主控：`STM32F407VGT6 / LQFP100`

```text
需求 → power tree / schematic → 真实四层 stackup
→ placement → routing rules → DRC + manual review
→ Gerber → bring-up
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

```text
传播 → transmission line / Z0 → reflection / termination
→ return path / layer transition → crosstalk
→ differential pair / USB FS → TDR / eye / oscilloscope
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

V2 SI 工程资产：

- [SI Upgrade Plan](projects/stm32f407-mainline/v2/si-upgrade-plan.md)
- [SI Net Inventory](projects/stm32f407-mainline/v2/si-net-inventory.md)
- [SI Routing Constraints](projects/stm32f407-mainline/v2/si-routing-constraints.md)
- [SI Review](projects/stm32f407-mainline/v2/si-review.md)
- [Part 2 Fault Lab](projects/stm32f407-mainline/fault-lab/part2-si-faults.md)

### ✅ Part 3｜Power Integrity：从“有 3.3 V”到“电源网络可解释”

从这里开始：

**[13_Part3_电源完整性/00_本Part导读.md](13_Part3_电源完整性/00_本Part导读.md)**

Part 3 从 STM32F407 的真实去耦要求出发：

```text
瞬态电流
→ local decoupling
→ C / ESR / ESL / SRF / DC Bias
→ mounting inductance
→ PDN / target impedance
→ anti-resonance
→ plane / spreading inductance
→ ground bounce / SSN
→ Buck hot loop
→ measurement integrity
→ KiCad PI Review
```

核心章节：

- [瞬态电流与去耦](13_Part3_电源完整性/01_瞬态电流与去耦.md)
- [真实电容：ESR / ESL / 自谐振](13_Part3_电源完整性/02_真实电容_ESR_ESL与自谐振.md)
- [安装电感与布局](13_Part3_电源完整性/03_安装电感与布局.md)
- [PDN 与目标阻抗](13_Part3_电源完整性/04_PDN与目标阻抗.md)
- [多电容与反谐振](13_Part3_电源完整性/05_多电容与反谐振.md)
- [电源地平面与地弹](13_Part3_电源完整性/06_电源地平面与地弹.md)
- [Buck 热环路与布局](13_Part3_电源完整性/07_Buck热环路与布局.md)
- [示波器测电源噪声](13_Part3_电源完整性/08_示波器测电源噪声.md)
- [KiCad 中的 PI 落地与 Review](13_Part3_电源完整性/09_KiCad中的PI落地与Review.md)
- [参考资料与数据纪律](13_Part3_电源完整性/10_参考资料与数据纪律.md)

互动实验：

- [Decoupling Impedance Lab](interactive/decoupling-impedance-lab.html)
- [Target Impedance Lab](interactive/target-impedance-lab.html)
- [Buck Hot Loop Lab](interactive/buck-hot-loop-lab.html)

V2 PI 工程资产：

- [PI Upgrade Plan](projects/stm32f407-mainline/v2/pi-upgrade-plan.md)
- [PI Rail Budget](projects/stm32f407-mainline/v2/pi-rail-budget.md)
- [PI Review](projects/stm32f407-mainline/v2/pi-review.md)
- [Part 3 Fault Lab](projects/stm32f407-mainline/fault-lab/part3-pi-faults.md)

Part 3 明确修正/避免的常见误导：

- 不把 `100 nF` 当所有芯片通用魔法值；
- 不用固定 `≤2 mm` 替代完整 decoupling-loop review；
- 不假设标称 `10 µF` 在 DC Bias 下仍有 10 µF；
- 不把 ESR 越低越好写成无条件规则；
- 不把 `100 nF + 1 µF + 10 µF` 当自动覆盖全频段；
- 不把 target impedance 当所有器件的万能签核公式；
- 不把 plane 当零阻抗超级导线；
- 不把 regulator 额定电流等同于热与瞬态能力；
- 不用长示波器地线的波形直接判定 PCB 噪声。

---

## 整本教材路线

| Part | 主题 | 主线产出 |
|---|---|---|
| 0 | 二层 → 多层认知跃迁 | 能分析 reference / return / edge rate |
| 1 | STM32F407 四层 V1 | 第一块可 Review 的四层 MCU 板 |
| 2 | Signal Integrity | V1 → V2：传输线/反射/端接/回流/串扰/差分 |
| 3 | Power Integrity | V2：去耦/PDN/ESL/安装电感/Ground Bounce/Buck |
| 4 | EMI / EMC | 回路面积/共模/接口/ESD/电缆/预兼容测试 |
| 5 | 四层综合 | STM32F407 V2：USB/CAN/SDIO |
| 6 | 四层 → 六层 | Stackup / reference / 多电源域 |
| 7 | 六层高速 | STM32H7 + Ethernet + SDRAM |
| 8 | FPGA 专项 | Bank / BGA fanout / clock / DDR / pin planning |
| 9 | 工程交付 | DFM / 测量 / 调试 / Gerber / BOM / 量产 |

---

## 主线不是六块互不相干的 Demo

```text
STM32F407 V1 — 四层基本功
      ↓
STM32F407 V2 — USB / CAN / SDIO + SI/PI/EMC
      ↓
STM32H7 V3 — 六层 + Ethernet / SDRAM
```

另有 FPGA 板级设计专项。每学一个理论，都立刻回到“正在画的那块板”验证。

---

## Fault Lab：故意画错，然后亲手修

课程保留第二条暗线：**故障板实验**。

```text
Symptom
→ DRC 为什么可能看不见？
→ current path / field / parasitic
→ root cause
→ measurement plan
→ KiCad Before / After
→ Checklist
```

Part 3 新增典型故障：

- 电容很近但 GND 绕远；
- 多颗去耦共享长窄 neck；
- MLCC 只看 nominal C；
- 无依据的“电容农场”；
- 3V3 plane narrow neck；
- 多个 VSS 串联后单 via 落地；
- Buck CIN 放错位置；
- SW copper 过大；
- FB 穿 noisy region；
- 长探头地线制造伪尖峰；
- 只看 regulator rated current；
- 擅自修改 VCAP。

---

## 教材可视化约定

技术图优先使用 SVG：可缩放、可审阅、可版本控制。

统一视觉语言：

- **红色**：signal / outgoing current / high-di/dt path；
- **蓝色**：return current；
- **深灰**：GND reference；
- **铜色**：signal/power copper；
- **紫色**：field / impedance / sensitive relationship；
- **红色警示**：错误结构；
- **绿色**：改进结构。

静态图不够时使用 HTML/JS 互动实验；KiCad 操作使用真实软件流程；外部图片优先使用官方/明确开放许可来源。

---

## 数字与规则的写作纪律

课程区分：

1. **物理原理**；
2. **工程经验**；
3. **器件厂家要求**；
4. **接口标准要求**；
5. **板厂制造限制**；
6. **系统设计目标**；
7. **教学数量级示例**。

关键数字尽量就近给出一手资料来源和适用条件。

---

## 当前一手资料基线

- KiCad 9 PCB Editor：https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html
- STM32F407VG：https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html
- STM32F407 Datasheet：https://www.st.com/resource/en/datasheet/stm32f407vg.pdf
- ST AN4488：https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf
- ST AN4879 USB hardware guide：https://www.st.com/resource/en/application_note/an4879-usb-hardware-design-guidelines-for-stm32-microcontrollers-stmicroelectronics.pdf
- USB-IF USB 2.0 documents：https://www.usb.org/documents?search=usb%202.0
- TI Power Delivery Network Analysis：https://www.ti.com/lit/an/swpa222a/swpa222a.pdf
- TI Good Buck Converter Layout Practices：https://www.ti.com/lit/pdf/slva494
- TI Buck Converter Layout Considerations for Radiated EMI：https://www.ti.com/lit/an/snva755/snva755.pdf
- Murata MLCC DC Bias：https://ds.murata.com/simsurfing_data/pdf/en-us/mlcc/sim_mlcc_measuringcond_e.pdf
- JLCPCB controlled-impedance stackup：https://jlcpcb.com/impedance

板厂、标准和软件参数可能变化，实际下单/设计冻结前重新核对。

---

## 关于旧版目录

仓库中的 `01_零基础入门`、`03_二层板实战`、`04_多层板理论`、`05_KiCad多层板操作`、`06_实战项目` 等是重构前的内容来源。

**不会长期保留两套平行教材。**

迁移原则：好的解释合并、好的案例重写保留、重复内容合并、过度绝对/误导规则修正，已完成迁移的旧章节在对应 Part 稳定后逐步删除。Git 历史保存旧版本。

---

## 学习目标

最终毕业作品不是“一块看起来很复杂的六层板”，而是：

> **一块你能解释每个重要设计决策的六层板。**

别人问你为什么这样叠层、为什么这个电容放这里、为什么这根线换层、为什么这个接口需要这样做，你能从电流路径、电磁场、器件要求和制造约束解释，而不是回答“网上都这么画”。
