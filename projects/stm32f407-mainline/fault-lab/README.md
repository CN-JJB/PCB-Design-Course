# Fault Lab｜故障板实验室

> 目标：不是背“正确规则”，而是训练你看到一块有问题的 PCB 时，能从 **症状 → 电流/参考结构 → 根因 → 修改** 推理。

当前 Part 0 + Part 1 先定义 8 个故障场景。后续可验证 KiCad 工程建立后，每个场景会提供 `bad` / `fixed` 两个版本。

## F01｜Decoupling Parade

**故意错误**：所有 100 nF 电容排成一条漂亮直线，远离 MCU。

观察：
- 原理图完全正确；
- ERC/DRC 可能全过；
- 局部供电环路被拉长。

要回答：
1. 哪个 VDD pin 的 local current path 变大？
2. 哪个几何部分增加寄生电感？
3. 应该怎样重新 placement？

## F02｜Remote VCAP

**故意错误**：VCAP1/2 电容经长而细的 track 接 MCU。

要回答：
- VCAP 的功能是什么？
- 为什么这不是普通 1.2V rail？
- 修复时最先改 placement 还是加一个更大电容？为什么？

## F03｜Clock Across the Board

**故意错误**：HSE crystal 放在 MCU 另一侧，中间跨普通 GPIO。

要回答：
- oscillator loop 哪部分变大？
- 哪些外部信号可能耦合进入？
- 如何缩小局部系统？

## F04｜Use L2 as an Escape Layer

**故意错误**：为了少几个 via，在 L2 solid GND 上走一条普通 GPIO。

要回答：
- 这条 GPIO 自己可能没问题，为什么它会影响其他 Top signals？
- reference plane 的“公共基础设施”价值是什么？

## F05｜Bottom Across Power Split

**故意错误**：SWCLK 在 L4 跨越 L3 的 3V3/5V 分界。

要回答：
- L4 reference 是谁？
- reference structure 在哪里突变？
- 为什么单看 B.Cu 看不出问题？

## F06｜Hot LDO

**故意错误**：看到 AP2112 “600 mA”就按 5V→3.3V、600mA 连续负载设计，无热分析。

要回答：
- `P=(Vin−Vout)I` 是多少？
- current rating 与 thermal capability 为什么不是一回事？
- V2 应何时改用更合适的 regulator architecture？

## F07｜Debug Connector Trap

**故意错误**：SWD header 被高器件挡住，pin 1 标识模糊，GND 接触路径差。

要回答：
- 哪些问题属于 SI？
- 哪些问题属于 mechanical/debuggability？
- 为什么“能制造”仍不等于“能调试”？

## F08｜Gerber Surprise

**故意错误**：编辑器里看起来有标识/地铜，最终 Gerber 中 layer/zone/mask 与预期不同。

要回答：
- 为什么必须用最终输出查看器？
- 哪些问题是 PCB Editor 视图无法替代的？

---

## 每个 Fault 的分析模板

```markdown
# Fault Fxx

## Symptom

## What DRC sees

## What DRC does NOT see

## Signal / power path

## Return / reference structure

## Root cause

## Fix

## Before / After image

## New checklist item
```

后续 Part 2/3/4 会继续新增：

- reflection / termination；
- split-plane crossing；
- missing reference transition；
- differential asymmetry；
- crosstalk；
- bad buck hot loop；
- connector common-mode path；
- ESD placement。

最终 Fault Lab 会变成整本教材的第二条实战主线。