# 11｜Final Design Review：什么时候可以说“这块四层板我真的会了”

> V2 的毕业标准不是“DRC 绿了”，也不是“USB 能枚举”。你要能够解释整块板，并且知道剩余风险在哪里。

---

# 11.1 Final Review 的输入

必须有：

- frozen schematic；
- frozen PCB；
- stackup；
- rule matrix；
- SI review；
- PI review；
- EMC review；
- DFM checklist；
- BOM risk register；
- release package；
- bring-up/validation results；
- open bug list。

缺任何一项，Final Review 都只能算阶段 Review。

---

# 11.2 先讲系统，不看 PCB

你应该能在白板画出：

```text
USB 5V
→ 3.3V
→ STM32F407
   ├─ USB FS → USB-C
   ├─ CAN → PHY → CAN connector
   ├─ SDIO → microSD
   └─ SWD/UART
```

并解释：

- 电源怎么来；
- 每个接口为什么存在；
- 哪些接口对外；
- 哪些路径是敏感/高速/瞬态路径。

如果只能靠打开 schematic 才说得清，系统理解还不够。

---

# 11.3 Stackup Review

你必须回答：

### 为什么 L2 是完整 GND？

不能回答：

> “因为四层板都这么做。”

应该回答：

- 给 L1 关键信号提供连续 reference；
- 缩小 return loop；
- 降低串扰和共模转换风险；
- 给 decoupling/接口提供低阻抗 return structure。

### 为什么 L3 不是万能 reference？

因为：

- L3 可能包含 power islands/splits；
- L4 signal 的 return 取决于实际 reference structure；
- GND↔PWR reference transition 需要高频 return path。

---

# 11.4 USB Review

现场回答：

1. D+/D- 从 MCU 到 connector 的完整路径；
2. 为什么 ESD 在那个位置；
3. ESD current 最终往哪里走；
4. differential impedance 如何由 stackup 决定；
5. 为什么没有大量蛇形；
6. Shield 怎么处理，为什么；
7. CC1/CC2 role；
8. VBUS 怎么进入 power tree；
9. 如果 USB 不枚举先查什么。

---

# 11.5 CAN Review

回答：

1. bxCAN controller 与 CAN transceiver 的区别；
2. 为什么 TCAN33x/类似 PHY 能支持更高速能力但本板仍是 classic CAN；
3. 120 Ω 什么时候装；
4. CANH/CANL 的 transient path；
5. TVS / CMC footprint 的作用和代价；
6. connector cable 怎么影响 EMC；
7. 如何验证 termination/topology；
8. CAN error counter 能告诉你什么。

---

# 11.6 SDIO Review

回答：

1. 为什么 CLK 最先布；
2. source resistor 为什么在 MCU 侧；
3. CMD/D0~D3 为什么不追求“零误差等长”；
4. card power transient 从哪来；
5. L2 reference 是否连续；
6. ES0182 有哪些项目相关限制；
7. firmware 如何规避 hardware flow control / NEGEDGE 等限制；
8. 写卡错误如何区分 SI、PI、firmware、connector。

---

# 11.7 Power Review

回答：

- 5V → 3V3 power path；
- regulator thermal loss；
- 3V3 worst-case current；
- microSD transient margin；
- VCAP 为什么特殊；
- 每个 VDD decoupling loop；
- 3V3 plane 有没有 neck；
- 测 ripple 时为什么不用长 ground lead。

---

# 11.8 EMC/ESD Review

回答：

- USB cable 的 common-mode path；
- CAN cable 的 common-mode path；
- reference slot 如何产生 common-mode conversion；
- TVS 为什么不能只看“离接口多少 mm”；
- near-field probe 能证明什么、不能证明什么；
- CMC 为什么不是万能药；
- shield/chassis/system GND 的角色。

---

# 11.9 DFM Review

回答：

- 当前板厂 stackup；
- 最小工艺；
- USB controlled-impedance release note；
- critical footprint 是否核 datasheet；
- DNP policy；
- BOM alternate；
- testpoint access；
- Gerber viewer 检查结果；
- release commit SHA。

---

# 11.10 风险不是“全部消灭”，而是全部知道

Final Review 允许存在风险，但不能存在**不知道的风险**。

例如：

```text
Risk: AP2112 thermal margin limited at continuous SD write + max CPU
Severity: Major
Evidence: calculated dissipation + temperature measurement
Mitigation: V2 usage limit / V3 replace with buck
Owner: Hardware
Status: Accepted for teaching V2
```

这比假装“没有问题”更工程化。

---

# 11.11 四层毕业 Checklist

## Architecture
- [ ] 能画完整 block diagram
- [ ] 能解释每个接口存在原因

## Schematic
- [ ] power tree 可解释
- [ ] MCU special pins 可解释
- [ ] USB/CAN/SDIO 约束有一手来源

## Layout
- [ ] placement priority 可解释
- [ ] critical current loop 可画出
- [ ] reference plane 可指出

## SI
- [ ] transmission-line 判断不是靠 MHz 口诀
- [ ] impedance 来源明确
- [ ] reflection/termination 可解释
- [ ] USB/SDIO/CAN 差异能说清

## PI
- [ ] decoupling loop 可画出
- [ ] ESR/ESL/DC bias 知道为什么重要
- [ ] power budget / thermal budget 有记录

## EMC
- [ ] DM/CM 可区分
- [ ] connector/cable path 可分析
- [ ] ESD discharge path 可画出

## DFM
- [ ] fab/assembly/test 可交付
- [ ] Gerber release 可追溯

## Bring-up
- [ ] 有 staged plan
- [ ] bug 使用 evidence-driven 流程

全部做到，才算通过 Part 5。

---

# 11.12 下一步为什么要上六层

到此你会发现四层不是“不够高级”，而是**资源开始变紧**：

- L2 必须保护为 GND；
- L3 又要 power；
- Bottom 关键 signal reference 不总是理想；
- 接口越来越多时 routing channel 紧张；
- 多 power domain 会挤压 L3；
- 更高速 parallel bus 会需要更稳定的 routing/reference environment。

这就是 Part 6 的入口：

> **不是因为“六层更高级”而上六层，而是因为四层的物理资源不再满足系统目标。**

---

## 本章最终交付

创建：

`projects/stm32f407-mainline/v2/final-design-review.md`

并写一段 500~1000 字的 V2 设计说明：

> “如果把这块板交给另一个工程师，我希望他理解哪些最关键的设计决策？”

这份说明比一张漂亮 3D Render 更能证明你真的学会了。