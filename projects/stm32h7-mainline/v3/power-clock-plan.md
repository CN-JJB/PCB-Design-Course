# V3 Power / Clock Plan

## Rail Architecture

| Rail | Source | Load | Local Decoupling | Sensitive to |
|---|---|---|---|---|
| 3V3_MCU | 3V3_SYS | H743 VDD | per pin + bulk | SSN |
| VCAP1/2 | MCU internal LDO | core support | per AN4938 | layout inductance |
| VDDA/VREF | filtered 3V3 | analog | local | PHY/SDRAM noise |
| 3V3_SDRAM | 3V3_SYS | VDD/VDDQ | distributed | DQ switching |
| 3V3_PHY | 3V3_SYS branch | PHY/magnetics | local | analog MDI |

## Clock Plan

| Clock | Source | Frequency | Consumer | PCB Priority |
|---|---|---:|---|---|
| HSE | crystal/oscillator | TBD | MCU | P0 |
| FMC_SDCLK | MCU | 100 MHz | SDRAM | P0 |
| RMII_REF_CLK | PHY | 50 MHz | MCU | P0 |
| USB | MCU PLL | 48 MHz domain | USB | P1 |

## Bring-up Policy

- external SDRAM not used before init
- first SDRAM test with simplified cache/MPU policy
- DMA enabled only after basic memory stability
- Ethernet stress only after PHY/link baseline

## Review

- [ ] VCAP is not external rail
- [ ] VDD pin groups have local caps
- [ ] SDRAM VDD/VDDQ loop reviewed
- [ ] PHY analog branch reviewed
- [ ] clock direction recorded
- [ ] FMC 100 MHz source documented
