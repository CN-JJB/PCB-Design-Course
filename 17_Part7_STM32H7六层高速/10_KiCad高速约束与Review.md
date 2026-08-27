# 10｜KiCad 9：把高速约束真正落到工程里

> KiCad 的价值不是替你理解物理，而是把已经理解的工程规则变成可重复检查的约束。

---

# 1. Constraint Source Matrix

| Constraint | Source |
|---|---|
| SDRAM SDCLK 100 MHz | MCU datasheet + project baseline |
| SDRAM timing cycles | memory datasheet + RM0433 |
| SDRAM skew target | project timing budget |
| MDI differential impedance | PHY/Ethernet interface |
| USB geometry | USB guide + board stackup |
| min width/clearance | manufacturer + project margin |
| reference layer | stackup architecture |

没有 source 的数字，不先进规则文件。

---

# 2. Net Class 不等于完整高速规则

建议分：

- SDRAM_CLK
- SDRAM_DATA
- SDRAM_ADDR_CTRL
- RMII_CLK
- RMII_DIGITAL
- ETH_MDI
- USB_FS
- POWER
- ANALOG

Net Class 可以提供默认 track width、via、differential pair defaults 与 clearance。

但“默认 route width”不自动等于“禁止更窄”。需要 hard limit 的，用 board constraints / Custom Rules 明确表达。

---

# 3. SDRAM 至少拆三组

~~~text
FMC_SDCLK
FMC_DQ_DQM
FMC_ADDR_CTRL
~~~

因为它们的 timing、direction 与 priority 不同。

---

# 4. Length / Skew

KiCad length/skew 工具适合查看 routed length、matched tuning、skew。

工程文件还必须保存：

- timing target
- stackup propagation assumption
- converted length target
- actual result

不能只有“KiCad 显示绿了”。

---

# 5. Rule Area

建议定义：

## SDRAM routing corridor

限制 layer/via，保留 tuning space，阻止 slow GPIO 穿越。

## Ethernet connector zone

保留 magnetics/ESD/chassis，排除 SDRAM 与 SW node。

## Power switching zone

keep clock、analog、MDI away。

---

# 6. 自动与人工边界

可自动化：

- clearance
- width
- via
- differential pair
- keepout
- layer restriction
- length/skew

必须人工审：

- reference continuity
- return transition
- connector discharge path
- decoupling loop inductance
- SDRAM topology quality

最终流程：

~~~text
DRC
+ length/skew report
+ reference overlay
+ current-loop review
+ visual review
~~~

---

# 7. MDI 与 RMII

ETH_MDI 使用 differential pair constraints，实际 width/gap 来自当前 stackup + manufacturer impedance calculation。

RMII 是 single-ended LVCMOS，不因为属于 Ethernet 就使用差分规则。RMII_REF_CLK 单独做 high-priority class。

---

# 8. SDRAM Tuning

1. 先自然走；
2. 导出 actual length；
3. 换算 delay；
4. 找真正违反 timing target 的 nets；
5. 只补这些；
6. 再审 meander coupling/reference。

---

# 9. Release 保存

每次 release 保存：

- DRC report
- unresolved exclusions
- length/skew table
- netclass/rule version
- stackup screenshot
- impedance source
- reference-transition map
- manual Review signoff
- .kicad_dru

---

# 10. 自动/人工矩阵

| Rule | KiCad Auto | Manual Review |
|---|---|---|
| clearance | ✅ | sampling |
| width | ✅ | intent |
| diff pair | ✅ | field/reference |
| length/skew | ✅ | timing meaning |
| reference continuity | ❌ | ✅ |
| return transition | ❌ | ✅ |
| ESD path | ❌ | ✅ |
| hot loop | ❌ | ✅ |

---

# 11. Release 前检查

- [ ] .kicad_dru 已版本控制
- [ ] stackup 与板厂 source 一致
- [ ] impedance geometry 已重算
- [ ] SDRAM group 可单独导出
- [ ] RMII 没被误设 diff
- [ ] MDI 没有 test stub
- [ ] DRC exclusions 有理由
- [ ] manual Review 有签核

本章完善 routing-rule-matrix.md。
