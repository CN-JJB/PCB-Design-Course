# 🎮 STM32H743 V3｜START HERE

> **这是六层高速主线唯一开工入口。** 前提：V2 已完成，Part 6 的 Layer Count / Stackup / Reference Transition 已通过。

当前状态：**🧩 Engineering Draft**。

## 关卡地图

| Gate | 任务 | 主要产出 | 通过标准 |
|---|---|---|---|
| 1 | System / Source Freeze | [system-spec.md](system-spec.md), [source-freeze.md](source-freeze.md) | exact device/source/环境边界可追溯 |
| 2 | Layer Count / Stackup | [layer-count-decision.md](layer-count-decision.md), [stackup-decision-record.md](stackup-decision-record.md), [layer-role-map.md](layer-role-map.md) | 6 层选择可解释，每层 reference 明确 |
| 3 | Pin / Power / Clock | [pin-peripheral-map.md](pin-peripheral-map.md), [power-clock-plan.md](power-clock-plan.md) | FMC/RMII/USB/debug 无资源冲突 |
| 4 | SDRAM Architecture | [sdram-part-selection.md](sdram-part-selection.md), [sdram-timing-budget.md](sdram-timing-budget.md) | ns→cycle calculation 完整 |
| 5 | SDRAM PCB Budget | [sdram-routing-constraints.md](sdram-routing-constraints.md) | ps/mm/allowed skew/actual route 可回填 |
| 6 | Ethernet Boundary | [ethernet-phy-decision.md](ethernet-phy-decision.md), [ethernet-interface-review.md](ethernet-interface-review.md) | REF_CLK/strap/reset/MDI/magnetics/shield明确 |
| 7 | Floorplan / Rules | [floorplan-plan.md](floorplan-plan.md), [routing-rule-matrix.md](routing-rule-matrix.md), [kicad-rule-plan.md](kicad-rule-plan.md) | placement freeze + rules 可落到 KiCad |
| 8 | Reference / Joint Review | [reference-transition-map.md](reference-transition-map.md), [joint-review.md](joint-review.md) | SI/PI/EMC Major finding 闭环 |
| 9 | Bring-up / Stress | [bringup-test-plan.md](bringup-test-plan.md), [validation-matrix.md](validation-matrix.md) | SDRAM / Ethernet / power 有真实 evidence |
| 10 | Final Release Gate | [release-gate.md](release-gate.md), [final-design-review.md](final-design-review.md) | 六层毕业问题可审计 |

# Gate 1｜现在先做什么

打开 [system-spec.md](system-spec.md) 和 [source-freeze.md](source-freeze.md)。

### 必须先处理的当前 TBD

- firmware operating point；
- 5V/3V3 peak assumption；
- temperature target；
- enclosure；
- ESD target；
- final fab stackup；
- datasheet / RM / errata revision。

### 通过标准

- [ ] exact MCU / SDRAM / PHY 选择明确；
- [ ] system performance baseline 可计算；
- [ ] environment/manufacturing target 不再阻塞后续；
- [ ] 所有 source revision 有记录或明确 reopen trigger。

**Gate 1 没过，不进入 SDRAM timing。**

# 最关键的顺序纪律

V3 禁止这样做：

```text
先布 SDRAM
→ 再找等长规则
→ 再问 datasheet
```

必须这样做：

```text
datasheet timing
→ controller timing
→ board timing budget
→ stackup ps/mm
→ routing constraint
→ actual route
→ stress evidence
```

## 完成以后

→ [Part 9｜工程交付与量产化](../../../19_Part9_工程交付与量产化/00_本Part导读.md)
