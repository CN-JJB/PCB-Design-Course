# V2 Final Design Review

## System explanation

In 500–1000 Chinese characters, explain the board to another hardware engineer without relying on screenshots.

## Architecture

- [ ] Can draw block diagram from memory
- [ ] Every interface has a purpose
- [ ] Out-of-scope features are explicit

## Stackup / Reference

- [ ] Why L2 is solid GND can be explained physically
- [ ] L3/L4 reference risks understood
- [ ] Stackup source/date recorded

## USB

- [ ] Type-C UFP role
- [ ] CC handling
- [ ] DP/DM geometry/reference
- [ ] ESD current path
- [ ] Shield strategy
- [ ] Bring-up decision tree

## CAN

- [ ] Controller vs PHY distinction
- [ ] Classic CAN limitation documented
- [ ] Termination topology understood
- [ ] Protection/common-mode path understood

## SDIO

- [ ] CLK priority/source termination understood
- [ ] Group routing rationale
- [ ] ES0182 limitations/workarounds documented
- [ ] Read/write stress evidence

## PI

- [ ] Power budget
- [ ] regulator thermal budget
- [ ] VCAP/decoupling loops
- [ ] microSD transient margin

## EMC

- [ ] DM/CM paths can be drawn
- [ ] USB/CAN cable boundaries understood
- [ ] ESD path can be drawn
- [ ] Near-field evidence interpreted correctly

## DFM / Release

- [ ] Critical footprints checked
- [ ] BOM/DNP documented
- [ ] Test access validated
- [ ] Gerber/drill viewed
- [ ] Release commit recorded

## Remaining risks

| ID | Severity | Risk | Evidence | Mitigation/acceptance | Owner |
|---|---|---|---|---|---|

## Final decision

- [ ] PASS — ready for teaching/manufacturing release
- [ ] CONDITIONAL — accepted risks listed
- [ ] FAIL — blockers remain
