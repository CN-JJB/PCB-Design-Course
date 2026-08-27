# projects｜工程闯关区

> 教材告诉你“为什么”；这里告诉你“现在做什么”。

## 第一次进入 projects？

不要从文件列表随便挑。

### MCU 主线

1. **[STM32F407 V1｜第一块四层板 START HERE](stm32f407-mainline/v1/START_HERE.md)**
2. **[STM32F407 V2｜四层综合 START HERE](stm32f407-mainline/v2/START_HERE.md)**
3. **[STM32H743 V3｜六层高速 START HERE](stm32h7-mainline/v3/START_HERE.md)**

### FPGA 专项

4. **[Artix-7 V1｜FPGA 板级设计 START HERE](artix7-mainline/v1/START_HERE.md)**

## 每个项目的共同规则

每个项目都按：

```text
Requirement / Source
→ Schematic
→ Stackup / Rules
→ Placement
→ Routing
→ Review
→ Release
→ Bring-up / Validation
```

每一关必须明确：

- **做什么**
- **输入**
- **产出**
- **通过标准**
- **下一关**

## 工程状态与闯关进度不是一回事

- `START_HERE.md`：告诉你当前如何一步步做；
- `PROJECT_STATUS.md`：告诉你整个项目已经达到 Draft / Frozen / Validated / Released 中的哪一级；
- `hw/`：真实 KiCad 源文件；
- `bom/`：exact BOM / alternate；
- `sim/`：IBIS / S-parameter / 仿真；
- `test/`：实测证据；
- `release/`：不可变 release。

先看 `START_HERE.md`，不要先看 `PROJECT_STATUS.md`。
