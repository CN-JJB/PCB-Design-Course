# STM32F407 V1｜Schematic Review

## Review record

- Schematic revision:
- KiCad version:
- Reviewer:
- Date:

## Power

- [ ] every VDD/VSS accounted for
- [ ] VCAP network exact
- [ ] VDDA/VSSA branch documented
- [ ] VBAT default valid
- [ ] regulator CIN/COUT exact MPN/package
- [ ] test points for 5V/3V3/GND

## Clock / Reset / Boot

- [ ] HSE symbol/package exact
- [ ] load network justified from selected part
- [ ] NRST network checked against ST guidance
- [ ] BOOT0 default/recovery state clear

## Debug / User I/O

- [ ] SWDIO/SWCLK/VTREF/GND/NRST accessible
- [ ] UART TX/RX/GND accessible
- [ ] LED current resistor calculated
- [ ] button default state known
- [ ] expansion pins documented

## Library provenance

- [ ] MCU LQFP100 footprint checked against ST package drawing
- [ ] regulator package checked
- [ ] connectors checked against mechanical drawings
- [ ] polarity / pin-1 reviewed
- [ ] custom library changes recorded

## ERC / Findings

| ID | Severity | Finding | Action | Status |
|---|---|---|---|---|
| V1-SCH-001 | | | | |

## Gate 3 Pass

- [ ] ERC has no unexplained blocker
- [ ] Blocker findings = 0
- [ ] critical footprint provenance complete
- [ ] exact MPN list sufficient to begin PCB
- [ ] schematic committed to hw/

通过后进入：[stackup-rule-plan.md](stackup-rule-plan.md)
