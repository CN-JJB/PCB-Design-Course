# 02｜Pin 规划、时钟与资源冲突：综合板从这里开始真正“挤”起来

> MCU 引脚很多，不代表你可以最后再分配。综合板最痛苦的返工之一，就是 PCB 已经布局完成，才发现 USB、SDIO、CAN、SWD、晶振或 Boot pin 互相抢脚。

---

# 2.1 Pin Planning 的目标不是“把线连上”

真正目标是同时满足：

1. 外设功能正确；
2. Alternate Function 合法；
3. debug/boot 不被误占；
4. 关键接口从 MCU 到 connector 的物理方向合理；
5. 高速/时钟网络不被迫穿过整块板；
6. 电源/地引脚周围还有去耦空间；
7. pin swap / remap 不会破坏 firmware 维护。

所以 pin planning 是**原理图设计 + PCB floorplan 的联合问题**。

---

# 2.2 先画 Peripheral Map

先不看封装引脚，列功能：

```text
USB FS
  DP
  DM
  VBUS sense (if used)

CAN1
  TX
  RX

SDIO 4-bit
  CK
  CMD
  D0
  D1
  D2
  D3

Debug
  SWDIO
  SWCLK
  NRST
  SWO (optional)

Clock
  HSE_IN
  HSE_OUT
  LSE_IN / LSE_OUT (if used)

Console
  UART_TX
  UART_RX
```

然后才映射到 STM32 alternate functions。

---

# 2.3 关键原则：先分“不可随便动”的脚

优先级建议：

## 第一优先级：固定或强约束

- VDD / VSS；
- VCAP；
- VDDA / VSSA；
- HSE / LSE；
- NRST；
- BOOT；
- USB DP/DM；
- SWDIO / SWCLK。

## 第二优先级：接口成组

- SDIO CLK/CMD/D0~D3；
- CAN TX/RX；
- UART debug。

## 第三优先级：普通 GPIO

- LED；
- key；
- chip-select；
- optional control pins。

这个顺序本质上是在保护**未来最难改的东西**。

---

# 2.4 USB 引脚要和 connector floorplan 一起看

你最终想要的是：

```text
MCU USB pins
   ↓ 短、直接
ESD / optional tuning footprint
   ↓
USB-C connector at board edge
```

如果 pin assignment 导致 USB 从 MCU 左侧出来，而 connector 被机械要求固定在最右边，你就已经制造了跨板 routing 问题。

因此 pin planning 时必须把 MCU 暂时放在一个草图板框里。

不是精确 Placement，只做方向判断：

- USB 口在哪；
- CAN 在哪；
- microSD 在哪；
- SWD 在哪；
- MCU 哪一边对哪个接口最友好。

---

# 2.5 SDIO 是最值得提前规划的一组

SDIO 至少包含 6 根关键线：

```text
CK
CMD
D0
D1
D2
D3
```

如果 MCU pin 分布和 microSD connector 方向不协调，很容易出现：

- 大量交叉；
- 多次换层；
- CLK 被迫绕远；
- D0~D3 为了等长做大量无意义蛇形；
- connector 下方逃线困难。

所以 microSD connector 的 pin order 也要进入 floorplan。

> 这里的第一目标不是“绝对等长”，而是**让组内路由环境简单、reference 连续、CLK 受控、没有巨大 outlier**。

---

# 2.6 SDIO Clock 还要检查 silicon errata

STM32F407 的 ES0182 对 SDIO 有明确限制。

所以 pin planning 完成后，项目文档里要额外记录：

```text
SDIO controller: STM32F407 SDIO
Bus width: 4-bit
Target SDIO_CK: [设计值]
Hardware flow control: do not use per errata
NEGEDGE: avoid per errata
BYPASS: verify per current errata
DMA / PCLK2 / SDIO clock relationship: firmware validation required
```

这是“PCB 与 firmware 的接口契约”。

好的硬件工程师不会把 silicon errata 扔给软件团队一句“你们自己看”。

---

# 2.7 CAN 不是只分配两个 GPIO

逻辑侧：

```text
CAN_TX → transceiver TXD
CAN_RX ← transceiver RXD
```

但你还要提前考虑：

- transceiver standby/silent pin 是否需要 MCU 控制；
- transceiver logic supply 是 3.3 V 还是 VIO；
- connector 在哪；
- termination enable 怎么做；
- TVS / CMC footprint 需要多少空间；
- bus ground / shield / chassis 是否有结构需求。

所以 CAN 的 pin planning 其实是一个**完整接口区域规划**。

---

# 2.8 Clock Tree 要和 USB / SDIO 一起冻结

STM32F407 有 USB / SDIO 对时钟域的共同要求。

RM0090 说明 SDIO adapter clock 最高可到 50 MHz，并且当 USB 使用时常见 48 MHz domain 会进入设计约束。

你必须在项目早期冻结：

- HSE frequency；
- PLL 规划；
- USB 48 MHz 来源；
- SDIO clock target；
- APB2 clock；
- firmware 是否需要 RNG 等共享 48 MHz 域的外设。

不要等 PCB 打样后才发现你想要的时钟组合碰到了 silicon errata 或时钟树限制。

---

# 2.9 SWD 是产品接口，不是临时飞线

SWD 至少要保证：

- SWDIO；
- SWCLK；
- GND；
- VTref / 3V3 reference；
- NRST 推荐带出；
- connector orientation 明确。

实物上还要问：

- 下载器能插吗？
- USB/CAN 线插着时会挡住吗？
- 装壳以后还能访问吗？
- pogo fixture 从哪一面接触？

Part 1 的“物理可访问性”在 V2 继续保留。

---

# 2.10 Pin Conflict Matrix

建议建立表：

| Function | Preferred Pin | Alternate | Conflict | Physical Direction | Final |
|---|---|---|---|---|---|
| USB_DP | datasheet AF | — | — | toward USB edge | ☐ |
| USB_DM | datasheet AF | — | — | toward USB edge | ☐ |
| SDIO_CK | datasheet AF | alt | [list] | toward microSD | ☐ |
| SDIO_CMD | ... | ... | ... | toward microSD | ☐ |
| CAN_TX | ... | ... | ... | toward CAN zone | ☐ |
| CAN_RX | ... | ... | ... | toward CAN zone | ☐ |
| SWDIO | fixed/debug | — | do not repurpose | debug edge | ☐ |

**Pin number 和 AF number 必须从当前 STM32 datasheet/reference manual/CubeMX 核对，不要从本教材抄固定数字。**

这是因为封装、型号、revision 和 alternate function 都可能不同。

---

# 2.11 KiCad + STM32CubeMX 的协作方式

推荐：

1. CubeMX 用来检查 peripheral / pin / clock conflict；
2. 项目文档记录最终 pin map；
3. KiCad schematic 才作为硬件 release source；
4. CubeMX 改 pin 后，必须人工同步并做 schematic review；
5. 不把自动生成工具当单一真相源。

为什么？

CubeMX 很擅长告诉你：

> 这个 pin 能不能配置成 SDIO_D1。

但它不会替你判断：

> 这个 pin 导致 D1 在 PCB 上必须绕 MCU 半圈，是否值得换另一个映射。

---

# 2.12 本章 Review

在进入原理图综合前：

- [ ] USB pin 已冻结；
- [ ] SDIO 6 根线已冻结；
- [ ] CAN logic pins 已冻结；
- [ ] SWD / NRST 未被误占；
- [ ] HSE/LSE pin 已确认；
- [ ] 关键接口方向与板边有初步 floorplan；
- [ ] clock tree 已能支持 USB/SDIO 目标；
- [ ] ES0182 SDIO 限制已写入 firmware constraints；
- [ ] Pin Conflict Matrix 已保存到 Git。

---

## 本章任务

创建并填写：

`projects/stm32f407-mainline/v2/pin-clock-plan.md`

下一章正式把 USB、CAN、SDIO、电源和 MCU 合到一张可 Review 的原理图里。