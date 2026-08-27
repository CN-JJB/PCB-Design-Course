# Artix-7 V1 Bring-up Test Plan

## Stage 0 — Power Off
- [ ] BGA orientation
- [ ] rail resistance
- [ ] bank VCCO
- [ ] config straps
- [ ] DDR3 orientation
- [ ] VREF/VTT
- [ ] GTP supply
- [ ] JTAG connector

## Stage 1 — Rails
- [ ] VCCINT
- [ ] VCCBRAM
- [ ] VCCAUX
- [ ] VCCO banks
- [ ] DDR3 1.5 V
- [ ] DDR VREF/VTT
- [ ] GTP rails
- [ ] INIT_B/DONE state

## Stage 2 — JTAG
- [ ] IDCODE
- [ ] chain detection
- [ ] simple bitstream

## Stage 3 — Clock + GPIO
- [ ] system oscillator
- [ ] LED heartbeat
- [ ] each bank loopback
- [ ] voltage level check

## Stage 4 — SPI Boot
- [ ] power-cycle
- [ ] CCLK
- [ ] Flash transaction
- [ ] DONE
- [ ] fallback/recovery

## Stage 5 — DDR3
- [ ] MIG calibration
- [ ] basic memory test
- [ ] full-range
- [ ] pseudo-random
- [ ] stress
- [ ] temperature
- [ ] rate A/B

## Stage 6 — GTP
- [ ] refclk
- [ ] PLL
- [ ] internal diagnostic loop
- [ ] external link
- [ ] error-rate evidence

Every failure must include evidence and one-variable-at-a-time A/B.
