# V2 Pin / Clock / Peripheral Plan

> Pin number / AF number 必须在实际设计时从当前 STM32F407 datasheet / RM0090 / CubeMX 核对。本模板不把固定 pin number 当教材真理。

## Peripheral map

| Function | Signal | Preferred pin | Alternate | Conflict | Physical direction | Frozen |
|---|---|---|---|---|---|---|
| USB FS | DP | TBD | — | — | USB edge | ☐ |
| USB FS | DM | TBD | — | — | USB edge | ☐ |
| CAN1 | TX | TBD | TBD | TBD | CAN zone | ☐ |
| CAN1 | RX | TBD | TBD | TBD | CAN zone | ☐ |
| SDIO | CK | TBD | TBD | TBD | microSD | ☐ |
| SDIO | CMD | TBD | TBD | TBD | microSD | ☐ |
| SDIO | D0 | TBD | TBD | TBD | microSD | ☐ |
| SDIO | D1 | TBD | TBD | TBD | microSD | ☐ |
| SDIO | D2 | TBD | TBD | TBD | microSD | ☐ |
| SDIO | D3 | TBD | TBD | TBD | microSD | ☐ |
| SWD | SWDIO | fixed/debug | — | do not repurpose | SWD edge | ☐ |
| SWD | SWCLK | fixed/debug | — | do not repurpose | SWD edge | ☐ |
| Debug | UART TX | TBD | TBD | TBD | header | ☐ |
| Debug | UART RX | TBD | TBD | TBD | header | ☐ |

## Clock plan

| Clock | Target | Source | Consumers | Constraint / note |
|---|---:|---|---|---|
| HSE | TBD | crystal/oscillator | SYSCLK PLL | AN2867 / project |
| SYSCLK | ≤ device limit | PLL | CPU/bus | RM0090 |
| 48 MHz domain | 48 MHz target | PLL | USB / SDIO-related domain | RM0090 |
| SDIO_CK | TBD | SDIO divider | microSD | RM0090 + ES0182 |

## ES0182 SDIO contract

- [ ] Hardware flow control limitation reviewed
- [ ] NEGEDGE limitation reviewed
- [ ] BYPASS limitation reviewed
- [ ] DMA/PCLK2/SDIO_CK relationship reviewed
- [ ] Silicon revision recorded
- [ ] Firmware workaround owner assigned

## Floorplan sanity

- [ ] USB pins face USB zone reasonably
- [ ] SDIO pins can fan out to socket without cross-board routing
- [ ] CAN pins do not force PHY into MCU core
- [ ] SWD remains physically accessible
- [ ] oscillator pins remain local
