# STM32F407 V1｜Design Decision Record

> 每个重要选择都记录“为什么”，避免下一版只剩一个无法解释的 PCB 文件。

## D-001｜Why STM32F407VGT6?

**Decision**：STM32F407VGT6 / LQFP100。

**Why**：足够丰富的外围用于后续 USB/CAN/SDIO/Ethernet 教学；LQFP100 让 Part 1 聚焦四层板而不是 BGA fanout。

**Source**：ST product page / datasheet。

## D-002｜Why 4 layers?

**Decision**：V1 使用四层。

**Why**：课程目标是建立连续 reference plane、真实 stackup 与多层工作流；不是因为 F407 “必须”四层才能工作。

## D-003｜Layer assignment

```text
L1 Signal + Components
L2 Solid GND
L3 Power
L4 Secondary Signal + Components
```

**Why**：L1 可直接邻近连续 L2；标准工艺、成本/复杂度适合教学。

**Important limitation**：L4 的相邻参考是 L3 Power，因此不能把 L1/L4 视为完全等价高速层。

## D-004｜Manufacturing stackup case

**Decision**：课程案例采用 JLCPCB `JLC04161H-3313` 公开数据。

**Checked**：2026-08-26。

**Why**：真实板厂公开 stackup，L1-L2 外层介质较薄，便于讲 reference coupling 和阻抗。

**Risk**：厂家参数会变。下单前重新核对。

## D-005｜Why AP2112K-3.3 for teaching V1?

**Decision**：作为 V1 教学 LDO。

**Why**：电路简单、官方 datasheet 明确，适合第一次 power tree。

**Limitation**：不能把 600 mA electrical rating 当 thermal guarantee。V2 外设增加后重新做 architecture/power budget。

## D-006｜Fast-signal layer policy

**Decision**：V1 快边沿/关键网络优先 L1；Bottom 关键线必须逐条 Review L3 reference。

**Why**：来自实际 stackup 的 reference relationship，而不是“Top 永远比 Bottom 好”。

## D-007｜L2 policy

**Decision**：L2 不走普通 signal。

**Why**：完整 GND 是全板共享的 return/reference infrastructure；用它解决一个局部走线问题可能破坏很多网络的参考环境。

## D-008｜No USB/CAN/SDIO in V1

**Decision**：V1 只预留扩展，不实现数据接口。

**Why**：先学四层基本功；V2 用真实接口驱动 SI/EMC 章节。

## D-009｜No fake KiCad deliverable

**Decision**：没有经过 KiCad 打开/DRC 验证前，不把人工拼写的 `.kicad_sch/.kicad_pcb` 标为课程成品。

**Why**：可复现性优先于“文件看起来齐全”。

## D-010｜Review evidence

**Decision**：关键 Checklist 项必须指向 source / rule / screenshot / Gerber / measurement。

**Why**：单纯打勾无法复盘，也无法让别人审计设计。