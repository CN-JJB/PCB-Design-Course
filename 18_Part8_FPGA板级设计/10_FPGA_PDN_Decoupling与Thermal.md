# 10｜FPGA PDN、Decoupling 与 Thermal：从 XPE 到板上阻抗

> FPGA 的功耗不是一个固定数字。它随逻辑利用率、toggle、clock、I/O、BRAM、GTP 与温度变化。

---

# 1. 先做 Power Estimate

使用 XPE / Vivado power estimate：

输入：

- device / package；
- speed grade；
- utilization；
- clocks；
- toggle；
- BRAM/DSP；
- I/O standard；
- drive/slew；
- DDR；
- GTP；
- ambient/airflow。

输出是：

> regulator/thermal/PDN 的设计输入。

---

# 2. Power Budget 要分 Rail

| Rail | Voltage | Static | Dynamic | Peak/Transient | Regulator |
|---|---:|---:|---:|---:|---|
| VCCINT | 1.0 | TBD | TBD | TBD | TBD |
| VCCBRAM | 1.0 | TBD | TBD | TBD | TBD |
| VCCAUX | 1.8 | TBD | TBD | TBD | TBD |
| VCCO_3V3 | 3.3 | TBD | TBD | TBD | TBD |
| VCCO_DDR | 1.5 | TBD | TBD | TBD | TBD |
| MGTAVCC | per DS181 | TBD | TBD | TBD | TBD |
| MGTAVTT | per DS181 | TBD | TBD | TBD | TBD |

---

# 3. Decoupling 不是 BGA 周围“撒芝麻”

每颗 capacitor 的价值取决于：

- target rail；
- C / ESR / ESL；
- DC bias；
- package；
- mounting loop；
- via；
- plane spreading。

布局时不要让：

> capacitor 离 ball 很近，但 capacitor ground via 绕很远。

---

# 4. BGA 下方电容

如果背面空间允许：

- 将高频 local caps 放 BGA 背面；
- 通过短 via 连接 rail/ground；
- 避免长细 neck。

但 assembly、testability、via-in-pad 工艺需要同时考虑。

---

# 5. VCCO per Bank

I/O switching current 可能集中在某个 Bank。

因此 VCCO decoupling 应按 Bank/activity 审查，而不是全部堆到 FPGA 某一个角。

---

# 6. DDR3 与 FPGA Bank 同时切换

DDR3 x16 + DQS + address/control 会制造明显 simultaneous switching。

这时要联合审：

- 1.5 V FPGA VCCO；
- DDR3 VDDQ；
- VTT/VREF；
- common GND inductance；
- plane neck；
- byte-lane timing。

---

# 7. Thermal

Artix-7 不等于“大芯片所以一定热”。

thermal 取决于：

- power；
- package；
- copper；
- airflow；
- ambient；
- logic activity；
- GTP。

要记录：

- estimated junction；
- θJA/thermal model source；
- copper spreading；
- airflow assumption；
- validation method。

---

# 8. 测量

Bring-up 至少测：

- rail DC；
- startup；
- ripple；
- high-load droop；
- regulator temperature；
- FPGA case temperature；
- DDR3 concurrent load；
- GTP activity if enabled。

---

# 9. Review

- [ ] XPE/Vivado power report archived
- [ ] rail budget完整
- [ ] regulator transient/thermal margin
- [ ] decoupling model/source记录
- [ ] VCCO按Bank审
- [ ] DDR rail/VTT/VREF审
- [ ] GTP rail审
- [ ] thermal assumption有验证
