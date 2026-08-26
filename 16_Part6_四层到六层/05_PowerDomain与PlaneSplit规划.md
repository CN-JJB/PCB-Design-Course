# 05｜Power Domain 与 Plane Split：电源铜不是拼图游戏

> 六层板多了 plane 资源以后，最容易出现的新错误是：把 power layer 切成很多“看起来很整齐”的岛，然后忘了这些岛同时会改变信号参考、电源电流路径、去耦回路和 EMI 结构。

---

# 1. Power plane 有两种角色

同一块 power copper 可能同时承担：

1. **DC / low-frequency power distribution**；
2. **某些信号的 high-frequency reference structure**。

这两个角色不一定冲突，但必须同时 Review。

例如 L4 是 3V3/1V8/1V2 多个岛：

- 对供电来说，它们可能很合理；
- 对邻近 signal layer 来说，每个 split 都是潜在 reference discontinuity。

所以不能只从 power tree 看 power plane。

---

# 2. STM32H7 为什么让这个问题更明显

ST 当前资料显示 STM32H743 具有更复杂的电源与功能域：

- VDD 主数字供电；
- VDDA / VREF 模拟相关；
- internal regulator / core-domain 相关引脚；
- USB 相关供电；
- 多个 power domain；
- 外部 SDRAM / Ethernet PHY 又会引入新的 rail。

AN4938 是 H74x/H75x 硬件开发的一手资料入口；真正 V3 原理图阶段必须按具体 package 和 power configuration 逐 pin 核对。

这里 Part 6 只建立架构方法，不提前抄一套电容值。

---

# 3. Plane Split 的三类风险

## 3.1 Signal crosses split

最直接：快速信号投影路径下方出现 plane gap。

结果：

- return current 绕路；
- loop area 变大；
- impedance 突变；
- common-mode conversion 风险上升。

## 3.2 Power island narrow neck

一个大面积 power island 通过很窄的 neck 接到 source。

可能造成：

- DC drop；
- spreading inductance 增加；
- transient current 受到限制；
- plane resonance / local impedance 改变。

## 3.3 Decoupling via geometry disconnect

电容在视觉上“跨在 GND 和 PWR 之间”，但：

- PWR via 绕很远；
- GND via 共享细 neck；
- capacitor 到 chip pin 的 current loop 很长。

plane 再大也补不回来 mounting loop 的问题。

---

# 4. 先做 Power-Region Map，再切铜

不要直接在 KiCad 里开始画 zone polygon。

先做：

| Rail | Source | Loads | Estimated current | Transient concern | Routing/reference conflict | Plane/trace strategy |
|---|---|---|---:|---|---|---|
| 3V3 | | MCU/IO | | | | |
| 1Vx | | PHY/Memory | | | | |
| VDDA | | analog | | | | |
| VREF | | ADC ref | | | | |

然后在 floorplan 上标：

- source；
- bulk；
- load cluster；
- high-di/dt local loop；
- signal corridors；
- connector boundary。

最后才决定某 rail 用 plane island、wide trace 还是 local pour。

---

# 5. “独立电源层”不等于所有 rail 都要铺 plane

对于小电流 rail：

- 一条受控宽度的短走线；
- local copper pour；
- point-of-load regulator 附近的小区域；

可能比为了“有电源层”切出一个巨大但狭长的 island 更好。

判断因素：

- current；
- transient load；
- voltage drop budget；
- return/reference role；
- routing obstruction；
- thermal；
- manufacturing / copper balance。

---

# 6. GND plane 优先保持完整

课程默认策略：

> **优先完整 GND，分割 power，而不是分割 GND 去迁就功能区。**

“模拟地 / 数字地必须割开”不作为默认规则。

对于 STM32H7 的 mixed-signal 设计，更重要的是：

- current path；
- analog supply filtering；
- VREF integrity；
- noisy return 不要穿过 sensitive region；
- ADC front-end 与 digital switching 的布局隔离。

是否物理分地必须由具体芯片指南和系统接口决定，而不是名字里有 `A`/`D` 就切地。

---

# 7. Plane Pair 与 Decoupling 的关系

如果 PWR/GND plane 靠得很近，可以形成 distributed capacitance，但它只是 PDN 的一部分。

仍然需要：

- on-package / on-die capacitance；
- local MLCC；
- bulk / regulator output network；
- low-inductance mounting；
- plane spreading path。

所以不要写：

> “六层有电源地平面对，所以可以少放去耦。”

这通常是错误的推理。

---

# 8. KiCad 实操

在 KiCad 中：

1. 给每个 rail 建清晰 net name；
2. zone 的 priority / clearance / thermal strategy 有依据；
3. 使用 Rule Area 防止关键 signal corridor 被错误 power island 侵入；
4. refill 后检查 narrow neck / orphan island；
5. 切换只看 plane layers，人工走查每条 critical route 的 reference；
6. 3D Viewer 不能替代 plane continuity review。

---

# 9. 本章任务

在 V3 的 `layer-role-map.md` 之外，再画一张：

`Power Region Overlay`

要求同时显示：

- rail region；
- signal corridor；
- intended reference；
- decoupling cluster；
- regulator hot loop；
- connector / chassis zone。

如果 power island 与 critical signal corridor 冲突，必须在 routing 前解决。

---

## 本章一句话

> **Power plane 不是彩色拼图；每一次切割都同时改变供电路径和电磁参考结构。**