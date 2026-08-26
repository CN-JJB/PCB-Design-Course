# V2 Test Point / Debug Access Plan

| Signal | Purpose | Access type | Stub risk | Fixture-ready | Notes |
|---|---|---|---|---|---|
| GND | reference | large loop/pad | none | yes | multiple locations |
| 5V | input power | pad | none | yes | near power entry |
| 3V3 | main rail | pad | none | yes | near MCU/load |
| NRST | reset/debug | pad/header | low | yes | SWD bundle |
| SWDIO | programming | header/pogo | low | yes | |
| SWCLK | programming | header/pogo | medium | yes | continuous reference |
| UART_TX | bring-up console | header/pogo | low | yes | |
| UART_RX | bring-up console | header/pogo | low | yes | |
| CAN_TX | logic debug | pad | low | optional | |
| CAN_RX | logic debug | pad | low | optional | |
| CANH | bus waveform | connector/pad | bus-side | optional | avoid long branch |
| CANL | bus waveform | connector/pad | bus-side | optional | avoid long branch |
| SDIO_CLK | SI/bring-up | very small controlled pad if needed | high | optional | no long stub |
| USB DP/DM | compliance/debug | connector/controlled access | very high | no casual TP | do not create long stubs |

## Physical access checks

- [ ] USB cable does not block SWD
- [ ] CAN wiring does not block test pads
- [ ] microSD insertion does not cover pogo area
- [ ] all power points accessible with board mounted
- [ ] ground reference exists next to high-speed measurement points
