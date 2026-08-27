# I/O Standard Matrix

| Interface | Signal Group | Bank | VCCO | IOSTANDARD | Direction | Clock/Diff Requirement | Source |
|---|---|---|---:|---|---|---|---|
| Config | SPI | 0 | 3.3 V candidate | LVCMOS33 candidate | mixed | CCLK | UG470 |
| GPIO | header | TBD | 3.3 V | LVCMOS33 | mixed | none | project |
| Low V | header | TBD | 1.8 V | LVCMOS18 | mixed | none | project |
| DDR3 | DQ/DQS/A/C | TBD | 1.5 V | MIG-generated | mixed | DQS/CK | UG586 |
| GTP | TX/RX | MGT | n/a | GTP | serial | dedicated | UG482 |

## Rule

No signal is assigned only by “free pin”.  
Every row must satisfy package pin type + bank voltage + tool legality + PCB routability.
