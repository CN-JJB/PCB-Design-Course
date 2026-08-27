# 11｜FPGA Bring-up：从 JTAG IDCODE 到 DDR3 与 GTP

> FPGA Bring-up 的第一条规则：先证明 device alive，再证明 configuration，再证明 user I/O，最后才碰 DDR3/GTP。

---

# 1. Stage 0：Power Off

- short；
- BGA orientation；
- regulator feedback；
- configuration mode straps；
- Flash orientation；
- DDR3 orientation；
- Bank VCCO；
- VREF/VTT；
- GTP rails；
- JTAG connector。

---

# 2. Stage 1：Power

限流上电。

测：

- VCCINT；
- VCCBRAM；
- VCCAUX；
- VCCO；
- DDR 1.5 V；
- VREF/VTT；
- GTP rails；
- PROGRAM_B / INIT_B / DONE。

先不要求 bitstream 自动启动。

---

# 3. Stage 2：JTAG IDCODE

最先做：

> 读 IDCODE。

如果 IDCODE 都读不到：

优先查：

- power；
- JTAG TCK/TMS/TDI/TDO；
- configuration state；
- BGA solder；
- cable/debugger。

不要先查 HDL。

---

# 4. Stage 3：最小 Bitstream

烧一个极简 bitstream：

- clock divider；
- LED toggle；
- optional UART heartbeat。

目标：

- 验证 configuration；
- 验证 system clock；
- 验证一个简单 Bank。

---

# 5. Stage 4：SPI Boot

验证：

~~~text
power cycle
→ INIT_B
→ CCLK activity
→ Flash transaction
→ DONE
→ LED heartbeat
~~~

如果 JTAG 能配置、SPI boot 不行：

重点查 configuration mode / Flash / CCLK / CFGBVS / bitstream properties。

---

# 6. Stage 5：Bank I/O

逐 Bank 测：

- correct VCCO；
- LVCMOS level；
- loopback；
- differential pair；
- clock input。

避免一次把所有 header 都打开。

---

# 7. Stage 6：DDR3 MIG

首先使用 MIG 官方/generated calibration status。

区分：

- calibration fail；
- read/write data error；
- intermittent error；
- temperature/frequency dependent error。

A/B：

- 降 memory rate；
- 放宽 timing；
- 查看 VREF/VTT；
- 调 ODT/drive only with source；
- 检查 byte lane；
- 检查 DQS；
- 检查 power noise。

---

# 8. Stage 7：GTP

如果启用 GTP：

- refclk presence；
- PLL lock；
- internal loopback；
- PRBS；
- external loopback；
- BER；
- eye/IBERT。

先 internal loopback，再怀疑 connector/channel。

---

# 9. 常见伪故障

## Vivado pin/XDC 与 PCB 不一致

现象像焊接或 SI，根因只是 mapping。

## DDR MIG calibration fail

不一定 PCB；也可能：

- reference clock；
- reset；
- MIG config；
- wrong part；
- VREF/VTT；
- pin map。

## GTP BER 高

不一定 trace impedance；也可能：

- refclk jitter；
- wrong equalization；
- connector；
- AC coupling；
- power rail。

---

# 10. Validation Matrix

必须有 evidence：

- oscilloscope；
- Vivado Hardware Manager；
- MIG calibration report；
- memory stress log；
- IBERT/PRBS；
- thermal；
- rail capture。

---

# 11. 本章产出

- bringup-test-plan.md
- validation-matrix.md
