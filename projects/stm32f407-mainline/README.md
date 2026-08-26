# STM32F407 Mainline｜课程主线工程

这个目录不是“示例代码附件”，而是整套课程的工程主线。

```text
STM32F407 V1 (4L basics)
      ↓
STM32F407 V2 (USB/CAN/SDIO + SI/PI/EMC)
      ↓
STM32H7 V3 (6L + Ethernet/SDRAM)
```

## 当前阶段：V1

目标：完成第一块可解释的四层 MCU 板。

### V1 资产

- `v1/hardware-constraints.md`：一手资料转成的硬件约束；
- `v1/design-decisions.md`：为什么这样选器件/叠层/布局；
- `review/design-review-checklist.md`：项目级 Review；
- `fault-lab/README.md`：故意错误案例。

## 关于 KiCad 工程文件

本仓库最终会维护可打开的 KiCad 工程，而不是只有截图。

当前环境无法运行 KiCad 做文件格式/DRC 验证，因此本次重构**不伪造 `.kicad_sch/.kicad_pcb` 文件**。工程文件只有在可以验证其可打开、规则正确、DRC 可复现时才作为“课程成品”提交。

在此之前，所有项目约束、网络表、布局意图和 Review 标准都先以可审计文本维护，避免出现“仓库里有个文件，但学生打不开”的假交付。

## V1 基线器件

- MCU：STM32F407VGT6 / LQFP100
- Teaching LDO：AP2112K-3.3（最终 BOM 仍需库存/生命周期/热预算复核）
- Input：5 V external input
- Debug：SWD
- Clock：internal first bring-up + HSE footprint

## 真实制造案例

课程四层 stackup 使用 JLCPCB `JLC04161H-3313` 当前公开数据作为案例（查询 2026-08-26）。

这不是绑定厂商：换 PCB manufacturer 时，必须重新导入该厂实际 stackup 和 impedance model。