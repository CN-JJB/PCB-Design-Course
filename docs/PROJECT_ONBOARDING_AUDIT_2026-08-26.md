# 项目“可直接上手性”审核｜2026-08-26

## 审核问题

一个第一次进入仓库的读者，能不能在不向作者提问的情况下知道：

1. **现在应该做什么？**
2. **做完以后下一步是什么？**
3. **做到什么标准才算这一关完成？**

## 审核前结论

### 课程层：基本清楚

根 README 已有 Part 0～9 路线和毕业 Gate，能回答“应该学什么”。

### 项目层：不够直接上手

主要问题：

- project README 先让读者看 PROJECT_STATUS，而不是告诉他第一步；
- PROJECT_STATUS 是最终成熟度 Gate，不是施工顺序；
- V2/H7/FPGA 工程文件很多，但缺少唯一顺序入口；
- V1 是第一块真正要做的板，却只有少量核心工程文档，缺需求→原理图→Stackup→布局→布线→Release→Bring-up 的逐关工作表；
- 读者容易提前打开 KiCad，跳过 requirement/source/mechanical freeze；
- 从 Part 5/7/8 导读进入时，没有显式跳到工程执行入口。

因此审核前判断：

| 项目 | 内容准备度 | 直接上手度 | 主要原因 |
|---|---:|---:|---|
| STM32F407 V1 | 中 | **不足** | 缺逐步工程工作表 |
| STM32F407 V2 | 高 | **中** | 文件齐但顺序不显式 |
| STM32H743 V3 | 高 | **中** | timing/ETH资料齐但入口分散 |
| Artix-7 V1 | 高 | **中** | Bank/BGA/DDR/GTP文件齐但容易中途切入 |

## 本轮修正

### 1. 根入口

新增根目录 START_HERE.md：

- Gate 0 前置检查；
- Part 0；
- V1；
- SI/PI/EMC；
- V2；
- Part 6；
- H7；
- FPGA；
- Part 9。

### 2. projects 唯一入口

新增 projects/README.md，并规定：

> 先看 START_HERE，不先看 PROJECT_STATUS。

### 3. 每个项目新增 START_HERE

- stm32f407-mainline/v1/START_HERE.md
- stm32f407-mainline/v2/START_HERE.md
- stm32h7-mainline/v3/START_HERE.md
- artix7-mainline/v1/START_HERE.md

每个 Gate 固定包含：

~~~text
做什么
→ 输入
→ 产出
→ 通过标准
→ 下一关
~~~

### 4. V1 补齐工程工作表

新增：

- system-spec.md
- source-freeze.md
- power-clock-plan.md
- schematic-review.md
- stackup-rule-plan.md
- placement-plan.md
- routing-rule-plan.md
- release-gate.md
- bringup-test-plan.md
- final-design-review.md

现在 V1 从“教材项目”变成了“可以立即从 Gate 1 开始填写并逐步生成真实 CAD 的工程任务”。

### 5. 当前下一步显式化

每个 PROJECT_STATUS 增加“▶ 当前下一步”。

读者不需要从未勾选的几十项里自己推断。

## 修正后的判断

### 可以直接开始什么？

**可以直接开始“做工程”。**

读者现在可以：

1. 从根 START_HERE 选择路线；
2. 进入项目 START_HERE；
3. 从 Gate 1 填真实 requirement/source；
4. 达标后逐步进入 schematic / PCB / release / test。

### 还不能直接做什么？

**不能把仓库当成已经完成的成品板直接下单。**

当前真实 CAD、BOM、Gerber、实测 evidence 仍需按 Gate 生成。项目状态保持 Engineering Draft 是正确的。

## 验收标准

本轮“入口重构”通过的标准：

- [x] 根目录有唯一 START_HERE
- [x] projects 有唯一工程入口
- [x] 每个主线项目有 START_HERE
- [x] 每一步写明任务
- [x] 每一步写明产出
- [x] 每一步写明通过标准
- [x] 每一步写明下一步
- [x] V1 有完整逐关工作表
- [x] PROJECT_STATUS 明确当前下一关
- [x] 教材导读可跳到项目执行入口
- [ ] 真实 KiCad CAD 生成并由 CI 验证
- [ ] 实板制造与 Bring-up evidence
- [ ] Release Complete

最后三项属于真实硬件实施阶段，不应通过补 Markdown 假装完成。
