# V3 Reference Transition Map

| Net / group | From layer/ref | To layer/ref | Signal via | Return-transfer support | Distance / geometry | Risk | Evidence |
|---|---|---|---|---|---|---|---|
| SDRAM CLK | | | | | | | |
| SDRAM data group | | | | | | | |
| Ethernet digital | | | | | | | |
| USB | | | | | | | |
| Debug | | | | | | | |

## Rules

- GND→GND：检查 local stitching via 与 plane continuity。
- GND→PWR：检查 local PWR↔GND high-frequency coupling path，不允许用单独 GND via 假装完成 reference transfer。
- 任何 transition 穿过 split / void：必须重新设计或给出明确验证依据。