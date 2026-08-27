# Vivado XDC ↔ KiCad Constraint Map

| Signal/Group | Ball | Bank | VCCO | IOSTANDARD / Resource | XDC Source | KiCad Net | PCB Rule Class | Status |
|---|---|---|---:|---|---|---|---|---|
| SYSCLK | TBD | TBD | TBD | clock-capable | XDC | SYSCLK | CLOCK | TBD |
| DDR3_BL0 | MIG | MIG | 1.5 V | MIG | generated | group | DDR3_BL0 | TBD |
| DDR3_BL1 | MIG | MIG | 1.5 V | MIG | generated | group | DDR3_BL1 | TBD |
| GTP_TX | MGT | n/a | n/a | GTP | XDC | GTP_TX | GTP | TBD |

## Change Control

Any pin swap requires:

1. Vivado legality check
2. XDC update
3. schematic update
4. PCB net update
5. DRC / route review
6. regenerated table
7. commit freeze

## Version Freeze

- XDC commit:
- schematic commit:
- PCB commit:
- MIG output:
- KiCad rule file:
