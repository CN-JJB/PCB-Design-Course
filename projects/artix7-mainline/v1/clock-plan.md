# FPGA Clock Plan

| Clock | Source | Electrical | Pin Type | Frequency | Destination | Jitter Source |
|---|---|---|---|---:|---|---|
| SYSCLK | oscillator | LVCMOS TBD | MRCC/SRCC | 100 MHz | BUFG/MMCM | oscillator datasheet |
| GTP_REFCLK | external/oscillator TBD | differential | MGTREFCLK | TBD | GTP | source |
| JTAG_TCK | programmer | JTAG | dedicated | variable | config/debug | cable |

## Review

- [ ] system clock bank VCCO matches source
- [ ] clock-capable pin used
- [ ] GTP refclk uses dedicated pins
- [ ] no long stub
- [ ] reference plane continuous
- [ ] source damping footprint decision recorded
- [ ] XDC create_clock constraint exists
