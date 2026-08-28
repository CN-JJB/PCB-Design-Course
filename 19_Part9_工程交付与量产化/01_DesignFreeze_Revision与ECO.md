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

### 1.3.1 Physical Product Identity：手里这块板必须能回答“我是谁”

Revision 不能只存在于 Git tag、Gerber 文件名或工厂聊天记录里。

对进入 Pilot / Production 的 PCB，至少定义可见或机器可读的 physical identity，例如：

~~~text
Product / PCB Part Number
Hardware Revision
Variant / Assembly Option（按需要）
Lot / Serial / Date Code（按产品追溯策略）
~~~

视频建议把 part number / project name 与 revision 放在 PCB silkscreen 上，这个方向很适合教学，但课程不规定必须使用某一种字符串格式。

真正要求是：

> **拿到一块裸板或 PCBA 时，能够把它唯一映射回受控 release configuration。**

因此必须 cross-check：

~~~text
PCB marking
↔ PCB source revision
↔ fabrication package
↔ BOM revision
↔ placement file
↔ assembly variant
↔ firmware/test compatibility
↔ release manifest
~~~

如果空间、外观、保密或自动化需求不适合长 silkscreen，可采用受控的短码、2D code、label 或 enclosure label；但映射关系必须进入 release record。

### Physical Identity Gate

- [ ] board identity 不依赖“看布局猜版本”
- [ ] 标记内容与 release manifest 一致
- [ ] ECO 后 identity/revision 不会静默复用
- [ ] 旧库存/返修板能区分适用 revision
- [ ] 工厂不会仅凭“最新文件夹”决定生产版本

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
