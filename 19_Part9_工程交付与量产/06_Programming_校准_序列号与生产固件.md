# 06｜Programming、Calibration、Serial Number：生产固件也是硬件配置的一部分

> 量产时，“烧进去什么”与“这块板是什么版本”必须绑定。否则硬件再可追溯，最终产品仍然不可复现。

---

# 1. Production Image 必须可识别

生产烧录文件至少记录：

- firmware version；
- git commit；
- build timestamp；
- toolchain/version；
- configuration options；
- checksum/hash；
- hardware compatibility；
- release approver。

不要用：

> final.hex  
> final_new.hex  
> final_really_final.hex

---

# 2. Hardware Compatibility

建立明确矩阵：

| HW Revision | Supported FW | Bootloader | Calibration Schema |
|---|---|---|---|
| F407 V2 Rev A | 1.x | BL1 | CAL1 |
| H743 V3 Rev A | 2.x | BL2 | CAL2 |
| Artix-7 V1 Rev A | bitstream set A | SPI image A | n/a |

如果 firmware 对新硬件做了 pin/timing 改变，必须升级 compatibility record。

---

# 3. MCU Production Programming

可选：

- SWD/JTAG；
- bootloader；
- bed-of-nails fixture；
- gang programmer。

需要考虑：

- fixture access；
- connector是否只用于开发；
- readout protection；
- unique ID；
- provisioning；
- recovery。

---

# 4. FPGA Production Programming

Artix-7 需要区分：

- JTAG transient programming；
- SPI Flash production image；
- multiboot/fallback；
- bitstream properties；
- configuration voltage。

生产应冻结：

> FPGA bitstream + Flash image + Vivado release source。

---

# 5. Serial Number

Serial Number 不只是外壳贴纸。

它应该能关联：

- PCB revision；
- assembly lot；
- BOM revision；
- firmware；
- test record；
- calibration；
- failure/RMA。

推荐：

~~~text
Serial
→ Unit record
→ Lot
→ HW/BOM/FW/Test Revision
→ Measurement result
~~~

---

# 6. Calibration

需要校准的产品可能包括：

- ADC offset/gain；
- current/voltage measurement；
- oscillator trim；
- sensor offset；
- RF output；
- factory MAC/address；
- Ethernet/USB identity；
- secure key/certificate。

校准数据必须定义：

- measurement equipment；
- procedure；
- limit；
- format；
- storage；
- version；
- recalibration policy。

---

# 7. MAC / Unique IDs / Keys

如果产品需要：

- MAC address；
- UUID；
- license；
- certificate；
- secure key；

生产系统必须保证：

- 唯一性；
- 不重复；
- 可追溯；
- 权限控制；
- 不在普通 BOM/日志里泄露 secret。

课程只讲流程，不在仓库保存真实 secret。

---

# 8. Programming Fixture

fixture 设计考虑：

- connector cycle；
- pogo；
- GND；
- reset；
- boot strap；
- power；
- UART/SWD/JTAG；
- operator防呆；
- board orientation；
- ESD；
- fixture self-test。

---

# 9. Production Firmware 不能是 Debug Firmware

常见错误：

- watchdog关掉；
- debug interface全开；
- assert/printf占用接口；
- test mode没退出；
- calibration bypass；
- security未启用。

所以生产 release 要有：

> **Production Configuration Review**

---

# 10. 本章产出

填写：

- programming-release.md
- traceability-plan.md

通过：

- [ ] image 有 hash
- [ ] HW/FW compatibility
- [ ] programming procedure
- [ ] serial allocation
- [ ] calibration schema
- [ ] recovery path
- [ ] secret provisioning policy
