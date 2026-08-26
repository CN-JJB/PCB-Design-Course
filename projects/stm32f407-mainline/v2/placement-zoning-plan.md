# V2 Placement / Zoning Plan

## Mechanical anchors

| Item | Edge/position | Keepout | Cable/card access | Frozen |
|---|---|---|---|---|
| USB-C | TBD | TBD | plug clearance | ☐ |
| CAN terminal | TBD | TBD | wire clearance | ☐ |
| microSD | TBD | TBD | insertion/ejection | ☐ |
| SWD | TBD | TBD | debugger probe | ☐ |
| Mounting holes | TBD | TBD | screw/head | ☐ |

## Functional zones

```text
[USB boundary]   [MCU core]   [Debug]

[CAN boundary]   [Power]      [microSD]
```

## Golden-space priority around MCU

1. VCAP
2. VDD decouplers
3. VDDA/VSSA network
4. HSE network
5. USB source/tuning footprints
6. SDIO_CLK source resistor
7. Reset/boot parts

## Current-path review

### USB
Connector → ESD → pair → MCU

### CAN
Connector → TVS/CMC/termination option → PHY → MCU

### SDIO
MCU → source R (CLK) → socket; card power local cap → socket

### Power
USB VBUS → protection/bulk → regulator → 3V3 → loads

## Placement risk register

| ID | Risk | Why | Mitigation | Status |
|---|---|---|---|---|
| P-01 | USB pair forced to cross board | SI/EMC | rotate/move MCU/connector | Open |
| P-02 | SDIO_CLK source R cannot fit near MCU | SI | reserve golden space | Open |
| P-03 | CAN TVS behind PHY | ESD | reorder boundary | Open |
| P-04 | SWD blocked by USB cable | testability | move header | Open |
| P-05 | 3V3 regulator thermal copper too small | PI/thermal | reserve copper | Open |

## Freeze gate

- [ ] All connectors mechanically usable
- [ ] Protection parts precede protected logic spatially
- [ ] MCU decoupling loops feasible
- [ ] HSE local and quiet
- [ ] USB route feasible on L1/L2
- [ ] SDIO group feasible with low crossing/via count
- [ ] CAN bus side remains in connector zone
- [ ] Power entry does not cut sensitive routes
