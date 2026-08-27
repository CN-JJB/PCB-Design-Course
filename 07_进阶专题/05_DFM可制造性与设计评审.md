# 专题五｜DFM / DFA / DFT 与设计评审（已迁移）

> **本专题的旧版经验清单已由 Part 9 取代。**  
> 正式教材入口：**[Part 9｜工程交付与量产化](../19_Part9_工程交付与量产/00_本Part导读.md)**

---

## 为什么迁移

旧稿把一些**特定供应商/特定装配工艺的经验值**写得过于像通用规则，例如：

- 固定元件间距；
- 固定工艺边宽度；
- 固定 fiducial 数量；
- “普通件不要 via-in-pad”；
- 固定 X-ray 策略；
- 固定板厂 minimum 直接变成设计规则。

这些规则离开具体：

> PCB supplier + EMS + package + volume + inspection + reliability target

就可能失效。

---

# 新版对应章节

- [DFM / DFA / DFT 与 IPC 等级](../19_Part9_工程交付与量产/02_DFM_DFA_DFT与IPC等级.md)
- [Assembly Package / 拼板 / Fiducial / 钢网](../19_Part9_工程交付与量产/05_AssemblyPackage_拼板_Fiducial_钢网.md)
- [DFT / ICT / FCT / 测试夹具](../19_Part9_工程交付与量产/07_DFT_测试策略_ICT_FCT与夹具.md)
- [Production Release Gate](../19_Part9_工程交付与量产/13_ProductionReleaseGate与全书毕业.md)

---

# 保留的核心原则

旧专题真正值得保留的核心仍然成立：

> **设计的终点不是 DRC 清零，而是稳定制造、稳定装配、稳定测试。**

但新版不再要求你背一组固定尺寸，而是要求你建立：

```text
Supplier Capability
+ Project Margin
+ Assembly Process
+ Inspection/Test Strategy
+ Product Reliability
= DFX Rules
```

旧版完整内容仍可通过 Git 历史查看；当前课程以 Part 9 为准。
