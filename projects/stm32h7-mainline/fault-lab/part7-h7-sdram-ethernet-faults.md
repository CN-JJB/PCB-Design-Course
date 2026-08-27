# Part 7 Fault Lab｜STM32H743 + SDRAM + Ethernet

> 这些故障故意设计成“DRC 可能完全通过，但板子仍然不可靠”。每个案例都要求走：
>
> Symptom → Evidence → Timing/Current Path → Root Cause → PCB/FW Change → Side Effect → A/B Validation。

---

# A. SDRAM Timing / Controller

## Fault 01｜18 ns / 10 ns 向下取整

**错误：** tRCD = 18 ns，100 MHz 时填 1 cycle。

**为什么危险：** timing minimum 应满足不少于 18 ns；1 cycle 只有 10 ns。

**修复：** ceil → 2 cycles，并核对寄存器/HAL encoding。

---

## Fault 02｜因为 SDRAM 支持 166 MHz，所以 FMC 也跑 166 MHz

**错误：** 只看 memory speed grade。

**漏掉：** MCU FMC electrical limit、silicon revision、VDD、load、board implementation。

**修复：** V3 first-spin 维持 100 MHz；更高频率另开 timing/validation review。

---

## Fault 03｜复制别人的 RefreshCount

**错误：** 直接抄某教程的 refresh counter。

**为什么错：** refresh value 依赖实际 SDRAM clock、器件 refresh requirement 与 FMC COUNT 语义。

---

## Fault 04｜tRC、tRAS、tRP 只看一个字段

**错误：** 认为“TRCD/TRP 配好了，SDRAM timing 就结束”。

**修复：** 建完整 timing matrix，并检查字段之间的约束。

---

## Fault 05｜CAS Latency 当成越低越快越好

**错误：** first-spin 直接强行 CL2。

**风险：** margin 下降，调试变量增加。

**修复：** 先用项目 baseline CL3 建稳定基线，再做性能 A/B。

---

# B. SDRAM Routing / SI

## Fault 06｜所有 FMC 线强制完全等长

**表现：** 板上出现大片蛇形。

**根因：** 把 timing closure 误解成视觉等长。

**后果：** self-coupling、串扰、额外 via、clock 被无意义拖长。

---

## Fault 07｜SDCLK 为了“等长”绕远

**错误：** Clock 被当成普通 group member。

**修复：** SDCLK 先直接、干净、连续 reference；其他 group 对 clock 做 timing budget。

---

## Fault 08｜100 ps 项目目标被写成“SDRAM 标准”

**错误：** 把 V3 engineering target 当 JEDEC universal rule。

**修复：** 在规则表中保留 source=project timing budget。

---

## Fault 09｜一半 DQ 在 L1，一半 DQ 在 L6

**问题：** 长度可能一样，但 reference、via、delay、crosstalk 条件完全不同。

---

## Fault 10｜DQ 经由三次换层后仍只看总长度

**遗漏：** via discontinuity、reference transfer、vertical return。

---

## Fault 11｜蛇形节距很密

**现象：** KiCad 长度匹配完美，实测却更差。

**原因：** meander 自耦合让“几何长度”不等于预期电气延迟。

---

## Fault 12｜地址线自然差 8 mm，却全部补到 0.2 mm

**问题：** 没先验证 8 mm 对应的 ps 是否已经远小于 timing budget。

**修复：** ps-first，再决定是否 tuning。

---

## Fault 13｜每根 DQ 都串 33 Ω

**错误：** 把 source termination 当装饰性标配。

**修复：** 预留 footprint 可以；是否装、装多大依 IBIS/示波器证据。

---

# C. Power / SSN

## Fault 14｜SDRAM VDDQ 去耦全堆在 TSOP 一端

**问题：** 另一侧 I/O pin 的局部 switching loop 很差。

---

## Fault 15｜3V3_SDRAM 从细 neck 进入大铜皮

**误区：** “后面很大一块 plane，所以没事。”

**问题：** bottleneck 的阻抗/电感仍然存在。

---

## Fault 16｜H743 所有 GPIO OSPEEDR 统一最高

**风险：** edge 过快、过冲、串扰、SSN、EMI 增加。

**修复：** speed 由 timing + signal quality 决定。

---

## Fault 17｜VCAP 被拉到测试排针

**严重错误：** 把 core regulator stabilization node 当普通 rail。

---

# D. RMII / Ethernet

## Fault 18｜RMII 也建成 100 Ω differential pair

**错误：** RMII 是 single-ended LVCMOS。

**100 Ω differential** 属于 MDI 侧的 channel geometry。

---

## Fault 19｜REF_CLK direction 未冻结

**现象：** PHY 和 MCU 都在等对方时钟，或 strap/config 与 schematic 不一致。

---

## Fault 20｜PA7 / PC4 / PC5 同时分给 FMC 和 RMII

**问题：** 原理图后期才发现 alternate-function collision。

**修复：** 资源冻结阶段使用 PH5/PH6/PH7 的 SDRAM Bank 2 control path。

---

## Fault 21｜RBIAS 用 10 kΩ“差不多”

**错误：** LAN8742A 要求的 12.1 kΩ 1% 是器件 analog bias requirement，不是经验值。

---

## Fault 22｜PHY exposed pad 只接一根细线

**问题：** thermal / analog reference / return 都变差。

---

## Fault 23｜PHY 很靠近 RJ45，但 Magnetics 在板子中央

**问题：** MDI analog path 被拉长，隔离边界混乱。

---

## Fault 24｜MDI pair 上放长 test-point stub

**问题：** differential channel 出现明显 discontinuity/stub。

---

## Fault 25｜RJ45 shield 直接短到 System GND，理由只是“别人都这样”

**问题：** 没有 enclosure/chassis/ESD current path 定义。

---

## Fault 26｜Bob Smith 网络照抄另一颗 PHY

**错误：** termination/magnetics topology 必须从当前 PHY + magnetics + connector source 推导。

---

# E. Floorplan / Layer / EMC

## Fault 27｜先走 USB 和慢 GPIO，最后 SDRAM 只能绕

**问题：** routing priority 被低价值网络占领。

---

## Fault 28｜Buck SW node 正好位于 SDCLK 与 PHY 之间

**风险：** 电场/磁场耦合到两个最敏感时钟/analog 区。

---

## Fault 29｜Power Plane split 穿过 Address/Control corridor

**问题：** 信号几何连续，但 reference discontinuity 导致 return 绕行和共模转换。

---

## Fault 30｜RJ45 connector zone 和 SDRAM tuning zone 重叠

**问题：** cable/ESD/common-mode 能量与 memory timing corridor 物理混在一起。

---

# F. Bring-up / Firmware 伪故障

## Fault 31｜SDRAM 初始化前把 heap 放外部 RAM

**现象：** 启动随机 HardFault。

**根因：** 软件链接/初始化顺序，不是 SI。

---

## Fault 32｜只在 DMA + Cache 打开后数据错，就立刻改 PCB

**优先检查：** cache coherency、MPU attributes、buffer ownership。

---

## Fault 33｜Ethernet PHY ID 都读不到就开始调 LwIP

**正确顺序：** power → reset → clock → MDIO → PHY ID → link → MAC/stack。

---

## Fault 34｜降 SDRAM 频率后稳定，就宣布“PCB 一定坏”

**问题：** 降频同时改变 timing margin；可能是 controller timing、GPIO speed、PI、SI 或温度。

**需要更多 A/B。**

---

## Fault 35｜一次同时改 5 个 timing 参数、串阻和 GPIO speed

**问题：** 即使修好，也不知道根因。

---

# G. Release / Documentation

## Fault 36｜Stackup 改了但 SDRAM ps/mm 仍沿用旧值

**问题：** length→delay 转换失效。

---

## Fault 37｜板厂改 dielectric 后 MDI width/gap 不重算

**问题：** controlled impedance rule 已失效。

---

## Fault 38｜只保存 Gerber，不保存 Source Freeze

**后果：** 三个月后无法知道 timing/stackup/datasheet 依据。

---

## Fault 39｜DRC 0 Error 就 Release

**漏掉：** reference、return、timing meaning、ESD path、current loop、lifecycle。

---

## Fault 40｜验证只写“能 ping、内存能读写”

**不足：** 没有 full-range、long-run、temperature、throughput、concurrent stress 与证据。

---

# Fault Lab 使用方式

每个故障都填写：

| Field | Answer |
|---|---|
| Symptom | |
| Why DRC misses it | |
| First hypothesis | |
| Current/signal path | |
| Source/timing evidence | |
| Proposed change | |
| Side effects | |
| A/B test | |
| Result | |
| Checklist rule learned | |

目标不是记住 40 个错误，而是最终看到陌生板时，能自己构造这张分析表。
