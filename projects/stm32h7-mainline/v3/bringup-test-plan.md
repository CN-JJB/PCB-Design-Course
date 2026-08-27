# V3 Bring-up Test Plan

## Stage 0 — Power Off

- [ ] shorts
- [ ] polarity
- [ ] SDRAM orientation
- [ ] PHY orientation
- [ ] regulator feedback
- [ ] VCAP
- [ ] straps

## Stage 1 — Power

- [ ] current-limited input
- [ ] 3V3
- [ ] VCAP
- [ ] VDDA
- [ ] PHY supply
- [ ] reset

## Stage 2 — MCU

- [ ] SWD ID
- [ ] internal RAM
- [ ] HSE
- [ ] basic firmware

## Stage 3 — SDRAM Basic

- [ ] initialize FMC
- [ ] fixed-address test
- [ ] walking 1/0
- [ ] AA/55
- [ ] address-as-data
- [ ] pseudo-random
- [ ] full range

## Stage 4 — SDRAM Stress

- [ ] long duration
- [ ] temperature
- [ ] timing A/B
- [ ] GPIO speed A/B
- [ ] cache/MPU A/B
- [ ] DMA

## Stage 5 — Ethernet

- [ ] PHY ID
- [ ] straps
- [ ] link
- [ ] ping
- [ ] throughput
- [ ] long packet stress

## Stage 6 — Concurrent

- [ ] Ethernet + SDRAM
- [ ] DMA + CPU load
- [ ] GPIO switching
- [ ] rail noise measurement

All failures must record condition, address/bit/pattern if applicable, and evidence.
