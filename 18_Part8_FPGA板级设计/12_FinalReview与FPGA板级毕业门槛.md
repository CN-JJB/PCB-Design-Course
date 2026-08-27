# 12｜Final Review：FPGA 板级设计的毕业门槛

> 通过标准不是“FPGA 能下载程序”，而是你能解释 Bank、电源、配置、BGA、DDR3 和 GTP 为什么这样实现。

---

# System / Package

- [ ] exact FPGA order code
- [ ] package/pitch
- [ ] lifecycle
- [ ] GTP bonded status
- [ ] pin file revision

# Bank / I/O

- [ ] Bank role
- [ ] VCCO
- [ ] IOSTANDARD
- [ ] VREF/DCI
- [ ] clock-capable pin
- [ ] differential mate
- [ ] CFGBVS/config voltage

# Power

- [ ] XPE/Vivado estimate
- [ ] VCCINT/VCCBRAM/VCCAUX
- [ ] VCCO per Bank
- [ ] DDR rails
- [ ] GTP rails
- [ ] sequencing
- [ ] PDN/decoupling
- [ ] thermal

# Configuration

- [ ] JTAG
- [ ] SPI Flash
- [ ] M[2:0]
- [ ] PROGRAM_B/INIT_B/DONE
- [ ] CCLK
- [ ] recovery strategy

# Clock

- [ ] MRCC/SRCC
- [ ] system oscillator
- [ ] GTP refclk
- [ ] jitter source
- [ ] PCB reference continuity

# BGA

- [ ] escape strategy
- [ ] via/trace capability
- [ ] DFM
- [ ] power/GND escape
- [ ] DDR/GTP corridor
- [ ] layer count evidence

# DDR3

- [ ] exact memory
- [ ] MIG version
- [ ] DQS byte lane
- [ ] DQ/DM group
- [ ] CK/A/C topology
- [ ] VREF/VTT/ODT
- [ ] routing constraints
- [ ] calibration/stress

# GTP

- [ ] dedicated pins
- [ ] analog rails
- [ ] refclk
- [ ] channel impedance/loss
- [ ] via/connector
- [ ] AC coupling
- [ ] PRBS/BER validation

# Tool Co-design

- [ ] XDC ↔ schematic ↔ PCB一致
- [ ] no undocumented swap
- [ ] Vivado DRC
- [ ] KiCad DRC
- [ ] manual reference/PDN review

---

# 毕业问题

你必须能回答：

1. 为什么 DDR3 不能随便换 DQ 到另一个 Bank？
2. 为什么同一个 Bank 不能同时做 3.3 V 和 SSTL15？
3. 为什么 FPGA 需要多条电源 rail？
4. 为什么 CSG325 的 0.8 mm BGA 不自动意味着 via-in-pad？
5. 为什么 MIG 是 pin planning 的参与者？
6. 为什么 GTP 不是普通 LVDS？
7. 为什么 JTAG IDCODE 是 bring-up 第一证据？
8. 为什么 XDC 与 PCB 的 pin map 必须同 commit 冻结？

如果回答仍然是“开发板就是这样接”，就还没有完成 FPGA 板级训练。

---

## 本章产出

- final-design-review.md
- release-gate.md
- source-freeze.md
