# V3 KiCad Rule Plan

## Net Classes

| Class | Width | Clearance | Via | Diff width/gap | Layer preference | Source |
|---|---:|---:|---|---|---|---|
| P0_CLOCK | TBD | TBD | TBD | — | TBD | |
| MEMORY | TBD | TBD | TBD | — | TBD | |
| ETHERNET | TBD | TBD | TBD | TBD | TBD | |
| USB_DIFF | TBD | TBD | TBD | TBD | TBD | |
| ANALOG | TBD | TBD | TBD | — | TBD | |
| GENERAL | TBD | TBD | TBD | — | TBD | |

## Custom Rules Candidates

- allowed layers
- clearance around clock / aggressors
- target length / skew
- differential pair geometry
- connector/BGA local neck-down
- no-via / keepout regions

## Manual Review That DRC Does Not Replace

- reference continuity
- reference transition
- plane split crossing
- current-loop geometry
- EMC connector boundary
- power narrow neck / mounting inductance