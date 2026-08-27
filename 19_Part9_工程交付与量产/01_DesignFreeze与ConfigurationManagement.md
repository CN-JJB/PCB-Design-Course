# 01｜Design Freeze 与 Configuration Management：到底冻结了什么？

> “我已经把 PCB 画完了”不是 Design Freeze。真正的 Freeze 是一组相互一致、可以追溯的配置项同时进入受控状态。

---

# 1. Freeze 的对象

至少包括：

- system requirements；
- schematic；
- PCB；
- stackup；
- custom libraries；
- BOM；
- AVL；
- firmware/configuration image；
- manufacturing output；
- test procedure；
- regulatory/pre-compliance assumptions。

如果只冻结 Gerber，却继续改 BOM 或固件，就没有真正 freeze。

---

# 2. Hardware Revision ≠ Git Commit

Git commit 是实现记录。

Hardware Revision 是产品配置身份。

推荐区分：

~~~text
Git commit        → 精确源文件状态
HW Revision       → 对外硬件版本身份
BOM Revision      → 物料配置
FW Revision       → 程序配置
Test Revision     → 测试方法/限值
Manufacturing Lot → 实际生产批次
Serial Number     → 单台设备
~~~

---

# 3. 不采用“电气改 A、布局改 B、丝印改 C”这种万能版本算法

旧教材曾建议不同字母/小版本自动对应变更类型。

这在真实公司没有统一标准。

更可靠的是：

> **先定义本项目 Revision Policy，再坚持。**

例如：

- Rev A → Rev B：任何需要重新出 PCB 的工程变更；
- BOM Rev 独立；
- Firmware Rev 独立；
- ECO 记录变更原因与影响范围。

也可以使用 Semantic-ish 规则，但必须书面定义。

---

# 4. Release Manifest

每次发布建立一个 manifest：

| Item | Revision | Commit/Hash | Generated From | Approved |
|---|---|---|---|---|
| Schematic | Rev B | git SHA | source | |
| PCB | Rev B | git SHA | source | |
| BOM | B03 | hash | schematic | |
| Gerber | Rev B | hash | PCB | |
| Firmware | 1.4.2 | hash | FW repo | |
| Test | T07 | hash | test repo | |

它解决的是：

> “这批板到底用的是哪一套文件？”

---

# 5. Generated Files 不手改

典型禁区：

- 手改 Gerber；
- 手改 PnP 角度但不回源文件记录；
- 手改 BOM CSV 但 schematic metadata 不更新；
- 手工改 production firmware hex 但不留下 build identity。

如果制造商需要修正：

> 应创建 deviation / ECO，并把修正回灌 source。

否则下一版会复发。

---

# 6. Freeze Gate

正式 Freeze 前至少需要：

- schematic/ERC review；
- PCB DRC；
- SI/PI/EMC review；
- DFM/DFA/DFT；
- BOM lifecycle；
- fab capability；
- test strategy；
- unresolved risk register。

---

# 7. Reopen Freeze

Freeze 后仍然可以改。

但改变必须有：

- reason；
- affected items；
- validation scope；
- revision bump；
- ECO owner；
- release approval。

Freeze 不是“永不改变”，而是：

> **任何改变都变得可见。**

---

# 8. 三条项目主线怎样应用

## STM32F407 V2

重点是 BOM/USB/CAN/SDIO、assembly 和 functional test。

## STM32H743 V3

还要冻结 SDRAM timing source、stackup/impedance、PHY/magnetics。

## Artix-7 V1

还要冻结 Vivado/XDC/MIG、DDR3、BGA rules、FPGA image。

---

# 9. 本章产出

填写：

- design-freeze-record.md
- release-manifest.md

Design Freeze 通过标准：

- [ ] 所有 release item 有 revision
- [ ] 所有 generated files 可追到 source
- [ ] open risk 有 owner
- [ ] variant / DNP 状态明确
- [ ] firmware/test 与 hardware 对应关系冻结
