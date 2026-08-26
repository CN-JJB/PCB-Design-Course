# V2 BOM Risk Register

| Ref/Function | Candidate MPN | Critical parameters | DNP/Default | Alternate policy | Risk | Source |
|---|---|---|---|---|---|---|
| MCU | STM32F407VGT6 | package/revision/temp | populate | exact/approved family only | availability/revision | ST |
| USB-C | TBD | USB2 receptacle, mechanical tabs, cycle rating | populate | footprint-compatible only after mech review | footprint/mechanical | vendor + USB-IF |
| USB ESD | TBD | VRWM, low C, IEC performance | populate | parameter-equivalent | SI/ESD | vendor/ST |
| CAN PHY | TCAN332-family candidate | VCC, common-mode, fault, temp | populate | re-review electrical behavior | bus/EMC | TI |
| CAN TVS | TBD | standoff/clamp/capacitance | populate | transient target equivalent | protection | vendor/ref design |
| CAN CMC | TBD | impedance/current/parasitic | DNP default | populate only after EMC evidence | SI/EMC trade-off | vendor |
| CAN term | 120 Ω candidate | tolerance/power | DNP default | populate only if endpoint | topology | CAN system |
| microSD socket | TBD | detect, mechanical, insertion | populate | footprint/mech validated | supply/mechanical | vendor |
| 3V3 regulator | TBD | VIN/IOUT/thermal/stability | populate | full power review | thermal margin | vendor |
| MLCC | TBD | effective C @ DC bias, ESR/ESL, voltage | populate | verified effective-C substitute | PI | vendor |

## DNP decision template

```text
Ref:
Default: Populate / DNP
Why:
When to change:
Allowed values/parts:
Measurement that justifies change:
Impact if wrong:
```
