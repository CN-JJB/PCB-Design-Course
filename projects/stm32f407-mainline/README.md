# STM32F407 Mainline｜MCU 主线工程

> 如果你是第一次做本课程工程，**不要从本目录随便点文件**。

## 唯一开始方式

1. [STM32F407 V1 START HERE](v1/START_HERE.md) — 第一块四层板
2. [STM32F407 V2 START HERE](v2/START_HERE.md) — USB/CAN/SDIO + SI/PI/EMC
3. [STM32H743 V3 START HERE](../stm32h7-mainline/v3/START_HERE.md) — 六层 + SDRAM + Ethernet

主线关系：

~~~text
STM32F407 V1
      ↓
STM32F407 V2
      ↓
STM32H743 V3
~~~

## V1 当前目标

完成第一块**可解释、可制造、可调试**的四层 MCU 板。

不是先画 PCB，而是：

~~~text
System Spec
→ Source Freeze
→ Power / Clock
→ Schematic
→ Stackup / Rules
→ Placement
→ Routing
→ Release Gate
→ Bring-up
→ Final Review
~~~

具体每一步的任务和通过标准都在 [v1/START_HERE.md](v1/START_HERE.md)。

## KiCad 工程状态

仓库已经具备 KiCad 10 Docker Hardware CI，可以在真实 KiCad 源文件提交后运行 ERC / DRC / schematic parity。

当前主线仍**没有真实完成的 V1/V2/V3 CAD 成品**，因此项目保持 Engineering Draft。这里不会用人工拼出来的空壳 .kicad_sch/.kicad_pcb 冒充“已完成项目”。

## V1 基线器件

- MCU：STM32F407VGT6 / LQFP100
- Teaching LDO：AP2112K-3.3（最终 BOM 仍需库存/生命周期/热预算复核）
- Input：5 V external input
- Debug：SWD
- Clock：internal first bring-up + HSE footprint

## 真实制造案例

课程四层 stackup 使用 JLCPCB JLC04161H-3313 的公开数据作为教学案例（基线查询 2026-08-26）。

换 PCB manufacturer / stackup 时，必须重新核对介质、铜厚、规则和 impedance model。
