# 01｜FPGA 板级设计思维：先冻结 Device / Package，而不是先画接口

> FPGA 的型号后缀不是采购细节。Device + package 一变，Bank、I/O 数、GTP、memory pin group、BGA escape 都可能一起变。

---

# 1. 教学器件

冻结：

**XC7A35T-1CSG325C**

需要把 order code 拆开读：

- XC7A35T：Artix-7 35T；
- -1：speed grade；
- CSG325：325-ball chip-scale BGA；
- C：commercial temperature grade。

CSG325 是 15 mm × 15 mm、0.8 mm ball pitch。

---

# 2. 为什么不是“先选逻辑资源”

FPGA 选型至少同时看：

- logic / BRAM / DSP；
- user I/O；
- Bank 类型；
- package；
- clock-capable pins；
- GTP 是否 bonded；
- DDR3 pin grouping；
- configuration pins；
- thermal；
- PCB escape；
- cost / lifecycle。

如果只看 LUT 数，PCB 可能根本无法实现你想要的接口。

---

# 3. Package 是系统架构

同一个 FPGA die 换 package 后可能改变：

- 可用 user I/O；
- GTP 是否引出；
- power/GND ball 数量；
- BGA pitch；
- escape 难度；
-可用 clock pins；
- memory interface bank组合。

因此工程记录必须写：

> Exact device + exact package

不能只写“Artix-7 35T”。

---

# 4. CSG325 为什么适合教学

它同时提供两个很好的矛盾：

## 优点

- 0.8 mm pitch，比 0.5 mm BGA 更适合第一次 escape；
- 仍然足够密集；
- CSG325 上的 XC7A35T 可使用 GTP；
- FPGA 周围能看到真实的 Bank / power / transceiver grouping。

## 代价

- 不能再用 MCU LQFP 的“从四边直接扇出”思维；
- 内层、via、fanout、plane continuity 会真正决定 PCB。

---

# 5. 本 Part 的功能边界

Artix-7 V1 教学板包含：

- 100 MHz class system oscillator；
- JTAG；
- Master SPI configuration flash；
- x16 DDR3；
- 两组 3.3 V GPIO header；
- 一组 1.8 V I/O experiment bank；
- 一个 GTP lane / connector teaching path；
- status LEDs / reset / configuration controls。

不要求实现复杂 HDL。

---

# 6. 最先冻结的文件

在 PCB 之前先创建：

- package-bank-map.md
- io-standard-matrix.md
- power-rail-budget.md
- clock-plan.md
- configuration-plan.md

它们比“原理图画到多少页了”更重要。

---

# 7. Fault

## 只写 XC7A35T，不写 CSG325

后果：

- 误用另一个 package 的 pin；
- 误以为有/没有 GTP；
- footprint 与 symbol pinout 不一致；
- BGA escape 策略失效。

---

# 8. Review

- [ ] exact order code 冻结
- [ ] package mechanical drawing 核对
- [ ] pin file / package pin table 来源记录
- [ ] GTP availability 核对
- [ ] DDR3 bank feasibility 核对
- [ ] configuration mode 预选
- [ ] layer-count 假设记录
- [ ] thermal/power estimate 计划已建立
