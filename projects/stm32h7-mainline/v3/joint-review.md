# V3 SI / PI / EMC Joint Review

| ID | Issue | Domain | Current/Signal Path | Evidence | Severity | Proposed Fix | Validation | Status |
|---|---|---|---|---|---|---|---|---|
| JR-001 | TBD | SI/PI/EMC | TBD | TBD | TBD | TBD | TBD | Open |

## SDRAM

- [ ] SDCLK reference
- [ ] DQ/address skew
- [ ] VDDQ return
- [ ] SSN
- [ ] connector separation

## Ethernet

- [ ] RMII reference
- [ ] MDI geometry
- [ ] PHY analog supply
- [ ] magnetics/RJ45 boundary
- [ ] shield/chassis/ESD

## Power

- [ ] MCU local loops
- [ ] SDRAM local loops
- [ ] PHY local loops
- [ ] buck hot loop
- [ ] plane neck-down

## High-Speed Routing

- [ ] edge rate / interface requirement 已记录
- [ ] stackup / reference pair 已冻结
- [ ] impedance geometry 有 current source
- [ ] crosstalk 不是只凭 3H/3W 判断
- [ ] via transition 同时审 signal + return
- [ ] unused via stub 已按实际 start/end layer 检查
- [ ] differential intra-pair 与 lane-to-lane timing 分开审
- [ ] 详细结果见 [high-speed-routing-review.md](high-speed-routing-review.md)

## Gate

- Blockers open: TBD
- Majors open: TBD
- Risk accepted: TBD
- Review result: TBD
