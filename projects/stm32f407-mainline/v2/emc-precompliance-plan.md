# STM32F407 V2｜EMC Pre-compliance Plan

## 1. 测试目标

不是在实验室外“判定认证通过”，而是：

- 找 source hotspot
- 找 cable/chassis participation
- 比较整改趋势
- 建立正式测试前的 hypothesis list

---

## 2. Baseline Configuration

必须记录：

```text
Board revision:
Firmware revision:
Clock configuration:
Power source:
USB cable:
CAN cable / termination:
Enclosure condition:
Instrument:
Probe:
RBW / VBW:
Date:
```

---

## 3. Frequency Inventory

至少列：

- HSE / clock tree
- SYSCLK / peripheral clocks
- SDIO clock
- USB signaling-related components
- regulator switching frequency（如有）

对每个 source 写可能 harmonic / coupling path。

---

## 4. Near-field Scan Areas

### Area A｜MCU / HSE
目标：clock / return hotspot。

### Area B｜SDIO / fast GPIO region
目标：bus edge / reference discontinuity。

### Area C｜USB connector zone
目标：pair / shield / ESD/common-mode coupling。

### Area D｜CAN connector zone
目标：cable-facing current / protection layout。

### Area E｜power regulator（如有）
目标：hot loop / SW node。

---

## 5. A/B Experiments

### USB cable
1. baseline cable
2. unplug
3. short vs long cable
4. orientation change
5. diagnostic clamp ferrite

### CAN cable
1. baseline harness
2. disconnect cable
3. length/orientation change
4. optional CMC fitted / bypassed

### Source control
- GPIO OSPEEDR / slew configuration A/B
- source resistor fitted / bypassed

### Return control
- selected return via / stitching change
- temporary reference-path modification on prototype if feasible

---

## 6. ESD Preparation

正式 ESD 测试前：

- 标出所有 user-accessible points
- 画 current path
- 确认 protection BOM
- 确认 chassis/shield state
- 准备 firmware logging / reset reason

不要只记录“死机/没死机”，还要记录：

- transient reset
- communication error
- latch-up symptom
- self-recovery
- manual power-cycle need

---

## 7. Experiment Log

```text
Test ID:
Hypothesis:
Modification:
Frequency / symptom:
Before:
After:
Delta:
What changed physically:
Interpretation:
Confidence:
Next test:
```

---

## 8. Exit Criteria

进入正式合规测试前，希望达到：

- 所有主要频谱峰有 source hypothesis
- cable-dependent peak 已知道可能 coupling path
- USB/CAN protection current path 已 review
- prototype 已至少完成 5 个单变量 A/B 实验
- 所有 Major finding 都有 evidence 或 mitigation plan