# 🎮 STM32F407 V2｜START HERE

> **这是 V2 唯一开工入口。** 前提：V1 已完成，Part 2 / 3 / 4 的 SI / PI / EMC 主体已经学过。

当前状态：**🧩 Engineering Draft**。现有工程文档很丰富，但其中仍有 TBD；本页把它们排成严格顺序。

## 关卡地图

| Gate | 做什么 | 产出 | 通过标准 | 下一关 |
|---|---|---|---|---|
| 1 | Freeze system | [system-spec.md](system-spec.md) + [source-freeze.md](source-freeze.md) | mechanical/power/block scope 无 blocker TBD | Gate 2 |
| 2 | Pin / Clock | [pin-clock-plan.md](pin-clock-plan.md) | USB/CAN/SDIO/SWD pin + clock 冲突清零 | Gate 3 |
| 3 | Schematic | [schematic-integration-review.md](schematic-integration-review.md) | Blocker=0，power/interface defaults明确 | Gate 4 |
| 4 | Placement | [placement-zoning-plan.md](placement-zoning-plan.md) | connector/current loop/sensitive zone冻结 | Gate 5 |
| 5 | Stackup / Rules | [integration-rule-matrix.md](integration-rule-matrix.md) + SI/PI constraints | 所有 critical net 有 source/constraint | Gate 6 |
| 6 | Routing | [routing-execution-plan.md](routing-execution-plan.md) | reference/via/priority review 通过 | Gate 7 |
| 7 | SI / PI / EMC | [integration-review.md](integration-review.md) + 子 Review | Major finding 已关闭或有接受理由 | Gate 8 |
| 8 | DFM / BOM / DFT | [dfm-checklist.md](dfm-checklist.md) + [bom-risk-register.md](bom-risk-register.md) + [testpoint-plan.md](testpoint-plan.md) | 工厂/装配/测试 blocker=0 | Gate 9 |
| 9 | Release | [release-gate.md](release-gate.md) | fab/assembly/BOM/revision 可复现 | Gate 10 |
| 10 | Bring-up | [bringup-test-plan.md](bringup-test-plan.md) + [validation-matrix.md](validation-matrix.md) | USB/CAN/SDIO/power 全部有 evidence | Gate 11 |
| 11 | Final Review | [final-design-review.md](final-design-review.md) | 四层毕业问题全部可用 evidence 回答 | Part 6 |

## Gate 1｜今天真正应该做的第一件事

打开 [system-spec.md](system-spec.md)，把以下 TBD 先解决：

- Board size；
- USB edge；
- CAN edge；
- microSD insertion direction；
- SWD access；
- mounting holes；
- power budget 的 avg / peak / margin。

然后完成 [source-freeze.md](source-freeze.md)。

### Gate 1 通过标准

- [ ] 关键 mechanical 不再 TBD；
- [ ] MCU / USB / CAN / microSD exact architecture明确；
- [ ] 供电能力有数字预算；
- [ ] source revision / query date 可追溯；
- [ ] 任何仍保留的 TBD 都不会阻止 Pin Planning。

**通过以后只做 Gate 2，不要提前布 PCB。**

## 每关规则

打开某一关对应文件时，只做三件事：

1. 把该 Gate 的 `TBD` 变成有来源的 decision；
2. 把 finding 变成 closed / accepted / reopen；
3. 达到该 Gate 的通过标准后，才打开下一关。

## 最终去向

V2 Final Review 通过：

→ [Part 6｜四层到六层](../../../16_Part6_四层到六层/00_本Part导读.md)
