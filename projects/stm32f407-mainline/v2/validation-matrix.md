# V2 Validation Matrix

| Feature | Basic functional | Stress | SI evidence | PI evidence | EMC/ESD evidence | Pass criteria | Result |
|---|---|---|---|---|---|---|---|
| Power | 5V/3V3 correct | combined load | n/a | droop/ripple/temp | cable-mode comparison if needed | within project limits | ☐ |
| SWD | program/reset | repeated cycles | SWCLK if issue | rail stable | cable does not upset system | reliable | ☐ |
| USB FS | enumerate/transfer | long transfer/replug | waveform/topology if issue | VBUS/3V3 stable | cable A-B / near-field | project USB function | ☐ |
| CAN | send/receive | long-run multi-node | waveform/error counter | PHY supply stable | cable/protection A-B | zero unacceptable errors | ☐ |
| SDIO | read/write | continuous write + card variants | CLK/data if issue | card rail transient | near-field if needed | no data corruption | ☐ |
| Combined | all active | max intended workload | cross-interface errors | worst rail transient | near-field baseline | no regression | ☐ |

## Evidence rule

每个 PASS 至少关联一种证据：

- log；
- screenshot；
- scope capture；
- DMM measurement；
- thermal measurement；
- error counter；
- file checksum；
- test report。

不要只写“试过了，没问题”。
