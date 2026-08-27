# STM32F407 V1｜System Specification

Status: **DRAFT → FROZEN before schematic completion**

## 1. Project identity

| Item | Decision | Source / reason |
|---|---|---|
| MCU | STM32F407VGT6 / LQFP100 | course mainline |
| PCB | 4 layers | Part 1 goal |
| Input | 5 V external input | teaching baseline |
| Main rail | 3.3 V | MCU / GPIO / debug |
| Debug | SWD + UART | bring-up |
| Clock | internal first + HSE footprint | staged bring-up |

## 2. Must-have functions

- [ ] MCU minimum system
- [ ] 3.3 V regulator
- [ ] SWD
- [ ] NRST
- [ ] BOOT0
- [ ] UART console
- [ ] user LED
- [ ] user button
- [ ] GPIO expansion
- [ ] test points
- [ ] mounting holes

## 3. Explicitly out of scope

- USB data
- CAN transceiver
- SD card
- Ethernet
- SDRAM
- HDMI
- RF
- BGA

## 4. Mechanical freeze

| Item | Decision | Status |
|---|---|---|
| Board size | TBD | ☐ |
| 5 V input connector / edge | TBD | ☐ |
| SWD connector / edge | TBD | ☐ |
| UART access | TBD | ☐ |
| GPIO header orientation | TBD | ☐ |
| Mounting holes | TBD | ☐ |

## 5. Power budget

| Load | Avg | Peak / design max | Evidence | Margin |
|---|---:|---:|---|---:|
| STM32F407 | TBD | TBD | datasheet / workload assumption | TBD |
| LEDs | TBD | TBD | calculation | TBD |
| external GPIO allowance | TBD | TBD | project target | TBD |
| other | TBD | TBD | | |
| **Total** | **TBD** | **TBD** | | **TBD** |

## 6. Acceptance Gate

Gate 1 只有在下面全部成立后才通过：

- [ ] 必做/不做范围固定；
- [ ] mechanical blocker 已解决；
- [ ] power input / debug / clock strategy 明确；
- [ ] load budget 足以开始 regulator thermal review；
- [ ] 仍保留的 TBD 不阻止 schematic。

通过后进入：[power-clock-plan.md](power-clock-plan.md)
