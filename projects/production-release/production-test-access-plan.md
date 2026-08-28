# Production Test Access Plan

> 在 PCB Layout Freeze 前完成。目标不是“列出测试点”，而是定义生产缺陷如何被发现、定位和记录。

## 1. Product / Test Identity

- Product:
- HW Revision:
- Test Revision:
- EMS / Test Site:
- Planned Volume:
- Target Test Cycle:
- Fixture Side: TBD
- Fixture Revision: TBD

## 2. Fault Coverage Map

| ID | Fault / Defect | Detection Stage | Stimulus | Observation | Access Method | Pass/Fail | Diagnostic Resolution |
|---|---|---|---|---|---|---|---|
| TST-001 | | AOI / FP / ICT / FCT | | | | | |
| TST-002 | | | | | | | |

## 3. Physical Access Inventory

| Net / Node | Need | Side | Pad/Connector | Reference/GND | Instrument | Loading Risk | Fixture Probe |
|---|---|---|---|---|---|---|---|
| GND | reference | TBD | | | | low | |
| main rail | voltage | TBD | | | | low | |
| reset | control | TBD | | | | low | |
| program/debug | firmware | TBD | | | | medium | |
| high-speed/RF | only if justified | TBD | controlled access | | | high | |

## 4. High-Speed / RF Loading Review

For every access point on a sensitive net:

- [ ] pad / via / stub included in channel review
- [ ] reference path defined
- [ ] connector/probe transition defined
- [ ] calibration / de-embedding plan if required
- [ ] alternate BIST / loopback / boundary-scan considered

## 5. Fixture Mechanics

- datum / locating features:
- board support:
- pogo travel:
- keepout:
- connector height conflicts:
- top/bottom access:
- operator loading:
- expected probe life:
- maintenance interval:
- fixture self-test / golden DUT:

## 6. Programming / Traceability

- programmer:
- device ID/readback:
- firmware revision:
- serial number write:
- calibration data:
- test result storage:
- DUT ↔ test-log mapping:

## 7. Review Gate

- [ ] key production faults have detection paths
- [ ] critical rails / reset / programming are observable as required
- [ ] fixture side frozen
- [ ] sensitive-net test loading reviewed
- [ ] board support / datum frozen
- [ ] fixture revision and calibration controlled
- [ ] test result linked to DUT identity
