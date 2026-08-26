# Fault Lab｜Part 3 Power Integrity

> 每个故障都要求：**症状 → 电流回路 → 寄生参数假设 → 测量计划 → KiCad 修改 → Before/After → Checklist**。

---

## PI-01｜“漂亮电容排”离 MCU 太远

### 故障

所有 100 nF 排成整齐一列，距离 MCU 15~25 mm。

### 为什么 DRC 看不见

网络连接正确，间距也合法。

### 物理问题

local transient loop 被拉长，安装电感增加。

### 修复

把电容按 VDD pin ownership 分散到对应 pin group 附近。

---

## PI-02｜电容很近，但 GND 绕远

### 故障

电容到 VDD pin 只有 1 mm，但 GND pad 经过 15 mm 细线才到 via。

### 训练点

“距离近”不等于“完整 loop 低电感”。

### 修复

GND via 紧邻 capacitor ground pad，重画完整回流。

---

## PI-03｜多个去耦共享一条细 Neck

### 故障

4 颗 local decoupler 最后都通过同一段窄铜接到 3V3/GND。

### 物理问题

共享阻抗 + 共享电感，局部瞬态互相耦合。

### 修复

减少共享 bottleneck，让局部 loop 更独立。

---

## PI-04｜10 µF 只看标称值

### 故障

选择小封装、高介电常数 MLCC，BOM 写 10 µF，但没查 3.3 V 下有效电容。

### 训练点

DC Bias、温度、容差让 effective capacitance 与 nominal C 不同。

### 修复

查具体料号曲线/模型并更新 BOM。

---

## PI-05｜电容农场

### 故障

同一 rail 放：10 pF / 100 pF / 1 nF / 10 nF / 100 nF / 1 µF / 10 µF，只因为“覆盖所有频段”。

### 训练点

不同真实 RLC 支路并联可能出现 anti-resonance。

### 修复

按器件 requirement、target、模型和角色删减/调整。

---

## PI-06｜L3 3V3 被掐成细颈

### 故障

大量 via/keepout 把 3V3 zone 切成狭窄通道。

### 症状

平均电流尚可，但负载变化时 MCU 端 droop 明显。

### 修复

重新布局/zone，消除不必要 constriction。

---

## PI-07｜多个 VSS 串联后只落一颗地孔

### 故障

多个 MCU GND pin 在 Top 先串起来，再从远端单 via 到 L2。

### 物理问题

共享 `Lcommon`，SSN / Ground Bounce 风险增加。

### 修复

按封装位置更直接、分散地进入完整 GND plane。

---

## PI-08｜Bottom 高速线跨 L3 Power Split

### 故障

四层 `TOP-GND-PWR-BOTTOM` 中，Bottom 关键线跨过 L3 power island 边界。

### 训练点

这是 SI + PI 联合问题：参考结构不连续，回流/电源网络同时被扰动。

### 修复

重走层/路径，或重规划 split/stackup。

---

## PI-09｜Buck 输入电容“离输入接口近”

### 故障

CIN 靠连接器放，而不是靠 switching power pins。

### 物理问题

高 `di/dt` input switching loop 面积变大。

### 修复

CIN 与 switching pair/PGND 形成紧凑局部 loop。

---

## PI-10｜SW 铜铺得越大越放心

### 故障

为了“大电流”，SW node 被铺成巨大铜岛。

### 物理问题

高 `dv/dt` coupling area 增大，可能恶化 EMI/敏感节点耦合。

### 修复

SW 铜只做到电流/热所需大小，远离 FB/analog。

---

## PI-11｜FB 线穿过 SW/电感噪声区

### 故障

反馈采样走线与 SW node 平行或穿过 inductor noisy region。

### 修复

Kelvin sense 正确输出点，保持 quiet routing，遵守具体 converter recommended layout。

---

## PI-12｜长探头地线制造 400 mV“尖峰”

### 故障

用普通鳄鱼夹地线在 Buck/MCU 周围测 rail，高频振铃巨大。

### 测量实验

同一测点依次使用：

1. long ground lead；
2. ground spring；
3. full bandwidth；
4. 20 MHz limit。

### 学习点

先验证 Measurement Integrity，再判断 Power Integrity。

---

## PI-13｜只看 LDO 额定电流

### 故障

看到 regulator 标称 600 mA，就认定任何 600 mA 工作点都安全。

### 忽略

- VIN-VOUT；
- 功耗 `P=(VIN-VOUT)I`；
- PCB 铜/θJA；
- 环境温度；
- transient；
- dropout。

### 修复

建立 thermal + DC + transient 三类预算。

---

## PI-14｜把 VCAP 当普通 3.3 V rail 优化

### 故障

为了“降低阻抗”，擅自修改 VCAP 电容值/连接方式。

### 训练点

VCAP 是器件内部 regulator 节点，优先遵守 ST requirement；不能把通用 target-impedance 方法凌驾于 device requirement。

---

## Fault Lab 评分标准

每个故障 10 分：

- 2：能指出症状；
- 2：能画完整电流 loop；
- 2：能指出主要寄生/物理机理；
- 2：能提出可执行 KiCad 修复；
- 1：能设计测量验证；
- 1：能把结论写回 Checklist。

总目标不是“背 14 个答案”，而是形成：

> **看到 PCB → 画电流路径 → 找共享阻抗/电感 → 再决定规则与测量。**
