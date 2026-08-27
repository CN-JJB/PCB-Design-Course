# Configuration Plan

## Mode

- Primary: Master SPI
- Recovery/Debug: JTAG

## Configuration Pins

| Pin | Role | Pull/Connection | Testpoint |
|---|---|---|---|
| PROGRAM_B | reset config | TBD | yes |
| INIT_B | init/status | TBD | yes |
| DONE | configured | TBD | yes |
| M[2:0] | mode | TBD | accessible |
| CCLK | SPI clock | FPGA-driven | probe |
| CFGBVS | bank voltage select | TBD | no |

## Vivado Properties

- CFGBVS:
- CONFIG_VOLTAGE:
- CONFIG_MODE:
- CONFIGRATE:
- BITSTREAM compression:
- fallback/multiboot:

## SPI Flash

- exact part: TBD
- voltage: TBD
- capacity: TBD
- x1/x2/x4: TBD
- programming flow: TBD

## JTAG

- connector:
- TCK routing:
- cable:
- chain:
- IDCODE expected:

## Bring-up

- [ ] IDCODE first
- [ ] JTAG bitstream
- [ ] simple LED image
- [ ] power-cycle SPI boot
- [ ] CCLK scope
- [ ] DONE/INIT_B status
