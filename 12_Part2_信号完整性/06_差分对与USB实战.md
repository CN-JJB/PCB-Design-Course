# 06. 差分对与 USB 实战：等长只是最表面的一层

> **这一章为什么现在要学？**  
> USB D+/D− 是你在 STM32F407 V2 上最适合拿来学习差分布线的真实接口：有官方硬件指南、有连接器、有 ESD、有成对走线，而且速度比真正的 SerDes 更适合第一次练习。

<p align="center"><img src="../assets/svg/si-differential-fields.svg" width="900" alt="differential pair fields"></p>

---

## 6.1 差分接收端真正看什么

差分接收器主要关心：

\[
V_{diff}=V_P-V_N
\]

如果外界噪声同时给两根线加上相近的共模扰动：

\[
(V_P+V_n)-(V_N+V_n)=V_P-V_N
\]

理想情况下，共模成分被抵消。

但这要求两条路径足够对称；如果几何、延迟、阻抗不对称，共模与差模会互相转换。

---

## 6.2 差分不是“有两根线就自动抗干扰”

要让 pair 真正发挥作用，至少要关心：

- pair 两根线的 propagation delay；
- 差分 impedance；
- 几何对称；
- layer transition 对称；
- connector / ESD / pad transition 对称；
- pair 与 reference structure 的关系；
- pair 与其他网络的隔离。

因此：

> **“等长”是必要检查项之一，但绝不是差分设计的全部。**

---

## 6.3 Intra-pair skew：为什么两根线不能差太多

假设 P 比 N 长，P 的边沿更晚到达。

在这段时间差内：

- P/N 不再严格等幅反相；
- differential waveform 发生畸变；
- common-mode component 增加；
- 接收 eye margin 可能下降；
- EMI 可能变差。

但“允许差多少”必须来自具体 interface/device guide。

不要写统一：

> “所有差分对必须 ±0.1 mm。”

USB FS、USB HS、HDMI、PCIe、LVDS、MIPI 的 budget 完全不同。

---

## 6.4 Pair gap 为什么应该稳定

当两根线的 gap 突然变化：

- mutual capacitance / inductance 变化；
- odd-mode impedance 变化；
- differential impedance 出现 discontinuity。

因此正常 open-field routing 应保持稳定 pair geometry。

但 pad / connector / via breakout 区域不可避免会短暂 uncouple。我们的目标是：

- transition 尽量短；
- 两边对称；
- 不为了追求“全程固定 gap”做荒谬绕线。

KiCad 10 提供 `diff_pair_uncoupled` 约束，可对过长的 uncoupled section 做 DRC 检查。

---

## 6.5 差分对也需要参考面

“差分自己形成回路，所以完全不需要 GND plane”是错误的。

真实差分 pair 同时存在：

- P ↔ N 之间的耦合；
- P/N ↔ reference plane 的耦合；
- common-mode return current；
- connector/shield/chassis 等更大系统路径。

完整参考面有助于：

- 稳定阻抗；
- 控制 common mode；
- 减少环境变化；
- 让 layer transition 更可预测。

---

## 6.6 STM32F407 的 USB：先搞清楚你设计的是哪种模式

STM32F407 具有 USB OTG_FS，以及 OTG_HS 控制器；F407 的 HS 控制器要实现 USB High-Speed 480 Mbit/s 通常需要外部 ULPI HS PHY，但控制器也有 embedded FS PHY 可做 Full-Speed 工作。

本 V2 教学项目默认做：

> **USB Full-Speed device，12 Mbit/s，使用 STM32 embedded FS PHY。**

这意味着它比 USB HS 480 Mbit/s 宽容得多，适合第一次差分布局训练。

ST AN4879 当前版本明确说明：

- USB FS device/OTG 需要精确 48 MHz clock；
- ESD protection 应尽可能靠近 connector；
- VBUS 应远离 DP/DM；
- USB 的具体实现必须结合 MCU 型号和工作模式。

---

## 6.7 USB 阻抗数字怎么写才严谨

USB 生态中常见 90 Ω differential channel/trace 目标，但你不应该仅凭“大家都这么画”就写一个固定几何。

本课程流程：

1. 先确认你实现的是 FS 还是 HS；
2. 查 USB-IF 当前 specification / compliance requirements；
3. 查 ST AN4879 / MCU datasheet；
4. 锁定板厂 stackup；
5. 用板厂 field solver 反算 pair width/gap；
6. 记录 target、tolerance、来源和查询日期。

ST AN4879 对“作为 HS driver 一部分的 full-speed driver”给出 45 Ω ±10% 单端 impedance 说明，但**不要把这句话无条件复制到所有 STM32 embedded FS 场景**。课程以当前 USB-IF + 芯片官方 guide 的组合约束为准。

---

## 6.8 USB connector / ESD 的正确顺序

推荐从板边向 MCU 看：

```text
USB receptacle
     |
   ESD device   ← 尽可能靠近 receptacle
     |
  short, symmetric D+/D-
     |
   STM32 PHY
```

ESD protection 的目标是让 ESD 电流尽早被旁路，而不是让 surge 沿 D+/D− 先跑半块板再被钳位。

### 常见错误

```text
connector -------- 60mm trace -------- ESD -------- MCU
```

这里 ESD 器件虽然“原理图上有”，PCB 位置却失去大部分意义。

---

## 6.9 USB pair 周围不要放什么

尽量避免：

- switching regulator SW node；
- HSE oscillator；
- 大电流电源路径；
- 高速 clock 长距离平行；
- plane split；
- 不必要 test stub；
- 单边过孔/不对称 transition。

VBUS 也不应与 DP/DM 长距离贴近并行；ST AN4879 明确建议 VBUS 远离 DP/DM。

---

## 6.10 KiCad 10：真正用 Differential Pair Router

### 命名

KiCad 会根据成对命名识别差分：

- `USB_DP` / `USB_DN`（P/N suffix）；
- 或 `USB+` / `USB-`。

不要混用不被识别的 suffix。

### Board Setup

对 USB net class 设置来自你 stackup 求解的：

- differential pair width；
- pair gap；
- clearance。

### Routing

KiCad 10：

- Differential Pair Router：hotkey `6`；
- Pair Length Tuning：`8`；
- Pair Skew Tuning：`9`。

### 一个非常重要的工具事实

KiCad 的 tuner 可以帮你满足几何/长度 target，但它不会判断：

> 你为了等长塞进去的 meander 是否因为 spacing 太小而产生强 self-coupling。

所以 tuner 是工具，不是 SI judge。

---

## 6.11 蛇形线：不要为了 0.05 mm 的差值制造 20 mm 的问题

紧密 meander 的相邻段会彼此耦合，导致“几何长度增加”和“实际电气延迟增加”不再一一对应。

所以顺序应该是：

1. 先通过 placement / routing symmetry 自然等长；
2. 最后只修必要 skew；
3. meander spacing 留足，不做密集 accordion；
4. target 必须来自 protocol，而不是追求数字看起来为 0。

---

## 6.12 Fault Lab：四种差分“看起来正确”

### Fault A — 长度一样，gap 一路变化

长度报告 PASS，但 impedance discontinuity 很多。

### Fault B — D+ 过孔，D− 不过孔

长度可以调回来，但 transition 完全不对称。

### Fault C — 两根线都换层，但 return transition 不对称

pair 本身对称，reference structure 不对称。

### Fault D — 密集蛇形做到 0.01 mm skew

数字漂亮，但局部自耦合强、走线更长、更复杂。

---

## 6.13 Design Review

- [ ] USB mode（FS/HS）明确
- [ ] impedance target 有来源
- [ ] pair width/gap 与当前 stackup 对应
- [ ] DP/DM 全程环境大体对称
- [ ] ESD 靠近 connector
- [ ] VBUS 与 pair 不长距离并行
- [ ] 不跨 reference split
- [ ] layer transition 对称并审查 return structure
- [ ] skew target 来自需求，不追求无意义的绝对 0
- [ ] meander 不密集自耦合

---

## 6.14 本章任务

1. 为 V2 选择 USB receptacle 和 ESD part；
2. 从 ST AN4879 提取至少 5 条真正相关的硬件要求；
3. 用当前 stackup 计算 pair geometry；
4. 写进 `v2/si-routing-constraints.md`；
5. 在 KiCad 中用 differential router 完成 pair；
6. 用 skew tuner 只修真正需要的差值；
7. 做一次“几何对称性 Review”，不要只看长度数字。

---

## 参考资料

- ST AN4879, *USB hardware design guidelines for STM32 microcontrollers*: https://www.st.com/resource/en/application_note/an4879-usb-hardware-design-guidelines-for-stm32-microcontrollers-stmicroelectronics.pdf
- USB-IF Document Library / USB 2.0 Specification: https://www.usb.org/documents?search=usb%202.0
- KiCad 10 PCB Editor — differential routing and length tuning: https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html
