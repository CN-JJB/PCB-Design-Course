# 05｜Assembly Package：PnP、拼板、Fiducial、钢网与装配说明

> PCB fabrication 完成只是裸板。PCBA 量产最常见的昂贵错误往往来自方向、坐标、变体、拼板与装配说明。

---

# 1. Assembly Package

至少包含：

- BOM；
- component placement / CPL；
- assembly drawing；
- paste/stencil data；
- DNP/variant；
- polarity notes；
- special process；
- panel information；
- programming/test handoff。

---

# 2. Placement File 不是“导出就完事”

KiCad placement file 包含：

- RefDes；
- X/Y；
- rotation；
- side。

但生产前仍要核：

- footprint origin；
- rotation convention；
- bottom side transform；
- connector/polarized part orientation；
- DNP handling。

JLCPCB 当前 FAQ 也明确提醒：客户定义的 0° 与工厂定义可能不同，因此 preview/工程确认仍然需要检查。

---

# 3. Assembly Drawing

人类可读图至少要能判断：

- RefDes；
- pin 1；
- polarity；
- connector orientation；
- top/bottom；
- DNP；
- variant；
- board revision。

对于：

- diode；
- LED；
- electrolytic；
- IC；
- connector；
- crystal；
- battery；

不应只依赖机器坐标。

---

# 4. Fiducial

Fiducial 的数量、直径、边缘距离不是跨工厂万能值。

当前 JLCPCB Standard PCBA 指南建议：

- edge rail；
- fiducial copper/mask opening；
- 3–4 个板边基准；
- 对 board edge 有具体 clearance。

这是 JLCPCB 当前工艺要求，不是 IPC 对所有 EMS 的统一数字。

换 EMS 重新确认。

---

# 5. Panelization

选择：

- V-cut；
- route tab / mouse-bite；
- individual board；
- supplier panelization。

取决于：

- board outline；
- connector overhang；
- component edge distance；
- depanelization stress；
- volume；
- assembly line；
- test fixture。

JLCPCB 当前说明 V-cut 只能直线贯穿，并对 panel 尺寸/数量有自身工艺条件。

---

# 6. Depanelization 是可靠性问题

特别关注：

- MLCC 靠近 V-cut；
- BGA/QFN 靠板边；
- connector；
- flexing-sensitive sensor；
- crystal。

错误的掰板会产生：

- MLCC flex crack；
- solder joint stress；
- PCB delamination；
- connector mechanical damage。

所以 panel design 不能只由“怎么省拼板钱”决定。

---

# 7. Stencil / Paste

不要写：

> “QFN 统一 50% 开窗。”

正确流程：

- component vendor land/paste recommendation；
- stencil thickness；
- aperture design；
- area ratio；
- thermal pad void target；
- assembly process capability；
- X-ray / inspection plan。

任何 paste reduction 都应有 package/process context。

---

# 8. Inspection Strategy

不同封装对应不同可见性：

- 0402/0603：AOI；
- QFP：AOI + visual；
- QFN/BTC：底部焊点不可直接视觉确认，按风险决定 X-ray/process validation；
- BGA：通常依 X-ray/process controls/functional evidence。

不是所有项目都必须 100% X-ray。

---

# 9. JLC 当前案例

当前官方装配条款/帮助页可用于训练：

- BOM 结构；
- panel；
- fiducial；
- component edge；
- PnP preview。

但 release note 必须写：

> Supplier-specific requirement, verified on date.

不能把网页数字永久抄进公司规则。

---

# 10. Review

- [ ] BOM与PnP same variant
- [ ] DNP一致
- [ ] polarity drawing可读
- [ ] PnP preview完成
- [ ] panel/depanel stress已审
- [ ] fiducial按EMS要求
- [ ] stencil策略有package/process来源
- [ ] hidden-joint inspection plan明确
