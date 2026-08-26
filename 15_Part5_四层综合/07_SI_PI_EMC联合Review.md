# 07｜SI + PI + EMC 联合 Review：同一个问题为什么会同时出现在三个清单里

> 真实板子不会把问题标注成“这是 SI”“这是 PI”“这是 EMC”。一个回流中断可能同时造成反射、地弹、共模转换和辐射。Part 5 要学会跨学科 Review，而不是拿三份清单机械打勾。

---

# 7.1 从“网络”升级到“电流路径”

传统 Review 常问：

> 这根 USB 线长度多少？

联合 Review 更应该问：

```text
source 是谁？
→ current 从哪里出去？
→ reference/return 在哪里？
→ 经历哪些 discontinuity？
→ power return 如何闭合？
→ connector/cable 会不会把 differential energy 转成 common mode？
→ 怎么测？
```

---

# 7.2 一个 USB 例子：三种学科其实在看同一件事

## SI 看什么

- D+/D- differential geometry；
- impedance discontinuity；
- skew；
- ESD package parasitic；
- via / stub。

## PI 看什么

- USB PHY / MCU VDD 的 local supply；
- USB activity 时瞬态电流；
- VBUS power-entry；
- regulator / decoupling。

## EMC 看什么

- pair asymmetry；
- connector shield；
- ESD discharge path；
- cable common-mode；
- VBUS/common-mode coupling。

三个视角其实都在追踪**同一个物理系统里的场和电流**。

---

# 7.3 一个 SDIO 例子

## SI

- CLK edge；
- source termination；
- CMD/D0~D3 crosstalk；
- group timing。

## PI

- microSD write transient；
- card local decoupling；
- 3V3 narrow neck；
- shared return impedance。

## EMC

- periodic CLK harmonics；
- connector/slot geometry；
- long card edge currents；
- reference discontinuity → common-mode conversion。

所以如果 SDIO 写卡时 USB 偶发 reset，不要只盯 firmware。

可能链路是：

```text
SD write current spike
→ 3V3 droop / ground disturbance
→ MCU/USB PHY margin reduced
→ USB error/reset
```

也可能：

```text
SDIO_CLK / return geometry poor
→ common-mode / crosstalk
→ USB pair/ground disturbed
```

需要证据区分。

---

# 7.4 CAN 例子

## SI

- bus topology；
- termination；
- stub；
- transceiver edge。

## PI

- transceiver supply decoupling；
- dominant-state current；
- shared 3V3 path。

## EMC

- cable common-mode；
- ESD/EFT/surge；
- CANH/CANL asymmetry；
- CMC/protection parasitic；
- connector boundary。

如果加了一颗 CMC 后 EMC 改善但 waveform 变差，这就是典型的**多目标 trade-off**。

---

# 7.5 联合 Review 的 8 个视图

建议在 KiCad 中固定做八种视图：

## View 1：Top critical routing

隐藏丝印、value，只看：

- USB；
- SDIO；
- clocks；
- CAN bus。

## View 2：L2 GND

看：

- slots；
- antipad chains；
- return continuity；
- connector holes。

## View 3：L3 Power

看：

- 3V3 neck；
- power islands；
- L4 signal reference risk。

## View 4：Power loops

逐颗看：

- VCAP；
- VDD decoupling；
- SD card cap；
- transceiver cap；
- regulator input/output loops。

## View 5：Connector boundaries

- USB-C；
- CAN；
- microSD；
- SWD。

## View 6：Via / transition map

只看关键 net 的 via。

## View 7：Mechanical / assembly

- 插头；
- card；
- probe；
- screw；
- test fixture。

## View 8：Gerber-like final view

隐藏编辑器便利信息，用制造输出视角看最终铜、mask、silk、drill。

---

# 7.6 Severity 统一

不要 SI 一套严重度、PI 一套严重度。

统一：

### Blocker

可能导致：

- 板子不工作；
- 器件损坏；
- 接口无法枚举/通信；
- 电源错误；
- 制造不可行。

### Major

高概率导致：

- margin 很差；
- EMI/ESD 风险；
- intermittent failure；
- thermal/voltage risk；
- 难以调试。

### Minor

- manufacturability / maintainability；
- optimization；
- clarity。

### Note

- documented trade-off；
- future improvement。

---

# 7.7 Review Finding 必须有“验证闭环”

坏 finding：

> USB 走线不好。

好 finding：

```text
ID: V2-SI-USB-004
Severity: Major
Observation: DP/DM 经过 ESD 后出现不对称 jog，DM 额外 via ×1
Risk: differential-to-common-mode conversion + impedance discontinuity
Evidence: layout geometry
Action: move ESD 2.5 mm toward connector, rotate package, remove layer transition
Verification: DRC + pair topology review + USB enumeration + scope if needed
Status: Open
```

这样别人才能真正执行。

---

# 7.8 联合 Review 最容易发现的“跨领域 Bug”

### Bug A：去耦很好，但 GND plane 被 connector antipad 切成细颈

PI：shared impedance ↑  
SI：return detour  
EMC：loop/common-mode ↑

### Bug B：USB ESD 很近，但 TVS GND 经细长 trace 才进 plane

SI：parasitic ↑  
EMC/ESD：clamp residual ↑  
PI：瞬态进入 system ground 更深

### Bug C：SDIO_CLK 很短，但紧贴 microSD power neck

SI：coupling  
PI：dynamic load/ground noise  
EMC：periodic current loop

### Bug D：CAN CMC footprint 很漂亮，但 CANH/CANL 为绕 footprint 强烈不对称

SI：bus asymmetry  
EMC：common-mode conversion

---

# 7.9 Review 不是一次会议

建议至少四个 gate：

```text
Gate A — Schematic freeze
Gate B — Placement freeze
Gate C — Routing ~80%
Gate D — Pre-release / Gerber
```

越晚发现 placement-level 问题，修改成本越高。

---

# 7.10 本章交付

创建：

`projects/stm32f407-mainline/v2/integration-review.md`

至少包含：

- Review date / revision；
- reviewers；
- schematic findings；
- SI findings；
- PI findings；
- EMC findings；
- DFM findings；
- unresolved risk；
- waiver rationale；
- final sign-off。

---

## 本章任务

随机挑 V2 的一个接口，强制写出：

1. signal path；
2. return path；
3. power path；
4. transient path；
5. common-mode path；
6. measurement point；
7. failure symptom。

如果写不出来，说明你还只是“在看走线”，没有在看系统。