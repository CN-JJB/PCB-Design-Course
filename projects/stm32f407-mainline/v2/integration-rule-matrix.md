# V2 Integration Rule Matrix

> 所有数字必须在 release 前由当前 datasheet / interface spec / fabricator stackup / measurement 冻结。本表保存“规则为什么存在”。

| Class | Nets | Geometry / width | Spacing | Length / skew | Allowed layers | Reference | Source type | Verification |
|---|---|---|---|---|---|---|---|---|
| USB_FS | DP/DM | TBD by stackup solver | pair-specific | interface-specific | prefer L1 | L2 GND | USB/ST/fab | DRC + visual + functional |
| SDIO_CLK | CK | TBD | aggressor isolation | short, no arbitrary target | prefer L1 | L2 GND | RM0090/ES0182/project | visual + scope |
| SDIO_BUS | CMD,D0-D3 | TBD | group spacing | avoid large outlier | prefer L1 | L2 GND | project/timing | visual + stress test |
| CAN_BUS | CANH/CANL | transceiver/ref-design based | symmetry | topology/stub focus | connector zone | local reference | transceiver/system | bus waveform + errors |
| CAN_LOGIC | TX/RX | default digital | default | short | L1/L4 | continuous ref | device/project | DRC |
| CLOCK | HSE | device/oscillator layout | keep quiet | shortest local | L1 | local GND strategy | ST oscillator guidance | startup/MCO |
| POWER_3V3 | 3V3 | current/thermal based | clearance | n/a | L3 + local pours | GND | PI budget | voltage/temp |
| POWER_5V | 5V/VBUS | current/thermal based | clearance | n/a | local | GND | USB/power | voltage/temp |
| DEBUG | SWD/UART | default digital | default | practical | L1/L4 | continuous ref | project | debug test |

## Rule record template

```text
Rule ID:
Net/Class:
Rule:
Type: physical / device / interface / fab / project
Source:
Condition:
Why:
KiCad enforcement:
Manual review:
Hardware verification:
Owner:
Status:
```

## Rules that must NOT be written as universal constants

- [ ] “高速 > 50 MHz”
- [ ] “换层地孔必须 ≤1 mm”
- [ ] “差分一定 3W”
- [ ] “USB 一定某固定线宽/间距”
- [ ] “SDIO 必须所有线完全等长”
- [ ] “CAN 必须焊 120 Ω”
- [ ] “去耦必须 ≤2 mm”
- [ ] “电源 1 A 就画 1 mm”
