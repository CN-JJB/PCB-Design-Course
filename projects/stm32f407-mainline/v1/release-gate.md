# STM32F407 V1｜Pre-Manufacturing Release Gate

> **这一步的意义：在花钱下单前强制停一次。**

## CAD / Electrical

- [ ] schematic revision recorded
- [ ] PCB revision recorded
- [ ] ERC clean / waivers documented
- [ ] DRC clean / waivers documented
- [ ] schematic parity passed
- [ ] L2 solid GND manually inspected

## Library / Mechanical

- [ ] MCU footprint rechecked
- [ ] regulator footprint rechecked
- [ ] connector orientation
- [ ] pin-1 / polarity
- [ ] mounting-hole size/location
- [ ] board dimensions
- [ ] 3D/mechanical sanity

## Fabrication

- [ ] fab current capability checked
- [ ] stackup current ID checked
- [ ] Gerber generated
- [ ] drill generated
- [ ] independent Gerber viewer reviewed
- [ ] outline / mask / silkscreen / drill all present

## BOM / Assembly

- [ ] exact MPN for critical parts
- [ ] DNP clear
- [ ] substitute risk noted
- [ ] hand-solder / SMT process realistic

## Decision

- [ ] PASS — may order
- [ ] CONDITIONAL — accepted risks listed below
- [ ] FAIL — do not order

### Accepted risks

| ID | Risk | Why accepted | Verification |
|---|---|---|---|

通过后进入：[bringup-test-plan.md](bringup-test-plan.md)
