# 🎮 STM32F407 V1｜START HERE

> **这是 V1 唯一开工入口。** 目标不是读完 Part 1，而是完成一块可制造、可调试、可解释的四层 STM32F407 板。

当前状态：**🧩 Engineering Draft**  
真实 KiCad CAD 尚未提交，所以你现在要做的是**从 Gate 1 开始把工程真正做出来**。

## 开工前

先通过：

- [Part 0](../../../10_Part0_从二层到多层/00_本Part导读.md)
- [Part 1 项目导读](../../../11_Part1_STM32F407四层板/00_项目导读.md)

---

## 关卡总览

| Gate | 你要完成 | 主要产出 | 通过以后 |
|---|---|---|---|
| 1 | 冻结需求与资料 | `system-spec.md` / `source-freeze.md` | 画原理图 |
| 2 | 电源/时钟/调试架构 | `power-clock-plan.md` | 完整 schematic |
| 3 | 原理图 Review | `schematic-review.md` + `hw/*.kicad_sch` | Stackup |
| 4 | Stackup / Rule Freeze | `stackup-rule-plan.md` | Placement |
| 5 | Placement Freeze | `placement-plan.md` + PCB placement | Routing |
| 6 | Routing / DRC | `routing-rule-plan.md` + `hw/*.kicad_pcb` | Release Review |
| 7 | 制造前 Release Gate | `release-gate.md` | 下单 / 焊接 |
| 8 | Bring-up | `bringup-test-plan.md` + `test/` evidence | Final Review |
| 9 | V1 Final Review | `final-design-review.md` | Part 2 |

---

# Gate 1｜需求与 Source Freeze

### 做什么

1. 阅读 [需求规格与系统架构](../../../11_Part1_STM32F407四层板/01_需求规格与系统架构.md)；
2. 填完 [system-spec.md](system-spec.md)；
3. 核对 [hardware-constraints.md](hardware-constraints.md)；
4. 把真正使用的一手资料写入 [source-freeze.md](source-freeze.md)；
5. 更新 [design-decisions.md](design-decisions.md)；
6. 阅读 [产品级保护电路](../../../11_Part1_STM32F407四层板/09_产品级保护电路_从接口到SafeState.md)，在 `system-spec.md` 增加 Protection Requirement Table。

### 产出

- `system-spec.md`
- `source-freeze.md`
- `hardware-constraints.md`
- `design-decisions.md`

### 通过标准

- [ ] MCU exact MPN / package 固定；
- [ ] V1 必做/不做功能明确；
- [ ] board size / connector edge / mounting-hole 方案不再是“以后再说”；
- [ ] power input、SWD、UART、HSE strategy 有明确方案；
- [ ] reverse input / overload / inrush / brownout / watchdog 已完成 threat inventory，未实现项有 deferred rationale；
- [ ] critical source 都有文档名/revision或明确 recheck 规则；
- [ ] 不存在会阻止原理图开始的 Blocker TBD。

**通过 → Gate 2。**

---

# Gate 2｜Power / Clock / Boot / Debug

### 做什么

阅读 [电源树与 MCU 原理图](../../../11_Part1_STM32F407四层板/02_电源树与MCU原理图.md)，填 [power-clock-plan.md](power-clock-plan.md)。

### 产出

- 电源树；
- current budget；
- VDD / VDDA / VCAP / VBAT strategy；
- HSE / internal-clock bring-up plan；
- BOOT0 / NRST / SWD / UART plan。

### 通过标准

- [ ] 所有 MCU power pin 都有处理方案；
- [ ] regulator 不是只看额定电流，已有负载/热预算；
- [ ] HSE exact part 可以是尚未采购，但 requirement 与选择流程明确；
- [ ] SWD/NRST/VTREF/GND 可实际接调试器；
- [ ] 上电第一阶段允许用内部时钟，降低变量。

**通过 → Gate 3。**

---

# Gate 3｜完成 Schematic + ERC + 人工 Review

### 做什么

1. 在 `hw/` 创建真实 KiCad 10 工程；
2. 画完整 V1 schematic；
3. 跑 ERC；
4. 用 [schematic-review.md](schematic-review.md) 人工审查；
5. 完成 [库/封装/MPN Gate](../../../11_Part1_STM32F407四层板/08_库封装与MPN可信度.md)。

### 通过标准

- [ ] ERC 无未解释 blocker；
- [ ] 所有 VDD/VSS/VCAP/VDDA/VSSA/VBAT 已逐 pin 核对；
- [ ] reset/boot/debug 默认状态明确；
- [ ] critical footprint 对过原始 mechanical drawing；
- [ ] exact MPN 与 symbol/footprint 可以追溯；
- [ ] schematic-review Blocker = 0。

**通过 → Gate 4。**

---

# Gate 4｜Stackup 与规则冻结

### 做什么

阅读 [四层 Stackup 与 KiCad 设置](../../../11_Part1_STM32F407四层板/03_四层Stackup与KiCad设置.md)，填 [stackup-rule-plan.md](stackup-rule-plan.md)。

### 通过标准

- [ ] 实际/教学板厂 stackup ID 有来源与查询日期；
- [ ] L1/L2/L3/L4 角色明确；
- [ ] L2 保持 solid GND；
- [ ] manufacturing min 与课程 design rule 分开；
- [ ] critical net class / via / clearance 已写入 KiCad；
- [ ] 更换板厂时知道哪些规则必须 reopen。

**通过 → Gate 5。**

---

# Gate 5｜Placement Freeze

### 做什么

阅读 [布局与电流环路](../../../11_Part1_STM32F407四层板/04_布局与电流环路.md)，填 [placement-plan.md](placement-plan.md)，然后只做 placement，不急着布线。

### 通过标准

- [ ] connector / mounting hole / mechanical 首先冻结；
- [ ] MCU power/decoupling loop 能逐个解释；
- [ ] HSE local；
- [ ] regulator current path 清楚；
- [ ] SWD/UART/test point 可访问；
- [ ] 没有“因为没位置所以以后再挪”的关键器件。

**通过 → Gate 6。**

---

# Gate 6｜Routing / DRC / Manual Review

### 做什么

阅读 [布线与规则](../../../11_Part1_STM32F407四层板/05_布线与规则设置.md)，按 [routing-rule-plan.md](routing-rule-plan.md) 布线。

### 通过标准

- [ ] L2 未被普通 signal 破坏；
- [ ] critical nets 有连续 reference；
- [ ] power path 没有明显 neck/via bottleneck；
- [ ] HSE / SWCLK 等关键线无无意义 stub；
- [ ] DRC 无未解释 blocker；
- [ ] schematic parity 通过；
- [ ] 所有 DRC waiver 有理由。

**通过 → Gate 7。**

---

# Gate 7｜Release Gate：下单前停一次

### 做什么

阅读 [DRC、Gerber 与人工审查](../../../11_Part1_STM32F407四层板/06_DRC_Gerber与人工审查.md)，逐项完成 [release-gate.md](release-gate.md)。

### 通过标准

- [ ] Gerber / drill 用独立 viewer 看过；
- [ ] critical footprint / polarity / pin-1 再核一次；
- [ ] board outline / hole / connector mechanical 检查；
- [ ] fab stackup 重新确认；
- [ ] BOM exact MPN / DNP 清楚；
- [ ] Blocker = 0。

**只有此 Gate 通过，才允许下单。**

**通过 → Gate 8。**

---

# Gate 8｜Bring-up

### 做什么

阅读 [V1 Design Review 与 Bring-up](../../../11_Part1_STM32F407四层板/07_DesignReview与Bringup.md)，按 [bringup-test-plan.md](bringup-test-plan.md) 逐级上电，并把证据放入 `test/`。

### 推荐顺序

```text
Power-off resistance
→ current-limited power
→ 3V3
→ NRST
→ SWD ID/connect
→ internal-clock firmware
→ LED / UART
→ HSE
→ GPIO / user function
→ Protection fault injection
```

### 通过标准

- [ ] 没有跳过 power-off 检查；
- [ ] 每一步只有一个新增变量；
- [ ] 3V3、current、reset、SWD、UART、HSE 有 evidence；
- [ ] 失败有 issue → hypothesis → fix → retest 记录；
- [ ] 在安全 bench 条件下至少验证 brownout / watchdog；已实现的 current-limit / inrush protection 也完成 fault injection。

**通过 → Gate 9。**

---

# Gate 9｜V1 Final Review

填写 [final-design-review.md](final-design-review.md)。

### 通过标准

你能随机指着 PCB 任意一个重要区域回答：

- 为什么它在这里？
- 电流怎么走？
- reference 是谁？
- rule 来源是什么？
- DRC 检查了什么？
- 哪些必须人工检查？
- 如何测量证明？

全部通过以后：

→ **[Part 2｜Signal Integrity](../../../12_Part2_信号完整性/00_本Part导读.md)**

---

## 你现在的第一步

如果今天就开工：**不要打开 PCB Editor。先打开 [system-spec.md](system-spec.md)，完成 Gate 1。**
