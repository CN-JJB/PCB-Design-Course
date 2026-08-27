# 11｜Production Release、Golden Sample 与 Traceability

## 11.1 Production Release 是一组绑定关系

```text
hardware source commit
+ PCB revision
+ BOM revision / variant
+ fabrication package
+ assembly package
+ firmware/bitstream
+ test procedure
+ fixture version
+ work instruction
+ approved risks
```

缺任何关键项都可能造成“同一个版本做出不同产品”。

## 11.2 Golden Sample

Golden sample 不是“挑一块最好看的”。

它应：

- 对应明确 revision；
- 通过完整测试；
- 保存配置；
- 可用于 fixture / visual / functional reference；
- 有保管与失效替换规则。

## 11.3 Traceability Levels

根据产品需求选择：

### Lot-level

能追到一批。

### Unit-level

每台唯一 SN。

### Component-level

关键器件 lot/date code 也追踪。

不是所有产品都需要最高级别，但必须先决定。

## 11.4 Release Manifest

推荐：

```yaml
hardware_revision:
git_commit:
kicad_version:
stackup_id:
bom_revision:
variant:
firmware:
bitstream:
fixture_revision:
test_procedure:
fab_package_hash:
assembly_package_hash:
release_date:
approvers:
```

## 11.5 Rollback / Superseded

旧 release 不删除。

标记：

- active；
- superseded；
- stop-build；
- service-only。

维修现场经常需要知道“老版本到底是什么”。

## 11.6 Final Release Gate

- [ ] 设计冻结；
- [ ] DFM/DFA/DFT；
- [ ] BOM lifecycle；
- [ ] fabrication；
- [ ] assembly；
- [ ] programming；
- [ ] pilot yield；
- [ ] validation；
- [ ] open risks；
- [ ] manifest；
- [ ] golden sample；
- [ ] traceability。
