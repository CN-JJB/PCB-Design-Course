# 09｜KiCad 中的 PI 落地与 Design Review

> PI 最终必须变成 PCB 上可检查的对象：器件位置、铜、过孔、平面、测试点和明确的 Review 结论。

---

## 9.1 先建立 PI 设计对象

不要只按“电源网络”分类。

更实用的对象是：

```text
Rail
→ Source
→ Bulk
→ Distribution
→ Local decoupling
→ Load pins
→ Ground return
→ Test point
```

对 STM32F407 V2：

- 5V input；
- 3V3 source；
- 3V3 bulk；
- VDD local decoupling；
- VDDA/VREF；
- VCAP1/2；
- GND return；
- PI test points。

---

## 9.2 KiCad Net Classes：电源不要只靠默认线宽

可以为：

- `PWR_5V`；
- `PWR_3V3`；
- `ANALOG_PWR`；

建立不同 net class。

但线宽不应该拍脑袋。

依据包括：

- 电流；
- 允许压降；
- 铜厚；
- 温升；
- 制造能力；
- 是否最终进入 plane/zone。

对于大面积 zone，net class 仍可用于从器件 pin 到 zone 的局部连接与规则管理。

---

## 9.3 Zones：先画“电流怎么走”，再画形状

在 L3 画 3V3 zone 前先回答：

1. LDO 输出从哪里进入？
2. MCU load 在哪里？
3. 是否有 narrow neck？
4. zone 被 via/keepout/其他 rail 切成什么形状？
5. Bottom 关键高速网络是否会把它当 reference？

不要把 zone 当“自动填满剩余区域”的美化工具。

---

## 9.4 Thermal Relief 不是永远该开或关

Pad 与 plane 连接有：

- thermal relief；
- solid connection。

选择取决于：

- 焊接工艺；
- 电流；
- thermal mass；
- 器件类型；
- 制造/返修需求。

例如大电流 power pad、散热 exposed pad 与普通手焊 connector pad 的最佳策略可能不同。

所以：

> “所有电源 pad 一律 solid” 和 “所有 plane pad 一律 thermal” 都不是好教材规则。

---

## 9.5 Via 策略

PI Review 不只数 via 数量。

检查：

- VDD local path 是否有不必要 via；
- GND via 是否靠近 decoupler ground pad；
- power plane transition 是否形成瓶颈；
- 大电流路径是否需要并联 vias；
- exposed pad thermal vias 是否按器件要求；
- via array 是否反而切坏 reference plane。

---

## 9.6 Custom Rules 能做什么，不能做什么

KiCad 10 Custom Rules 可以针对：

- 特定 net / net class；
- 特定 footprint；
- 特定区域；

应用更细规则。

但它不能自动判断：

> “这颗去耦的真实安装电感是否足够低。”

所以 PI Review 仍需要人工电流路径检查。

### 一个可落地思路

可以用 Custom Rules 强化：

- power-net minimum width；
- 特定 net clearance；
- power via diameter/drill；
- 特定高电流区规则。

具体语法在 KiCad 的 Custom Rules editor 中维护，并随 `.kicad_dru` 一起纳入版本控制。

---

## 9.7 Placement Review：先过这一关再布信号

顺序：

### A. Regulator block

- source；
- required input/output capacitors；
- thermal path；
- quiet feedback（如果是 switcher）。

### B. MCU decoupling

- VDD；
- VCAP；
- VDDA/VREF。

### C. Bulk

- rail transition / connector / load cluster 合理位置。

### D. Testability

- test point + nearby ground。

如果这一步没过，不要进入“开始漂亮地拉高速线”。

---

## 9.8 Routing Review

### 电源去程

- 有无长窄 neck；
- 有无不必要换层；
- 高电流是否共享 bottleneck。

### Ground return

- local decoupling 是否直接进入 GND plane；
- 多个 VSS 是否共享细线；
- regulator ground 是否按 datasheet topology。

### Cross-domain

- analog rail 是否被数字 noisy current 穿越；
- Bottom signal 是否跨 power split；
- Buck SW 是否靠近 sensitive trace。

---

## 9.9 DRC 之后的 Manual PI Review

DRC 通过后必须额外做：

```text
[ ] 每个 VDD pin 找到本地 decoupler
[ ] 每颗关键 decoupler 画完整 loop
[ ] VCAP 完全按 ST requirement
[ ] VDDA/VREF 供电与去耦按官方资料
[ ] 3V3 无明显 narrow neck
[ ] L2 GND 完整
[ ] L3 split 不破坏 Bottom 关键参考
[ ] regulator input/output cap placement 合理
[ ] test point 有低电感 GND access
[ ] 若有 Buck：hot loop / SW / FB 完成专门审查
```

---

## 9.10 Power Tree Review 表

| Rail | Source | Consumers | Avg current | Peak/transient assumption | Caps | Layout status | Measurement |
|---|---|---|---:|---:|---|---|---|
| 3V3 | LDO | MCU + peripherals | TBD | TBD | ST + LDO req. | review | TP3V3 |
| VDDA | filtered 3V3 | analog | TBD | low | 100 nF + 1 µF per ST | review | TPVDDA |
| VCAP | internal | core regulator node | n/a | device | per ST | critical | optional |

关键是把：

> “不知道”

显式写成 `TBD`，而不是默默用默认值。

---

## 9.11 Design Decision Record

任何非显然选择都记录：

```markdown
### DDR-PI-xxx / PWR-xxx
Decision:
Evidence:
Alternative:
Why rejected:
Validation:
```

例：

```text
Decision: 不额外增加 10 nF decade decoupler
Evidence: STM32 官方要求 + 本板低功耗 + 无明确阻抗超标证据
Alternative: 100 nF + 10 nF 混放
Why rejected: 无来源，可能增加 BOM 且不保证改善
Validation: bring-up rail measurement
```

---

## 9.12 Fault Lab 进入 Review

Part 3 故障不只是给答案。

每个 fault 都必须经过：

```text
Symptom
→ current loop sketch
→ parasitic hypothesis
→ measurement plan
→ KiCad fix
→ before/after review
→ checklist update
```

这会训练真正的工程诊断能力。

---

## 9.13 本 Part 的 V2 PI Gate

在进入 Part 4 EMI/EMC 前，V2 至少满足：

### Source

- [ ] 3V3 source 额定值与热预算有依据
- [ ] regulator mandatory capacitors 满足 datasheet

### MCU

- [ ] ST AN4488 VDD decoupling 满足
- [ ] VDDA/VREF 满足
- [ ] VCAP 满足
- [ ] 每颗关键 local decoupler 完成 loop review

### PCB

- [ ] L2 GND 连续
- [ ] 3V3 distribution 无明显 bottleneck
- [ ] power split 完成 signal-reference review
- [ ] 测试点可低电感探测

### Evidence

- [ ] capacitor 具体料号/封装/电压等级记录
- [ ] 大容量 MLCC 检查 DC Bias
- [ ] 关键数字区分官方 requirement 与教学 estimate
- [ ] Bring-up measurement plan 完整

---

## 9.14 本章任务

对你的 V2 输出一份正式：

`PI Review v0.1`

必须包含：

1. power tree；
2. decoupling inventory；
3. 5 个关键 loop 截图；
4. rail budget；
5. capacitor effective-capacitance 记录；
6. L2/L3 plane screenshots；
7. 3 个 Fault Lab 修复；
8. measurement plan；
9. 未解决风险。

---

## 9.15 Part 3 的最终认知

如果你现在看到一颗 MCU 旁边的 100 nF，脑子里应该自动出现：

```text
它服务哪个 pin？
实际 C 还有多少？
ESR/ESL 呢？
安装电感呢？
GND 怎么回？
这条 rail 的其他频段谁负责？
会不会有共振峰？
怎么测？
```

这时你才从“会放去耦电容”跨到了**会做基础 Power Integrity**。
