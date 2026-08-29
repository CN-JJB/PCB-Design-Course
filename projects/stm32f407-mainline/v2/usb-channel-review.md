
# V2 USB Channel Review

> Review the complete USB path, not only the long parallel section. This sheet is for USB FS on STM32F407 V2; do not reuse geometry numbers on another stackup without recalculation.

## 1. Interface Identity

- USB mode: Full-Speed device
- PHY: STM32 embedded FS PHY
- Connector MPN:
- ESD MPN:
- Board fab:
- Stackup ID:
- Query date:
- Routing layer:
- Reference plane:
- Target differential impedance:
- Width:
- Gap:
- Geometry source:

## 2. Channel Segments

| Segment | Geometry / Layer | Reference | Symmetry | Discontinuity / Loading | Evidence | Result |
|---|---|---|---|---|---|---|
| connector contact → breakout | | | | | | |
| connector → ESD input | | | | | | |
| ESD package / pads | | | | Cio / pin topology | datasheet | |
| ESD output → controlled pair | | | | | | |
| controlled pair | | | | | fab/solver | |
| MCU/module breakout | | | | | | |
| PHY pad/package | vendor-defined | | | | datasheet | |

## 3. ESD Device Review

- [ ] exact MPN frozen
- [ ] datasheet pin topology checked
- [ ] no schematic pin short invented for layout convenience
- [ ] line capacitance / leakage acceptable
- [ ] flow-through layout used if supported by device
- [ ] TVS/array is close to connector
- [ ] discharge return is short and low inductance
- [ ] discharge current does not cross the core logic region

## 4. Reference / Return

- [ ] L2 reference is continuous under the full channel
- [ ] no plane split / slot / narrow neck under pair
- [ ] connector / ESD ground region connects robustly to reference structure
- [ ] any layer transition has symmetric P/N vias and reviewed return transition
- [ ] local GND patch is not being mistaken for a continuous plane

## 5. Differential Geometry

- [ ] width/gap calculated from current fab stackup
- [ ] video/blog example geometry not copied directly
- [ ] open-field pair geometry is stable
- [ ] connector / ESD fan-out sections are short
- [ ] P/N geometry is symmetric through pads and transitions
- [ ] no unnecessary detour created just to satisfy the router
- [ ] no dense skew meander without a real budget

## 5.1 Forum-Derived Stress Checks

> 这些检查来自实际工程师对 USB 2.0 布板的争论，用来找“看起来很专业但方向错了”的设计。它们不是协议规范。

### Geometry Before Cosmetics

- [ ] 没有为了亚毫米级 mismatch 自动添加密集蛇形
- [ ] 若添加 tuning，已写出当前 USB mode / device guide 的 skew budget
- [ ] meander 本身的局部 coupling / spacing 已检查
- [ ] pair 附近新增 copper 后重新确认了阻抗模型

### Microstrip vs Coplanar

- [ ] 若同层 GND pour 靠近 DP/DM，阻抗模型已切换/纳入 coplanar geometry
- [ ] soldermask 已按 fab model 纳入 calculator / field solver
- [ ] 没有把“铺更多 GND”自动等同于“阻抗更正确”
- [ ] copper-to-pair setback 有来源：solver / fab，而不是固定 3W 口号

### ESD / Stub

- [ ] ESD 器件没有通过长 stub 挂到主线上
- [ ] connector→ESD→PHY 尽量形成 flow-through path
- [ ] 测试点/探针焊盘没有形成明显 branch stub
- [ ] ESD GND discharge path 与 signal reference path 都已单独画出

### Evidence Note

记录以下任一项时，不写“论坛推荐”，而写：

~~~text
Observation:
Physical reason:
Project requirement:
Chosen geometry:
Evidence / source:
~~~

Forum threads used as practitioner context:

- https://electronics.stackexchange.com/questions/52851/usb-differential-pair-length
- https://electronics.stackexchange.com/questions/496135/advice-for-90-ohm-traces-of-a-usb-2-0-hub
- https://electronics.stackexchange.com/questions/669162/unexpected-low-characteristic-impedance-using-the-jlcpcb-impedance-calculator


## 6. Neighbor / EMC Review

- [ ] VBUS does not run long and close to DP/DM
- [ ] switching nodes / clocks are kept away
- [ ] no long test stub on DP/DM
- [ ] ESD boundary is at the connector
- [ ] shield / chassis strategy is documented if applicable

## 7. KiCad Evidence

- Net class:
- Tuning profile:
- Differential router screenshot:
- L2 reference projection screenshot:
- Connector/ESD close-up screenshot:
- DRC result:
- Review commit:

## 8. Release Decision

- [ ] PASS
- [ ] PASS WITH ACTIONS
- [ ] FAIL

### Open Actions

| ID | Issue | Physical reason | Fix | Evidence | Status |
|---|---|---|---|---|---|
| USB-01 | | | | | |
