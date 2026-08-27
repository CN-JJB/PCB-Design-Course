# Part 8 Fault Lab｜FPGA Board-Level Engineering

> 目标不是背错误，而是训练：**Vivado legality + PCB physics + power/configuration + manufacturing** 联合诊断。

---

# A. Device / Package / Bank

## Fault 01｜只冻结 XC7A35T，不冻结 CSG325
同 die 不同 package 的 I/O、GTP、pinout、pitch 都可能不同。

## Fault 02｜把 CSG324 pin file 用到 CSG325
看起来只差一个 ball，实际上 GTP/bonding 与 user I/O map 不同。

## Fault 03｜同一 Bank 同时放 LVCMOS33 和 SSTL15
VCCO 是 Bank 级物理供电，不是每个 pin 自己选择。

## Fault 04｜1.8 V sensor 接在 3.3 V Bank，只改 XDC IOSTANDARD
软件文本不能改变 PCB 上真实 VCCO。

## Fault 05｜为了 PCB 好走，把 DQS 换成普通 differential pair
DQS 必须使用 memory interface 指定资源。

## Fault 06｜把 MRCC/SRCC 当普通 GPIO 用完，最后 system clock 找不到合法 pin
Pin planning 没把 dedicated/clock resources 前置。

## Fault 07｜CFGBVS 与 VCCO_0 / CONFIG_VOLTAGE 不一致
可能造成 configuration bank 电气/工具约束冲突。

---

# B. Power / Sequencing / PDN

## Fault 08｜VCCINT/VCCBRAM/VCCAUX/VCCO 全叫 FPGA_PWR
失去 rail owner、voltage、sequencing、measurement 信息。

## Fault 09｜按“FPGA 大概 5 W”选 regulator
没有 XPE/Vivado utilization/toggle/IO/GTP 输入。

## Fault 10｜照抄 UG483 电容数量，不做本项目 power estimate
把 guide recommendation 误当固定 BOM。

## Fault 11｜所有去耦都在 BGA 同一侧
某些 power balls 的 local loop 很差。

## Fault 12｜电容很靠近 FPGA，但 ground via 很远
几何距离近不等于 loop inductance 小。

## Fault 13｜VCCO_DDR 通过细 neck 进入大 plane
瓶颈仍是局部阻抗。

## Fault 14｜3.3 V VCCO 先上很久，VCCAUX 后上，完全没审 DS181 条件
忽略 recommended sequencing 与 VCCO/VCCAUX voltage-difference condition。

## Fault 15｜GTP analog rail 从数字 core rail 随手分支
SerDes analog supply 的 noise/sequencing 没有独立 Review。

## Fault 16｜DDR3 VREF/VTT 紧贴 switching regulator SW node
reference/termination 被噪声直接污染。

---

# C. Configuration / JTAG / Clock

## Fault 17｜JTAG IDCODE 读不到就开始改 HDL
device alive 证据都没有。

## Fault 18｜JTAG 能下载，SPI boot 失败，却先怀疑 FPGA 主逻辑
应先查 mode、Flash、CCLK、CFGBVS、bitstream properties。

## Fault 19｜JTAG TCK 经过长排针 stub
低 nominal frequency 不代表边沿慢。

## Fault 20｜CCLK 分叉去多个 test header
configuration clock 的 SI 被调试结构破坏。

## Fault 21｜DONE 只接 LED，没有测试点/逻辑状态记录
失去 configuration diagnosis evidence。

## Fault 22｜100 MHz oscillator 接普通 GPIO
没有使用合适 clock-capable resource。

## Fault 23｜3.3 V oscillator 接进 1.8 V Bank
clock planning 与 Bank planning 脱节。

## Fault 24｜GTP REFCLK 接普通 LVDS clock pair
GTP 必须使用 dedicated MGTREFCLK。

---

# D. BGA Escape / DFM

## Fault 25｜看到 0.8 mm BGA 就直接上 via-in-pad
没有先证明普通 dog-bone/through-via 不可行。

## Fault 26｜为了逃线，把板厂 minimum trace 当全板 default
capability ≠ project design rule。

## Fault 27｜只算“一根线能过”，没算 solder mask / annular ring / drill
几何模型不完整。

## Fault 28｜先让 GPIO 从最方便方向逃出，DDR3 最后绕路
routing priority 错位。

## Fault 29｜GTP lane 在 BGA 下换多次层，因为普通 GPIO 抢了 corridor
pin/fanout/floorplan 没联合冻结。

## Fault 30｜所有 power ball 每球一 via，理由只是“越多越好”
没有 current/PDN/plane spreading 依据。

## Fault 31｜中心 ball 逃不出时才发现六层不够
Layer-count review 太晚。

---

# E. DDR3 / MIG

## Fault 32｜PCB 先选最顺手的 16 个 DQ pin，再让 MIG 接受
流程反了。

## Fault 33｜DQ0..7 跨两个 DQS byte group
逻辑编号正确，物理层资源非法。

## Fault 34｜DQS pair 合法，但 DM 放到另一个 byte group
Byte-lane membership 被破坏。

## Fault 35｜把 MCU SDR SDRAM 的“共同时钟等长”规则直接搬到 DDR3
忽略 DQS source-synchronous byte-lane 结构。

## Fault 36｜“DDR3 永远 fly-by”
拓扑必须由 MIG、memory count/rank、reference design 冻结。

## Fault 37｜所有 DDR3 nets 都强制完全等长
制造无意义蛇形并破坏 byte-lane/clock topology。

## Fault 38｜VREF 走长线穿过数字 switching zone
reference noise 影响 input threshold。

## Fault 39｜ODT/VTT/series resistor 值照抄另一块开发板
没有当前 MIG/memory/source 依据。

## Fault 40｜PCB 改了 DQ swap，但 XDC 没更新
Vivado、schematic、PCB 三份 truth source 分裂。

---

# F. GTP / High-Speed Differential

## Fault 41｜把 GTP_TXP/N 设置成 LVDS IOSTANDARD
GTP 不是 SelectIO。

## Fault 42｜只要 100 Ω 就宣布 channel 合格
忽略 loss、via stub、connector、AC coupling、refclk jitter。

## Fault 43｜所有 GTP 都无脑串 100 nF
AC coupling 位置/数值要看 protocol/endpoint/guide。

## Fault 44｜只因数据率高就默认 backdrill
是否需要由 board thickness、stub、loss budget 决定。

## Fault 45｜外部链路 error 高，直接重画 PCB，不先做 internal diagnostic
没有先隔离 FPGA internal / refclk / connector / channel。

---

# G. Tool / Release

## Fault 46｜Vivado DRC 通过 = PCB 正确
Vivado 不检查 connector ESD、PDN loop、via manufacturability。

## Fault 47｜KiCad DRC 通过 = FPGA pin 合法
KiCad 不知道 DQS byte group / Bank VCCO / GTP dedicated pin。

## Fault 48｜XDC、原理图、PCB 各自在不同 commit
任何 pin swap 都不可追溯。

## Fault 49｜MIG regenerate 后 PCB 没重新对 pin map
generated constraint 已变化，physical board 仍旧版本。

## Fault 50｜只保存 Gerber，不保存 XPE/MIG/XDC/source freeze
以后无法复现为什么这个 Bank、电源、DDR topology 是这样。

---

# 使用方式

每个 Fault 都填写：

| Field | Answer |
|---|---|
| Symptom | |
| Vivado sees? | |
| KiCad sees? | |
| Physical reason | |
| Source / tool evidence | |
| Proposed change | |
| Side effect | |
| A/B validation | |
| Final rule learned | |

最终目标：

> **看到 FPGA 板问题时，不把“工具没报错”当成无罪证明。**
