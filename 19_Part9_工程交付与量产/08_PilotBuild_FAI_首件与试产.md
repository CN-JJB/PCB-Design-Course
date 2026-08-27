# 08｜Pilot Build / FAI：量产前先验证“生产系统”

> Pilot Build 的对象不是只验证 PCB。它验证的是：设计资料 + 供应链 + 工艺 + 程序 + 测试 + 操作员这一整套系统。

---

# 1. Prototype ≠ Pilot

Prototype 关注：

> 设计能不能工作？

Pilot 关注：

> 同一套资料和工艺能不能重复做出一批一致的产品？

---

# 2. Pilot Build 前冻结

- release manifest；
- fab data；
- BOM/AVL；
- assembly data；
- programming image；
- test software；
- fixture；
- work instruction；
- inspection criteria；
- defect code。

---

# 3. FAI — First Article Inspection

FAI 要检查：

- board revision；
- critical dimensions；
- component identity；
- polarity；
- orientation；
- solder quality；
- programming；
- current；
- functional test；
- labels/serial；
- special process。

FAI 数量不是全行业固定 5/10 片。

由：

- risk；
- process maturity；
- volume；
- supplier；
- customer quality plan

决定。

---

# 4. 首件不是“第一块能亮”

第一块能开机只说明：

> 至少一个样本没有被所有错误同时击中。

FAI 还必须对照：

- drawing；
- BOM；
- assembly drawing；
- test limits；
- source revision。

---

# 5. Pilot Run 要记录过程

至少记录：

- build quantity；
- starts；
- complete；
- rework；
- scrap；
- first-pass yield；
- final yield；
- defect count；
- defect category；
- station；
- lot/date code。

---

# 6. FPY

First Pass Yield：

~~~text
FPY = 第一次通过测试的数量 / 投入测试数量
~~~

例如：

- 100 boards；
- 86 first-pass pass；

FPY = 86%。

最终修好 98 块并不意味着工艺良率是 98%。

---

# 7. Rework 也必须统计

如果：

- 30% 板子都要补焊 U3；
- 最终 100% 都修好；

这不是“100% yield”。

它是明确的 process/design signal。

---

# 8. FAI / Pilot Decision

结束后只允许：

- RELEASE；
- CONDITIONAL RELEASE；
- RE-PILOT；
- DESIGN CHANGE；
- PROCESS CHANGE。

不要用：

> “问题不大，先做一千块看看。”

---

# 9. 本章产出

填写：

- pilot-build-report.md
- yield-log.csv

并把所有 defect 使用统一 defect code。

---

# Review

- [ ] build config唯一
- [ ] FAI criteria已冻结
- [ ] FPY与final yield分开
- [ ] rework独立统计
- [ ] defect code统一
- [ ] open issue有owner
- [ ] pilot decision有批准
