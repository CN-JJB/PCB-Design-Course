# Part 3｜Power Integrity：电源不是一根 3.3 V 线

> 本 Part 从一个最普通的问题开始：**STM32 已经接上 3.3 V，为什么还要在每个 VDD 旁边放 100 nF？**
>
> 答案不是“因为参考设计这么画”，而是：芯片在极短时间内会要求电流变化，电源网络必须在不同时间尺度上提供低阻抗的闭合电流路径。

---

## 这一 Part 要解决什么

完成 Part 2 后，我们已经会从 Signal / Return / Reference 的角度看高速信号。

现在把同一种思维搬到电源：

```text
芯片负载突然变化
        ↓
需要瞬态电流 ΔI
        ↓
VRM / LDO 来不及瞬间响应
        ↓
局部去耦电容先提供电荷
        ↓
电流经过 VDD → 芯片 → GND → 电容形成闭合回路
        ↓
回路阻抗决定电源跌落、噪声和地弹
```

所以 Power Integrity（PI）关心的不是“电源电压名义值是多少”，而是：

> **在负载真正工作的频率范围内，芯片看到的电源网络阻抗是否足够低。**

---

## 章节路线

1. [瞬态电流：为什么需要去耦](01_瞬态电流与去耦.md)
2. [真实电容：C、ESR、ESL 与自谐振](02_真实电容_ESR_ESL与自谐振.md)
3. [安装电感：为什么“位置”比电容值更重要](03_安装电感与布局.md)
4. [PDN 与 Target Impedance](04_PDN与目标阻抗.md)
5. [多电容网络与 Anti-Resonance](05_多电容与反谐振.md)
6. [电源/地平面、Ground Bounce 与 SSN](06_电源地平面与地弹.md)
7. [Buck Hot Loop：开关电源为什么最吃布局](07_Buck热环路与布局.md)
8. [如何正确测电源噪声](08_示波器测电源噪声.md)
9. [KiCad 中的 PI 落地与 Design Review](09_KiCad中的PI落地与Review.md)

---

## 本 Part 的主线项目

仍然是：

`STM32F407 V1 → STM32F407 V2`

V2 在 SI 之外新增 PI 目标：

- 为 VDD / VDDA / VCAP 建立来源明确的去耦方案；
- 不再把“100 nF 越近越好”停留在口号，而是分析安装电感；
- 记录 3.3 V rail 的负载预算与允许扰动；
- 区分 LDO 的低频供能角色与本地去耦的高频角色；
- 为将来的 STM32H7 / SDRAM / FPGA 建立 PDN target-impedance 思维；
- 增加一个 Buck 供电 Fault Lab，训练高 `di/dt` 回路布局；
- 增加电源噪声测量流程，避免被示波器探头自己骗到。

项目资产会放到：

`projects/stm32f407-mainline/v2/`

---

## 本 Part 不会教成什么样

### 不会把 100 nF 当魔法数字

STM32F407 的 VDD 去耦值有 ST 官方要求，但“为什么有效”必须从电荷、阻抗和寄生参数解释。

### 不会说“电容越大越好”

一个 10 µF MLCC 在实际 DC Bias 下可能没有 10 µF；一个很大的电容也可能因为 ESL 在高频已经表现得像电感。

### 不会把 Target Impedance 当万能 sign-off

目标阻抗是非常重要的 PI 工具，但具体高速 SoC/DDR 的签核方法会依器件厂商而变。我们先把它当作工程思维和设计约束框架。

### 不会把 Buck 的 SW 节点当普通网络

Buck 的关键不是把所有线都加粗，而是识别**高 `di/dt` 的不连续电流环路**，优先压缩该环路面积。

---

## 本 Part 的可视化

静态 SVG：

- 瞬态电流来源；
- 真实电容 RLC 模型与阻抗曲线；
- 好/坏去耦安装回路；
- PDN 频率分工；
- Anti-Resonance；
- Plane pair；
- Ground Bounce；
- Buck hot loop；
- 正确/错误示波器探测。

互动实验：

- Decoupling Impedance Lab；
- Target Impedance Lab；
- Buck Hot Loop Lab。

互动页面用来建立趋势直觉，不冒充厂商电容 S 参数、SPICE、PIA 或 3D EM 求解器。

---

## 一手资料基线

本 Part 的工程约束优先来自：

- ST AN4488：STM32F4 电源与去耦要求；
- STM32F407 Datasheet；
- TI Power Delivery Network Analysis；
- TI Good Buck Converter Layout Practices / Buck Converter Layout Considerations for Radiated EMI；
- Murata / TDK MLCC DC Bias 与元件模型资料；
- KiCad 9 PCB Editor 官方文档。

> 数字分三类：**器件要求、设计目标、教学示例**。正文会明确它们的身份，不混在一起。

---

## 学完后怎样算“会 PI”

给你一块 MCU 板，你应该能回答：

1. 芯片电流突然变化时，最先从哪里拿到电荷？
2. 为什么 LDO 明明就在板上，却不能替代芯片旁边的 100 nF？
3. 这颗电容在目标频率下到底像 C、R 还是 L？
4. 哪段 PCB 几何构成了去耦回路的主要安装电感？
5. 什么是 PDN impedance，什么是 target impedance？
6. 为什么混放多个电容值可能产生反谐振峰？
7. Ground Bounce 的 `L·di/dt` 从哪里来？
8. Buck 哪个回路是真正必须最小的 hot loop？
9. 为什么普通 10 cm 示波器地线很容易把“电源噪声”测大？
10. 在 KiCad 中你会如何把这些知识转成 placement、zone、via 与 Review 动作？

如果只能回答“每个 VDD 放一颗 100 nF”，还没有学会 PI。


## 补充：DC Power Integrity

11. [DC Power Integrity：IR Drop、电流密度与热](11_DC_Power_Integrity_IRDrop与电流密度.md)

PI 不只等于去耦和 Ztarget。毕业 Review 必须同时覆盖 DC drop、瞬态、频域阻抗、热与测量。
