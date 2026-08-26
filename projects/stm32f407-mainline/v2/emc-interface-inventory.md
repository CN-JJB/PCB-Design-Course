# V2 EMC Interface Inventory

| Interface / Entry | External conductors | Reference / shield | Main EMC risk | Protection / option | Verification |
|---|---|---|---|---|---|
| USB FS | D+, D-, VBUS, GND, shield | GND + USB shield/chassis strategy | ESD, pair imbalance, cable CM | low-C TVS, optional CMC/bypass | cable A/B, near-field, USB functional test |
| CAN | CANH, CANL, optional shield/reference | transceiver GND + system cable strategy | ESD/EFT/surge, cable CM | CAN TVS, optional CMC, termination | cable A/B, transient plan, communication test |
| Power input | VIN, GND | power return | conducted/radiated switching noise, surge/ESD | input protection/filter per source | ripple/current probe/near-field |
| SWD header | SWDIO, SWCLK, NRST, GND, VREF | GND | user-touch ESD, clock radiation | optional series/ESD if product-accessible | A/B resistor, ESD path review |
| User button/reset | signal + exposed structure | GND | ESD directly into sensitive node | RC/series/protection as needed | controlled ESD immunity test plan |

## Review 规则

每个接口必须有以下答案：

```text
Where can external current enter?
Where does it return?
Where can board noise couple outward?
What structure can become an antenna?
What protects the internal IC?
How will we verify the hypothesis?
```

## 注意

这张表是课程 V2 的工程清单，不是任何认证标准的替代品。实际产品要按目标市场、环境、线束、机壳和接口标准补充。