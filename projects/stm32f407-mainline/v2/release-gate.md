# V2 Manufacturing Release Gate

## Identity

- Board revision: `TBD`
- Schematic revision: `TBD`
- BOM revision: `TBD`
- Git commit: `TBD`
- Fabricator / stackup ID: `TBD`
- Release date: `TBD`

## Electrical

- [ ] ERC PASS / waivers recorded
- [ ] DRC PASS / waivers recorded
- [ ] VCAP / VDDA / power-tree reviewed
- [ ] USB reviewed
- [ ] CAN reviewed
- [ ] SDIO reviewed

## SI

- [ ] USB pair stackup/geometry confirmed
- [ ] SDIO_CLK topology confirmed
- [ ] Critical reference/via transitions reviewed
- [ ] No uncontrolled critical stubs

## PI

- [ ] Decoupling loops reviewed
- [ ] 3V3 bottleneck reviewed
- [ ] regulator thermal budget reviewed
- [ ] microSD transient margin documented

## EMC / ESD

- [ ] USB protection path reviewed
- [ ] CAN protection path reviewed
- [ ] cable/common-mode boundaries reviewed
- [ ] shield/system-ground decision documented

## DFM

- [ ] Critical footprints checked against datasheets
- [ ] Fabricator capabilities checked
- [ ] Mechanical clearances checked
- [ ] BOM alternates/DNP checked
- [ ] Test access checked

## Output

- [ ] Gerbers viewed in independent viewer
- [ ] PTH/NPTH drills viewed
- [ ] BOM/CPL cross-checked
- [ ] controlled-impedance note included
- [ ] assembly notes included
- [ ] release source commit frozen

## Waivers

| ID | Finding | Evidence | Risk | Approver | Expiry/future action |
|---|---|---|---|---|---|
