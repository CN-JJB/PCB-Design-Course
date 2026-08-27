# DDR3 / MIG Plan

## Memory

- Part: AS4C64M16D3B-12BIN
- Density: 1 Gbit
- Organization: 64M × 16
- VDD/VDDQ: 1.5 V
- Package: 96-ball FBGA

## MIG

- Vivado version:
- MIG version:
- Interface width: x16
- Data rate: TBD
- System clock: TBD
- Bank selection: TBD
- Generated XDC commit: TBD

## Byte Lanes

| Byte Lane | DQS Pair | DQ[7:0] | DM | Bank | VCCO |
|---|---|---|---|---|---:|
| BL0 | TBD | TBD | TBD | TBD | 1.5 V |
| BL1 | TBD | TBD | TBD | TBD | 1.5 V |

## Address/Control

- Bank:
- CK pair:
- Address:
- BA:
- RAS/CAS/WE:
- CKE/CS/ODT:
- VREF:
- VRP/VRN/DCI:

## Rule

Any PCB-driven pin swap must be revalidated through MIG/Vivado.
