# Ethernet Interface Review

## RMII Digital Side

- [ ] REF_CLK direction frozen
- [ ] 50 MHz clock route direct
- [ ] single-ended rules, not diff pair
- [ ] RMII pin map no FMC conflict
- [ ] reference plane continuous
- [ ] no long stubs

## PHY

- [ ] straps verified
- [ ] RBIAS 12.1 kΩ 1%
- [ ] exposed pad grounded
- [ ] analog supply local
- [ ] crystal placement reviewed
- [ ] reset sequence defined

## MDI / Magnetics

- [ ] PHY-recommended topology used
- [ ] 100 Ω differential geometry from current stackup
- [ ] pairs symmetric
- [ ] no testpoint stub
- [ ] magnetics exact part checked
- [ ] center tap supply reviewed

## RJ45 / Boundary

- [ ] isolation boundary clear
- [ ] shield/chassis strategy documented
- [ ] cable-side termination documented
- [ ] ESD/common-mode path documented
- [ ] connector zone excludes SDRAM tuning
- [ ] high-voltage capacitor source/rating documented

## Validation

- [ ] PHY ID
- [ ] link
- [ ] ping
- [ ] throughput
- [ ] long stress
- [ ] cable A/B / EMC observations
