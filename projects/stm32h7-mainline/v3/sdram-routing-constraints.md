# SDRAM Routing Constraints

## Project Intent

- primary target is timing margin, not aesthetic equal length
- board-induced group skew initial target: <= 100 ps
- this is a V3 engineering target, not a universal SDRAM rule

## Timing Groups

| Group | Nets | Direction | Preferred Layer | Reference | Via Budget |
|---|---|---|---|---|---|
| CLK | SDCLK | MCU→SDRAM | TBD | solid plane | minimum |
| Data | DQ0..15, DQM | bidirectional | TBD | solid plane | low |
| Address | A0..11, BA0/1 | MCU→SDRAM | TBD | solid plane | low |
| Command | RAS/CAS/WE/CS/CKE | MCU→SDRAM | TBD | solid plane | low |

## Propagation

- stackup propagation assumption: TBD ps/mm
- 100 ps converted mismatch: TBD mm after stackup freeze
- actual delay report: TBD

## Routing Rules

- natural route first
- no forced global equal length
- SDCLK direct and clean
- keep group reference consistent
- avoid dense meander
- tune in dedicated corridor
- minimize layer transitions
- series damping footprints only where justified

## Review

- [ ] clock-to-group timing reviewed
- [ ] group skew reviewed
- [ ] via transition map complete
- [ ] no split-plane crossing
- [ ] meander spacing reviewed
- [ ] actual KiCad length/skew exported
