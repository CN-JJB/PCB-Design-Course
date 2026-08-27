# 05｜KiCad 10 Variants、DNP 与产品配置：不要复制三个工程文件维护三个版本

## 5.1 Variant 解决什么

同一 PCB 可能有：

- Base；
- Debug；
- Production；
- Optional CAN；
- 不同 connector；
- 不同 BOM cost tier。

如果通过复制工程：

```text
board_A.kicad_sch
board_B_final.kicad_sch
board_prod2.kicad_sch
```

很快就会失去一致性。

## 5.2 Variant 的工程原则

- PCB connectivity 的本质差异不要强行塞进 DNP；
- 仅装配差异适合 variant；
- DNP 必须同步 BOM / placement / assembly drawing；
- variant 不能隐藏电气风险。

## 5.3 Source of Truth

建议：

```text
KiCad project
→ variant definition
→ variant-specific BOM
→ position file
→ assembly output
→ release manifest
```

## 5.4 DNP Review

DNP 器件仍可能通过：

- footprint pad；
- stub；
- parasitic；
- ESD path；
- unpowered input；
- test pad

影响产品。

所以 DNP 不等于“这个器件不存在”。

## 5.5 Jobset

KiCad 10 的 Jobset 用于把一组输出固定成可重复任务。

课程推荐建立：

```text
release.kicad_jobset
```

用于统一输出和 CI。

## 5.6 CLI

自动化时显式记录版本：

```bash
kicad-cli version
kicad-cli jobset run --stop-on-error -f release.kicad_jobset project.kicad_pro
```

具体 CLI 参数以当前 KiCad 官方文档为准。

## 5.7 Release Manifest

每个 variant 保存：

```text
project commit
KiCad version
variant
BOM hash
fab package hash
assembly package hash
firmware/bitstream
date
```

这样“生产版”才不是一句口头描述。
