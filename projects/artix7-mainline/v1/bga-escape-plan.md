# BGA Escape Plan

## Package

- CSG325
- 15×15 mm
- 0.8 mm pitch

## Manufacturer Inputs

- min trace:
- min spacing:
- min drill:
- min annular ring:
- via pad:
- solder mask:
- via-in-pad supported/cost:
- blind via supported/cost:

## Escape Strategy

| Ball Group | Priority | Fanout Type | Preferred Direction | Routing Layers |
|---|---|---|---|---|
| Power/GND | P0 | TBD | plane access | n/a |
| DDR3 | P0 | TBD | memory side | TBD |
| GTP | P0 | TBD | connector edge | TBD |
| SYSCLK | P0 | TBD | clock source | TBD |
| Config/JTAG | P1 | TBD | debug side | TBD |
| GPIO | P2 | TBD | header side | TBD |

## Layer Count Evidence

- outer ring escape:
- second ring:
- center ball escape:
- route corridors:
- plane continuity:
- final layer count:

## DFM Gate

- [ ] pad source matches UG475
- [ ] via fits fab capability
- [ ] trace channel proven
- [ ] no unnecessary HDI
- [ ] escape screenshot archived
