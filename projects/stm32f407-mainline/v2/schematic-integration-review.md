# V2 Schematic Integration Review

## Finding format

```text
ID:
Severity: Blocker / Major / Minor / Note
Block:
Observation:
Why it matters:
Source:
Required action:
Verification:
Status:
```

## Gate checklist

### Power / MCU
- [ ] All VDD/VSS pins accounted for
- [ ] VCAP strictly per STM32 requirement
- [ ] VDDA/VSSA strategy documented
- [ ] Reset / Boot states defined
- [ ] Power budget and regulator thermal budget linked

### USB-C / USB FS
- [ ] Device/UFP role correct
- [ ] Both CC pins handled per current Type-C spec
- [ ] VBUS path/sense reviewed
- [ ] Low-capacitance ESD suitable for USB
- [ ] ESD located in connector boundary topology
- [ ] Shield strategy documented

### CAN
- [ ] Controller/transceiver distinction documented
- [ ] Logic levels compatible
- [ ] Mode pin default state safe
- [ ] 120 Ω termination optional/DNP policy defined
- [ ] TVS/CMC option topology reviewed
- [ ] Connector pinout/shield/GND strategy defined

### SDIO
- [ ] CK/CMD/D0-D3 connected to verified AF pins
- [ ] Pull-ups sourced and documented
- [ ] CLK source resistor footprint at MCU side
- [ ] card power local decoupling
- [ ] ES0182 constraints linked to firmware plan

### Debug/Test
- [ ] SWDIO/SWCLK/GND/VTref/NRST available
- [ ] UART bring-up header defined
- [ ] Critical power test points defined

## Open findings

| ID | Severity | Block | Finding | Action | Status |
|---|---|---|---|---|---|
| V2-SCH-001 | | | | | |
