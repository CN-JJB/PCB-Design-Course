# 02｜电源树与 MCU 原理图：先画电流，再画符号

> 🎯 **本章任务**：完成 STM32F407VGT6 的电源/复位/启动/调试核心原理图，并为后续布局标出“必须靠近”的器件关系。

---

## 1. 原理图不是网络连接清单

如果你只检查：

```text
VDD 都接 3V3
VSS 都接 GND
```

你只完成了 connectivity。

真正的 PCB 设计还要提前知道：

- 哪些电容属于哪个 power pin；
- 哪些环路需要极短；
- 哪些器件必须和 MCU 一起放；
- 哪些网络必须在 L2 GND 上方保持完整参考；
- 哪些器件只是可选装调试位。

所以本章会在原理图阶段给器件打“布局语义”。

---

## 2. ST 官方电源要求先抄到 Constraint Sheet

依据 ST AN4488（STM32F4 hardware development）：

### VDD

- 每个 VDD pin 使用局部 `100 nF` ceramic decoupling；
- package 另配较大的 bulk capacitor，AN4488 给出 minimum 4.7 µF、typical 10 µF 的量级。

### VDDA

AN4488 给出：

```text
100 nF + 1 µF
```

作为模拟电源局部去耦建议。

### VCAP1 / VCAP2

对于本课程所选 STM32F407VGT6 这类具有两个 VCAP pin 的配置，按 AN4488 / Datasheet 使用低 ESR ceramic capacitor；AN4488 给出每个 `2.2 µF` 的典型要求。

重要：

> VCAP 是内部 regulator 的外部稳定电容节点，不是给外部负载使用的 1.2 V 电源。

### VBAT

无外部电池时，根据 AN4488 建议连接到 VDD，并按文档处理局部去耦。

---

## 3. 先画一张“供电关系图”

```text
5V_IN
  │
  ├─ protection / bulk
  │
  └─ AP2112K-3.3
       │
       ├────────────── 3V3_MAIN
       │                  │
       │                  ├─ VDDx + local 100nF
       │                  ├─ VBAT (no battery in V1)
       │                  ├─ GPIO / LEDs / headers
       │                  │
       │                  └─ analog branch → VDDA/VREF+
       │
      GND ============================= L2 plane
```

注意我们没有先讨论“L3 电源平面怎么切”。

顺序是：

1. 先知道谁给谁供电；
2. 再知道各时间尺度上的本地电流从哪里来；
3. 最后决定铜结构。

---

## 3.1 Power Tree 前面还有一层：Protection Boundary

不要把电源树只画成：

~~~text
5V_IN → LDO → 3V3
~~~

产品级版本应该先问：

~~~text
External source
→ overcurrent / reverse / overvoltage / inrush protection
→ regulator
→ rail
→ load
~~~

其中：

- fuse / eFuse 处理 source energy / overload；
- reverse-polarity circuit 处理错误输入方向；
- OVP cutoff 与 TVS clamp 解决不同时间尺度的过压；
- soft-start / eFuse slew-rate 处理大输入电容 hot-plug；
- regulator 自己的 abs-max 不能替代 upstream protection。

具体器件是否需要取决于产品 threat model，不在 V1 机械堆满。完整框架见：[09｜产品级保护电路](09_产品级保护电路_从接口到SafeState.md)。


## 4. LDO：不要把最大电流和热能力混为一谈

V1 教学参考器件：`AP2112K-3.3`。

Diodes Incorporated 官方资料：

- 3.3 V fixed output option；
- guaranteed 600 mA minimum output-current capability；
- typical application uses `1 µF` CIN and `1 µF` COUT；
- 对 1 µF ceramic 推荐 X5R/X7R。

但线性稳压器热功耗近似：

```text
P_LDO ≈ (5.0 - 3.3) × I_LOAD
      ≈ 1.7 × I_LOAD
```

举例：

```text
100 mA → 0.17 W
200 mA → 0.34 W
300 mA → 0.51 W
```

是否能安全散掉这些热，取决于封装、环境温度、PCB 铜面积等。

所以设计决策写成：

> V1 用 LDO 是因为系统负载较轻、教学简单；V2 外设增加后重新做 power budget，不承诺沿用。

---

## 5. 去耦电容：原理图画法要服务布局

### 不推荐的画法

```text
MCU power pins
     │
[一大排 C1 C2 C3 C4 C5 C6 C7 C8]
```

电气连接没错，但 PCB 工程师看不出：

- C1 服务哪个 pin；
- 哪些是 local；
- 哪个是 bulk；
- VDDA 哪两个属于模拟支路。

### 推荐的教学画法

把电源脚按区域/功能分组，并用注释明确：

```text
VDD_A ─ C101 100nF   [PLACE AT PIN GROUP A]
VDD_B ─ C102 100nF   [PLACE AT PIN GROUP B]
...
VDD bulk ─ C110 4.7/10uF

VDDA ─ C120 100nF + C121 1uF
VCAP1 ─ C130 2.2uF
VCAP2 ─ C131 2.2uF
```

这样原理图已经开始指导 placement。

---

## 6. 为什么“离芯片 2 mm”不是万能规则？

旧式 Checklist 很喜欢写：

> 去耦必须 ≤2 mm。

这个数字可能在某些结构里是有用的布局经验，但不能代替真正目标。

真正目标是：

> **让高频供电电流的闭合路径具有尽量低的寄生电感。**

影响因素包括：

- capacitor package；
- pad geometry；
- trace/via length；
- via spacing；
- power/ground plane distance；
- MCU package inductance。

因此 Part 1 会使用“尽量贴近、直接、低电感”的几何原则；Part 3 再用 PDN/ESL 模型定量解释。

---

## 7. VCAP 布局优先级非常高

VCAP pin → capacitor → GND 的路径要：

- 极短；
- 无不必要支路；
- 低电感接入 GND plane；
- 不把 VCAP 当作普通 1.2 V rail 拉去其他地方。

故障板实验会故意把 VCAP 电容放远，让你在 Review 时找出来。

---

## 8. Reset / Boot / SWD

### BOOT0

V1 默认配置为正常 Flash boot，并提供可控方式进入其他启动模式。具体 pull 方案依据 STM32F407 datasheet / AN4488。

### NRST

按 ST 的 hardware guidance 实现 reset 网络，并提供：

- reset button；
- SWD header access；
- test point（可选但推荐教学板保留）。

### SWD

至少：

```text
SWDIO
SWCLK
NRST
GND
VTREF/3V3
```

Header 周围不要先堆高器件；bring-up 时物理可接近性也是设计要求。

---

## 9. HSE：先留出“安静的小回路”

晶体/振荡器区域的关键不是“画两根很短的线”这么简单，而是：

- oscillator loop 紧凑；
- 元件靠近对应引脚；
- 不让高速/大电流 switching route 穿过附近；
- 参考结构连续；
- 不把长测试线/stub 挂在 oscillator node 上。

晶体 load capacitor 的具体值不在本章拍脑袋指定，必须根据：

- crystal `CL`；
- STM32 oscillator characteristics；
- stray capacitance

计算/验证。

---

## 10. 原理图 Review 顺序

### Power

- [ ] exact MCU part/package；
- [ ] 所有 VDD/VSS pin；
- [ ] VDDA/VREF+；
- [ ] VCAP1/2；
- [ ] VBAT；
- [ ] local + bulk decoupling；
- [ ] regulator input/output capacitor；
- [ ] power test points。

### Boot/Reset/Debug

- [ ] BOOT0 默认状态明确；
- [ ] NRST circuit；
- [ ] SWDIO/SWCLK；
- [ ] VTREF + GND；
- [ ] header pinout 不会镜像。

### Clock

- [ ] HSE part/footprint；
- [ ] load network 来源明确；
- [ ] placement note 已写进 schematic。

---

## 11. ❌ 故障板练习

下面哪些问题 ERC 可能发现不了？

1. 所有 100 nF 电容都放在 MCU 20 mm 外；
2. VCAP 电容经一条很细很长的线接到 pin；
3. HSE 晶体放在板子另一边；
4. SWD connector 被高电解电容挡住；
5. LDO 标称 600 mA，于是设计按 600 mA 连续负载而没有热分析。

答案：**全部可能需要人工工程 Review。**

这就是为什么课程不把 ERC/DRC 当毕业证。

---

## 12. 本章输出

完成：

```text
power tree
MCU core schematic
constraint annotations
initial power budget
placement-critical component list
schematic review checklist
```

下一章我们第一次真正决定“板子里面四层铜怎么排”。