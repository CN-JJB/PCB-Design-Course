# STM32F407 V1｜Routing Rule / Execution Plan

## Priority

1. HSE local network
2. MCU local power / VCAP
3. SWD / clock-like debug nets
4. 3V3 distribution
5. UART / user I/O
6. expansion GPIO
7. low-risk residual nets

## Critical-net review

| Net/group | Preferred layer | Reference | Via policy | Special check |
|---|---|---|---|---|
| HSE | L1 local | L2 | avoid | no stub |
| SWCLK | L1 | L2 | low | continuous reference |
| SWDIO | L1 preferred | L2 | low | debug access |
| NRST | simple/direct | L2 | low | noise/recovery |
| VCAP | local copper | GND | minimal | lowest loop L |
| 3V3 | L3 + local L1 | return GND | current-dependent | no neck |

## Manual checks after DRC

- [ ] L2 has no accidental routing/cut
- [ ] no signal crosses a harmful L3 split when using L4
- [ ] power necks/via bottlenecks reviewed
- [ ] critical return transitions reviewed
- [ ] no dense unnecessary meanders
- [ ] test pads do not create long critical stubs

## Gate 6 Pass

- [ ] KiCad DRC no unexplained blocker
- [ ] schematic parity passed
- [ ] critical nets manually reviewed
- [ ] power path reviewed for IR/thermal intent
- [ ] board is ready for manufacturing-file review

通过后进入：[release-gate.md](release-gate.md)
