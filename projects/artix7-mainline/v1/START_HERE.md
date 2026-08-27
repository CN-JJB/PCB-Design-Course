# 🎮 Artix-7 V1｜START HERE

> **这是 FPGA 项目唯一开工入口。** 不要从 DDR3、GTP 或 BGA 布线中间切入。

当前状态：**🧩 Engineering Draft**。

## 关卡地图

| Gate | 任务 | 主要产出 | 通过标准 |
|---|---|---|---|
| 1 | Device / Source Freeze | [system-spec.md](system-spec.md), [source-freeze.md](source-freeze.md) | exact device/package/tool/source冻结 |
| 2 | Bank / Pin Plan | [package-bank-map.md](package-bank-map.md), [io-standard-matrix.md](io-standard-matrix.md) | VCCO/IOSTANDARD/Bank 冲突清零 |
| 3 | Power / Sequence | [power-rail-budget.md](power-rail-budget.md), [pdn-review.md](pdn-review.md) | XPE/rail/sequence/thermal 有预算 |
| 4 | Config / Clock | [configuration-plan.md](configuration-plan.md), [clock-plan.md](clock-plan.md) | JTAG/SPI/clock-capable pin/refclk明确 |
| 5 | BGA Escape | [bga-escape-plan.md](bga-escape-plan.md) | layer/via/fab strategy 通过 DFM |
| 6 | DDR3 / MIG | [ddr3-mig-plan.md](ddr3-mig-plan.md), [ddr3-routing-review.md](ddr3-routing-review.md) | byte lane / DQS / CK / VREF / VTT 可路由 |
| 7 | GTP Channel | [gtp-interface-plan.md](gtp-interface-plan.md) | line rate/channel/refclk/AC coupling/S-parameter plan明确 |
| 8 | Vivado ↔ KiCad | [vivado-kicad-constraint-map.md](vivado-kicad-constraint-map.md) | XDC/schematic/PCB pin map一致 |
| 9 | Bring-up | [bringup-test-plan.md](bringup-test-plan.md), [validation-matrix.md](validation-matrix.md) | JTAG→config→DDR3→IBERT/BER 有 evidence |
| 10 | Final Review | [release-gate.md](release-gate.md), [final-design-review.md](final-design-review.md) | FPGA 板级毕业 Gate 通过 |

# Gate 1｜现在先做什么

1. 打开 [system-spec.md](system-spec.md)；
2. 完成 [source-freeze.md](source-freeze.md) 中的 Vivado / MIG / KiCad tool freeze；
3. 确认 exact FPGA suffix、DDR3 suffix、Flash candidate、目标 GTP line rate。

### 通过标准

- [ ] device/package exact；
- [ ] 功能范围固定；
- [ ] Vivado/MIG/KiCad version 记录；
- [ ] DDR3/GTP 的目标不是“以后再说”；
- [ ] fab capability / layer-count hypothesis 已进入 reopen list。

**通过以后才进入 Bank / Pin Planning。**

# 最重要的纪律

FPGA 项目不允许：

```text
PCB pin 好走
→ 随便换 FPGA pin
→ 最后让 Vivado 想办法
```

正确顺序：

```text
Device/Bank rule
↔ MIG / XDC
↔ BGA escape feasibility
↔ PCB floorplan
→ freeze
```

## 完成以后

→ [Part 9｜工程交付与量产化](../../../19_Part9_工程交付与量产化/00_本Part导读.md)
