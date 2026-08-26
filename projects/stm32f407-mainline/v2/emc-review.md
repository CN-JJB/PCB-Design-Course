# STM32F407 V2｜EMC Review

## 0. Review 范围

本 Review 不是“预测认证必过”，而是设计期发现高概率结构风险。

---

## 1. Noise Source Review

- [ ] HSE / SYSCLK / SDIO / fast GPIO 已列入 source inventory
- [ ] switching regulator（如有）高 dv/dt / di/dt 节点已标出
- [ ] 不需要的高速 GPIO slew 已考虑降低

## 2. Return / Reference Review

- [ ] critical signal 下方 reference 连续
- [ ] 无高速线跨 reference slot
- [ ] layer transition 有合理 return transition
- [ ] plane neck / split / via field 未明显阻断回流

## 3. Common-Mode Conversion Review

- [ ] USB pair 在 connector/protection zone 保持几何对称
- [ ] CANH/CANL protection/filter 路径对称
- [ ] 外部接口附近没有明显不对称 reference discontinuity
- [ ] shield/system boundary 有明确结构

## 4. ESD / Immunity Review

- [ ] 所有用户可触达导体已列入 entry inventory
- [ ] TVS 拦截 topology 正确
- [ ] discharge path 低电感、不过敏感核心区
- [ ] protection device capacitance / working voltage / rating 已按接口核对
- [ ] NRST / user inputs 等敏感节点有 immunity 策略

## 5. Shield / Chassis Review

- [ ] USB shield net 有明确含义
- [ ] chassis/system coupling 不是随手复制 reference design
- [ ] 若无真实 chassis，不制造“假 chassis ground”概念
- [ ] connector shell / mounting tabs 的 net assignment 明确

## 6. Board Structure Review

- [ ] board-edge copper/via 结构有用途说明
- [ ] noisy source 不因布局方便紧贴 connector/cable launch
- [ ] slot / aperture / narrow neck 已检查
- [ ] antenna/isolation keepout 未被 stitching via 破坏

## 7. Pre-compliance Review

- [ ] clock/switching inventory 完成
- [ ] near-field scan 区域定义
- [ ] USB cable A/B test 定义
- [ ] CAN cable A/B test 定义
- [ ] 至少一个 source-control A/B 实验
- [ ] 至少一个 return-path A/B 实验

---

# Finding Template

```text
ID:
Area:
Severity: Blocker / Major / Minor / Observation
Symptom / risk:
Source:
Coupling path:
Antenna / victim:
Return path:
Proposed PCB change:
Possible side effect:
Verification:
Source / requirement:
```

---

# Sign-off

通过 Part 4 Review 的标准：

- Blocker = 0
- Major 都有明确修复或验证计划
- 外部接口都有 ESD + CM path 图
- 不使用“多打地孔 / 加磁珠”作为无解释的整改结论
- 所有关键整改可通过 A/B 实验验证