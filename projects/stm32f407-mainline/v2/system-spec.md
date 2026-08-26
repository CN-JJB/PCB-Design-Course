# STM32F407 V2 — System Specification

Status: `DRAFT → FROZEN before placement`

## Product intent

四层 MCU 综合训练板：把 USB FS、CAN、microSD/SDIO、SWD、3.3 V power tree 与 SI/PI/EMC/DFM 方法集中到同一块 PCB。

## Frozen scope

| Item | Decision | Source / reason |
|---|---|---|
| MCU | STM32F407VGT6 / LQFP100 | V1→V2 continuity |
| PCB | 4-layer | Part 5 goal |
| USB | USB 2.0 FS device | ST AN4879 + USB-IF |
| Connector | USB-C, USB2-only UFP | modern connector exercise |
| CAN | classic CAN 2.0B ×1 | STM32F407 bxCAN |
| CAN PHY | 3.3 V CAN transceiver candidate: TCAN332 family | final MPN review required |
| Storage | microSD, SDIO 4-bit | RM0090 + ES0182 |
| Debug | SWD + UART console | bring-up |
| Input | USB VBUS 5 V | simplified V2 power source |
| Main rail | 3.3 V | MCU/SD/CAN PHY |

## Explicitly out of scope

- USB PD
- USB SuperSpeed
- Ethernet
- SDRAM
- HDMI
- RF
- BGA
- isolated CAN
- CAN FD controller functionality

## Mechanical freeze

- Board size: `TBD`
- USB edge: `TBD`
- CAN edge: `TBD`
- microSD insertion direction: `TBD`
- SWD access after enclosure: `TBD`
- Mounting holes: `TBD`

## Power budget

| Load | Average | Peak | Evidence | Margin |
|---|---:|---:|---|---:|
| STM32F407 | TBD | TBD | datasheet/measurement | TBD |
| microSD | TBD | TBD | card measurement/design target | TBD |
| CAN PHY | TBD | TBD | datasheet | TBD |
| LEDs/other | TBD | TBD | calculation | TBD |
| Total | TBD | TBD | | |

## Acceptance gates

- [ ] Schematic review passed
- [ ] Placement freeze passed
- [ ] Routing review passed
- [ ] SI/PI/EMC joint review passed
- [ ] DFM/BOM review passed
- [ ] Release gate passed
- [ ] Bring-up matrix passed
