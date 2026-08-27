# Package / Bank Map

> Fill from exact XC7A35T CSG325 UG475 package file / Vivado device view.

| Bank | Bank Type | Planned VCCO | Role | VREF/DCI | Clock Pins | Notes |
|---|---|---:|---|---|---|---|
| 0 | Config | 3.3 V candidate | SPI/config | CFGBVS | dedicated | verify |
| TBD | HR | 3.3 V | GPIO | TBD | MRCC/SRCC | |
| TBD | HR | 1.8 V | low-voltage I/O | TBD | | |
| TBD | HR | 1.5 V | DDR3 | MIG | DQS/MRCC | |
| MGT | GTP | analog rails | SerDes | n/a | MGTREFCLK | |

## Dedicated Pins

- PROGRAM_B:
- INIT_B:
- DONE:
- CFGBVS:
- M0/M1/M2:
- CCLK:
- TCK/TMS/TDI/TDO:
- VCCBATT:
- XADC pins:

## Review

- [ ] every external signal has bank owner
- [ ] every bank has one VCCO plan
- [ ] DDR banks match MIG
- [ ] no GTP/selectIO confusion
- [ ] package ball map version recorded
