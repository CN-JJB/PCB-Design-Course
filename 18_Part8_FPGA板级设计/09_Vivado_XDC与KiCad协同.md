# 09｜Vivado XDC ↔ KiCad：FPGA Pin Planning 必须双向同步

> FPGA 项目最危险的文件不一致，是 XDC、原理图和 PCB 三份 pin map 各自“看起来都对”。

---

# 1. 三个真相源

FPGA 板至少有：

1. **Vivado XDC**
2. **Schematic net/pin map**
3. **PCB net / physical routing**

三者必须同一版本。

---

# 2. XDC 记录什么

典型：

- PACKAGE_PIN；
- IOSTANDARD；
- DRIVE；
- SLEW；
- DIFF_TERM；
- CLOCK constraint；
- CFGBVS / CONFIG_VOLTAGE；
- MIG generated pin constraints；
- GTP location/reference。

---

# 3. KiCad 记录什么

- FPGA ball number；
- net；
- physical class；
- differential pair；
- layer；
- width/gap；
- via；
- length/skew；
- placement；
- reference plane。

---

# 4. 两类约束不要互相冒充

Vivado 能检查：

- Bank voltage / IOSTANDARD consistency；
- dedicated pin legality；
- clock route legality；
- memory physical rules；
- timing。

KiCad 能检查：

- geometry；
- clearance；
- diff pair；
- routed length/skew；
- layer/via；
- footprint/board rules。

两边都不能自动判断：

- connector ESD path；
- PDN loop；
- via stub 是否在 channel budget；
- BGA escape 是否有制造余量；
- regulator thermal。

---

# 5. Pin Change Workflow

任何 pin change 必须走：

~~~text
change request
→ check device legality in Vivado
→ update XDC
→ update schematic
→ ERC
→ update PCB netlist
→ reroute
→ DRC
→ regenerate pin-map report
→ review
~~~

不能直接在 PCB editor 里“改一个 pin label”。

---

# 6. Pin Map Export

项目应保存：

| Signal | Ball | Bank | VCCO | IOSTANDARD | KiCad Net | PCB Class | Source |
|---|---|---|---|---|---|---|---|

这张表是 FPGA/PCB 团队的共同语言。

---

# 7. DDR3

DDR3 constraints 首先由 MIG 生成。

PCB 如果提出 swap：

> 必须回 MIG 验证。

尤其不能擅自交换：

- DQS；
- DQ 跨 byte group；
- CK；
- VREF/DCI pin。

---

# 8. Review Gate

- [ ] XDC commit frozen
- [ ] schematic commit frozen
- [ ] PCB commit frozen
- [ ] pin-map export regenerated
- [ ] Bank VCCO matrix一致
- [ ] IOSTANDARD一致
- [ ] MIG output与PCB一致
- [ ] GTP lane/refclk一致
- [ ] no manual undocumented pin swap
