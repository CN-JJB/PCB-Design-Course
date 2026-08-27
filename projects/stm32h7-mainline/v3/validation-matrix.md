# V3 Validation Matrix

| ID | Test | Condition | Expected | Actual | Evidence | Pass |
|---|---|---|---|---|---|---|
| V-01 | 3V3 rail | idle/max load | within target | TBD | scope | TBD |
| V-02 | SDCLK | 100 MHz | clean/stable | TBD | scope | TBD |
| V-03 | SDRAM pattern | full range | 0 errors | TBD | log | TBD |
| V-04 | SDRAM long | extended | 0 errors | TBD | log | TBD |
| V-05 | SDRAM thermal | temp range | 0 errors | TBD | log | TBD |
| V-06 | PHY ID | boot | correct | TBD | console | TBD |
| V-07 | Ethernet link | 100M | stable | TBD | log | TBD |
| V-08 | Ping | 1 h | no loss target | TBD | log | TBD |
| V-09 | Throughput | sustained | target | TBD | pcap/log | TBD |
| V-10 | Concurrent | ETH+SDRAM+DMA | stable | TBD | log/scope | TBD |
| V-11 | ESD/pre-EMC | planned | no functional upset target | TBD | report | TBD |

## Rule

No row becomes PASS without attached evidence.
