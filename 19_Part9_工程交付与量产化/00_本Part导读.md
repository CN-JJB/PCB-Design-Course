# Part 9｜工程交付与量产化：把“能工作的样板”变成可重复产品

> Part 0～8 训练设计与验证；Part 9 解决最后一个工程问题：**别人能不能在没有设计者坐在旁边解释的情况下，准确制造、装配、烧录、测试、追溯和维护这块板。**

## 本 Part 的主线

```text
Design Freeze
→ Revision / ECO
→ DFM / DFA
→ DFT / Fixture
→ BOM / AVL / Lifecycle
→ Variants / DNP
→ Fabrication Package
→ Assembly Package
→ Programming / Calibration
→ Pilot Build / FAI / Yield
→ Reliability / Pre-compliance
→ Production Release / Traceability
→ Final Capstone
```

## 本 Part 不会做什么

- 不把“Gerber 发出去了”叫 release；
- 不把“BOM 有料号”叫供应链完成；
- 不把“样板能跑”叫量产验证；
- 不把 DRC 当 DFM/DFA/DFT；
- 不用空白模板冒充真实生产记录。

## 最终交付对象

每个真实项目应逐步形成：

```text
hw/
docs/
bom/
sim/
test/
release/
```

其中 `release/` 下的每个正式版本都应是不可含糊的冻结快照。

## 章节

1. [Design Freeze、Revision 与 ECO](01_DesignFreeze_Revision与ECO.md)
2. [DFM 与 DFA](02_DFM_DFA.md)
3. [DFT、Testpoint 与 Fixture](03_DFT_Testpoint与Fixture.md)
4. [BOM Lifecycle、Alternate 与 AVL](04_BOM_Lifecycle_Alternate_AVL.md)
5. [KiCad 10 Variants、DNP 与产品配置](05_KiCad10_Variants_DNP与产品配置.md)
6. [Fabrication Package](06_FabricationPackage.md)
7. [Assembly Package](07_AssemblyPackage.md)
8. [Programming、Calibration 与 Serial Number](08_Programming_Calibration_Serial.md)
9. [Pilot Build、FAI 与 Yield](09_PilotBuild_FAI与Yield.md)
10. [Reliability 与 Pre-compliance](10_Reliability与Precompliance.md)
11. [Production Release、Golden Sample 与 Traceability](11_ProductionRelease_GoldenSample与Traceability.md)
12. [Final Capstone：完整硬件 Release](12_FinalCapstone.md)

## 毕业标准

你必须能拿一个 commit / release tag 回答：

- 这批板由哪套源文件生成？
- 使用哪个 stackup / fab capability？
- 哪个 BOM variant？
- 哪些 DNP？
- 哪个 firmware / bitstream？
- 如何烧录？
- 如何测试？
- 哪些问题在 ECO 中被修改？
- Pilot build 良率和主要 defect 是什么？
- 哪一份证据支持 production release？

如果这些问题只能靠“问当时画板的人”，工程就还没真正交付。


13. [参考资料与工具基线](13_参考资料与工具基线.md)
