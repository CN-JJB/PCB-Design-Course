# DDR3 Routing Review

## Reference

- MIG generated pinout:
- MIG example design:
- board stackup:
- impedance source:
- propagation:
- DDR3 datasheet:

## Groups

| Group | Nets | Layer | Reference | Skew/Timing Rule | Via Budget | Actual |
|---|---|---|---|---|---|---|
| CK | CK_P/N | TBD | TBD | MIG | low | TBD |
| BL0 | DQS0/DQ0..7/DM0 | TBD | TBD | MIG | low | TBD |
| BL1 | DQS1/DQ8..15/DM1 | TBD | TBD | MIG | low | TBD |
| A/C | Address/Command | TBD | TBD | MIG | low | TBD |

## Topology

- memory count/rank:
- address/control topology:
- termination:
- ODT:
- VTT:
- VREF:

## Manual Review

- [ ] DQ stays with correct DQS byte group
- [ ] DQS pair uses dedicated pins
- [ ] CK route clean
- [ ] no split reference crossing
- [ ] byte-lane via behavior consistent
- [ ] meander not excessively dense
- [ ] VREF/VTT kept quiet
- [ ] MIG report archived
