# V2 Bring-up Test Plan

## Stage 0 — No power

- [ ] Visual inspection
- [ ] MCU/regulator/connector orientation
- [ ] 5V-GND resistance
- [ ] 3V3-GND resistance
- [ ] DNP config checked

## Stage 1 — Power only

- [ ] Current-limited supply
- [ ] 5V measured
- [ ] 3V3 measured
- [ ] VCAP checked against STM32 requirement
- [ ] No abnormal heat

## Stage 2 — Debug

- [ ] SWD connect
- [ ] Device ID read
- [ ] Program/erase/reset
- [ ] UART heartbeat

## Stage 3 — Clock

- [ ] HSI boot
- [ ] HSE startup
- [ ] PLL lock
- [ ] 48 MHz domain
- [ ] MCO or low-loading clock evidence

## Stage 4 — USB FS

- [ ] Attach/CC behavior
- [ ] Enumeration
- [ ] Repeated plug/unplug
- [ ] Data transfer
- [ ] Multiple host/cable A-B test

## Stage 5 — CAN

- [ ] Known-good second node
- [ ] Termination topology correct
- [ ] TX/RX logic
- [ ] Dominant/recessive waveform
- [ ] Error counters
- [ ] Long-run frames

## Stage 6 — SDIO

- [ ] Low-speed init
- [ ] Basic read
- [ ] 4-bit mode
- [ ] Write
- [ ] Continuous read/write stress
- [ ] Multiple cards
- [ ] ES0182 workarounds verified

## Stage 7 — Combined stress

- [ ] USB transfer + CAN traffic + SD write + CPU load
- [ ] 3V3 droop/ripple recorded
- [ ] Thermal rise recorded
- [ ] Error counters/logs recorded

## Stop conditions

Immediately remove power if:

- 3V3 out of safe range
- abnormal current
- regulator/MCU overheating
- VCAP incorrect
- VBUS backfeed suspected
- protection devices heating unexpectedly
