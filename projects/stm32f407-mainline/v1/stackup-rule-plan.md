# STM32F407 V1｜Stackup & Rule Plan

## 1. Fabricator case

- Manufacturer: JLCPCB teaching case
- Stackup ID: JLC04161H-3313 baseline
- Query date: 2026-08-26
- Recheck date before order: TBD

## 2. Layer roles

| Layer | Role | Main reference | Rules |
|---|---|---|---|
| L1 | component + primary signal | L2 GND | critical nets preferred |
| L2 | solid GND | — | no ordinary signal |
| L3 | power distribution | — | review splits/necks |
| L4 | secondary signal | primarily L3 structure | critical nets reviewed individually |

## 3. Rule source hierarchy

1. device requirement
2. project electrical target
3. fab capability
4. teaching heuristic

## 4. KiCad rule baseline

| Class | Width | Clearance | Via | Source / note |
|---|---:|---:|---|---|
| Default | TBD | TBD | TBD | design > fab min |
| Power | TBD | TBD | TBD | IR/thermal |
| Clock/Debug critical | TBD | TBD | TBD | reference-aware |
| Mechanical/keepout | n/a | n/a | n/a | drawing |

## 5. Stackup Freeze Gate

- [ ] actual dielectric/copper data recorded
- [ ] manufacturing minimum separated from design rule
- [ ] L2 solid GND policy agreed
- [ ] layer roles documented in KiCad
- [ ] critical net classes created
- [ ] fab change reopen rule understood

通过后进入：[placement-plan.md](placement-plan.md)
