# 03｜四层 Stackup：从真实板厂数据开始，而不是从“经典层序”开始

> 🎯 **本章任务**：选定 V1 的四层物理结构，把真实铜厚/介质厚度录入 KiCad，并理解为什么同样是 `SIG-GND-PWR-SIG`，不同 stackup 的电磁表现也会不同。

![STM32F407 V1 四层叠层](../assets/svg/part1-four-layer-stackup.svg)

---

## 1. 层序 ≠ Stackup

写：

```text
L1 Signal
L2 GND
L3 Power
L4 Signal
```

只说明了每层用途。

真正 Stackup 还包括：

- 外层铜厚；
- 内层铜厚；
- L1↔L2 介质厚度；
- L2↔L3 core 厚度；
- L3↔L4 介质厚度；
- dielectric material / Dk；
- solder mask；
- finished board thickness。

这些参数决定 impedance、propagation、field confinement、plane coupling 和 via vertical length。

---

## 2. V1 真实案例：JLCPCB 1.6 mm 四层受控阻抗叠层

查询日期：**2026-08-26**。

JLCPCB 当前 Controlled Impedance 页面公开多种四层叠层。本课程选 `JLC04161H-3313` 作为**教学案例**，不是对厂商的唯一推荐。

页面：https://jlcpcb.com/impedance

当前公开的主要几何数据包括：

| Structure | Material / Copper | Nominal thickness |
|---|---|---:|
| L1 | outer copper | 0.035 mm |
| L1→L2 | 3313 prepreg | 0.09940 mm |
| L2 | inner copper | 0.0152 mm |
| L2→L3 | core | 1.265 mm |
| L3 | inner copper | 0.0152 mm |
| L3→L4 | 3313 prepreg | 0.09940 mm |
| L4 | outer copper | 0.035 mm |

板厂页面同时给出介质参数用于其阻抗体系，并提供官方 impedance calculator。

> **重要**：下单前必须重新核对板厂页面和订单系统。厂商可能调整材料、叠层名称、工艺或计算模型。

---

## 3. 为什么这个案例适合教学？

### L1 离 L2 很近

约 0.1 mm 的 outer dielectric 让 L1 信号对 L2 GND 有较强几何耦合。

这意味着：

- L1 很适合作为主高速信号层；
- 回流更容易集中在相邻 GND 平面；
- 微带阻抗由清晰的走线—平面几何关系决定。

### L2 与 L3 相距很远

中间 core 约 1.265 mm。

所以不能幻想 L2 GND 与 L3 Power 像“非常靠近的平板电容”一样提供很强的高频 interplane decoupling。

这反而能让 Part 3 的 PI 教学更清楚：离散去耦电容与安装电感仍然非常重要。

### L4 紧邻 L3，而 L3 是 Power

因此 V1 设定：

> **关键快速信号优先 L1 / reference L2 GND；L4 用作次要、低风险信号与必要 escape，不把 Top/Bottom 当完全对称的高速层。**

原因不是“Bottom 天生差”，而是本 stackup 的 reference relationship 不同。

---

## 4. 为什么不直接给你一条“50 Ω = 0.18 mm”？

因为受控阻抗取决于 stackup、copper thickness、Dk model、solder mask、etching compensation、finished geometry，以及差分时的 gap。

课程流程是：

1. 选 board house stackup；
2. 用板厂 impedance calculator / field solver 得到目标几何；
3. 把几何写入 KiCad Net Class / rule；
4. 下单时选择对应 controlled-impedance stackup；
5. fabrication note 明确 impedance target/net list。

**不要从另一篇博客复制线宽。**

---

## 5. KiCad 10：Physical Stackup 实操

KiCad 官方手册：https://docs.kicad.org/9.0/zh/pcbnew/pcbnew.html

进入：

```text
PCB Editor
→ Board Setup
→ Board Stackup
→ Physical Stackup
```

### Step 1：Copper layers = 4

### Step 2：按本次制造案例填写铜厚

### Step 3：填写 L1-L2 / core / L3-L4 介质厚度

### Step 4：材料与 Dk

如果 KiCad 对某些计算功能需要材料参数，使用与板厂当前模型一致的值并注明来源。不要用“FR4 = 4.4”作为所有频率、所有树脂含量、所有玻纤结构的永恒常数。

### Step 5：检查总厚度

KiCad Physical Stackup 应与订单 nominal finished thickness 相符。

---

## 6. Layer Naming

推荐在工程说明中统一：

```text
L1 / F.Cu   = SIG_TOP
L2 / In1.Cu = GND_REF
L3 / In2.Cu = PWR
L4 / B.Cu   = SIG_BOT
```

### L2 纪律

Part 1：不走普通信号、不为了方便切地、不随意画 split；允许必要 antipad/through-hole clearance，但要检查形成的铜颈和回流影响。

### L3 纪律

3V3 主区域；可根据实际需要包含其他低风险供电区域；任何在 L4 上的重要信号都必须知道自己参考的是哪块铜。

---

## 7. ❌ 故障板：把 L3 切得像拼图，然后 Bottom 到处走高速

假设 L3 有：

```text
3V3 | 5V | VDDA | AUX
```

四块分割区域。

Bottom 上一条 SWCLK 从 3V3 区跨到 5V 区，再跨到空隙。

如果只看 B.Cu：走线非常漂亮。

但参考结构不停改变。

正确策略：

- V1 关键时钟/调试快边沿优先放 L1；
- 如果必须 Bottom，先规划 L3 reference continuity；
- 后续 SI 章节再讲 reference transition 的具体处理。

---

## 8. Stackup Design Review

- [ ] 层序来自项目需求，不是复制模板；
- [ ] physical thickness 来自真实板厂；
- [ ] 查询日期已记录；
- [ ] L1 的 reference plane 明确；
- [ ] L4 的 reference plane 明确；
- [ ] L2 是否保持连续；
- [ ] L3 split 是否会影响 Bottom 关键网络；
- [ ] 受控阻抗宽度没有凭空猜；
- [ ] fabrication output 与订单 stackup 一致。

---

## 9. 本章任务

在 KiCad V1 工程中：

1. 设置四层；
2. 输入本章 stackup（或你自己板厂的真实 stackup）；
3. 给层写语义；
4. 画一张自己的 stackup 截图/表格放进 `design-decisions.md`；
5. 写下：

```text
Fast signals default layer: L1
Primary reference: L2 GND
Bottom critical-signal policy: review L3 reference before routing
```

下一章开始 placement。