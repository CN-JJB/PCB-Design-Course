# STM32H743 V3 System Specification

## Identity

- Project: STM32H743 V3 Six-Layer
- MCU: STM32H743ZIT6 / LQFP144
- PCB: 6-layer controlled impedance
- Status: teaching baseline / not production frozen

## Functional Scope

| Function | Requirement | Status |
|---|---|---|
| SDRAM | 8 MiB x16 SDR SDRAM | Frozen |
| Ethernet | 10/100 RMII | Frozen |
| USB | USB FS | Frozen |
| Debug | SWD | Frozen |
| Expansion | UART/I2C/GPIO as space allows | Secondary |

## Performance Baseline

- CPU: up to 480 MHz device capability; firmware operating point TBD
- FMC_SDCLK: 100 MHz project baseline
- RMII_REF_CLK: 50 MHz
- SDRAM: AS4C4M16SA-6TIN candidate

## Power

| Rail | Source | Loads | Peak assumption | Validation |
|---|---|---|---|---|
| 5V_IN | external | regulator | TBD | input current |
| 3V3_SYS | regulator | MCU/SDRAM/PHY | TBD | rail scope |
| VDDA/VREF | filtered branch | MCU analog | TBD | ripple |
| VCAP | internal LDO support | MCU only | n/a | voltage check |

## Environment / Manufacturing

- Board thickness: 1.6 mm nominal
- Stackup ID: TBD at production freeze
- Temperature target: TBD
- Enclosure: TBD
- ESD target: TBD
- Assembly: standard SMT + connectors

## Exit Criteria

- [ ] source freeze complete
- [ ] pin map frozen
- [ ] power/clock plan frozen
- [ ] stackup/impedance frozen
- [ ] SDRAM timing/routing review passed
- [ ] Ethernet boundary review passed
- [ ] SI/PI/EMC joint review passed
- [ ] bring-up/validation evidence archived
