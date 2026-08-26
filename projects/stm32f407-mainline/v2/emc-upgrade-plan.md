# STM32F407 V2｜EMC Upgrade Plan

## 目标

把 V2 从“功能可用 + SI/PI 可解释”升级为：

> **对外接口有明确电磁边界、ESD 路径可解释、共模风险可测试、正式认证前有预兼容计划。**

---

## Workstream A｜USB

- [ ] D+/D- protection package 对称
- [ ] TVS topology 为 connector-side protection
- [ ] TVS discharge path 低电感
- [ ] VBUS route 与 data pair 耦合审查
- [ ] USB shield net/connection strategy 明确
- [ ] optional CMC / bypass 策略有测量依据

## Workstream B｜CAN

- [ ] CANH/CANL transient protection
- [ ] TVS / optional CMC footprint 可替换
- [ ] termination topology 与项目网络一致
- [ ] connector-side transient path 不穿 MCU core area
- [ ] shield/reference strategy 明确

## Workstream C｜Board-level EMI

- [ ] HSE / SDIO / fast GPIO source inventory
- [ ] reference-plane overlay review
- [ ] board-edge / slot / connector coupling review
- [ ] via fence 只在有明确结构用途时使用
- [ ] noisy/sensitive region separation

## Workstream D｜Immunity

- [ ] 所有用户可触达 connector / button / header 做 ESD entry inventory
- [ ] NRST 等敏感节点检查外部耦合
- [ ] protection current path 有图
- [ ] firmware reset / watchdog behavior 作为系统抗扰一部分记录

## Workstream E｜Pre-compliance

- [ ] clock/switching inventory
- [ ] near-field scan plan
- [ ] USB cable A/B experiment
- [ ] CAN cable A/B experiment
- [ ] clamp ferrite diagnostic experiment
- [ ] source resistor A/B
- [ ] return-path A/B

---

## 完成标准

V2 EMC 阶段不是“预计肯定过认证”。

完成标准是：

1. 每个外部接口有 electromagnetic boundary review；
2. 每个 protection device 有完整 current path；
3. 所有 major EMC finding 有验证方法；
4. 预兼容实验能够区分 source / coupling / cable effects；
5. 正式认证前知道需要核对哪个标准和测试等级。