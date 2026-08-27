# Artix-7 V1 System Specification

## Device

- FPGA: XC7A35T-1CSG325C
- Package: CSG325
- Package size: 15×15 mm
- Ball pitch: 0.8 mm
- PCB target: six-layer minimum hypothesis; final from escape review

## Functional Scope

| Block | Baseline |
|---|---|
| System clock | 100 MHz oscillator |
| Configuration | Master SPI + JTAG |
| DDR3 | AS4C64M16D3B-12BIN x16 |
| GPIO | 3.3 V bank |
| Low-voltage I/O | 1.8 V experiment bank |
| GTP | one teaching lane |
| Debug | JTAG + status pins |

## Excluded From V1

- PCIe product implementation
- multi-rank DDR3
- FMC connector
- complex HDL/application stack
- multi-lane production SerDes

## Exit Criteria

- [ ] exact package/bank map frozen
- [ ] IOSTANDARD/VCCO matrix passed
- [ ] XPE power budget
- [ ] configuration plan
- [ ] clock plan
- [ ] escape plan
- [ ] MIG pinout reviewed
- [ ] GTP plan reviewed
- [ ] XDC/schematic/PCB map synchronized
- [ ] bring-up and validation ready
