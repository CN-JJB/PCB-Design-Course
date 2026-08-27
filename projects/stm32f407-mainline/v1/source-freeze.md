# STM32F407 V1｜Source Freeze

> 任何写进 PCB 的关键数字，都应该能从这里追到源头。

| Item | Exact source | Revision / date | Retrieved | Used for | Recheck |
|---|---|---|---|---|---|
| STM32F407 datasheet | TBD exact revision | TBD | 2026-08-26 baseline | pins/power/electrical | release |
| STM32F4 hardware guide | ST AN4488 | TBD | 2026-08-26 baseline | power/reset/layout | release |
| oscillator guide | ST AN2867 if crystal used | TBD | TBD | HSE network | HSE freeze |
| regulator | AP2112 datasheet | TBD | 2026-08-26 baseline | CIN/COUT/thermal | BOM freeze |
| PCB fab | JLC04161H-3313 teaching case | current query | 2026-08-26 | stackup | order |
| KiCad | 10.0.x official docs | current | 2026-08-26 | tool/rules | release |

## Frozen numbers / assumptions

| Item | Value | Type | Source |
|---|---|---|---|
| MCU | STM32F407VGT6 | REQ | project |
| Layers | 4 | TARGET | course |
| VDD local decoupling | per current ST guidance | REQ | ST |
| VCAP | per exact device configuration | REQ | ST |
| Default geometry | see hardware-constraints | EXAMPLE | course |
| Final stackup | TBD before order | FAB | manufacturer |

## Reopen triggers

- MCU/package suffix change
- regulator change
- HSE part change
- board manufacturer/stackup change
- KiCad major version change
- new silicon errata affecting hardware
