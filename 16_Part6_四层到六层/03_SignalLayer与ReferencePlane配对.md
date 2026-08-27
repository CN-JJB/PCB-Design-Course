# 03｜Signal Layer 与 Reference Plane 配对：回流到底“认”哪一层

> 高速信号不是“在铜线上跑”，而是以导体与周围参考结构共同构成的电磁场传播。六层设计真正重要的不是给 L2 写上 `GND`，而是确认**每条关键网络在每一段路径上到底由什么结构承载场与回流**。

---

# 1. “最近的平面”只是第一近似

对一条 microstrip / stripline 来说，return current 会分布在能让高频回路阻抗较低的参考导体上。工程上通常先看：

- 哪个 plane 与 signal layer 的 dielectric spacing 更小；
- plane 是否连续；
- plane 是 GND 还是某个 power rail；
- 周围是否还有第二个 plane 参与场分布；
- 是否存在 coplanar copper、shield via fence、connector chassis 等结构。

因此不能机械写：

> “L3 一定参考 L2，因为编号更近。”

真正应该写：

> “L3 与 L2/L4 的几何距离分别是多少？两者是否连续？field solver / stackup 定义表明主要参考是谁？”

---

# 2. Microstrip、Stripline 与“夹在中间”

## 外层 microstrip

典型：

```text
L1  signal
--- dielectric h ---
L2  solid GND
```

优点：

- 易布线、易探测、易返修；
- 与邻近 GND coupling 可以很强；
- 适合 connector → protection → PHY/MCU 的关键短路径。

风险：

- field 一部分进入空气 / solder mask；
- 更容易受外部结构、元件、邻近铜影响；
- 需要把 solder mask / coplanar copper 等纳入阻抗模型。

## 内层 stripline

典型：

```text
Plane
--- dielectric ---
Signal
--- dielectric ---
Plane
```

优点：

- field 更受内部结构约束；
- 外界耦合通常较低；
- 对密集高速总线很有吸引力。

但“内层 = 自动最佳”也是错误的。你必须确认：

- 上下 plane 是什么 net；
- spacing 是否对称；
- 是否跨越 split；
- layer transition 时 reference 如何接续。

---

# 3. Reference 可以是 Power Plane 吗？

可以，但不能只因为它是“plane”就默认没问题。

如果某高速信号主要参考一个连续、低阻抗的 power plane，那么 return current 可以在该 plane 上形成局部路径。但信号最终的驱动/接收电流回路往往还与 GND system 有关系，因此需要考虑：

- power plane 是否连续；
- power-to-GND decoupling 在相应频率是否提供足够低的 transfer impedance；
- 换层后 reference 是否从 PWR 变成 GND；
- 该 power island 是否在 connector / BGA / SDRAM 区域被切断。

因此课程优先让关键高速层参考**连续 GND**，不是因为“电源不能参考”，而是因为 GND 通常更容易保持全板连续、跨功能区一致，也更容易 Review。

---

# 4. 六层板的 Layer Role Map

每个 signal layer 都要有一张“角色卡”。例如候选结构：

```text
L1  High-speed + components
L2  Solid GND
L3  Secondary signal / memory group
L4  Power / local plane
L5  Solid GND
L6  Low/medium speed signal
```

不要到 routing 一半才临时决定 L3 可以走什么。

记录：

| Layer | Primary role | Intended reference | Allowed critical nets | Forbidden/avoid | Review note |
|---|---|---|---|---|---|
| L1 | critical signal | L2 GND | clocks, diff pairs | noisy switch-node region | |
| L2 | solid reference | — | — | signal routing | |
| L3 | internal signal | geometry-dependent | memory / buses |跨 power split | |
| L4 | power / optional reference | — | rail copper | random signal cuts | |
| L5 | solid GND | — | — | signal routing | |
| L6 | secondary signal | L5 GND | low/medium-speed | critical bus unless justified | |

---

# 5. 为什么“完整 GND”价值这么高

一个连续 GND plane 同时解决：

- signal return path；
- ESD/EMC discharge / common-mode current 的一部分路径；
- decoupling current loop；
- connector ground reference；
- measurement reference；
- layer transition 的 stitching path。

所以把一个完整 GND plane 拿去“省几根线”通常收益很小，代价却覆盖 SI/PI/EMC 三个领域。

这也是课程持续强调：

> **不要在专用 reference plane 上路由普通信号。**

这不是审美规则，而是避免用局部 routing convenience 破坏全局基础设施。

---

# 6. Reference Discontinuity 的四种典型形式

## 6.1 Plane split

信号越过两个 power island / ground cut 的边界。

## 6.2 Void / antipad corridor

大量 via 的 antipad 把 reference plane 局部打成狭窄通道。

## 6.3 Connector / slot / mounting hole

机械开槽、绝缘间隙或屏蔽结构改变 reference geometry。

## 6.4 Layer transition

信号 via 换到另一 signal layer，而新旧 layer 的 reference 不同。

这四种都应该被当作“场结构突变”，而不是仅仅“铜有没有断”。

---

# 7. KiCad 落地

在 KiCad 9 中：

1. `Board Setup → Physical Stackup` 写入真实铜厚/介质结构；
2. 为每个 copper layer 写清名称与用途；
3. plane layer 用 zone / plane discipline 保持连续；
4. 不依赖 Net Class 自动理解 reference；
5. 用 Rule Area / Keepout 防止关键 reference 区被普通 routing 侵入；
6. 对关键 net 在 Review 文档中记录 `routing layer + reference layer`。

KiCad 的 Net Class 适合定义默认线宽、间距、via、差分几何，但官方文档也明确说明：**Net Class 的 track width / via size 是默认/optimal 值，不等于硬性 min/max DRC 约束。**需要强制约束时用 Custom Rules。

官方文档：
https://docs.kicad.org/9.0/zh/pcbnew/pcbnew.html

---

# 8. 本章任务

建立：

`projects/stm32h7-mainline/v3/layer-role-map.md`

至少包含：

- 每层 primary role；
- 每个 critical net group 的 preferred layer；
- intended reference；
- allowed transition；
- split/void 禁止区；
- 需要板厂 impedance control 的层。

---

## 本章一句话

> **不要问“这根线走哪层最方便”，先问“这根线和它的回流将由哪一对导体共同传播”。**