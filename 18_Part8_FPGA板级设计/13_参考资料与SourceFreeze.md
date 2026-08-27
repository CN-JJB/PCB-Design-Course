# 13｜Part 8 一手资料与 Source Freeze

## AMD 7 Series

- DS181 — Artix-7 DC and AC Switching Characteristics  
  https://docs.amd.com/v/u/en-US/ds181_Artix_7_Data_Sheet

- UG475 — 7 Series Packaging and Pinout  
  https://docs.amd.com/

- UG471 — 7 Series SelectIO Resources

- UG472 — 7 Series Clocking Resources

- UG470 — 7 Series Configuration  
  https://docs.amd.com/v/u/en-US/ug470_7Series_Config

- UG483 — 7 Series PCB Design Guide  
  https://docs.amd.com/v/u/en-US/ug483_7Series_PCB

- UG586 — 7 Series Memory Interface Solutions  
  https://docs.amd.com/r/en-US/ug586_7Series_MIS/

- UG482 — 7 Series GTP Transceivers

- UG1099 — Recommended Design Rules and Strategies for BGA Devices

- UG440 — Xilinx Power Estimator

## DDR3

Alliance AS4C64M16D3B：

https://www.alliancememory.com/AS4C64M16D3/

生产冻结记录：

- exact suffix；
- datasheet revision；
- IBIS；
- temperature；
- lifecycle/PCN。

## PCB

记录：

- board house；
- layer stack；
- dielectric；
- trace/space；
- drill；
- via pad；
- impedance；
- HDI/via-in-pad 是否使用。

## Tool

记录：

- Vivado version；
- MIG version；
- XDC commit；
- KiCad version；
- schematic/PCB/rules commit。

---

# Source Freeze Table

| Item | Exact Source | Revision | Retrieved | Used For | Recheck |
|---|---|---|---|---|---|
| FPGA DS181 | AMD | TBD | 2026-08-26 | power/electrical | release |
| Package UG475 | AMD | TBD | 2026-08-26 | BGA/pins | release |
| PCB UG483 | AMD | 1.14 baseline | 2026-08-26 | PDN/layout | release |
| Config UG470 | AMD | 1.17 baseline | 2026-08-26 | SPI/JTAG | release |
| Memory UG586 | AMD | 4.2 baseline | 2026-08-26 | DDR3/MIG | release |
| BGA UG1099 | AMD | 2.1 baseline | 2026-08-26 | escape/DFM | release |
| XPE UG440 | AMD | 2026.1 baseline | 2026-08-26 | power | release |
| DDR3 | Alliance | TBD | 2026-08-26 | memory | release |
| Fab stackup | TBD | TBD | TBD | impedance/escape | order |

---

# Final Rule

任何 FPGA pin、电压、termination、DDR group、GTP channel、BGA geometry 与 power number 都必须可追溯。

**开发板原理图可以是参考，但不是规格来源。**
