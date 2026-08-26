# 06｜DRC、Gerber 与人工审查：软件通过只是开始

> 🎯 **本章任务**：把 V1 从“KiCad 里看起来完成”推进到“可以交给板厂”。你会建立两套检查：**自动 DRC** 和 **人工工程 Review**。

---

## 1. DRC 能检查什么？

典型自动规则：

- clearance；
- minimum track width；
- via size / drill；
- unconnected items；
- copper-to-edge；
- courtyard / keepout；
- 某些 length / differential / custom rule 条件。

这些问题非常重要。

但 DRC 不等于“电气设计正确”。

---

## 2. DRC 很难替你证明什么？

例如：

- 去耦电容是否真的形成低电感环路；
- HSE 是否被 switching route 包围；
- L1 高速信号是否跨 L2 slot；
- Bottom signal 是否跨 L3 power split；
- connector pinout 是否方向反了；
- SWD header 是否物理上插不进去；
- LDO 热设计是否足够；
- test point 是否探得到。

所以我们的 Definition of Done 不是：

```text
0 DRC errors
```

而是：

```text
0 unresolved DRC errors
+ Manual Design Review passed
+ Fabrication output review passed
```

---

## 3. DRC Waiver 纪律

真实工程中有时会出现有意违反通用规则的结构。

处理方式不是：

> “右键 Ignore，红点消失。”

而是记录：

```text
Violation:
Why it exists:
Why it is acceptable:
Source/analysis:
Reviewer:
```

没有解释的 waiver = 未解决问题。

---

## 4. Gerber 不是“Save As”

Gerber/Drill 是给制造端的最终几何描述。

输出前确认：

- F.Cu / In1.Cu / In2.Cu / B.Cu；
- F.Mask / B.Mask；
- F.Silkscreen / B.Silkscreen（如使用）；
- Edge.Cuts；
- drill files；
- 必要 fabrication notes。

不要只检查压缩包有没有文件，要用 Gerber Viewer 看“制造端将看到什么”。

---

## 5. 四层 Gerber Viewer 检查顺序

### 5.1 Edge.Cuts

- 闭合；
- 没有重复边；
- cutout 正确；
- mounting hole 位置正确。

### 5.2 L2 GND

这是 V1 的重点：

- 是否连续；
- 有没有意外 isolated island；
- through-hole/via antipad 是否形成过窄铜颈；
- 是否被误画的 keepout/zone cut 切开。

### 5.3 L3 Power

- 3V3 region 是否覆盖需要区域；
- 是否有狭窄 neck；
- Bottom 关键网络下方的 reference 是否合理；
- 是否有无意孤岛。

### 5.4 Solder Mask

- fine-pitch pad 开窗；
- test point 开窗；
- mounting/mechanical copper 是否符合意图。

### 5.5 Silkscreen

- polarity；
- connector pin 1；
- board revision；
- 不压焊盘；
- 调试接口标注。

---

## 6. Fabrication Notes

建议在 `fabrication-notes.md` 中记录：

```text
Board: STM32F407 V1
Revision: A
Layer count: 4
Nominal thickness: 1.6 mm
Stackup case study: JLC04161H-3313 (re-check at order time)
Outer copper: according to selected order
Inner copper: according to selected order
Controlled impedance: none required in V1 / or specify if later enabled
Special process: none
```

V1 没有必须做 impedance-controlled interface，就不要为了“高级感”硬加 50 Ω 要求。

---

## 7. BOM 与 PCB 要同步 Review

板子能制造不代表能装。

检查：

- exact MPN；
- footprint 与 package 一致；
- polarity；
- stock / lifecycle；
- alternate part 是否需要不同 footprint；
- connector mating part；
- crystal package 与 CL；
- LDO input/output capacitor dielectric/voltage rating。

尤其 MLCC：标称 1 µF 并不意味着在 DC bias 下永远保持 1 µF。Part 3 PI 会深入。

---

## 8. Pre-Fab Design Review 三层结构

### Level A：能不能制造

DRC / drill / edge / mask / fab output。

### Level B：能不能上电

Power tree / pinout / footprint / reset / SWD / boot / decoupling。

### Level C：电磁结构是否合理

Reference plane / return path / clock / loops / connector / power distribution。

这三层都通过，才下单。

---

## 9. ❌ 故障板：Gerber 里才发现的错误

常见例子：

- PCB Editor 看见 logo，但它画在 User.Drawings，不在 silkscreen；
- mounting hole 是 NPTH/PTH 类型弄错；
- In1 GND zone 没 refill；
- Edge.Cuts 有两个重叠轮廓；
- test point 被 solder mask 覆盖；
- connector pin 1 丝印在错误一侧。

这就是为什么：

> **最终输出必须用最终输出查看器检查。**

不要只相信编辑器视图。

---

## 10. V1 出货 Checklist

### Schematic

- [ ] ERC reviewed；
- [ ] MCU exact part；
- [ ] power/VCAP/VDDA/VBAT reviewed；
- [ ] reset/boot/SWD reviewed。

### PCB

- [ ] DRC zero unresolved；
- [ ] stackup documented；
- [ ] L2 continuity review；
- [ ] L3 power review；
- [ ] decoupling placement review；
- [ ] HSE review；
- [ ] debug accessibility review。

### Fabrication

- [ ] Gerber layer-by-layer reviewed；
- [ ] drill reviewed；
- [ ] board outline reviewed；
- [ ] fabrication notes updated；
- [ ] board-house current stackup rechecked。

### Assembly

- [ ] BOM/footprint match；
- [ ] polarity marks；
- [ ] connector orientation；
- [ ] programming fixture/cable access。

---

## 11. 本章输出

生成并归档：

```text
fab/
├── gerber/
├── drill/
├── fabrication-notes.md
└── gerber-review.md

review/
└── pre-fab-review.md
```

下一章不是“项目结束”，而是最容易被忽视的阶段：**板子回来以后怎么安全 Bring-up，怎么把问题变成下一版知识。**