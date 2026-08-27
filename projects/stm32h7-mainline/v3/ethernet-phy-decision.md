# Ethernet PHY Decision

## Device

- PHY: LAN8742A / LAN8742Ai
- Interface: RMII
- Speed: 10/100BASE-TX
- Package: 24-pin QFN
- Status at source freeze: TBD recheck

## Clock

- PHY crystal: 25 MHz
- RMII REF_CLK: 50 MHz
- Clock source direction: PHY → MCU
- REFCLKO mode/strap: TBD verify

## Bias / Power

- RBIAS: 12.1 kΩ 1%
- VDD1A/VDD2A: 3.3 V
- VDDIO: project mode TBD
- VDDCR: internal regulator node
- exposed pad: GND plane + via array

## Management

- MDIO address: TBD
- nRST: controlled by MCU/reset circuit
- interrupt: optional/TBD
- strap table: attach before release

## MDI

- TXP/TXN
- RXP/RXN
- magnetics part: TBD
- RJ45/MagJack: TBD
- controlled impedance geometry: TBD from stackup
- test stubs: prohibited

## Source

- https://www.microchip.com/en-us/product/lan8742a
- datasheet revision: TBD
