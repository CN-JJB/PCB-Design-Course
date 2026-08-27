# 05｜SDRAM 板级时序与“等长”：真正该匹配什么

> “并行总线要等长”只说对了一半。更准确的说法是：**必须让所有被同一个采样事件约束的信号，在接收端保留足够 setup/hold margin。**

---

# 1. PCB 长度只是时间的一种表达

传播延迟近似：

~~~text
td = length / velocity
~~~

FR-4 上常见量级是几 ps/mm，但准确值取决于 stackup、microstrip/stripline、Dk 和 trace geometry。

所以真正要冻结的是：

> **board skew，单位 ps。**

长度是在已冻结 stackup 上对它的换算。

---

# 2. SDR SDRAM 不是 DDR

V3 没有 DQS。

因此不要套：

- DQ-to-DQS
- write leveling
- read leveling
- DDR fly-by
- ODT
- byte lane

这里是共同 CLK 驱动的同步 SDR 总线。

---

# 3. 四个 timing groups

## A. Clock

**SDCLK**

优先级最高：

- route clean；
- reference 连续；
- 少 via；
- 少 stub；
- 远离 SW node。

## B. Address / Command

A[11:0]、BA[1:0]、RAS/CAS/WE/CKE/CS。

MCU → SDRAM。

## C. Write Data

DQ[15:0] + DQM。

MCU → SDRAM。

## D. Read Data

同一组 DQ 反向：

SDRAM → MCU。

双向 bus 的难点就是同一根 DQ 要同时满足两个方向。

---

# 4. “全部一样长”为什么可能更坏

如果把所有线强制同一长度：

- 会制造大量蛇形；
- 增加 self-coupling；
- 增加串扰；
- 让 routing corridor 更乱；
- 可能迫使换层；
- 让 SDCLK 也被拖长。

正确顺序：

~~~text
natural route
→ measure length / delay
→ calculate skew
→ compare timing budget
→ tune only necessary nets
~~~

---

# 5. V3 的项目级 skew target

为了 first-spin 教学 margin，V3 使用：

> **board-induced group skew ≤ 100 ps 作为初始项目目标。**

注意：

- 这不是 JEDEC 通用规则；
- 不是所有 SDRAM 都必须 100 ps；
- 是 V3 的 engineering target。

假设实际 stackup 传播约 6.5 ps/mm：

~~~text
100 ps / 6.5 ps/mm ≈ 15 mm
~~~

因此“十几毫米级”只是某个 stackup 的换算结果。

---

# 6. 更重要的是 Clock-to-Signal

只看：

~~~text
max(DQ length) - min(DQ length)
~~~

是不完整的。

真正要看：

- CLK ↔ address/control
- CLK ↔ write data
- CLK ↔ read data

也就是：

> 信号到达时间相对于采样 clock edge 的位置。

---

# 7. SDCLK 的角色

Clock 不是“也放进一组一起等长”。

它是参考。

布局时：

1. 先把 SDCLK 路径做得直接；
2. 确认 reference；
3. 再用其他 group 与它做 timing comparison。

不要为了和一根绕远的 address 线一样长，把 clock 也绕远。

---

# 8. Via budget

每个 via 都可能改变：

- delay；
- discontinuity；
- reference transition；
- local return path。

V3 目标：

- SDRAM bus 尽量单层；
- 如果必须换层，整个 group 的 reference 行为要一致；
- 不要让 3 根 DQ 在 L1、8 根在 L3、5 根在 L6，最后只靠“长度一样”宣布通过。

---

# 9. 蛇形的副作用

meander 太密会发生同线段之间的耦合。

所以蛇形不是免费 delay。

原则：

> **少补、疏补、在安静区域补。**

如果需要大量蛇形才能满足“规则”，优先回头修 placement。

---

# 10. Series termination footprint

建议给：

- SDCLK
- 少数 command/control high-risk source nets

预留可调 source series footprint。

但默认不把值写死成 22 Ω / 33 Ω。

流程：

~~~text
IBIS / scope evidence
→ choose damping
→ populate value
~~~

---

# 11. SDRAM Skew Lab

[SDRAM Skew Lab](../interactive/sdram-skew-lab.html)

调整：

- ps/mm
- mismatch mm
- skew target
- setup budget

观察几毫米差异对应多少 ps。

---

# 12. KiCad 落地

每个 timing group 记录：

- allowed layers
- routed length
- propagation assumption
- max skew
- via count
- reference plane
- tuning region

KiCad 可以算 length/skew，但不能自己判断你的 100 ps 目标有没有物理依据。

---

# 13. Review

- [ ] SDCLK 独立优先
- [ ] DQ natural route 优先
- [ ] timing groups 明确
- [ ] skew 用 ps 记录
- [ ] stackup propagation 已冻结
- [ ] reference continuity 已检查
- [ ] via transition 有 map
- [ ] meander 不过密
- [ ] termination footprint 有理由
- [ ] 没有套 DDR 规则

---

## 本章产出

**sdram-routing-constraints.md**


# 增补｜完整的 Board Timing Budget

本章必须最终产生一张可计算、可回填实际长度的表。

## A. 先从 Datasheet Margin 开始

对每个 timing group：

```text
controller output timing
+ package uncertainty
+ PCB flight/skew
+ memory setup/hold
+ jitter / clock uncertainty
→ remaining margin
```

不要从“想控制在 10 mm”反推物理意义。

## B. Stackup Freeze 后得到传播延迟

记录：

```text
Layer:
Structure:
Dk model:
Field-solver delay:
ps/mm:
Source/date:
```

只有这一步完成后，`100 ps` 才能转换成真实 mm mismatch。

## C. Actual Route 回填

| Group | Target ps | ps/mm | Allowed ΔL | Actual max-min | Via delta | Remaining margin |
|---|---:|---:|---:|---:|---:|---:|
| CLK↔A/C | TBD | TBD | TBD | TBD | TBD | TBD |
| CLK↔Write DQ | TBD | TBD | TBD | TBD | TBD | TBD |
| CLK↔Read DQ | TBD | TBD | TBD | TBD | TBD | TBD |

## D. Via Delay 不能只数颗数

如果不同网络 via 结构不同，要考虑：

- layer span；
- barrel / stub；
- pad/antipad；
- reference transition。

“每根都 2 个 via”不一定代表电气延迟一致。

## E. Measurement / Validation

PCB timing 预算最终由：

- memory stress；
- clock frequency A/B；
- GPIO slew A/B；
- temperature / voltage corner（条件允许时）；
- 示波器关键节点观察

来验证趋势。

**长度绿色只是输入证据，不是内存通过的最终证据。**
