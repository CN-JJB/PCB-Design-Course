# V2 DFM Checklist

## Fabrication

- [ ] Current target fabricator capability checked
- [ ] 4-layer stackup ID/date recorded
- [ ] Board thickness/copper/dielectric recorded
- [ ] Min trace/space verified
- [ ] Via drill/annular ring verified
- [ ] Slots/NPTH/PTH verified
- [ ] Controlled-impedance process confirmed
- [ ] Surface finish defined

## Footprints

- [ ] STM32F407 LQFP100 land pattern checked
- [ ] USB-C connector datasheet checked
- [ ] microSD socket mechanical/land pattern checked
- [ ] CAN connector checked
- [ ] CAN PHY / ESD arrays pin-1 checked
- [ ] regulator thermal land pattern checked

## Assembly

- [ ] Polarity/pin-1 silk clear
- [ ] DNP parts documented
- [ ] Rotation checked in CPL
- [ ] Hand-solder/rework access acceptable
- [ ] Connector insertion clearance verified

## Test

- [ ] 5V/3V3/GND test points
- [ ] SWD accessible
- [ ] NRST accessible
- [ ] UART accessible
- [ ] CAN test access
- [ ] SDIO_CLK measurement access without uncontrolled stub

## Release

- [ ] Gerber viewed independently
- [ ] Drill viewed independently
- [ ] BOM/CPL cross-check
- [ ] Release commit recorded
