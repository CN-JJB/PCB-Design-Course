# FPGA Power Rail Budget

## Tool Inputs

- XPE version:
- Vivado version:
- Device:
- Junction target:
- Ambient:
- Airflow:
- Logic utilization:
- Clock activity:
- I/O activity:
- DDR:
- GTP:

## Rail Budget

| Rail | Nominal | Static | Dynamic | Transient/Peak | Regulator | Margin |
|---|---:|---:|---:|---:|---|---:|
| VCCINT | 1.0 V | TBD | TBD | TBD | TBD | TBD |
| VCCBRAM | 1.0 V | TBD | TBD | TBD | TBD | TBD |
| VCCAUX | 1.8 V | TBD | TBD | TBD | TBD | TBD |
| VCCO_3V3 | 3.3 V | TBD | TBD | TBD | TBD | TBD |
| VCCO_DDR | 1.5 V | TBD | TBD | TBD | TBD | TBD |
| DDR VTT | 0.75 V class | TBD | TBD | TBD | TBD | TBD |
| MGTAVCC | verify DS181 | TBD | TBD | TBD | TBD | TBD |
| MGTAVTT | verify DS181 | TBD | TBD | TBD | TBD | TBD |

## Sequencing

Recommended baseline from DS181:

VCCINT → VCCBRAM → VCCAUX → VCCO  
Power-off reverse.

Exact regulator implementation:
- TBD

## Evidence

- XPE report:
- schematic:
- startup capture:
- rail ripple:
- regulator temperature:
