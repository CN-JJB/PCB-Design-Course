# STM32F407 V1｜Placement Plan

## Placement order

~~~text
Board outline / holes
→ connectors
→ MCU
→ regulator power path
→ MCU decoupling / VCAP
→ HSE
→ SWD / UART
→ LED / button
→ GPIO headers
→ test points
~~~

## Zones

| Zone | Anchor | Must be near | Must stay away from | Status |
|---|---|---|---|---|
| MCU core | U1 | decoupling/VCAP/HSE | noisy connector edge | ☐ |
| Power | input/LDO | CIN/COUT | HSE | ☐ |
| Debug | SWD edge | MCU | inaccessible interior | ☐ |
| Expansion | headers | intended pin groups | critical HSE loop | ☐ |

## Current-loop review

### 3V3 local decoupling

~~~text
VDD pin → local capacitor → GND via/plane → MCU GND
~~~

Actual refs / pins: TBD

### Regulator input loop

Actual components/path: TBD

### Regulator output loop

Actual components/path: TBD

## Gate 5 Pass

- [ ] mechanical anchors frozen
- [ ] each MCU decoupling capacitor has a clear served region/pin
- [ ] VCAP extremely local
- [ ] HSE local and quiet
- [ ] power path visually obvious
- [ ] SWD/UART/test access practical
- [ ] no critical component waiting for “routing later”

通过后进入：[routing-rule-plan.md](routing-rule-plan.md)
