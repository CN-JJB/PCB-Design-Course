# Hardware CI

本仓库使用 KiCad 官方 Docker image `kicad/kicad:10.0.5` 作为当前稳定 CI 基线。

## 当前自动检查

当真实 `.kicad_sch` / `.kicad_pcb` 被提交后：

- schematic ERC；
- PCB DRC；
- schematic parity；
- CI report archive。

如果当前没有 CAD，workflow 会明确输出“no CAD source”，而不是制造假 PASS。

## 下一步：Jobset Release

每个项目加入 `release.kicad_jobset` 后，再把 CI 扩展为：

```text
ERC
→ DRC
→ jobset
→ Gerber / drill
→ position / BOM
→ IPC-D-356
→ STEP
→ manifest/hash
```

## 人工 Gate 仍然存在

CI 不能证明：

- return path 正确；
- SI / PI / EMC 合格；
- footprint mechanical 正确；
- fabrication note 正确；
- 实板已经验证。

因此 CI PASS 只是 Release Gate 的一个输入。
