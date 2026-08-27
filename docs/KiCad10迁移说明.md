# KiCad 10 迁移与课程基线

课程自 2026-08 起以 **KiCad 10.0.x** 为正式工具基线。

## 为什么升级

正式课程现在不只是画原理图和 PCB，还需要：

- 可重复 ERC / DRC；
- Manufacturing Jobset；
- Design Variants / DNP；
- CLI 自动导出；
- fabrication / assembly 输出；
- Hardware CI。

因此版本基线必须与工程交付 Part 9 对齐。

## 课程要求掌握

```text
Project
Schematic
PCB
Physical Stackup
Net Classes
Custom Rules
Rule Areas / Keepouts
Design Variants
Jobsets
kicad-cli
ERC / DRC
Gerber / Drill / Position / BOM
STEP
IPC-D-356
ODB++ / IPC-2581（理解用途与工厂要求）
```

## 版本纪律

- 示例以 10.0.x 为基线；
- UI 菜单路径只作为辅助，不作为知识核心；
- 自动化命令在 CI 中显式打印 `kicad-cli version`；
- 新大版本出现后先建立 migration note，再升级课程；
- 任何因为版本变化导致的规则/输出差异必须记录。
