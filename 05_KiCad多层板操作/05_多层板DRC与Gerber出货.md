# 第五章｜多层板 DRC 与制造输出（更新说明）

> 本章旧版的“Gerber 出货”流程已由主线课程中的 Release Package 方法取代。  
> KiCad 9 当前制造输出与正式交付请优先阅读：
>
> **[Part 9｜制造资料包：Gerber / IPC-2581 / ODB++](../19_Part9_工程交付与量产/04_制造资料包_Gerber_IPC2581_ODB.md)**

---

# 仍然有效的基本工作流

```text
ERC / DRC
→ manual SI / PI / EMC review
→ stackup / impedance freeze
→ generate manufacturing outputs
→ independent CAM/output review
→ release manifest
→ supplier handoff
```

---

# KiCad 9 当前主要制造输出

KiCad 9 PCB Editor 可生成：

- Gerber；
- Excellon / Gerber drill；
- component placement；
- IPC-D-356；
- IPC-2581；
- ODB++。

因此现在不再把：

> “Gerber + 一个 drill 文件”

写成唯一正式交付形式。

---

# 旧版中不再作为通用规则的内容

以下内容必须按项目/板厂重新核对：

- PTH / NPTH 是否合并输出；
- 固定阻抗公差；
- “换层伴飞地孔 100%”；
- 固定板厂 stackup 编号；
- 固定下单价格与周期；
- 固定内层“应该零走线”；
- “X2 默认就能完整表达 stackup”。

这些都不是跨供应商、跨工程的永久规则。

---

# Release 前应该检查什么

## Electrical / PCB

- DRC；
- open exclusions；
- length/skew；
- reference / return；
- stackup / impedance；
- plane split；
- current loop。

## Manufacturing Output

- copper layers；
- outline；
- mask；
- silkscreen；
- drill / slot；
- drill map；
- special fab notes；
- impedance table。

## Assembly

- BOM；
- placement；
- drawing；
- DNP/variant；
- paste/stencil；
- polarity。

## Version

- hardware revision；
- source commit；
- output hash；
- release manifest。

---

# 收板验收

不能通过裸眼断面“数铜层”替代正式质量证据。

根据产品/供应商要求使用：

- supplier inspection report；
- electrical test；
- impedance coupon/report；
- dimension/finish inspection；
- incoming sampling；
- IPC/customer acceptance criteria。

---

当前课程正式规则以 **Part 9** 和实际供应商 Source Freeze 为准。
