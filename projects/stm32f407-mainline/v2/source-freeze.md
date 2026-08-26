# V2 Source / Version Freeze

Query baseline: 2026-08-26

| Source | Version/date | Used for | Recheck before release |
|---|---|---|---|
| STM32F407 datasheet | TBD exact rev | electrical/package/pins | ☐ |
| RM0090 | TBD exact rev | clocks/USB/CAN/SDIO | ☐ |
| ES0182 | current rev at release | silicon limitations | ☐ |
| ST AN4488 | current rev | hardware development/power | ☐ |
| ST AN4879 | Rev 10 / Jan 2025 baseline | USB hardware/PCB | ☐ |
| USB Type-C Cable/Connector | Release 2.5 / 2026-04-08 baseline | connector/CC role | ☐ |
| TCAN33x datasheet | Rev F / May 2025 baseline | CAN PHY | ☐ |
| TI TIDA-00629 | current reference package | CAN ESD/EFT/surge method | ☐ |
| KiCad | exact local version TBD | implementation/output | ☐ |
| Fabricator stackup | ID/date TBD | impedance/DFM | ☐ |

## Rule

任何关键数字发生争议时，先记录：

1. 资料名；
2. revision/date；
3. section/table；
4. 适用条件；
5. 当前 design 是否真的满足这些条件。
