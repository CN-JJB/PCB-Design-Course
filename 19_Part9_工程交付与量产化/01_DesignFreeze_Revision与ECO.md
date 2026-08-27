# 01｜Design Freeze、Revision 与 ECO：硬件不能只有“最终版”

## 1.1 为什么硬件必须有冻结点

PCB 一旦进入制造，修改成本与软件完全不同。必须把“当前工作区”与“已发布版本”分开。

推荐状态：

```text
DRAFT
→ REVIEW
→ FROZEN
→ RELEASED
→ SUPERSEDED
```

## 1.2 Freeze 的输入

至少冻结：

- exact MPN；
- schematic；
- PCB；
- stackup；
- rules；
- mechanical；
- BOM；
- firmware/bitstream compatibility；
- test plan；
- source documents / errata；
- open risks。

有关键 TBD 的设计只能叫 Draft。

## 1.3 Revision

硬件 revision 应能映射到：

- PCB marking；
- Git commit/tag；
- BOM revision；
- assembly variant；
- firmware compatibility；
- test procedure。

不要只在文件名里写：

```text
final
final2
final_really
```

## 1.4 ECO

Engineering Change Order 至少回答：

| Field | 内容 |
|---|---|
| ECO ID | 唯一编号 |
| Reason | 为什么改 |
| Affected rev | 影响版本 |
| Schematic change | 原理图 |
| PCB change | PCB |
| BOM change | BOM |
| FW/Test impact | 软件/测试 |
| Verification | 如何证明 |
| Rollout | 从哪批开始 |
| Disposition | 旧库存怎么办 |

## 1.5 Change Classification

### Class A｜Document-only

不改变产品电气/制造。

### Class B｜Form/Fit/Function 不变的受控替代

仍需验证 datasheet、footprint、rating 与生产影响。

### Class C｜功能/性能/布局变化

必须 reopen 对应 Design Review 和 validation。

## 1.6 Release 纪律

- Release 由 commit/tag 指向，不由“共享盘里最新文件”定义；
- 已 release 文件不得静默覆盖；
- ECO 后产生新 revision；
- 所有 waiver 进入 release record。

## 1.7 练习

从 V2 / V3 选一个历史修改，写完整 ECO：

```text
symptom
→ root cause
→ change
→ affected artifacts
→ verification
→ revision
```
