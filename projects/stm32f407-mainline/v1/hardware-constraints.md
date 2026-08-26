# STM32F407 V1｜Hardware Constraints

> 状态：Part 1 baseline。任何具体器件/板厂变更都必须更新本表。

## 1. MCU

```text
Part: STM32F407VGT6
Package: LQFP100
Primary source: ST Datasheet + AN4488
```

Sources:

- https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html
- https://www.st.com/resource/en/datasheet/stm32f407vg.pdf
- https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf

## 2. Power

| Item | Constraint / baseline | Source | PCB interpretation |
|---|---|---|---|
| VDD | one 100 nF ceramic per VDD pin | ST AN4488 | local low-inductance loop to adjacent GND |
| package bulk | min 4.7 µF, typ 10 µF in AN4488 guidance | ST AN4488 | MCU power region, not a replacement for local caps |
| VDDA | 100 nF + 1 µF guidance | ST AN4488 | local analog supply decoupling |
| VCAP1/2 | 2.2 µF low-ESR ceramic each for applicable two-VCAP configuration | ST AN4488 / DS | extremely short to pin/GND; no external load |
| VBAT | connect per AN4488 when no battery used | ST AN4488 | must not be left as an undefined afterthought |
| 3V3 regulator | AP2112K-3.3 teaching choice | Diodes AP2112 DS | thermal budget required; CIN/COUT per DS |

AP2112 source:
https://www.diodes.com/part/view/AP2112

## 3. Clock

| Item | Constraint |
|---|---|
| Initial bring-up | internal oscillator first |
| HSE | exact crystal/oscillator part TBD from required accuracy and clock plan |
| Load capacitors | calculate from selected crystal CL + MCU guidance + parasitics; do not copy generic value |
| PCB | crystal/load network close to oscillator pins; no unnecessary stub |

## 4. Reset / Boot / Debug

| Item | Baseline |
|---|---|
| BOOT0 | known default state for normal Flash boot; controllable for recovery |
| NRST | implement per ST hardware guide; manual button + debug access |
| SWDIO | route to accessible debug header |
| SWCLK | short; primary reference L2 GND when on L1 |
| VTREF | target 3V3 to debugger as required by selected ST-LINK connection |
| GND | debug connector has clear low-impedance ground connection |
| SWO | optional teaching/debug feature |

## 5. Stackup

Teaching case, checked 2026-08-26:

```text
JLCPCB JLC04161H-3313 / nominal 1.6 mm
L1 outer Cu: 0.035 mm
3313 PP:      0.09940 mm
L2 inner Cu:  0.0152 mm
Core:         1.265 mm
L3 inner Cu:  0.0152 mm
3313 PP:      0.09940 mm
L4 outer Cu:  0.035 mm
```

Source:
https://jlcpcb.com/impedance

Policy:

```text
L1 = primary signal
L2 = solid GND reference
L3 = power distribution
L4 = secondary signal
```

## 6. Course Geometry Baseline

这些是 V1 的保守教学几何，不是板厂下限，也不是电气上限：

```text
Default trace:     0.20 mm
Default clearance: 0.20 mm
General via:       0.60 / 0.30 mm
Light power route: 0.50 mm starting point only
```

需要电流能力时重新做 current/thermal/voltage-drop analysis。

## 7. Critical Nets

| Net | Layer preference | Reference | Why |
|---|---|---|---|
| HSE_IN/OUT | L1 local | L2 | oscillator loop |
| SWCLK | L1 | L2 | potentially fast edge |
| SWDIO | L1 preferred | L2 | debug integrity |
| NRST | L1/simple | L2 | bring-up/recovery |
| VCAP1/2 | local only | GND | regulator stability |
| 3V3_MAIN | L3 + local L1 | GND/power network | supply distribution |

## 8. Open Items / TBD

- [ ] exact 5 V connector
- [ ] exact HSE part and CL network
- [ ] exact SWD connector family/pinout
- [ ] final AP2112 thermal budget after load estimate
- [ ] final expansion-header pin map
- [ ] final board dimension after mechanical review
- [ ] final manufacturer stackup re-check immediately before order

**TBD 是可见风险，不是错误。没有来源的伪精确数字才是错误。**