# FPGA PDN Review

## Rail Targets

| Rail | Voltage | Estimated Current | Allowed Ripple | Target Impedance | Regulator | Evidence |
|---|---:|---:|---:|---:|---|---|
| VCCINT | 1.0 | TBD | TBD | TBD | TBD | XPE |
| VCCBRAM | 1.0 | TBD | TBD | TBD | TBD | XPE |
| VCCAUX | 1.8 | TBD | TBD | TBD | TBD | XPE |
| VCCO_3V3 | 3.3 | TBD | TBD | TBD | TBD | XPE |
| VCCO_DDR | 1.5 | TBD | TBD | TBD | TBD | XPE/MIG |
| MGT rails | TBD | TBD | TBD | TBD | TBD | DS181/UG482 |

## Decoupling
- capacitor source/model:
- DC bias checked:
- mounting loop:
- BGA backside placement:
- via strategy:
- plane spreading:
- anti-resonance review:

## Sequencing
- startup capture:
- power-off capture:
- PROGRAM_B / INIT_B / DONE overlay:

## Thermal
- power estimate:
- ambient:
- airflow:
- measured temperature:
