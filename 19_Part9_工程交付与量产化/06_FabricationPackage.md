# 06｜Fabrication Package：板厂真正需要的是受控制造定义

## 6.1 最小输出

根据供应商能力，常见 fabrication package 包括：

- copper / mask / silkscreen fabrication data；
- drill；
- board outline；
- fabrication drawing / notes；
- stackup；
- impedance requirement；
- material / finish requirement；
- route / V-score information；
- netlist/verification data（如 IPC-D-356）；
- ODB++ / IPC-2581（如果双方流程支持）。

不要假设所有工厂都使用同一格式组合。

## 6.2 Gerber Review

独立 viewer 检查：

1. board outline；
2. 每层 copper；
3. soldermask；
4. silkscreen；
5. drill；
6. slot；
7. NPTH/PTH；
8. layer alignment。

## 6.3 Stackup Note

至少写：

```text
layer count
overall thickness
copper
material family
controlled impedance structures
target/tolerance
approved fab adjustment policy
coupon/TDR requirement
```

### 6.3.1 Material Identity 与 Substitution Control

“FR-4”不是足够完整的 reliability specification。

按产品需要冻结：

- approved laminate family / exact material；
- Tg；
- Td；
- Z-axis expansion / CTE；
- moisture behavior；
- CAF requirement；
- lead-free reflow compatibility；
- Dk / Df or controlled-impedance relevance；
- copper thickness / construction；
- applicable certification。

**Higher Tg 不是自动更可靠。**

材料选择必须回到具体 failure mechanism。

Fab substitute material 前应满足：

~~~text
property equivalence
→ impedance/process impact review
→ reliability impact review
→ approval / ECO when required
~~~

而不是由工厂在量产时静默换成“差不多的 FR-4”。

## 6.4 Drill Review

区分：

- plated；
- non-plated；
- slot；
- via；
- mechanical hole；
- special via process。

## 6.5 Fabrication Drawing

关键机械信息不要只藏在 CAD：

- dimensions；
- tolerances；
- datum；
- hole notes；
- finish；
- special edge / bevel；
- controlled depth / backdrill（如有）。

## 6.6 Netlist Cross-check

如生产流程支持，使用独立 netlist / electrical verification 数据帮助发现 CAM 处理或文件错误。

## 6.6.1 Controlled-Impedance Board 还需要“可验证结构”

如果一个项目声称 controlled impedance 是 release requirement，那么 fabrication package 不应只有 Gerber + 一句“90 Ω”。

Lee Ritchey 的 Design-for-Test 资料提出了一个很实用的制造验证思路：

- 每个受控阻抗层提供对应 test trace / coupon；
- single-ended 与 differential structure 分开；
- 用 stacking stripe / edge witness 检查层序、介质与 etch；
- 对 plane pair 需要时预留可测结构。

### 📐 一个最小 Coupon 思维图

~~~text
Panel edge
┌──────────────────────────────────────────┐
│  L1  SE coupon  ───────────────────────  │
│  L1  DIFF coupon ══════════════════════  │
│  L3  SE coupon  ───────────────────────  │
│  L3  DIFF coupon ══════════════════════  │
│                                          │
│  stacking stripes  ||||||||||||||        │
└──────────────────────────────────────────┘
~~~

这里的目标不是让每个 hobby prototype 都做复杂 IPC coupon，而是训练一个重要思维：

> **如果某个制造参数真的重要，就应该问“我如何证明它制造对了？”**

### Fabrication Drawing 新增阻抗表

| Net class / structure | Layer | Reference | W | S/G | Target Z | Tolerance | Coupon | Fab may adjust? |
|---|---|---|---:|---:|---:|---:|---|---|
| USB_DIFF | | | | | | | | |
| CLK_SE | | | | | | | | |

### “板厂会测”要具体到测试等级

资料集中记录的 JLCPCB laminated-structure 文档区分不同阻抗测试/精度服务。课程不把某个当前百分比写成永久规则，而要求 release package 明确：

- 订单选择的 impedance service；
- acceptance tolerance；
- coupon 是否由 fab 生成还是设计者提供；
- 是否要 TDR report；
- CAM 调线宽是否允许；
- report 是否作为 lot evidence 归档。

### Stacking Stripe 为什么值钱？

阻抗 fail 有时不是线宽问题，而是：

~~~text
layer order swapped
dielectric thickness wrong
wrong material
etch bias
wrong copper
~~~

这些错误在成品板上可能表现成“所有高速网络都怪怪的”。

stacking stripe / witness structure 的价值，就是在装配前给你一个低成本的物理证据。

### 来源

- Lee Ritchey, *PCB Design For Test — Test Structures And Types Of Tests, Part 1*  
  https://resources.altium.com/p/pcb-design-test-test-structures-and-types-tests-part-1
- JLCPCB, *Multi-Layer PCB Standard Laminated Structures*  
  https://jlcpcb.com/help/article/multi-layer-pcb-standard-laminated-structures
- Zachariah Peterson, *Impedance Control: How to Specify Your Requirements for PCB Manufacturers*  
  https://resources.altium.com/p/pcb-manufacturing-and-impedance-control-how-specify-your-requirements


## 6.7 Release Gate

- [ ] 从冻结 commit 生成；
- [ ] Jobset / CLI 可重复；
- [ ] Gerber viewer 已人工复核；
- [ ] stackup 与 fab 已确认；
- [ ] drill / slots 已确认；
- [ ] package hash / manifest 已生成。
