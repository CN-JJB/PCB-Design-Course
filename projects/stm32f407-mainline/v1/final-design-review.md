# STM32F407 V1｜Final Design Review

## Project identity

- PCB revision:
- source commit:
- KiCad version:
- BOM revision:
- test firmware commit:
- reviewer/date:

## System

- [ ] system-spec frozen
- [ ] source-freeze current
- [ ] open TBD list reviewed

## Power / Clock

- [ ] regulator budget valid
- [ ] MCU supply/VCAP valid
- [ ] HSE strategy validated
- [ ] reset/boot/debug validated

## PCB

- [ ] stackup/reference explainable
- [ ] L2 solid GND
- [ ] placement current loops explainable
- [ ] critical nets reference-aware
- [ ] DRC + manual review complete

## Manufacturing

- [ ] fab outputs archived/reproducible
- [ ] BOM exact enough for build
- [ ] critical footprints verified

## Bring-up

- [ ] power evidence
- [ ] SWD evidence
- [ ] UART/LED evidence
- [ ] HSE evidence
- [ ] issue/fix/retest log

## Graduation questions

Answer without relying only on screenshots:

1. Why four layers?
2. Why this stackup?
3. Why is L2 kept solid?
4. What is the return path of SWCLK?
5. What is the current loop of one VDD decoupler?
6. Why is HSE placed there?
7. Which rules came from ST, fab, or course target?
8. Which checks DRC cannot prove?
9. What did bring-up actually validate?

## Decision

- [ ] PASS — enter Part 2
- [ ] CONDITIONAL — accepted items documented
- [ ] FAIL — reopen listed Gate

Next: [Part 2 Signal Integrity](../../../12_Part2_信号完整性/00_本Part导读.md)
