# V3 Source Freeze

| Item | Exact Source | Revision / Date | Retrieved | Used For | Recheck |
|---|---|---|---|---|---|
| STM32H743 datasheet | DS12110 | TBD | 2026-08-26 | FMC/power/pins | release |
| STM32H7 RM | RM0433 | TBD | 2026-08-26 | FMC/ETH registers | release |
| STM32H743 errata | ES0392 | TBD | 2026-08-26 | silicon limits | release |
| H7 hardware guide | AN4938 | Rev 7 baseline | 2026-08-26 | power/layout | release |
| SDRAM | AS4C4M16SA datasheet | TBD | 2026-08-26 | timing | release |
| PHY | LAN8742A datasheet | TBD | 2026-08-26 | RMII/MDI | release |
| Reference board | NUCLEO-H743ZI2 schematic | current | 2026-08-26 | RMII baseline | optional |
| PCB fab | six-layer stackup | TBD | TBD | impedance | order |
| KiCad | PCB Editor docs | 10.0.x | 2026-08-26 baseline | rules | release |

## Critical Frozen Numbers

- FMC_SDCLK: 100 MHz project baseline
- SDRAM skew target: <=100 ps project initial target
- RBIAS: 12.1 kΩ 1% per PHY requirement
- MDI geometry: TBD from final stackup

Any source revision change triggers a recheck of dependent rules.
