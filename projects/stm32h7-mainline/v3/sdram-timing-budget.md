# SDRAM Timing Budget

## Clock

- FMC_SDCLK: 100 MHz
- Tclk: 10 ns
- SDRAM: AS4C4M16SA-6TIN

## Memory Timing → FMC Cycles

| Field | Memory Requirement | Calculation | Physical Cycles | Register/HAL Encoding | Final |
|---|---:|---|---:|---|---|
| TRCD | 18 ns min | ceil(18/10) | 2 | verify RM0433 | TBD |
| TRP | 18 ns min | ceil(18/10) | 2 | verify | TBD |
| TRAS | 42 ns min | ceil(42/10) | 5 | verify | TBD |
| TRC | 60 ns min | ceil(60/10) | 6 | verify | TBD |
| TWR | 2 tCK min | direct | 2 | verify | TBD |
| TMRD | 2 tCK min | direct | 2 | verify | TBD |
| TXSR | 61.5 ns example | ceil(61.5/10) | 7 | verify | TBD |

## Refresh

- Rows/cycles: 4096 refresh / 64 ms
- Average interval: 15.625 µs
- 100 MHz equivalent: ~1562.5 SDCLK cycles
- FMC COUNT formula: verify RM0433
- Margin: TBD
- Final value: TBD

## CAS / Read Settings

- CAS latency baseline: CL3
- Read pipe: TBD from controller timing
- GPIO speed: TBD from timing + scope validation

## PCB Timing Budget

| Group | Setup/Hold Source | Board Skew Target | Actual | Margin |
|---|---|---:|---:|---:|
| SDCLK↔Address/Control | MCU+SDRAM | TBD | TBD | TBD |
| SDCLK↔Write Data | MCU+SDRAM | TBD | TBD | TBD |
| SDCLK↔Read Data | MCU+SDRAM | TBD | TBD | TBD |

## Rule

No programmed timing value is allowed without a source and unit conversion record.
