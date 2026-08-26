# V2 Routing Execution Plan

## Priority

1. HSE / VCAP / critical local loops
2. USB D+/D-
3. SDIO_CLK
4. SDIO_CMD + D0~D3
5. CANH/CANL bus-side
6. CAN logic / SWD / UART
7. 3V3 / 5V local distribution
8. low-speed GPIO
9. pours / stitching / cleanup

## Network plan

| Class | Priority | Preferred layer | Reference | Via policy | Topology | Manual review |
|---|---:|---|---|---|---|---|
| USB_FS | 2 | L1 | L2 GND | avoid unless required | connector→ESD→MCU | symmetry/ref/stub |
| SDIO_CLK | 3 | L1 | L2 GND | minimal | source R→card | aggressor/parallelism |
| SDIO_BUS | 4 | L1 | L2 GND | low and similar | group | outlier/ref |
| CAN_BUS | 5 | L1 near edge | GND/connector structure | low | connector→protection→PHY | symmetry/transient path |
| POWER | 7 | L3 + local Top | GND | current-based | source→loads | neck/via bottleneck |

## Via question for every critical transition

1. Why does this signal change layer?
2. What is the old reference?
3. What is the new reference?
4. How does return current transition?
5. Could placement/routing order remove this via?

## Completion gate

- [ ] L2 GND not used as rescue routing layer
- [ ] USB has no uncontrolled stub
- [ ] SDIO_CLK source resistor is at source
- [ ] SDIO group has no extreme outlier
- [ ] CAN termination footprint does not create long branch
- [ ] Critical return paths manually reviewed
- [ ] Pours do not create islands/slots/asymmetry
