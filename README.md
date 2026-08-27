# PCB 设计教材｜从二层板到四层 / 六层高速板

> 面向**已经能独立完成二层板**的学习者。主课程通过同一个 MCU 产品家族持续升级，并以 FPGA 板级设计作为专项副线，系统训练 4 层 / 6 层 PCB、SI、PI、EMI/EMC、DFM、测量、Design Review 与工程交付。

本课程不以“背规则”为目标，而是要求关键设计决策能够追溯到：**电流路径、电磁场、器件要求、接口规范、制造约束和验证证据**。

## 🚀 第一次来？不要从目录里猜

**直接从 [START_HERE.md](START_HERE.md) 开始。** 它把整套课程拆成 Gate：每一步明确“做什么、产出什么、通过标准、下一步”。

如果你已经知道自己要做哪个工程，也可以直接进入 [projects/ 闯关区](projects/README.md)。

## 正式主课程

| Part | 主题 | 教材状态 | 工程状态 |
|---|---|---|---|
| 0 | 二层 → 多层认知跃迁 | 📘 Complete | — |
| 1 | STM32F407 V1 第一块四层板 | 📘 Complete | 🧩 Engineering Draft |
| 2 | Signal Integrity | 📘 Complete+ | 🧩 V2 SI Draft |
| 3 | Power Integrity | 📘 Complete+ | 🧩 V2 PI Draft |
| 4 | EMI / EMC | 📘 Complete+ | 🧩 V2 EMC Draft |
| 5 | STM32F407 V2 四层综合 | 📘 Complete | 🧩 Engineering Draft |
| 6 | 四层 → 六层 | 📘 Complete | 🧩 H7 Transition Draft |
| 7 | STM32H743 六层高速综合 | 📘 Complete+ | 🧩 Engineering Draft |
| 8 | Artix-7 FPGA 板级设计 | 📘 Complete+ | 🧩 Engineering Draft |
| 9 | 工程交付与量产化 | 📘 Complete | 🧩 Release Infrastructure |

状态含义：

- **📘 Complete**：教材主链闭合。
- **📘 Complete+**：主体完整，本轮继续补充高级内容。
- **🧩 Engineering Draft**：规格、约束、Review 等工程文档已存在，但仍有 TBD 或缺少真实 CAD / 实测证据。
- **🧪 Prototype Validated**：真实板已完成 Bring-up 与测试证据归档。
- **📦 Release Complete**：制造、装配、BOM、版本与 Release Gate 全部冻结。

> **重要：教材完成不等于硬件已经验证。** 仓库不会把模板、TBD 或教学假设伪装成生产冻结结果。

## 学习顺序

```text
Part 0  二层 → 多层
  ↓
Part 1  STM32F407 V1 四层基本功
  ↓
Part 2  SI
  ↓
Part 3  PI
  ↓
Part 4  EMI / EMC
  ↓
Part 5  STM32F407 V2 四层综合毕业板
  ↓
Part 6  四层 → 六层
  ↓
Part 7  STM32H743 V3：SDRAM + Ethernet 六层高速
  ↓
Part 9  工程交付 / DFM / DFA / DFT / Release / Pilot Build

FPGA 专项副线：
Part 6 基础 → Part 8 Artix-7：Bank / BGA / DDR3 / GTP / XDC ↔ KiCad
```

## 入口

- [Part 0｜从二层到多层](10_Part0_从二层到多层/00_本Part导读.md)
- [Part 1｜STM32F407 四层板](11_Part1_STM32F407四层板/00_项目导读.md)
- [Part 2｜Signal Integrity](12_Part2_信号完整性/00_本Part导读.md)
- [Part 3｜Power Integrity](13_Part3_电源完整性/00_本Part导读.md)
- [Part 4｜EMI / EMC](14_Part4_EMI_EMC/00_本Part导读.md)
- [Part 5｜四层综合](15_Part5_四层综合/00_本Part导读.md)
- [Part 6｜四层到六层](16_Part6_四层到六层/00_本Part导读.md)
- [Part 7｜STM32H7 六层高速](17_Part7_STM32H7六层高速/00_本Part导读.md)
- [Part 8｜FPGA 板级设计](18_Part8_FPGA板级设计/00_本Part导读.md)
- [Part 9｜工程交付与量产化](19_Part9_工程交付与量产化/00_本Part导读.md)

## 前置复习与旧版资产

原来的 `01_零基础入门` ～ `08_附录` 不再作为正式主线。它们保留为：

- 二层板 / 原理图 / KiCad 前置复习；
- 旧版案例；
- FAQ、Checklist、速查表、踩坑案例等参考资产。

统一入口见 [00_课程总览/学习路线.md](00_课程总览/学习路线.md) 与 [90_Legacy旧版教材/README.md](90_Legacy旧版教材/README.md)。

## 工程主线

```text
STM32F407 V1
  ↓
STM32F407 V2 — USB / CAN / SDIO + SI / PI / EMC
  ↓
STM32H743 V3 — 六层 + SDRAM + Ethernet

FPGA：
Artix-7 V1 — Bank / BGA / DDR3 / GTP
```

工程资料在 `projects/`。每个工程最终应包含：

```text
hw/       KiCad source + rules + jobset
docs/     system spec / decisions / constraints / reviews
bom/      BOM / alternates / lifecycle
sim/      IBIS / S-parameters / simulation evidence
test/     bring-up / measurement / validation
release/  immutable manufacturing releases
```

当前仓库中的 CAD / 测量 / release 资产必须以真实工程产生；缺失时明确标记为 Draft，而不是创建假的“完成文件”。

## KiCad 基线

正式课程自本轮起以 **KiCad 10.0.x** 为基线；KiCad 9 内容只保留兼容说明。课程使用：

- Physical Stackup
- Net Classes / Custom Rules
- Design Variants
- Jobsets
- `kicad-cli`
- ERC / DRC 自动化
- Gerber / drill / position / BOM
- IPC-D-356、ODB++、IPC-2581 等工程交付格式的概念与适用边界

版本变化时，以 KiCad 官方当前文档为准。

## 数字与规则纪律

课程中的数字必须明确属于哪一种：

1. 器件厂家 requirement；
2. 协议 / 标准 requirement；
3. 板厂能力或当前 stackup；
4. 系统设计 target；
5. 教学数量级或 heuristic。

不会把 `3W`、`100 nF`、固定 TVS 距离、固定 MHz 门槛、固定线宽等写成跨场景铁律。

## 最终毕业标准

最终不是“会把六层板布通”，而是：

> **有一套你能解释每个重要设计决策、能复现制造、能用证据验证、能受控发布的多层高速硬件工程。**
