# 13｜Part 7 参考资料与 Source Freeze

> 高速板的参数必须能追溯到具体版本。论坛答案或“上次项目的数值”不能直接变成 release rule。

---

# 1. MCU

官方入口：

https://www.st.com/en/microcontrollers-microprocessors/stm32h743-753/documentation.html

生产冻结记录：

- DS12110 revision
- RM0433 revision
- ES0392 revision
- AN4938 revision
- exact MCU order code
- silicon revision if known

---

# 2. SDRAM

Alliance AS4C4M16SA：

https://www.alliancememory.com/as4c4m16sa/

记录 exact suffix、speed grade、temperature、package、datasheet revision、PCN/EOL 与 IBIS。

V3 baseline：**AS4C4M16SA-6TIN**。

采购前重新确认 availability/lifecycle。

---

# 3. Ethernet PHY

LAN8742A：

https://www.microchip.com/en-us/product/lan8742a

记录 exact variant、package、temp、datasheet revision、errata、PHY address/strap、RBIAS、supply mode 与 REF_CLK mode。

---

# 4. Reference Board

NUCLEO-H743ZI2 schematic：

https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-c01_schematic.pdf

只用于 RMII pin baseline、LAN8742A implementation、power/clock/debug reference，不替代 V3 自己的需求与 Review。

---

# 5. PCB Manufacturer

生产冻结记录：

- manufacturer
- stackup ID
- board thickness
- copper
- dielectric
- impedance calculation
- capability
- project design rules
- tolerance

---

# 6. KiCad

https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html

冻结：

- KiCad version
- project/schematic/PCB/rule files
- custom library commit
- DRC report

---

# 7. Source Freeze Template

填写 projects/stm32h7-mainline/v3/source-freeze.md：

| Item | Exact source | Revision/date | Retrieved | Used for | Recheck |
|---|---|---|---|---|---|

---

# 8. Final Rule

任何进入 hardware release 的关键数字，都必须能沿 source-freeze 找回去，包括 SDRAM clock、FMC timing、refresh、skew、impedance、RBIAS、decoupling、fab rules 与 ESD topology。

---

# 9. Part 7 真正的产物

~~~text
datasheet / standard / fab source
→ engineering interpretation
→ PCB constraint
→ KiCad implementation
→ DRC/manual review
→ measurement
→ validation evidence
→ release decision
~~~

这就是“会画六层板”和“会做六层板工程”的分界线。
