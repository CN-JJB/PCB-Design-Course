# Artix-7 V1 Validation Matrix

| ID | Test | Condition | Expected | Actual | Evidence | Pass |
|---|---|---|---|---|---|---|
| V01 | JTAG IDCODE | power-up | correct device | TBD | HW Manager | TBD |
| V02 | SYSCLK | nominal | stable | TBD | scope | TBD |
| V03 | SPI boot | repeated cycles | reliable boot | TBD | log/scope | TBD |
| V04 | Bank 3V3 | load | correct levels | TBD | scope | TBD |
| V05 | Bank 1V8 | load | correct levels | TBD | scope | TBD |
| V06 | DDR3 MIG | nominal | calibration pass | TBD | report | TBD |
| V07 | DDR3 stress | long-run | zero errors | TBD | log | TBD |
| V08 | DDR3 thermal | temp | target | TBD | log | TBD |
| V09 | GTP internal | diagnostic | target | TBD | tool report | TBD |
| V10 | GTP external | connector | target | TBD | tool report | TBD |
| V11 | PDN | worst load | within rail target | TBD | scope | TBD |
| V12 | Thermal | worst load | within target | TBD | thermal | TBD |

No PASS without evidence.
