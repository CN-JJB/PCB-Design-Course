# V3 Six-Layer Floorplan Plan

## Blocks

- MCU core zone
- SDRAM zone
- PHY zone
- Magnetics/RJ45 zone
- Power switching zone
- USB/SWD zone
- Slow I/O zone

## Critical Adjacency

1. MCU ↔ SDRAM
2. PHY ↔ Magnetics ↔ RJ45

## Placement Freeze Checklist

- [ ] SDRAM orientation minimizes DQ crossing
- [ ] SDCLK direct corridor exists
- [ ] address/control corridor exists
- [ ] PHY RMII side faces MCU
- [ ] PHY MDI side faces magnetics
- [ ] RJ45 at correct mechanical boundary
- [ ] power hot loop isolated
- [ ] VCAP local
- [ ] VDDA/VREF quiet
- [ ] tuning corridor reserved
- [ ] no unavoidable split crossing
- [ ] test access preserved

## Evidence

- block diagram: TBD
- placement screenshot: TBD
- critical corridor annotation: TBD
- layer/reference overlay: TBD
