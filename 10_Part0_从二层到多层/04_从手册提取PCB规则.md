# 04｜从 Datasheet / Hardware Guide 提取 PCB 规则

> 🎯 **本章目标**：不再先上网搜“STM32 最小系统图”，而是学会从一手资料自己建立电源、时钟、复位、启动、调试和布局约束表。

本课程主线器件：**STM32F407VGT6，LQFP100**。

ST 官方资料：

- 产品页：https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html
- Datasheet（STM32F405/407）：https://www.st.com/resource/en/datasheet/stm32f407vg.pdf
- AN4488《Getting started with STM32F4xxxx MCU hardware development》：https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf

---

## 1. 为什么“抄最小系统图”是个坏习惯？

网上一张看起来很专业的原理图，可能：

- 来自另一个封装；
- 来自另一个 STM32F4 型号；
- 使用了旧版器件要求；
- 省略了作者认为“大家都知道”的电容；
- 把可选方案画成必选；
- 把板级调试器和目标 MCU 混在一起；
- 甚至本身就有错误。

所以课程采用一条原则：

> **先建立“要求表”，再画原理图。**

---

## 2. 先认识三类文档

### Datasheet

回答：

- 引脚是什么；
- 电压范围是什么；
- 电气极限是什么；
- 封装和 pinout 是什么；
- 某些外围接口支持什么；
- 时钟/模拟/IO 的电气条件是什么。

### Reference Manual

主要回答 MCU 内部外设如何工作、寄存器怎么配置。

它对 PCB 仍然重要，但不是第一份“最小硬件”文档。

### Hardware Design Guide / Application Note

像 AN4488 这种文档直接面向板级设计者，会集中讲：

- power supply；
- package；
- clock；
- reset；
- boot；
- debug；
- reference schematic。

**这是第一次设计 MCU 板时最值得逐页读的资料。**

---

## 3. 建一张 Hardware Requirement Table

不要边画边查。先建立表格：

| Topic | Requirement | Source | Schematic action | PCB action |
|---|---|---|---|---|
| VDD | 每个 VDD pin 需要局部去耦 | AN4488 §Power supplies | 100 nF per VDD | 电容靠近相应供电引脚，缩短环路 |
| Bulk | 包级需要较大储能电容 | AN4488 | ≥4.7 µF，typ. 10 µF（按文档） | 放在 MCU 供电区域 |
| VCAP | 内核稳压器输出需指定低 ESR 电容 | AN4488 / Datasheet | VCAP1/2 各 2.2 µF（针对具有两个 VCAP 的相关器件/封装） | 极短连接到 GND，不作为外部电源使用 |
| VDDA | 模拟电源需局部去耦 | AN4488 | 100 nF + 1 µF | 与敏感模拟回路一起规划 |
| VBAT | 无电池时不要悬空 | AN4488 | 接 VDD，并按建议去耦 | 连接简短 |
| SWD | 调试接口要可接入 | AN4488 | SWDIO/SWCLK/NRST/GND/Vref | Header 靠板边、走线清楚 |

> **注意**：上表是本课程针对 STM32F4 主线的“阅读结果示例”，不是所有 MCU 通用模板。换器件后必须重新查。

---

## 4. 用 AN4488 练一次：电源章节怎么读？

AN4488 对 STM32F4 电源给出了非常具体的建议。以其 Rev.7 的 Power supply schemes 为例：

### 4.1 VDD 去耦

文档给出的结构包括：

- 每个 VDD pin 对应一个 `100 nF` ceramic；
- 整个 package 另有一个较大的 bulk capacitor，文档给出 minimum 4.7 µF、typical 10 µF 的量级。

这里真正要学的不是背 `100 nF`，而是区分两种时间尺度：

- 小电容服务局部快速电流环路；
- 较大电容服务更低频/更大能量尺度。

后面 Part 3 会再解释为什么“电容容量越大越适合高频”是错误直觉。

### 4.2 VCAP

STM32F4 内部稳压器需要外部 VCAP 电容。AN4488 对具有 VCAP1/VCAP2 的器件给出了低 ESR ceramic 电容要求（典型为每个 2.2 µF）。

这类引脚属于：

> **看起来像电源脚，但用途由芯片内部稳压器决定，不能凭经验处理。**

因此规则必须来自器件文档。

### 4.3 VDDA / VREF+

模拟电源不能因为“我暂时不用 ADC”就随便悬空。AN4488 给出了 VDDA/VREF+ 的连接和去耦建议。

这提醒你：

> “这个外设我不用” ≠ “它的供电引脚可以不管”。

### 4.4 VBAT

无外部后备电池时，AN4488 给出了 VBAT 接 VDD 并加局部电容的建议。

同样不要靠猜。

---

## 5. 把一句手册文字翻译成 PCB 动作

手册写：

> 每个 VDD pin 放一个 100 nF capacitor。

初学者可能只做原理图：

```text
VDD --- C --- GND
```

但 PCB 设计者还必须继续翻译：

### 电流环路

```text
local cap → VDD pin → internal switching → VSS pin → cap GND
```

因此要问：

- 电容离哪个 VDD/VSS pair 最近？
- 电容到 power pin 的路径是否短而宽？
- GND 端如何低电感接入平面？
- 是否为了“摆整齐”反而把所有电容排成一排远离 MCU？
- 电容过孔位置是否让电流绕路？

这就是从 **schematic compliance** 升级到 **PCB implementation**。

---

## 6. ❌ 故障板：原理图完全正确，布局仍然失败

假设 MCU 周围 8 个 100 nF 去耦电容全部正确连接，但布局时为了美观，把它们排在距离 MCU 边缘较远的一条直线上。

ERC：通过。

DRC：通过。

BOM：正确。

但局部电源环路的几何长度明显增加。

后面 PI 章节你会学到：

```text
V = L · di/dt
```

连接结构的寄生电感 `L` 可能比“电容标称值是不是 100 nF”更影响高频效果。

所以 Review 时不只检查“有没有电容”，还检查“电容是否真正形成短小电流环路”。

---

## 7. 手册阅读顺序：主线 STM32F407

第一次开项目时，建议按下面顺序：

1. 确认 exact part number 与 package；
2. Datasheet pinout；
3. power supply pins；
4. VCAP / VDDA / VREF / VBAT；
5. reset；
6. boot pins；
7. SWD/JTAG；
8. HSE/LSE requirements；
9. USB / CAN / SDIO 等你实际要用的接口；
10. errata；
11. 对照官方开发板原理图作为**第二来源交叉检查**。

顺序很重要：官方开发板可以参考，但不能替代 datasheet/design guide。

---

## 8. 🛠️ 本章任务：做自己的 Constraint Sheet

新建：

```text
projects/stm32f407-mainline/review/hardware-constraints.md
```

至少包含：

```text
[Power]
VDD:
VDDA:
VREF+:
VBAT:
VCAP1:
VCAP2:

[Clock]
HSE:
LSE:

[Boot/Reset]
BOOT0:
NRST:

[Debug]
SWDIO:
SWCLK:
SWO:
NRST:

[Interfaces]
USB FS:
CAN:
SDIO:
```

每一项都写：

- source document；
- section / table / figure；
- schematic action；
- PCB action。

---

## 9. Design Review

- [ ] exact MCU part number 已锁定；
- [ ] package pinout 已核对；
- [ ] 所有 supply / reference / VCAP 类引脚都有明确处理；
- [ ] 每条关键要求有一手资料来源；
- [ ] 原理图规则已翻译成布局/走线动作；
- [ ] 没有因为“不使用某外设”就擅自悬空供电/参考脚；
- [ ] 已查看最新 datasheet revision / errata。

---

## 10. 本章最重要的一句话

> **工程设计不是“记住 STM32 怎么接”，而是学会对任何新芯片重复这一套资料提取流程。**

下一章把这些规则真正放进 KiCad 10。