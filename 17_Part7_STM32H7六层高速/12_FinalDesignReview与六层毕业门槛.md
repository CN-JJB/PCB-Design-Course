# 12｜Final Design Review：什么叫真正完成一块六层高速板

> 六层毕业标准不是“我终于布完了”，而是“每个关键决策都有来源，每个关键风险都有验证”。

---

# 1. Final Review Checklist

## System

- [ ] exact MCU / SDRAM / PHY
- [ ] lifecycle / package
- [ ] feature scope
- [ ] power budget
- [ ] clock tree
- [ ] pin ownership
- [ ] connector boundary

## STM32H743

- [ ] VDD/VDDLDO/VCAP
- [ ] VDDA/VREF
- [ ] HSE/SWD/reset/boot
- [ ] decoupling
- [ ] datasheet revision
- [ ] errata review

## SDRAM

- [ ] organization / bank / row / column
- [ ] FMC pin map
- [ ] SDCLK frequency
- [ ] timing fields
- [ ] refresh / CAS
- [ ] routing groups
- [ ] skew / clock-to-group
- [ ] reference plane
- [ ] via budget
- [ ] termination option
- [ ] bring-up test

## Ethernet

- [ ] RMII map
- [ ] REF_CLK direction
- [ ] straps / RBIAS / power
- [ ] exposed pad
- [ ] MDI pair
- [ ] magnetics / RJ45
- [ ] shield/chassis
- [ ] ESD/common-mode path
- [ ] link/stress validation

## Stackup

- [ ] exact manufacturer stackup
- [ ] dielectric / copper
- [ ] layer role
- [ ] reference pairing
- [ ] impedance geometry
- [ ] transition map
- [ ] plane split overlay

## SI / PI / EMC

- [ ] edge-rate assumptions
- [ ] impedance
- [ ] reflection/crosstalk
- [ ] parallel bus skew
- [ ] local decoupling
- [ ] VDDQ/PHY power
- [ ] buck hot loop
- [ ] SSN
- [ ] connector common-mode
- [ ] shield/chassis
- [ ] ESD path

## KiCad / DFM

- [ ] Net Class source
- [ ] Custom Rules
- [ ] .kicad_dru
- [ ] DRC zero unexplained violations
- [ ] exclusions reviewed
- [ ] length/skew report
- [ ] stackup metadata
- [ ] drill/mask/assembly/testpoint

## Bring-up

- [ ] staged plan
- [ ] SDRAM pattern suite
- [ ] cache/MPU separated
- [ ] Ethernet PHY ID
- [ ] link / packet stress
- [ ] concurrent SDRAM+ETH stress
- [ ] evidence archived

---

# 2. 六层毕业门槛

你应该能解释：

- 为什么是 6 层，不是 4/8 层？
- 为什么 SDRAM 是 100 MHz？
- 为什么某组允许某个长度差，而另一组不允许？
- 为什么这个 via 需要 return transition？
- 为什么 PHY 在这里？
- 为什么 shield 这样处理？
- 为什么 DRC 通过仍不能 Release？

如果最后回答仍然是“网上都这样画”，就还没有毕业。

---

# 3. Release Gate

只接受：

- PASS
- PASS WITH DOCUMENTED RISK
- FAIL / BLOCKED

不接受“应该没问题”。

本章产出 final-design-review.md。
