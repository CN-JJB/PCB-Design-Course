# STM32H7 Mainline

主线 V3 从 STM32F407 V2 的四层综合板升级到 **STM32H743ZIT6 / LQFP144 六层系统板**。

Part 6 只冻结层数、stackup、reference、power-domain 与 transition architecture；Part 7 才进入 SDRAM / Ethernet / 完整原理图和 PCB 实施。

目录：

- `v3/layer-count-decision.md`
- `v3/stackup-decision-record.md`
- `v3/layer-role-map.md`
- `v3/reference-transition-map.md`
- `v3/kicad-rule-plan.md`
- `v3/part6-transition-review.md`
- `fault-lab/part6-stackup-faults.md`

原则：**所有关键决策必须可追溯到器件、接口、板厂或系统目标，不允许只写“经验上这样更好”。**