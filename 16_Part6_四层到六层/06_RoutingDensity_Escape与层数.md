# 06｜Routing Density、Escape 与层数：多一层不是为了“塞更多线”

> 当板子变密时，最容易出现的错误是把 routing density 当成纯几何问题。真正的工程目标是：**让每条关键网络在满足 reference、spacing、via、power、EMC 和制造约束的前提下仍有可行通道。**

---

# 1. Routing Density 的真正定义

“板子很挤”至少包含五种不同压力：

1. **pin escape pressure**：器件引脚能否离开封装区；
2. **channel pressure**：两个器件之间是否有足够通道通过一组网络；
3. **reference pressure**：可用的 signal layer 是否都有合理参考；
4. **via pressure**：大量 via 是否把 plane 打出 antipad corridor；
5. **power pressure**：routing 是否切断 power copper / decoupling path。

如果只是视觉上拥挤，不一定需要加层；如果上述任何一个压力让关键约束无法满足，就进入层数升级评审。

---

# 2. LQFP 与 BGA 的层数驱动力不同

## LQFP

STM32H743ZIT6 是 LQFP144、20×20 mm。引脚在封装外围，escape 相对直观：

- 主要压力是 pin count、接口数量和板框；
- 不需要从内部 ball rows 穿出；
- 适合 Part 7 先把六层、SDRAM、Ethernet 的方法学讲清楚。

ST 当前产品页列出的 STM32H743ZIT6 状态为 Active，封装为 LQFP144。

## BGA

BGA 的 routing layer 需求常由：

- pitch；
- ball map；
- pad / via technology；
- minimum trace/space；
- dog-bone / via-in-pad；
- escape direction；
- power/ground ball distribution；
- blind/buried via 能力；

共同决定。

所以“0.8 mm BGA = 六层”不是可靠公式。

---

# 3. Escape 时为什么 reference 也会受伤

大量 signal via 穿过 GND plane 时，每个 via 都需要 antipad。

单独一个 antipad 通常没问题；当一排 via 密集排列时，antipad 可能连接成：

- slot-like corridor；
- narrow return neck；
- 局部 reference void。

因此 BGA / high-pin-count package 的 escape review 不只是看“线出来没有”，还要看：

> **plane 在 via forest 下面还剩下什么形状。**

---

# 4. 六层能给你的真正自由度

相比 V2 四层：

```text
4-layer:
L1 signal
L2 GND
L3 PWR
L4 signal
```

六层可以多出一个真正的 signal corridor 和一个额外 plane / reference 选择。

这带来的价值是：

- SDRAM data/address/control 可以有更清晰的 group routing；
- Ethernet/clock/USB 不必与 memory bus 抢同一层；
- power islands 不必同时承担所有 Bottom 高速 reference；
- 调试、GPIO、低速总线可以主动“退居次优层”，把最佳通道让给关键网络。

这种**优先级分层**才是多层板成熟度。

---

# 5. Routing Budget：在布线前分配资源

为 V3 做一张 Layer Routing Budget：

| Net group | Pin count | Edge-rate concern | Preferred layer | Reference | Via budget | Priority |
|---|---:|---|---|---|---:|---|
| SDRAM CLK | | high | | | | P0 |
| SDRAM DQ/DQS-like group | | high | | | | P0/P1 |
| SDRAM addr/cmd | | high | | | | P1 |
| Ethernet interface | | medium/high | | | | P1 |
| USB | 2 | controlled diff | | | | P1 |
| SWD | | debug | | | | P2 |
| UART/I2C/GPIO | | low | | | | P3 |

注意：STM32 FMC SDRAM 不等同于 DDR，因此不要把 DDR 的 DQS/fly-by 规则原样套过来；Part 7 会按 STM32 FMC + 具体 SDRAM datasheet 建规则。

---

# 6. 什么时候六层仍然不够

出现以下情况要认真比较八层：

- 两个以上高密度 BGA 同时存在；
- 关键 bus 数量多到 signal layers 仍严重争抢；
- 多个高速 signal layer 无法同时获得连续 GND reference；
- power-domain 数量迫使 plane 被切得过碎；
- 为了六层必须使用板厂极限线宽/极限过孔；
- 必须大量跨 reference 换层；
- 需要更强的 plane-pair / shielding / isolation 结构。

多两层的成本有时低于一次板级 SI/EMC 重构。

---

# 7. 本章工程任务

在 `projects/stm32h7-mainline/v3/layer-count-decision.md` 增加：

### Routing Capacity Evidence

- estimated pin groups；
- critical routing channels；
- expected via clusters；
- plane perforation risks；
- 6-layer vs 8-layer tradeoff。

不要写：

`六层应该够。`

要写：

`为什么够，哪里最紧，出现什么条件就升级八层。`

---

## 本章一句话

> **多层板的目标不是最大化可布线数量，而是给高优先级网络分配“带参考的可用通道”。**

# 增补｜把 Escape 压力量化成制造决策

## A. Via 工艺不是“最后问板厂”

BGA / 高密度板在 layer-count review 时必须提前列出：

| Item | Candidate | Need source |
|---|---|---|
| finished drill | TBD | fab capability |
| pad / annular ring | TBD | fab capability |
| aspect ratio | TBD | fab capability |
| through via | yes/no | escape study |
| blind / buried via | yes/no | cost/yield |
| microvia | yes/no | HDI process |
| via-in-pad | yes/no | fill/cap requirement |
| backdrill | yes/no | high-speed stub budget |

层数、孔工艺与成本是同一个决策树，不应“先画六层，再让板厂想办法生产”。

## B. Escape Channel Estimate

对 BGA 先计算：

```text
ball pitch
- pad diameter
- clearance
- trace width
- via pad / antipad
→ 每两列球之间可通过多少条线
```

然后按 ring / row 统计：

- 外圈可直接 Top escape；
- 中圈需要多少 routing layer；
- power/GND via 消耗多少通道；
- DDR / GTP 等高约束网络是否还能保持 reference。

## C. 六层 vs 八层完整 Gate

只有同时回答下面问题才允许冻结 6 层：

1. 关键组是否有足够 routing channel？
2. 每个关键 signal layer 是否有明确 reference？
3. power domains 是否迫使信号跨 split？
4. BGA escape 是否需要破坏 reference 才能完成？
5. via / antipad forest 是否造成 plane neck？
6. 额外两层的成本是否低于复杂 HDI / 返工风险？

如果 6 层只能靠极小线宽、激进孔径、频繁换层或大量 reference discontinuity 才“布得完”，8 层可能反而是更便宜的工程方案。

## D. 输出

建立 `routing-capacity-evidence.md`：

- package map；
- escape sketch；
- layer allocation；
- via process；
- fab capability source/date；
- unresolved risks；
- 4/6/8-layer comparison。
