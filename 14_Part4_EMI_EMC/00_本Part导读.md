# Part 4｜EMI / EMC：从“会跑”到“不会到处辐射，也不怕外界干扰”

> 这一 Part 不把 EMC 当玄学，而把它看成 **SI + PI + 结构 + 连接器 + 电缆 + 机壳** 的系统问题。

前面你已经学过：

- Signal Path / Return Path
- Reference Plane
- Reflection / Crosstalk
- PDN / Decoupling / Ground Bounce

现在要回答：

> **为什么板内几毫米的电流路径问题，最后会变成一根 1 米电缆上的共模电流？**

---

## 本 Part 的项目目标

继续升级 `STM32F407 V2`，重点检查：

- USB 接口的 ESD / Shield / Return Path
- CAN 接口的 TVS / CMC 预留 / 终端与共模路径
- 板边与连接器附近的 current path
- 可能把板内噪声转换成 cable common-mode 的结构
- ESD 电流能否在进入数字区前被安全分流
- 预兼容测试如何定位“谁在辐射”

---

## 学习顺序

1. **差模与共模**：先搞清到底是什么电流在辐射
2. **PCB 为什么会变成天线**：loop、slot、wire/cable、common-mode conversion
3. **连接器与电缆**：EMC 的放大器
4. **ESD 与 TVS 布局**：高 di/dt 电流怎么泄放
5. **Shield / Chassis Ground**：什么时候系统地与机壳地不能简单等同
6. **USB / CAN 接口 EMC**：把知识落到 V2
7. **预兼容测试**：近场探头、电缆实验、频谱归因
8. **KiCad EMC Review**：把问题变成可检查的工程流程
9. **混合信号接地、功能分区与屏蔽边界**：什么时候保持 solid GND，什么时候 split 才有证据，以及 shield/chassis 如何接

---

## 本 Part 的一个核心模型

任何 EMC 问题都先画电流：

```text
noise source
   ↓
coupling path
   ↓
antenna structure / victim
   ↓
return path
```

不要先问：

> “要不要加磁珠？”

先问：

> “噪声电流从哪里来？通过什么阻抗耦合？最后在哪个结构上形成了大回路或共模电流？”

---

## 本 Part 不使用的“铁律”

不会再写成：

- TVS 必须离连接器 `<5 mm`
- 板边地孔必须 `≤10 mm`
- 时钟必须离板边多少毫米
- 所有屏蔽壳都必须直接接数字地
- 加共模电感一定更好
- 拔掉电缆后改善就 100% 是共模

这些都只能作为特定条件下的工程经验，不能替代电流路径分析。

---

## 本 Part 交付

完成后你应该能拿到一张 PCB 截图并回答：

1. 主要高速/开关噪声源在哪里？
2. 哪些结构可能形成 differential-mode loop？
3. 哪些接口可能把噪声变成 common-mode cable current？
4. ESD 从连接器打进来时，电流实际走哪条路径？
5. TVS 是不是只是“放了器件”，但泄放回路很差？
6. Shield / chassis / system GND 的关系是什么？
7. 如何用低成本实验判断辐射是否与电缆有关？
8. KiCad DRC 看不到哪些 EMC 风险？

---

## 一手资料基线

本 Part 优先引用：

- ST AN4879：STM32 USB hardware / PCB guidelines
- TI SLVA680A：ESD Protection Layout Guide
- TI SLLA561 / SLA856A：EMC 与差模/共模布局思路
- TI CAN / Ethernet interface EMC design guides
- KiCad 10 官方 PCB Editor 文档

具体标准限值不作为本 Part 的固定“背诵表”，因为认证类别、距离、产品类型和标准版本会改变；真正做认证前必须核对目标产品适用标准。

## 进阶补充

10. [传导 EMI 与电源端口](10_传导EMI与电源端口.md)
11. [ESD、EFT、Surge](11_ESD_EFT_Surge与接口抗扰度.md)
12. [EMC 预兼容测试体系](12_EMC预兼容测试体系.md)
13. [参考资料与数据纪律](13_参考资料与数据纪律.md)


## 本 Part 新增互动实验

- [Mixed Ground & Shield Lab](../interactive/mixed-ground-shield-lab.html)：比较 solid/split ground、区域间距/H、跨区边沿与 360°/pigtail shield termination 的风险趋势。
