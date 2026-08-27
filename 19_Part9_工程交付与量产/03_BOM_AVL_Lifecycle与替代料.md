# 03｜BOM / AVL / Lifecycle：替代料不是“参数差不多”

> PCB 可以完全正确，但量产仍可能因为一个停产 PHY、缺货 Flash 或错误替代 MLCC 停线。

---

# 1. Production BOM 的最小字段

建议至少：

| Field | Meaning |
|---|---|
| RefDes | 位号 |
| Qty | 单板数量 |
| Description | 工程描述 |
| Manufacturer | 原厂 |
| MPN | Manufacturer Part Number |
| Package | 封装 |
| Value | 电气值 |
| DNP | 是否不装 |
| Approved Alternate | 已批准替代 |
| Lifecycle | Active/NRND/EOL 等 |
| Risk | Supply/technical risk |
| Revision | BOM revision |

JLCPCB 当前 BOM 接口也要求 Designator、Footprint、Comment/Description 等，并推荐明确 MPN；但量产 BOM 应比在线贴片最低上传格式更完整。

---

# 2. AVL 是 Approved，不是 Available

AVL = Approved Vendor/Manufacturer List。

不是：

> “这个平台现在有库存。”

替代件必须先证明：

- pin compatible；
- package compatible；
- electrical compatible；
- timing/analog behavior；
- temperature；
- lifecycle；
- qualification；
- firmware dependency；
- manufacturing impact。

---

# 3. MLCC 替代案例

“10 µF 0805 10 V X5R”仍不够。

还要看：

- DC bias effective capacitance；
- ESR/ESL；
- tolerance；
- temperature characteristic；
- height；
- flex termination；
- voltage derating；
- supplier change。

PI 课程已经说明：

> 标称容量相同 ≠ PDN 行为相同。

所以关键去耦/compensation 元件不能做 uncontrolled substitution。

---

# 4. Oscillator / Crystal 替代

要比较：

- frequency；
- load capacitance；
- ESR；
- drive level；
- ppm；
- startup；
- package/ground pad；
- oscillator output standard；
- phase noise/jitter。

“同频率”不等于替代。

---

# 5. Ethernet PHY / Memory / FPGA

这些通常属于高风险替代：

- PHY register behavior / straps；
- SDRAM timing / organization；
- DDR3 pin/package/timing；
- FPGA speed/package；
- configuration Flash command support。

替代可能需要：

> schematic + firmware + timing + validation 一起重开。

---

# 6. Lifecycle Gate

Release 前对 A 类器件检查：

- Active / NRND / EOL；
- PCN/PDN；
- lead time；
- MOQ；
- second source；
- distributor；
- counterfeit risk。

高风险件至少包括：

- MCU/FPGA；
- memory；
- PHY；
- regulator/controller；
- connector；
- oscillator；
- special transformer/magnetics。

---

# 7. DNP / Variant

不要用：

- 删除行；
- 把 Qty 改 0 但无 variant；
- 在工厂邮件里说“C37 不装”。

应该把 variant 作为受控配置。

例如：

~~~text
Variant STD
Variant ETH
Variant DEBUG
~~~

每个 variant 的 BOM / placement / assembly drawing 必须一致。

---

# 8. Alternate Approval

建立替代料表：

| Primary | Alternate | Reason | Electrical Review | PCB/FW Impact | Validation | Approved |
|---|---|---|---|---|---|---|

没有完成 validation 的只能叫：

> Candidate Alternate

不能叫 Approved Alternate。

---

# 9. 本章任务

使用：

**projects/production-release/bom-avl-template.csv**

为三个主线项目分别选 5 个高风险器件，建立：

- lifecycle；
- alternates；
- validation scope。

---

# Review

- [ ] 所有关键 BOM 行有 exact MPN
- [ ] DNP/variant受控
- [ ] 高风险器件 lifecycle核查
- [ ] alternates不是采购员现场决定
- [ ] substitution有影响分析
- [ ] BOM revision进入 release manifest
