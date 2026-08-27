# STM32F407 V1｜Bring-up Test Plan

## Stage 0｜Power Off

- [ ] visual inspection
- [ ] 5V-to-GND resistance
- [ ] 3V3-to-GND resistance
- [ ] polarity/orientation check
- [ ] no visible solder bridge

Evidence: test/bring-up/

## Stage 1｜Current-limited Power

- current limit:
- observed current:
- 5V:
- 3V3:
- abnormal heating:

Pass:
- [ ] 3V3 within project target
- [ ] current plausible
- [ ] no hot component

## Stage 2｜Reset / Debug

- NRST level:
- VTREF:
- ST-LINK connection:
- MCU ID / access:

Pass:
- [ ] debugger connects reliably

## Stage 3｜Minimal Firmware

Use internal clock first.

- [ ] LED blink
- [ ] UART hello
- [ ] reset button works

## Stage 4｜HSE

- [ ] enable HSE
- [ ] verify firmware clock state
- [ ] scope only with appropriate probe/method if needed
- [ ] A/B internal vs HSE stable

## Stage 5｜GPIO / Expansion

- [ ] header pin map verified
- [ ] selected GPIO toggle/readback
- [ ] user button
- [ ] UART stress/basic loop

## Failure log

| ID | Stage | Symptom | Hypothesis | Change | Retest | Status |
|---|---|---|---|---|---|---|

## Gate 8 Pass

- [ ] all stages completed
- [ ] evidence archived
- [ ] any Major issue closed/accepted
- [ ] final current/rail values recorded

通过后进入：[final-design-review.md](final-design-review.md)
