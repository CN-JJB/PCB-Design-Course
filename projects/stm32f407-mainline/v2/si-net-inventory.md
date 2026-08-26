# V2 SI Net Inventory

> 这张表是 Part 2 的核心工程资产。每个精确数字都要写来源；没有来源就标 `assumption`。

| Net / Group | Source | Load | Topology | Edge / Data info | Planned layer | Reference | Impedance target | Length / Skew | Spacing | Termination | Constraint source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| USB_DP / USB_DM | STM32F407 FS PHY | USB receptacle | point-to-point diff | USB FS 12 Mbit/s | L1 | L2 GND | TBD from current USB/ST/fab flow | pair symmetry | TBD by solver | PHY-defined | ST AN4879 + USB-IF + fab | TODO |
| SDIO_CK | STM32F407 | SD connector/card | point-to-point | GPIO edge TBD | L1 | L2 GND | not assumed | TBD | enlarged vs default if needed | source R footprint | datasheet/IBIS/measurement | TODO |
| SPI_SCK | STM32F407 | external connector/device | point-to-point | GPIO edge TBD | L1 | L2 GND | not assumed | TBD | review | source R footprint | device/measurement | TODO |
| HSE loop | oscillator pins | crystal network | local resonant loop | analog oscillator | L1 | local GND environment | N/A | very short/symmetric | isolate | N/A | ST oscillator guide | TODO |
| SWDCLK | debugger | STM32 | point-to-point | debugger dependent | L1 | L2 GND | not assumed | short | review | optional | debug interface practical | TODO |

---

## 使用规则

1. **不要因为 net 名叫 CLK 就自动填 50 Ω。**
2. `Impedance target` 只有协议/器件/设计确实需要时才填。
3. `Edge / Data info` 优先记录 rise/fall/source model，而不只写 MHz。
4. `Reference` 必须能在实际 PCB 上连续指出。
5. `Termination` 写 topology 和位置，不只写阻值。
6. `Constraint source` 必须可追溯。
7. PCB 修改后同步更新此表。

---

## Review 问题

对每一行逐条问：

- source 真的是唯一 source 吗？
- load 是一个还是多个？有没有 stub？
- rise time 从哪里来？
- line delay 大概多少？
- reference plane 是哪一层？
- 有没有 plane slot / void？
- 换层时 return path 怎么过渡？
- impedance 数字来自哪里？
- spacing 是制造最小值，还是 SI 约束？
- 有没有测量方法？
