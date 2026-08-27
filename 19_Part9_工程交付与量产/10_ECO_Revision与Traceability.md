# 10｜ECO、Revision 与 Traceability：改一颗电阻，也要知道影响谁

---

# 1. ECO 是 Engineering Change Order

任何生产后变更至少回答：

- 为什么改；
- 改什么；
- 影响什么；
- 哪些库存还能用；
- 是否需要返工；
- 是否影响 firmware/test；
- 如何验证；
- 从哪个 serial/lot 生效。

---

# 2. Change 分类

可按公司定义：

- design；
- BOM；
- supplier；
- process；
- firmware；
- test；
- documentation。

不要假设：

> “不改铜，就不用升版本。”

例如换晶振：

PCB 不变，但可能影响：

- startup；
- timing；
- EMC；
- BOM；
- qualification。

---

# 3. Impact Analysis

ECO 影响矩阵：

| Domain | Check |
|---|---|
| Electrical | voltage/timing/SI/PI |
| Mechanical | package/height |
| Firmware | register/driver |
| Manufacturing | stencil/process |
| Test | limit/fixture |
| Regulatory | EMC/safety |
| Supply | stock/AVL |
| Documentation | drawing/BOM/manual |

---

# 4. Traceability Level

不是所有产品都需要 unit-level 全追踪。

可以分：

## Lot-level

知道这批用了：

- PCB lot；
- assembly lot；
- BOM revision；
- firmware。

## Unit-level

每个 serial 对应：

- exact test；
- calibration；
- rework；
- firmware；
- genealogy。

需求取决于产品风险/行业/客户。

---

# 5. IPC-1782

当前 IPC revision table 将：

**IPC-1782B**

列为制造和供应链电子产品 traceability 标准。

课程不复制其具体条款，只用它说明：

> Traceability 应该被当成可设计的系统，而不是出事后临时翻邮件。

---

# 6. PCN / PDN

供应商 PCN/PDN 触发：

- alternate review；
- last-time buy；
- requalification；
- firmware update；
- BOM revision。

不要让采购单独决定：

> “厂家说兼容，直接换。”

---

# 7. Deviation vs ECO

## Deviation

一次性/限定批次偏离。

例如：

- 指定 lot 用临时替代；
- 指定 200 pcs 做返工。

## ECO

永久工程定义发生变化。

两者都要有：

- scope；
- approval；
- expiry/effective date。

---

# 8. ECO Impact Lab

打开：

[ECO Impact Lab](../interactive/eco-impact-lab.html)

选择“换 LDO / 换晶振 / 改 PCB / 换 DDR3”，观察需要重开的 Review/Validation 范围。

---

# 9. Review

- [ ] change reason明确
- [ ] affected inventory处理
- [ ] cross-domain impact
- [ ] validation scope
- [ ] effective serial/lot
- [ ] release docs更新
- [ ] deviation有expiry
- [ ] traceability可查
