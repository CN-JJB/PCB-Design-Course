# V3 Routing Rule Matrix

| Group | Type | Timing/Impedance Source | Preferred Layer | Reference | Via Budget | KiCad Auto | Manual Review |
|---|---|---|---|---|---|---|---|
| FMC_SDCLK | single | FMC timing | TBD | GND | minimum | width/layer | edge/return |
| FMC_DQ | single bidi | timing budget | TBD | solid plane | low | length/skew | topology |
| FMC_ADDR_CTRL | single | timing budget | TBD | solid plane | low | length/skew | topology |
| RMII_REF_CLK | single | PHY/MCU | TBD | GND | low | width/layer | edge |
| RMII | single | PHY/MCU | TBD | GND | low | clearance | direction/ref |
| ETH_MDI | differential | PHY + stackup | TBD | solid ref | minimum | diff rules | boundary |
| USB_FS | differential | ST/USB | TBD | GND | low | diff rules | ESD/ref |
| POWER | plane/track | PI/current | n/a | GND | n/a | clearance | neck/hot loop |

## Stackup Inputs

- stackup ID: TBD
- impedance calculator revision: TBD
- propagation ps/mm: TBD
- copper/dielectric: TBD

## Rule File

- .kicad_dru revision: TBD
- DRC report: TBD
- length/skew export: TBD
