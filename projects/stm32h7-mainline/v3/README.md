# STM32H743 V3 Engineering Workspace

> **先点这里： [START_HERE.md](START_HERE.md)**

六层高速综合：SDRAM timing、Ethernet boundary、六层 reference 与验证。

不要从 PROJECT_STATUS 或文件列表猜顺序。START_HERE 已经把工程拆成 Gate，每一关都有：

- 做什么；
- 输入；
- 产出；
- 通过标准；
- 下一关。

## 工程区

- [PROJECT_STATUS.md](PROJECT_STATUS.md) — 整体成熟度，不是开工顺序
- [hw/](hw/) — real KiCad source
- [bom/](bom/) — exact BOM / alternates
- [sim/](sim/) — IBIS / S-parameter / simulation manifests
- [test/](test/) — bring-up / measurement evidence
- [release/](release/) — immutable release packages

> 当前状态仍是 Engineering Draft。可以**直接开始设计流程**，但不能理解成“已经有一块可以直接下单的成品板”。
