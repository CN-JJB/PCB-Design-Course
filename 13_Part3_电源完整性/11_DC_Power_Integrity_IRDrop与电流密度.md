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

## 11.3.1 Via Bottleneck：宽铜到了换层点，可能突然只剩一根“细水管”

很多 power rail 在平面上看起来很宽，但真正失败发生在 layer transition：

~~~text
wide pour
========
   ●     ← one via
========
wide pour
~~~

这时限制条件可能变成：

- via barrel resistance；
- plating thickness；
- hole diameter；
- board thickness；
- local thermal environment；
- 并联 via 之间的 current sharing；
- via 到平面的 neck / antipad geometry。

### 不要只背“一个 0.3 mm via 能过 X A”

Sierra 的 current-carrying 资料把 via 近似为圆柱导体，并强调 current capacity 与横截面积、温升和 plating 有关。

真正设计流程是：

~~~text
Rail current
→ allowable ΔV
→ allowable ΔT
→ via geometry / plating
→ required parallel-via count
→ current density / thermal check
→ measurement or simulation if critical
~~~

### 🎮 找瓶颈练习

给一条 5 A rail：

- top pour 8 mm 宽；
- bottom pour 8 mm 宽；
- 中间只有 1 个小 via。

问学生：

> “这还是一条 8 mm 宽的电源路径吗？”

答案是：**只在大部分路段是。最窄的等效导体决定局部压降与温升。**

### 来源

- Sierra Circuits, *How to Design a Via with Current-Carrying Capacity*  
  https://www.protoexpress.com/blog/how-to-design-via-with-current-carrying-capacity/
- Sierra Circuits, *How Via Stitching Facilitates High-Current PCB Designs*  
  https://www.protoexpress.com/blog/how-via-stitching-facilitates-high-current-pcb-designs/


## 11.4 Plane Current Density

大铜面平均看起来很宽，不代表每个区域电流密度都低。

特别检查：

- 电源从小器件 pad 扩散进 plane 的入口；
- split / slot 附近；
- BGA / LQFP 电源 pin 集中区；
- regulator output；
- connector / fuse；
- thermal relief。

## 11.4.1 IPC-2152 的真正意义：铜宽不是唯一散热变量

很多初学者把“电流线宽计算器”理解成：

~~~text
I → 查表 → 得到 width
~~~

但 IPC-2152 思路比这复杂：温升还取决于 **内/外层、邻近平面、板厚、介质导热、铜分布和环境**。

### 为什么同样 2 mm 宽，内层和外层温升不同？

外层铜可以直接和空气/表面环境交换热；内层铜主要通过 FR-4 和周围铜结构扩散。

所以资料中的 IPC-2152 解读强调：

- internal trace 常需要更大的 width 才得到类似温升；
- 邻近大面积 plane 会成为 heat spreader；
- 铜电阻还会随温度上升，形成 `I²R → 温升 → R 增大 → 更多发热` 的反馈。

### 这会改变“Power Plane 有没有价值”的讨论

在 SI/EMI 章节，我们可能因为 reference continuity 选择双 GND；

但在高电流板上，一整层 power copper 还可能提供：

- 更低 DC resistance；
- 更低 current density；
- 更好的 lateral heat spreading；
- 更低局部热点。

所以 `PWR plane vs GND+GND` 不能只从 plane capacitance 判断。

### 项目动作

对 >1 A 的关键 rail，不只记录 width，还要记录：

| Item | 记录内容 |
|---|---|
| layer | inner / outer |
| copper | finished oz / µm |
| narrowest neck | mm |
| via transition | count / drill / plating assumption |
| adjacent copper | solid plane / sparse / none |
| allowed ΔT | project target |
| allowed ΔV | project target |

### 来源

- NextPCB, *PCB Trace Width Calculation: High-Current Design & Thermal Analysis*  
  https://www.nextpcb.com/blog/pcb-trace-width-calculation-high-current-design-and-thermal-analysis

> 文章中的具体百分比属于其 IPC-2152 解读和案例。正式产品的温升/载流仍需用当前板厂铜厚、实际环境和测量/热仿真闭环。


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


## 11.10 不要从“线宽”直接背“能过多少安培”

视频与很多经验资料会出现“6 mil 能过 1 A”“20 mil 能过几安培”一类数字。它们可以帮助纠正“几安培一定需要整层 power plane”的直觉，但不能成为通用 design rule。

导体 sizing 必须至少绑定：

- copper thickness；
- external / internal layer；
- allowable temperature rise；
- trace length / DC drop；
- 邻近 copper plane 的散热；
- ambient / airflow；
- via / connector bottleneck。

IPC-2152 的用途就是在这些热与结构条件下评估 conductor current-carrying capability，而不是提供一个固定 `width → current` 常数。

因此课程策略是：**先做 DC/thermal sizing，再决定 rail 用 trace、pour 还是 plane。**


## 11.10.1 IPC Calculator 的正确定位

Phil's Lab #112 在 trace-current sizing 部分给出 IPC-2221 calculator 作为入门工具。

课程保留它的教学价值，但项目 sign-off 采用更严格分级：

~~~text
IPC-2221-style formula
→ quick screening

IPC-2152 / modern thermal calculator
→ engineering estimate

prototype thermal + voltage measurement
→ evidence
~~~

原因是 conductor current capability 不只由 width/copper thickness 决定，还受 layer position、board thermal environment、adjacent copper、allowed temperature rise 与 length 影响。

所以任何“X mil = Y A”必须带适用条件。

