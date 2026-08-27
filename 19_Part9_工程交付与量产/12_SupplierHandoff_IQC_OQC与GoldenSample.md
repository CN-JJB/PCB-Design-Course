# 12｜Supplier Handoff、IQC/OQC 与 Golden Sample

> 好的生产交接不是“工程师和工厂关系熟”，而是即使人员更换，资料和判定标准仍然能工作。

---

# 1. Supplier Kickoff

正式量产前和 PCB/EMS 确认：

- release revision；
- fab notes；
- assembly notes；
- quality/acceptance；
- panel；
- programming；
- test；
- packaging；
- traceability；
- change notification；
- NCR/deviation流程。

---

# 2. IQC

Incoming Quality Control 的目标不是把每个器件重新认证。

重点针对风险：

- critical IC；
- connector；
- magnetics；
- custom part；
- PCB；
- high-counterfeit-risk part；
- special lot/date requirement。

可以检查：

- part identity；
- lot/date；
- packaging；
- moisture sensitivity；
- damage；
- CoC/trace docs；
- sample measurement。

---

# 3. Bare PCB Incoming

根据合同/质量等级可检查：

- board revision；
- dimensions；
- finish；
- drill；
- solder mask；
- workmanship；
- impedance report；
- electrical test；
- coupon；
- lot trace。

IPC-A-600 与 IPC-6012 属于不同角色：

- 一个偏 acceptability；
- 一个偏 qualification/performance。

采购文件必须明确采用哪套要求。

---

# 4. PCBA Acceptance

J-STD-001 与 IPC-A-610 也不是同一个用途：

- J-STD-001：焊接材料/过程/要求；
- IPC-A-610：组装后 acceptability。

当前官方版本为 J 修订。

---

# 5. Golden Sample

Golden Sample 可以帮助：

- orientation；
- appearance；
- labeling；
- fixture；
- UI/LED；

但不要让它取代 drawing/spec。

因为 Golden Sample 本身可能：

- 过时；
- 返修过；
- 使用旧 BOM；
- 没有隐藏内部特征。

所以：

> Golden Sample 是辅助参考，不是唯一 source of truth。

---

# 6. OQC

Outgoing Quality Control 可按风险抽检：

- visual；
- label；
- serial；
- functional；
- packaging；
- accessories；
- firmware；
- calibration。

抽样方案应该来自公司/客户质量计划，不在课程里固定某个 AQL 数字。

---

# 7. Supplier Change

供应商不能静默改变：

- PCB material；
- stackup；
- component；
- process；
- alternate；
- test limit。

Change notification 条款应进入采购/质量接口。

---

# 8. Review

- [ ] supplier收到唯一 release package
- [ ] acceptance criteria书面化
- [ ] critical incoming plan
- [ ] bare PCB criteria
- [ ] PCBA criteria
- [ ] golden sample有revision
- [ ] OQC plan有source
- [ ] supplier change notification受控
