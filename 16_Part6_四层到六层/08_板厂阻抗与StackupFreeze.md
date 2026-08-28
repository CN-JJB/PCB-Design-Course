# 08｜板厂阻抗与 Stackup Freeze：不冻结介质，就没有真正冻结线宽

> Controlled impedance 不是“在 KiCad 里写 50 Ω”就结束。阻抗来自制造出来的几何，所以 stackup、铜厚、介质、线宽、线距、阻焊和板厂补偿必须作为一个版本冻结。

---

# 1. 阻抗是一组制造参数的结果

关键变量：

- target impedance；
- routing layer；
- reference plane；
- dielectric thickness；
- dielectric constant；
- copper thickness；
- trace width；
- differential spacing；
- solder mask；
- coplanar ground gap（如果使用）；
- etch compensation / finished copper。

所以“50 Ω = 0.2 mm 线宽”没有跨 stackup 的意义。

---

# 2. 使用板厂标准 Stackup 的好处

标准 stackup 通常意味着：

- 材料和厚度组合成熟；
- 阻抗 calculator 有对应模型；
- 制造容差更明确；
- 价格和交期更稳定；
- CAM 工程师更容易核对。

自定义 stackup 不是不能做，但应有明确收益，而不是为了“看起来对称”。

---


## 2.1 标准 Stackup 太多时：先 Shortlist，再 Solver

板厂页面经常同时给出很多标准结构。

不要这样选：

~~~text
看名字
→ 觉得某个 prepreg 更“高级”
→ 直接下单
~~~

更稳健的流程是：

~~~text
Project constraints
→ shortlist standard stackups
→ compare adjacency / H
→ assign layer roles
→ calculate impedance geometry
→ check density / crosstalk / PI
→ confirm fab
→ freeze
~~~

### 第一轮：不碰阻抗数字，先淘汰结构

先按这些条件删候选：

- finished thickness；
- copper weight；
- required layer count；
- HDI / via process；
- mechanical thickness；
- cost / lead time；
- material / reliability requirement。

### 第二轮：看关键 Signal–Reference Pair

对每个高速/敏感 routing layer，记录：

| Layer | Reference | H | Continuous? | Transition risk |
|---|---|---:|---|---|
| L1 | L2 | | | |
| L3 | L2/L4 | | | |
| L6 | L5 | | | |

不要只看：

> “这是六层板。”

要看：

> **关键 signal 到 reference 的实际距离是多少。**

### 第三轮：Target Impedance → Width / Gap → Density

当 H 确定后，再用制造商 calculator / solver 计算：

- single-ended width；
- differential width/gap；
- coplanar gap（若使用）。

此时才评估：

- BGA escape 能不能塞下；
- parallel bus spacing 是否够；
- neck-down 区是否需要单独建模；
- fabrication tolerance 是否现实。

JLCPCB 当前 2026-06-15 更新的 calculator guide 也把 layer count、finished thickness、铜厚、routing layer、target impedance 与 differential spacing 作为输入，并说明材料/几何参考值可能未来调整。

来源：
https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator

### 第四轮：材料不是用固定 GHz 门槛决定

“普通 FR-4 到某个 GHz 都不用管材料”只能作为很粗的入门直觉。

真正是否要升级材料，至少比较：

~~~text
channel length
× frequency-dependent loss
× required insertion-loss margin
× temperature / process variation
~~~

然后再决定是否需要：

- tighter Dk control；
- lower Df；
- lower roughness copper；
- specialty laminate；
- weave mitigation。

所以 stackup selection 的成熟问题不是：

> “频率有没有超过 2.5 GHz？”

而是：

> **当前 channel 在目标 Nyquist / harmonic range 下还有多少 loss / timing / eye margin？**


# 3. 当前 JLCPCB 六层能力作为教学案例

截至 2026-08-26，JLCPCB 的 6-layer 页面公开说明：

- 常见板厚包括 0.8/1.0/1.2/1.6/2.0 mm；
- 支持 controlled impedance；
- 公开 capability 包括约 3.5 mil 最小线宽/线距、0.15 mm drill / 0.25 mm via 等等级的能力范围。

但课程不会把“最小能力”当默认设计值。

制造规则有三个层次：

1. **factory absolute capability**；
2. **low-cost / standard process capability**；
3. **project design rule**。

项目设计规则应尽量留 margin，而不是永远踩最小值。

来源：
https://jlcpcb.com/6-layer-pcb

---

# 4. JLC06161H-1080 的教学意义

当前 impedance 页面显示 `JLC06161H-1080` 采用近外层的薄 1080 prepreg、较厚的 L2-L3 / L4-L5 core，以及中间 7628 prepreg。

这意味着：

- L1 ↔ L2 coupling 很强；
- L6 ↔ L5 coupling 很强；
- L2 ↔ L3 与 L4 ↔ L5 的距离明显不同；
- 你不能只从层序字符串推导 reference coupling。

因此选 stackup 后，下一步不是“开始画”，而是：

> 用制造商 calculator / field solver 把每个 controlled-impedance layer 的几何计算出来。

JLCPCB 2026-06-15 更新的 Impedance Calculator Guide 也明确要求输入 layer count、finished thickness、inner/outer copper、routing layer、target impedance 和 differential spacing 等。

---

# 5. Stackup Freeze Record

至少记录：

```text
Manufacturer:
Stackup ID:
Query date:
Finished thickness:
Outer copper:
Inner copper:
Material / Tg:
Layer role assignment:
Controlled-impedance nets:
Target impedance / tolerance:
Calculated trace width/gap:
Source URL / PDF:
CAM confirmation required?:
```

任何一项改变，都可能要求重新计算：

- impedance；
- timing delay；
- via geometry；
- plane coupling。

---

# 6. “板厂会帮我调阻抗”不代表可以不设计

如果订单选择阻抗控制，板厂可能根据其工艺调整线宽，但你仍要提供：

- 正确 net / layer；
- 正确目标阻抗；
- 正确 stackup；
- 合理原始 geometry；
- 正确 reference structure。

板厂不能替你修复：

- 差分对跨 split；
- reference transition 错误；
- ESD layout；
- pair uncoupling；
- layer role 设计错误。

---

# 7. 下单前必须重新核对

课程中记录的 JLCPCB 参数只用于 2026-08-26 的教学案例。

真正生产前重新访问：

- https://jlcpcb.com/impedance
- https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator

因为：

- stackup ID 可能更新；
- 材料/厚度可能调整；
- capability / pricing 会变化。

---

# 8. 本章工程任务

完成：

`projects/stm32h7-mainline/v3/stackup-decision-record.md`

必须有：

- 至少两个候选 stackup；
- layer-reference map；
- 制造 margin；
- impedance layer plan；
- freeze / reopen 条件。

---

## 本章一句话

> **只要 stackup 还会变，受控阻抗的线宽就还没有真正确定。**

# 增补｜阻抗验收不是“板厂说会控”

## A. Fabrication Tolerance Budget

冻结 controlled impedance 时同时记录：

- target impedance；
- allowed tolerance；
- trace width / spacing；
- copper thickness；
- finished copper assumption；
- dielectric thickness；
- Dk / material family；
- soldermask inclusion；
- etch compensation responsibility；
- coupon requirement。

如果板厂允许调整线宽，必须明确：

> **允许板厂在哪个范围内调整、调整后是否需要回传确认。**

## B. Coupon / TDR

对需要阻抗验收的项目，release note 至少说明：

- 是否要求 impedance coupon；
- coupon 对应哪些 layer / structure；
- TDR 报告是否作为 lot evidence；
- acceptance 是按目标值、容差还是厂内标准流程。

课程不假设“有阻抗单就是整板所有走线都被逐条 TDR 测过”。

## C. Stackup Change Control

下面任何变化都触发 reopen：

```text
fab
stackup ID
material family
dielectric thickness
copper weight
controlled-impedance layer
trace geometry
soldermask assumption
```

必须重新：

```text
solver
→ KiCad rule
→ fab note
→ review
→ release
```
