# V2 SI Routing Constraints

> 这里记录“真正要落进 KiCad 的数字”，并强制保存来源。不要把博客经验值直接当生产规则。

---

## 1. Board Stackup Baseline

- Board fab: JLCPCB（教学案例）
- Layer count: 4
- Board thickness: 1.6 mm class
- Stackup name: 继承 Part 1 已记录的实际 stackup
- Query date: 2026-08-26
- Fabricator page: https://jlcpcb.com/impedance

> 下单前重新核对板厂当前 stackup；如果 stackup 变化，本文件的 controlled-impedance geometry 全部重新计算。

---

## 2. USB FS Differential Pair

- Mode: USB Full-Speed device, STM32 embedded FS PHY
- Protocol source: USB-IF current USB 2.0 documents
- MCU guide: ST AN4879
- Routing layer: L1 preferred
- Reference: L2 solid GND
- Pair width: **TBD by current fab field solver**
- Pair gap: **TBD by current fab field solver**
- Pair-to-other clearance: **TBD from board geometry / review**
- Max skew: **do not invent universal number; derive from applicable guide**
- Layer transitions: avoid if possible for V2 teaching board
- ESD: near connector
- VBUS: route away from DP/DM

### KiCad

Create `USB_FS` Net Class with the solved width/gap. Use differential router rather than manually drawing two independent tracks.

---

## 3. SDIO_CK

- Source: STM32F407
- Load: SD card interface
- Topology: point-to-point clock
- Routing: L1 / L2 GND preferred
- Source resistor footprint: yes, near MCU
- Initial fitted value: TBD by design/measurement; do not default to 33 Ω without justification
- Clearance: more than manufacturing minimum where routing space permits
- Long parallel run with data: minimize

---

## 4. SPI_SCK

- Source: STM32F407
- Load: on-board or external target
- If routed to connector, re-evaluate line length including cable
- Source resistor footprint: recommended for experiment
- Controlled impedance: only if analysis indicates need; not automatic

---

## 5. General SI Geometry Rules

These are design objectives, not universal numerical standards:

1. Keep critical nets over continuous reference plane.
2. Minimize unnecessary impedance discontinuities.
3. Avoid long stubs.
4. For layer transitions, review the corresponding return transition.
5. Increase spacing on high-risk aggressor/victim pairs rather than blindly using fab minimum.
6. Differential transition geometry should be symmetric.
7. Avoid dense meanders unless a real skew target requires them.
8. Preserve measurement access without creating long test stubs.

---

## 6. Constraint Source Hierarchy

Priority:

1. Protocol specification / compliance requirement
2. MCU / PHY / memory vendor hardware guide
3. Board fabricator stackup / impedance solver
4. IBIS / simulation / measurement
5. Engineering heuristic

If two sources conflict, record the conflict and resolve it explicitly; do not silently pick the prettier number.
