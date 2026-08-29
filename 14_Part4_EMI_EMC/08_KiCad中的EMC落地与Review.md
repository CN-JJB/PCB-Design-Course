# 08｜KiCad 中的 EMC 落地与 Review

> KiCad 能检查 clearance、short、某些几何规则，但不会自动告诉你“这根 cable 会不会被驱动成共模天线”。EMC Review 必须把软件规则和人工电流审查结合起来。

---

## 1. 先做 EMC Net / Region Inventory

在 V2 里给网络和区域分类：

### Noise sources
- HSE / clock
- SDIO clock/data
- fast GPIO
- regulator switching node（若有）

### External interfaces
- USB D+/D-/VBUS/shield
- CANH/CANL/shield/reference
- power input
- SWD / user-accessible header

### Sensitive nodes
- NRST
- crystal
- analog reference / ADC input

然后在 Review 文档中记录，而不是只靠脑子记。

---

## 2. Layer Overlay Review

对每个 critical net：

1. 显示该信号层
2. 显示相邻 reference plane
3. 看 projection 下方是否连续
4. 再显示 connector / board edge / chassis copper
5. 标出换层、slot、plane neck、shield transition

这是 KiCad 很适合做、但 DRC 不会替你做完的事情。

---

## 3. Zones / Keepouts 的 EMC 含义

Zone 不是“把空白填满”。

检查：

- GND zone 是否被密集 via / trace 切出 narrow neck
- connector protection 区的 discharge path 是否连续
- shield/chassis copper 是否与 system GND 有非预期 overlap / coupling
- antenna / isolation keepout 是否被错误填铜

---

## 4. Via Review

对 via 不再统一执行“打一圈”。

分类：

### Return-transition vias
服务换层信号回流。

### Shield/chassis stitching vias
服务屏蔽边界和结构高频连接。

### Plane-connect vias
降低某个 GND/current path 的 via inductance。

### Thermal vias
服务散热，不要和 EMC stitching 混为一谈。

Review 时每一类用途不同。

---

## 5. Connector Review Template

每个对外 connector 必须回答：

```text
External conductors:
Signal reference:
Shield/chassis relationship:
ESD entry points:
Protection device:
Protection return path:
Possible common-mode path:
Nearby clock/power noise source:
Optional filter / CMC:
Measurement plan:
```

---

## 6. Custom Rules 能做什么

KiCad custom rules 可以帮助约束：

- 某些网络与 board edge 的 clearance（如果这是项目定义的几何要求）
- noisy/sensitive net separation
- 特定 via / layer usage
- differential geometry

但规则值必须来自项目假设或器件/接口要求。

不要为了“EMC”随意写：

```text
(clock 到 board edge) > 10mm
```

然后把绿勾当作通过认证。

---

## 7. EMC Review 的人工五问

### Q1 Source
最强 `dv/dt` / `di/dt` 在哪里？

### Q2 Return
它的高频回流在哪？

### Q3 Conversion
哪里可能由 differential 转成 common mode？

### Q4 Antenna
哪根 cable / slot / seam / loop 可能高效辐射？

### Q5 Immunity
ESD/EFT 等外部电流从哪里进入、从哪里退出？

---

## 7.1 每一个 EMC 规则都要带 Source Tag

KiCad 里真正危险的不是“没有规则”，而是你设置了一堆**来历不明的规则**。

因此 V2/V3 的 EMC Review 表新增一列：

| Rule | Current value / action | Source tag | Applies to this design? | Evidence |
|---|---|---|---|---|
| USB ESD placement | | device/vendor | | |
| RF keepout | | module vendor | | |
| via-fence pitch | | heuristic / simulation | | |
| AGND/DGND treatment | | device + Ott/TI/ADI | | |
| chassis bond | | system EMC | | |

允许的 source tag：

~~~text
STANDARD
DEVICE
FAB
PHYSICS
HEURISTIC
PRACTITIONER
~~~

如果某条 KiCad rule 只能写：

> “网上都这么画。”

它就还没有资格冻结进项目。


## 8. V2 EMC Review 输出

项目必须提交：

- `emc-interface-inventory.md`
- `emc-review.md`
- `emc-precompliance-plan.md`
- Fault Lab

每个 critical finding 采用：

```text
Finding:
Severity: Blocker / Major / Minor / Observation
Current path:
Evidence:
Proposed change:
How to verify:
Source / requirement:
```

---

## 9. DRC PASS ≠ EMC PASS

下面这些可能全部 DRC PASS：

- USB shield current 穿 MCU 核心区
- TVS 有器件但 discharge path 很长
- CAN cable common-mode 被板内时钟耦合
- signal 跨 reference slot
- CMC footprint 两侧不对称
- chassis copper 只在 DC 上“接通”，RF 上通过长细 neck

所以正式流程必须保留人工 Review。

---

## 本章任务

对 V2 做一次完整 EMC Review：

1. 两个 Source finding
2. 两个 Return finding
3. 两个 Connector/ESD finding
4. 一个 Chassis/Shield finding
5. 一个可用 A/B 实验验证的 finding

---

## 本章通过标准

你能看一块陌生 PCB，不先问“加哪颗磁珠”，而能依次找：

**Source → Return → Conversion → Antenna → Immunity Path → Verification**。