# V3 Pin / Peripheral Map

> Recheck against the latest exact-part STM32H743ZIT6 alternate-function table before release.

## P0 Peripherals

### RMII Baseline

| Signal | MCU Pin | AF | Source |
|---|---|---|---|
| REF_CLK | PA1 | ETH | NUCLEO baseline |
| MDIO | PA2 | ETH | NUCLEO baseline |
| CRS_DV | PA7 | ETH | NUCLEO baseline |
| TXD1 | PB13 | ETH | NUCLEO baseline |
| MDC | PC1 | ETH | NUCLEO baseline |
| RXD0 | PC4 | ETH | NUCLEO baseline |
| RXD1 | PC5 | ETH | NUCLEO baseline |
| TX_EN | PG11 | ETH | NUCLEO baseline |
| TXD0 | PG13 | ETH | NUCLEO baseline |

### FMC SDRAM Control

| Signal | MCU Pin | Intent |
|---|---|---|
| SDNWE | PH5 | avoid RMII conflict |
| SDNE1 | PH6 | Bank 2 |
| SDCKE1 | PH7 | Bank 2 |
| SDCLK | PG8 | clock |
| SDNRAS | PF11 | command |
| SDNCAS | PG15 | command |
| NBL0 | PE0 | byte mask |
| NBL1 | PE1 | byte mask |

### Conflict Review

- [ ] PA7 not consumed by FMC alternative
- [ ] PC4/PC5 not consumed by FMC alternative
- [ ] SWD pins reserved
- [ ] HSE pins reserved
- [ ] USB pins reserved
- [ ] boot strap pins reviewed
- [ ] all package power pins accounted for
