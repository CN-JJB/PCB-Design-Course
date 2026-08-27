# 11｜DC Power Integrity：IR Drop、电流密度与热不是“低频小事”

> 前面的 PI 重点是瞬态电流、去耦与 PDN 阻抗。本章补上另一半：**直流压降、电流密度、连接电阻与温升**。

## 11.1 为什么“3.3 V plane”不是处处 3.3 V

真实供电路径包括：

```text
regulator
→ copper
→ via
→ plane neck
→ connector / fuse / shunt
→ package
→ load
→ ground return
```

每一段都有电阻。

因此 DC PI 最核心的式子仍然是：

```text
ΔV = I × R
P = I²R
```

难点不是公式，而是找到真实的 I 与 R。

## 11.2 需要检查的电阻来源

- 长而窄的 trace；
- plane narrow neck；
- 多层间 via bottleneck；
- connector contact；
- fuse / PTC；
- current shunt；
- ferrite bead DCR；
- cable；
- ground return；
- thermal rise 导致的电阻变化。

## 11.3 Via 不只看“能不能过电流”

一组 via 需要同时看：

- finished hole / plating；
- 数量；
- 电流分配是否均匀；
- 入口/出口铜是否形成 neck；
- 热；
- 制造能力。

“打很多 via”如果上下层都汇入一个窄颈，瓶颈仍在。

## 11.4 Plane Current Density

大铜面平均看起来很宽，不代表每个区域电流密度都低。

特别检查：

- 电源从小器件 pad 扩散进 plane 的入口；
- split / slot 附近；
- BGA / LQFP 电源 pin 集中区；
- regulator output；
- connector / fuse；
- thermal relief。

## 11.5 DC 与 AC PI 必须合并

一个 rail 可能：

- DC drop 合格，但高频阻抗很差；
- 高频 decoupling 很好，但 connector / neck 压降过大；
- 电压都勉强合格，但局部 I²R 发热过高。

所以 PI Review 至少拆成：

```text
DC drop
Transient response
Frequency-domain impedance
Thermal
Measurement
```

## 11.6 V2 / V3 工程表

| Segment | I max | R estimate | ΔV | P | Evidence |
|---|---:|---:|---:|---:|---|
| Regulator → 3V3 plane | TBD | TBD | TBD | TBD | layout / calc |
| Plane → MCU | TBD | TBD | TBD | TBD | layout |
| Plane → SD / SDRAM | TBD | TBD | TBD | TBD | layout |
| Ground return | TBD | TBD | TBD | TBD | layout |
| Connector path | TBD | TBD | TBD | TBD | datasheet |

## 11.7 测量

优先做四线/差分思维：

- 在 source 与 load 两端分别测；
- 明确负载状态；
- 记录 probe/reference；
- 记录温度；
- 做 idle ↔ stress A/B。

## 11.8 Design Review

- [ ] 最大电流场景有定义；
- [ ] source-to-load 与 return 路径都检查；
- [ ] via / plane neck 没有隐藏瓶颈；
- [ ] connector / fuse / bead / shunt 的 DCR 被计入；
- [ ] DC drop 与 transient / PDN review 不是互相替代；
- [ ] 热与电阻有闭环。

## 11.9 进阶：PDN 阻抗测量入口

专业 PI 验证会使用 VNA、注入或 2-port shunt-through 等方法测量低阻抗 PDN。课程此处只建立概念：**如果你声称某条 Z(f) 已被实测验证，就必须同时记录 fixture、校准、端口与频率范围。**
