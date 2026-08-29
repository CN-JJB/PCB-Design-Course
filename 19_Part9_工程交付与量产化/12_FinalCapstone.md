# 12｜Final Capstone：交付一套别人可以复现的硬件工程

> 全课程最终作品不是一张 PCB 截图，而是一套可复现工程。

## 12.1 选择毕业项目

推荐使用：

- STM32H743 V3 六层板；

并把：

- STM32F407 V2 作为四层对照；
- Artix-7 V1 作为 FPGA 专项扩展。

## 12.2 必须提交的证据

### A. Design

- system spec；
- exact MPN；
- schematic；
- PCB；
- stackup；
- constraints；
- design decisions；
- source freeze。

### B. Review

- schematic review；
- SI；
- PI；
- EMC；
- DFM/DFA/DFT；
- final design review。

### C. Manufacturing

- fabrication package；
- assembly package；
- BOM / AVL / alternates；
- variant；
- release manifest。

### D. Validation

- safe bring-up；
- rail measurement；
- interface test；
- memory/SerDes stress（项目适用时）；
- pre-compliance evidence；
- bug/fix/retest。

### E. Production

- programming package；
- fixture/test procedure；
- FAI；
- pilot yield；
- ECO；
- traceability。

## 12.2.1 Layout Review 不是“找难看的线”：按 Source → Return → Conversion → Antenna → Manufacturability 审

EEVblog #1323 / #974 这类真实 Layout Review 视频的价值，不是让学生模仿某个 reviewer 的个人风格，而是学习**如何系统地找问题**。

最终 Capstone 的 review 至少按下面五个视角走一遍：

| 视角 | 你在找什么 |
|---|---|
| Source | clock、switch node、fast edge、high di/dt 在哪里 |
| Return | reference 是否连续、换层是否有回流路径 |
| Conversion | 差模如何变成共模、via/connector/split 是否不对称 |
| Antenna | cable、board edge、slot、large loop 是否能被激励 |
| Manufacturability | via、mask、panel、stackup、assembly 是否能稳定生产 |

### Review 输出不能只是截图

每一个发现要记录：

~~~text
Observation
→ Why it matters
→ Source / evidence
→ Fix
→ Re-check result
~~~

这正是从“会画 PCB”走向“会做工程 Review”的分界。

### 视频来源

- EEVblog #1323 — *PCB Layout Review & Analysis*  
  https://www.youtube.com/watch?v=xhRhsCVF8mE
- EEVblog #974 — *PCB Layout Walkthrough - PART 4*  
  https://www.youtube.com/watch?v=JrH_itjMDjo


## 12.3 口头答辩

随机抽一个设计区域，你必须能回答：

1. 这条 requirement 来自哪里？
2. 为什么这个器件/拓扑？
3. 电流怎么闭合？
4. signal reference 是什么？
5. 这个数字是 requirement 还是 target？
6. KiCad 如何表达？
7. DRC 为什么不足？
8. 如何测？
9. 哪个失败会让你 reopen 设计？
10. 最终 release 如何复现？

## 12.4 禁止的“毕业证据”

以下都不能单独证明毕业：

- PCB 很漂亮；
- DRC 0 error；
- 示波器某一次看起来正常；
- “板子用了半年没坏”；
- reference design 也这么画；
- Gerber 已下单。

## 12.5 最终一句话

> **设计能力的终点不是把线连通，而是把需求、物理、约束、制造和证据连成一个可审计的系统。**
