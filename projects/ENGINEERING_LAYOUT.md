# projects/ 工程资产结构

教材正文解释“为什么”；`projects/` 保存“这块具体板到底怎么做、依据是什么、如何验证”。

## 标准结构

```text
project/version/
├── hw/       KiCad source / custom rules / jobset
├── docs/     system spec / decisions / constraints / reviews
├── bom/      exact BOM / alternates / lifecycle
├── sim/      IBIS / S-parameter / simulation manifests
├── test/     bring-up / measurement / validation evidence
└── release/  immutable release packages / manifests
```

历史上已经位于 version 根目录的 Markdown 工程文档暂不强制搬迁，避免破坏链接；后续新增文档优先归入上述结构。

## Evidence Rule

- `README` / template 不是测试证据；
- `TBD` 不是冻结参数；
- 仿真截图必须带 model / corner / stackup；
- 示波器截图必须带 probe / bandwidth / test condition；
- release 文件必须绑定 Git commit 与工具版本。
