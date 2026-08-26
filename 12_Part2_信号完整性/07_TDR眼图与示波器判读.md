# 07. TDR、眼图与示波器判读：从波形反推 PCB

> **这一章为什么现在要学？**  
> 因为 SI 不能只靠“看布局觉得不错”。真正工程闭环是：**设计 → 仿真/预测 → 测量 → 归因 → 修改。** 本章不要求你马上买昂贵仪器，而是先学会这些图到底在说什么。

<p align="center"><img src="../assets/svg/si-eye-and-tdr.svg" width="900" alt="eye diagram and TDR"></p>

---

## 7.1 示波器上的一个方波，能告诉你什么

看一个数字边沿时，至少观察：

- rise/fall time；
- overshoot / undershoot；
- ringing frequency；
- ringing decay；
- threshold crossing；
- source 与 load 的差异；
- 周期性 jitter；
- noise floor。

但一个波形只能告诉你“发生了什么”，不自动告诉你“为什么”。

例如 overshoot 可能来自：

- transmission-line reflection；
- probe ground inductance；
- package resonance；
- supply bounce；
- measurement bandwidth/setup。

所以工程判断必须结合 topology 和测量位置。

---

## 7.2 先学会不被探头骗

普通无源探头的长 ground lead 本身就是明显电感。

快边沿测量优先：

- ground spring；
- 极短 ground connection；
- 合适带宽探头；
- 在真正 receiver pin 附近测；
- 避免随意焊很长飞线。

### 一个简单验证

同一个节点：

1. 长鳄鱼夹地线测一次；
2. ground spring 测一次。

如果 ringing 大幅变化，你看到的一部分“SI 问题”其实属于 measurement loop。

---

## 7.3 TDR 是什么

TDR = Time Domain Reflectometry。

核心过程：

1. 向 DUT 发一个已知快速阶跃；
2. 阶跃沿 interconnect 传播；
3. 遇到 impedance discontinuity 产生反射；
4. 观察反射随时间变化；
5. 用传播延迟把“时间”映射到“位置”。

所以 TDR 很像：

> 给走线发一声“回声测试”，从回声判断哪里变宽、变窄、开路、短路或 transition 不连续。

---

## 7.4 TDR 上“向上”和“向下”是什么意思

在简化单 discontinuity 情况：

- 局部阻抗高于 reference Z0 → 正反射 → TDR 往上；
- 局部阻抗低于 reference Z0 → 负反射 → TDR 往下。

典型：

| 结构 | TDR 直觉 |
|---|---|
| open | 大幅向上 |
| short | 大幅向下 |
| 线突然变窄、Z 上升 | bump |
| 大 pad / 额外 capacitance | 可能先向下 |
| via inductive discontinuity | 可能表现为向上特征 |

真实 via/connector 是分布 RLC 结构，不能只凭“向上/向下”一句话完成建模。

---

## 7.5 TDR 的空间分辨率受边沿限制

更快的 TDR edge 可以分辨更小的结构。

直觉：

> 如果测试脉冲本身在空间上“很长”，两个很近的 discontinuity 会糊在一起。

因此：

- 测几十厘米线不一定需要极端快边沿；
- 想看 BGA/via/pad 细节需要更高带宽、更快 rise time。

测量设备的 rise time 就像显微镜的分辨率。

---

## 7.6 Eye Diagram 到底是什么

眼图不是一次波形，而是把很多 bit interval 对齐后叠加。

它把大量模式、噪声和 jitter 压缩成一个“接收窗口”视觉图。

主要看：

- **eye height**：垂直噪声/幅度 margin；
- **eye width**：水平 timing margin；
- crossing distribution；
- overshoot / ringing；
- deterministic/random jitter；
- mask margin（若协议规定）。

> **眼睛越开，一般代表接收判决余量越大；但是否合规必须看具体协议 mask/test method。**

---

## 7.7 什么会把眼图“关上”

### Reflection

阻抗不连续让多个延迟副本叠加。

### Loss

高频成分被更强衰减，边沿变慢，ISI 增加。

### Crosstalk

邻道模式相关噪声叠加到 victim。

### Jitter

边沿横向漂移，eye width 变小。

### Supply/ground noise

threshold 和 driver amplitude 被调制。

### Skew / mode conversion

差分对失去对称，common-mode 与 differential-mode 互换。

---

## 7.8 STM32F407 V2 需要做眼图吗？

对 USB FS、普通 SPI/SDIO 学习项目：

- 你不需要为了“显得高级”强行做完整高速 SerDes eye compliance；
- 但眼图概念非常值得提前学，因为 Part 7 六层高速板会真正用到。

当前阶段更实用的是：

- 比较 source/load edge；
- 观察 ringing；
- 验证 series resistor；
- 检查 USB waveform 是否明显畸变；
- 理解 compliance 测试是协议定义的，不是看“波形漂亮”就算 PASS。

---

## 7.9 TDR 和示波器如何组合定位问题

一个推荐思路：

### 波形告诉你“症状”

例如 receiver 有双台阶。

### TDR 告诉你“哪里不连续”

例如 connector 后 15 mm 出现明显低阻抗 dip。

### PCB 结构告诉你“为什么”

打开 layout，发现那里有一个巨大 test pad。

于是形成：

```text
waveform symptom
      ↓
TDR location
      ↓
layout geometry
      ↓
physical model
      ↓
fix
```

这才是 SI 调试，而不是“看到振铃就加电阻”。

---

## 7.10 Fault Lab：测量归因练习

### Case A

接收端 overshoot，但换 ground spring 后消失大半。

结论：先修测量方法。

### Case B

source 干净，load 有规律 staircase，时间间隔约等于 `2td`。

优先怀疑：reflection / round-trip。

### Case C

某一段 TDR 明显向下，PCB 对应位置有大面积 pad。

优先怀疑：局部 capacitive discontinuity。

### Case D

eye horizontal opening 变窄，但 amplitude 尚可。

优先排查：timing jitter / ISI / crosstalk，而不是只盯直流电压。

---

## 7.11 测量设备分三级

### Level 1 — 学习必备

- 普通示波器；
- 合理探头；
- logic analyzer。

可做：边沿、振铃、source/load 比较。

### Level 2 — 进阶

- 更高带宽 scope；
- differential probe；
- 简单 TDR/fast step setup。

可做：差分 waveform、反射定位。

### Level 3 — 专业 SI

- 高性能 TDR；
- VNA；
- compliance fixture/software；
- channel simulator。

可做：S-parameter、de-embedding、eye/mask、channel characterization。

本教材不会要求你买齐 Level 3 才能继续。

---

## 7.12 Design Review

- [ ] 测量点靠近真正的 receiver/source node
- [ ] probe connection 不形成巨大 loop
- [ ] 波形问题先区分 measurement artifact 与 DUT behavior
- [ ] 会用 flight time 解释重复反射间隔
- [ ] TDR interpretation 与 PCB 物理位置对应
- [ ] eye diagram 不脱离 protocol mask/spec 单独判 PASS
- [ ] 不从一个截图直接跳到唯一根因

---

## 7.13 本章任务

1. 画一张 V2 的 source/load 测量点图；
2. 为 SPI_SCK 预留 source 与 load 两个可探测位置；
3. 设计一页“长地线探头 vs ground spring”的实验记录模板；
4. 用 Reflection Lab 预测一个 100 mm 线的 round-trip 时间；
5. 写出如果 scope 上看到同样时间间隔的 ringing，你会如何验证。

---

## 参考资料

- Analog Devices, *Propagation Delay Measurements Using TDR*: https://www.analog.com/en/resources/technical-articles/propagation-delay-measurements-using-tdr-timedomain-reflectometry.html
- Keysight, *How to Analyze PCB Signal Integrity*: https://www.keysight.com/us/en/use-cases/analyze-pcb-signal-integrity.html
- Tektronix, *TDR Test*: https://www.tek.com/en/documents/primer/tdr-test
- Tektronix, *The Basics of Serial Data Compliance and Validation Measurements*: https://www.tek.com/en/documents/primer/basics-serial-data-compliance-and-validation-measurements
