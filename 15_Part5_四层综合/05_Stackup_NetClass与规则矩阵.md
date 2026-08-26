# 05｜Stackup、Net Class 与规则矩阵：规则不是“高速线统一一个宽度”

> V2 进入布线前，必须把“哪些网络属于哪一类、为什么这样约束、约束来自哪里”写清楚。否则你会在 PCB Editor 里边画边猜。

---

# 5.1 四层 Stackup 先冻结

沿用 Part 1 的基本策略：

```text
L1  Signal / Components
L2  Solid GND reference
L3  Power / low-risk distribution
L4  Signal / Components
```

但 Part 5 比 Part 1 多了接口和并行总线，所以必须重新确认：

- 板厂当前 4-layer stackup；
- L1→L2 dielectric height；
- L4→L3 dielectric height；
- copper thickness；
- controlled impedance capability；
- minimum trace/space/via；
- finished board thickness；
- soldermask assumptions。

**阻抗线宽只能在 stackup 冻结后确定。**

---

# 5.2 L2 保持完整 GND

V2 的纪律：

> L2 不作为“布不下时的救火层”。

L2 是：

- USB return reference；
- SDIO return reference；
- CAN logic return；
- MCU decoupling return；
- EMC 基础结构。

允许在 L2 出现的主要对象：

- GND plane；
- GND vias / antipads；
- 必要的 mechanical clearances。

不要为了少一根 via 把它切碎。

---

# 5.3 L3 的角色

L3 可以承载：

- 3V3 plane/pour；
- 5V local distribution；
- 低风险 power islands；
- 必要低速 signal（如果确实需要且 reference 被分析）。

但一旦 L4 signal 参考 L3，就要问：

- 下面是不是同一个连续 reference structure；
- 有没有 power split；
- return current 怎么回到 source domain；
- 换层时 reference transition 怎么完成。

所以 Part 5 的关键接口尽量优先 L1/L2。

---

# 5.4 先做 Network Inventory

把所有 net 分组：

## Class A：Power / special analog

- 5V；
- 3V3；
- VDDA；
- VCAP（special, not general power）；
- GND。

## Class B：USB differential

- USB_DP；
- USB_DM。

## Class C：SDIO clock

- SDIO_CK。

## Class D：SDIO data/command

- SDIO_CMD；
- SDIO_D0~D3。

## Class E：CAN logic

- CAN_TX；
- CAN_RX；
- optional mode control。

## Class F：CAN bus

- CANH；
- CANL。

## Class G：Clock / oscillator

- HSE_IN/OUT；
- LSE if used。

## Class H：Debug / low-speed

- SWDIO；
- SWCLK；
- UART；
- LEDs；
- keys。

---

# 5.5 Rule Matrix 要包含“来源”

推荐表格：

| Net/Class | Width/Geometry | Spacing | Length/Skew | Layer/Reference | Source | Verification |
|---|---|---|---|---|---|---|
| USB DP/DM | from stackup solver | pair-specific | interface need | L1 over L2 | ST/USB/board fab | DRC + visual + measurement |
| SDIO_CLK | design width | aggressor spacing | short/controlled | L1 over L2 | RM0090 + errata + project | review + scope |
| SDIO D0~D3 | design width | group spacing | group budget | L1 over L2 | project constraint | review |
| CANH/L | bus geometry | pair symmetry | not “length match” focus | connector zone | transceiver/ref design | visual + bus test |
| 3V3 | current-based | clearance | n/a | L3/Top pours | PI budget | voltage/temp |

规则文件必须让后来的人知道：

> “这个数字为什么存在？”

---

# 5.6 USB differential geometry

不要从网上抄：

```text
w = 0.20 mm
s = 0.15 mm
```

正确流程：

1. 冻结 fab stackup；
2. 定义 USB differential impedance target（按当前 USB/ST guidance）；
3. 用板厂/field solver 算 `w / s`；
4. 确认线宽线距在 fab capability 内；
5. 写入 KiCad Net Class / custom rule；
6. 下单时按板厂 controlled-impedance 流程确认。

USB FS 不是最严苛 SerDes，但仍值得训练正确方法。

---

# 5.7 SDIO Rule Matrix

SDIO 不应直接套 USB 的规则。

重点通常是：

- CLK 尽量短；
- CLK 与其他组保持合理隔离；
- CMD/D0~D3 不出现巨大长度 outlier；
- via 数量少；
- reference 连续；
- source resistor footprint 可用；
- group 环境一致。

长度容差不要从 DDR 规则硬搬过来。

真正需要多严格，要结合：

- SDIO_CK；
- edge rate；
- trace delay；
- card input timing；
- STM32 timing；
- measurement。

---

# 5.8 CANH/CANL 不等于“高速差分对”同一套规则

CAN 是 differential bus，但关注点和 USB/SerDes 不完全相同。

重点：

- CANH/CANL 几何对称；
- connector/protection/CMC 不制造严重 asymmetry；
- bus stub 受控；
- termination 与 topology 正确；
- common-mode / transient path；
- transceiver datasheet layout guidance。

不要因为 KiCad 有 Differential Pair Router，就认为所有 differential bus 的设计逻辑都一样。

---

# 5.9 Power Width 不能只靠“1 A = 1 mm”口诀

Power geometry 应考虑：

- current；
- copper thickness；
- allowed temperature rise；
- trace vs plane；
- via current；
- voltage drop；
- transient path；
- thermal spreading。

V2 的 3V3 大部分应尽量用 plane/pour + short local neck，而不是一条细长“电源线”。

---

# 5.10 KiCad 规则落地

建议至少建立：

```text
Default
USB_FS
SDIO_CLK
SDIO_BUS
CAN_LOGIC
CAN_BUS
POWER_3V3
POWER_5V
DEBUG
```

并使用：

- Net Classes；
- Differential Pair settings；
- Board Setup → Constraints；
- `.kicad_dru` Custom Rules；
- DRC。

但要牢记：

**Custom Rule 只是自动检查器，不是物理原因本身。**

---

# 5.11 一条规则的完整生命周期

例如 USB pair：

```text
Requirement
→ current USB/ST spec says differential target
→ board stackup gives dielectric/copper
→ solver gives w/s
→ KiCad rule enforces geometry
→ DRC checks implementation
→ Gerber/fab checks actual stackup
→ optional TDR/functional test verifies result
```

这就是“工程闭环”。

---

# 5.12 本章交付

创建：

`projects/stm32f407-mainline/v2/integration-rule-matrix.md`

每一条规则必须包含：

```text
Net/Class
Rule
Type: physical / device / interface / fab / project
Source
Reason
How enforced in KiCad
How manually reviewed
How verified on hardware
```

---

## 本章任务

找出 10 条你以前可能会写成口诀的规则，把它们改写成：

> 条件 + 来源 + 目的 + 验证方法。

下一章开始真正的 Routing Priority。