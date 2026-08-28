
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
