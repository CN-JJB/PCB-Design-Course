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
