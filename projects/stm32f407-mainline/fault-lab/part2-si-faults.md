# Fault Lab — Part 2 Signal Integrity

> 每个故障都要求：**先预测 → 再看图/互动实验 → 再修改 → 最后把新规则写进 Review。**

---

## SI-F01｜同样 10 MHz，风险完全不同

### Bad Setup

- Clock A: tr = 10 ns, length = 20 mm
- Clock B: tr = 1 ns, length = 120 mm

### 问题

为什么不能用“都是 10 MHz”判断？

### 工具

`interactive/edge-rate-lab.html`

### 修复/结论

比较 flight time 与 edge time；对 B 做 transmission-line screening。

---

## SI-F02｜50 Ω 线中间突然加宽

### Bad Setup

```text
50Ω geometry → wide section → 50Ω geometry
```

### 预测

宽线局部 Z0 通常下降，两个 transition 产生相反方向的反射特征。

### 修复

保持通道几何连续；若 pad/connector 不可避免，缩短 transition 并用仿真/测量验证。

---

## SI-F03｜Source Resistor 放在 Receiver 旁

### Bad Setup

```text
MCU -------- long line -------- 33Ω -- receiver
```

### 为什么错

它没有把 driver output impedance 与 transmission line 在发射点匹配起来，不能按 source termination 的预期机制工作。

### 修复

```text
MCU -- Rseries -- line -------- receiver
```

并通过测量/模型选择实际值。

---

## SI-F04｜跨参考面 Slot

### Bad Setup

L1 快速线正下方 L2 GND 有开槽。

### 要求

手画 return current 绕行路径。

### 修复

优先改线/改 plane，让关键线全程有连续 reference。

---

## SI-F05｜换层只有 Signal Via

### Bad Setup

前后都是 GND-referenced signal layer，但 signal via 周围没有合理 return transition。

### 修复

根据 stackup/速度/guide，在 transition 周围提供紧凑的 reference-layer connection；不机械背固定 1 mm。

---

## SI-F06｜两根线按制造最小间距并行 80 mm

### Bad Setup

Clock aggressor 与 reset/interrupt victim 长距离并行。

### 工具

`interactive/crosstalk-lab.html`

### 修复选择

- 拉开 spacing；
- 缩短 parallel run；
- 让 trace 更靠近 reference plane；
- 调低可配置 slew rate；
- 改 layer/topology。

---

## SI-F07｜USB“长度一样”但几何一路乱变

### Bad Setup

- D+/D− 总长度数字相同；
- pair gap 在 connector、ESD、过孔之间不停变化；
- D+ 有一次单独 via transition。

### 结论

长度 PASS ≠ differential channel PASS。

### 修复

优先 geometry symmetry、transition symmetry、reference continuity，再做必要 skew correction。

---

## SI-F08｜为了 0.01 mm Skew 塞密集蛇形

### Bad Setup

本来只有很小 skew，却加入密集 accordion meander。

### 风险

相邻 meander segments 自耦合，几何长度和电气 delay 不再简单对应，同时增加 loss/discontinuity。

### 修复

只按真实 protocol budget 修必要 skew，并增加 meander spacing。

---

## SI-F09｜USB ESD 放在 MCU 旁

### Bad Setup

```text
USB connector ------ long DP/DM ------ ESD -- MCU
```

### 为什么错

外部 ESD surge 已沿 PCB 传播很远才遇到保护器件。

### 修复

ESD device 尽可能靠近 receptacle，并按器件 datasheet 设计其 return path。

---

## SI-F10｜示波器长地线制造“振铃”

### 实验

同一节点分别用：

- 普通长 ground lead；
- ground spring。

### 目标

学习先排除 measurement artifact，再对 PCB 下结论。

---

# Fault Lab 提交模板

每个 Fault 建议保存：

```markdown
## SI-Fxx

### Prediction

### Before

### Physical model

### Measurement / simulation

### Fix

### After

### New checklist item
```

最终目标不是收集“十大错误”，而是形成你自己的 SI Review 方法。