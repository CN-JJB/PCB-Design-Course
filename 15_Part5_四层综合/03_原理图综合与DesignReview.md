# 03｜原理图综合与 Design Review：把模块“连起来”之前先问电流怎么走

> 原理图最危险的阶段不是缺一根线，而是每个 block 单看都正确，组合起来却出现供电、保护、启动、调试或接口边界问题。

本章目标：把 STM32F407、USB-C、CAN、microSD、SWD 和 3.3 V 电源组合成**一张能进行工程 Review 的原理图**。

---

# 3.1 推荐的原理图分层

不要把所有东西挤在一页。

推荐结构：

```text
00_System
01_Power
02_MCU_Core
03_USB
04_CAN
05_SDIO
06_Debug_IO
07_Connectors_Testpoints
```

这样 Review 时可以逐 block 检查，再回到 System 页看跨页关系。

---

# 3.2 MCU Core 页：先把“不可协商”的要求锁死

至少检查：

## VDD / VSS

- 每个电源/地 pin 都被正确连接；
- 去耦数量与器件要求对应；
- 去耦不是“所有 100 nF 放一排”；
- 每颗 decoupler 有可实现的低电感 loop；
- VSS 不通过一条长细线串联后才落地。

## VDDA / VSSA

- 按 ST hardware guide 处理；
- 与 digital supply 的连接方式有依据；
- analog decoupling 有明确回路；
- 不因“模拟地”三个字就盲目切割 GND plane。

## VCAP

- 严格按 STM32F407 datasheet / AN4488；
- 不作为外部 1.2 V rail；
- 不被其他负载使用；
- value / ESR / placement 不自行创造。

## NRST / BOOT

- reset network 可调试；
- boot strap 状态明确；
- 外部 connector/按键如果触及 NRST，要考虑 ESD/误触发。

---

# 3.3 USB-C Device-only 原理图 Review

建议把 USB 看成：

```text
Connector shell / CC / VBUS / D+ D-
      ↓
ESD boundary
      ↓
optional tuning / series footprints
      ↓
MCU USB FS PHY
```

## CC1 / CC2

V2 是 device/UFP，不做 PD。

- CC1/CC2 的 device termination 按当前 USB Type-C spec 实现；
- 不把 USB-A/Micro-B 的思维直接搬到 Type-C；
- 两个 CC pin 都要处理，因为 plug 可翻转。

## D+ / D-

- ESD device 低电容且适合 USB FS；
- 不加无依据大电容；
- series / tuning pad 如果预留，必须不制造长 stub；
- test point 如果需要，使用不会明显破坏主线的方式。

## VBUS

- connector VBUS → protection / power-entry → 5 V rail；
- 如果 MCU 使用 VBUS sensing，确认绝对最大值和 pin 类型；
- bulk / local input cap 按 USB 输入和 regulator 要求；
- 不能让 ESD/connector surge current 先穿过 MCU 区再去电源入口。

## Shield

- 明确 `Shield` 与 `Digital GND` 的设计关系；
- 如果没有 metal chassis，不要假装存在“真正 chassis”；
- 留出结构可调整性，但不要用没有物理对象的 `CHASSIS_GND` 标签自我安慰。

---

# 3.4 CAN 原理图 Review

CAN block 建议分：

```text
MCU logic
→ transceiver
→ optional mode control
→ protection / CMC option
→ termination option
→ connector
```

## Logic side

- TXD/RXD 电压兼容；
- standby/silent pin 默认状态明确；
- power-up 时不会因 MCU pin floating 让 transceiver 进入异常状态。

## Bus side

- CANH/CANL 成对、对称；
- TVS topology 与系统 transient 目标匹配；
- CMC footprint 如果预留，默认 DNP/0 Ω 策略明确；
- termination 120 Ω 不默认假定本板是端点；
- connector pinout 和 GND/shield strategy 明确。

## 重要：CAN transceiver ≠ CAN controller

TCAN332 等器件可以支持 CAN FD 物理层能力，但 STM32F407 内部 bxCAN 是 classic CAN 2.0B controller。

所以 V2 的功能规格必须写：

> Classic CAN only on this MCU implementation.

不要因为 transceiver datasheet 写 CAN FD 就在产品说明里误写 CAN FD。

---

# 3.5 microSD / SDIO 原理图 Review

## 必须核对

- CLK；
- CMD；
- D0~D3；
- card power；
- card detect（如果使用）；
- required pull-ups；
- connector shield/ground pins；
- local decoupling；
- ESD 是否需要，取决于用户可触及和产品环境。

## CLK source termination 预留

SDIO_CLK 是最主要 aggressor。

建议在 MCU source 侧预留 series resistor footprint。

但值不要写死：

```text
R_series = target - output impedance - interconnect contribution
```

最终通过：

- edge rate；
- trace length；
- measurement；
- card behavior；

来决定是否装、装多少。

## CMD / DATA pull-up

这些值必须来自当前 SD/host design guidance 或参考设计，不要因为“网上都用 10 kΩ”就把 10 kΩ 写成物理定律。

课程项目可以先定义 footprint 和 BOM candidate，再在 release 前核对来源。

---

# 3.6 电源原理图：把 Power Tree 画成能审核的图

至少画清：

```text
USB VBUS 5V
→ input protection
→ 5V rail
→ 3.3V regulator
→ 3V3 plane/rail
   ├─ MCU VDD
   ├─ VDDA branch
   ├─ microSD
   ├─ CAN transceiver
   └─ LEDs / peripherals
```

每一段标：

- nominal voltage；
- expected current；
- peak current；
- decoupling/bulk；
- source device；
- test point。

这比只看 net label 有用得多。

---

# 3.7 AP2112 之类 LDO 的 Review 思路

如果 V2 延续 5 V → 3.3 V LDO：

不要只看：

> `600 mA`。

必须同时计算：

```text
P_dissipation = (VIN - VOUT) × IOUT
```

例如 5 V → 3.3 V，如果平均 350 mA：

```text
P ≈ 1.7 × 0.35 = 0.595 W
```

这已经足以让小封装和局部铜面积成为热设计问题。

所以综合 Review 里要问：

- 平均负载是多少；
- SD write peak 是多少；
- regulator thermal margin；
- 是否需要未来 V3 改 buck；
- 5V 与 3V3 test point 是否可测。

---

# 3.8 ERC 通过 ≠ Schematic Review 通过

ERC 能发现：

- 未连接 pin；
- output-output 冲突；
- power flag 问题；
- 某些 pin type 错误。

ERC 很难发现：

- 120 Ω 在总线中间被错误默认焊接；
- TVS topology 方向正确但 discharge target 错；
- SDIO series R 放在 card 端而不是 source 端；
- VCAP 被误当普通 1.2 V rail；
- SWD header 供电参考缺失；
- USB-C CC role 配错；
- regulator thermal budget 不够。

因此 Design Review 必须是人工工程活动。

---

# 3.9 原理图 Review 顺序

推荐固定顺序：

1. Power tree；
2. MCU power / VCAP / reset / boot；
3. Clock；
4. Debug；
5. USB；
6. CAN；
7. SDIO；
8. 外部 connector；
9. Test points；
10. BOM / DNP option；
11. ERC；
12. Cross-sheet net audit。

---

# 3.10 本章交付

创建：

`projects/stm32f407-mainline/v2/schematic-integration-review.md`

每个 finding 使用：

```text
ID:
Severity: Blocker / Major / Minor / Note
Block:
Observation:
Why it matters:
Source:
Required action:
Verification:
Status:
```

---

## 本章任务

至少人为制造并找出 6 个错误：

1. USB ESD 放在 MCU 一侧；
2. CAN 120 Ω 永久装；
3. SDIO_CLK series R 放在 card 端；
4. VCAP 接了一个额外负载；
5. microSD 没有 local decoupling；
6. SWD header 没 VTref/GND。

然后再进入 Placement。

下一章开始，所有逻辑关系都要变成二维空间关系。