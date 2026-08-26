# 07｜KiCad 9 六层 Stackup 与规则落地：让软件表达你的工程决策

> KiCad 不会替你决定哪层该做 GND、哪条线该参考谁。正确顺序是：**工程决策 → Physical Stackup → Layer Role → Net Class / Custom Rules → Layout → Review。**

---

# 1. 先设置 Physical Stackup

在 KiCad 9：

`Board Setup → Board Stackup / Physical Stackup`

根据实际版本界面录入：

- copper layer count = 6；
- layer name / function；
- copper thickness；
- dielectric material；
- dielectric thickness；
- dielectric constant（按板厂/材料数据）；
- solder mask（如果阻抗模型需要）；
- finished board thickness。

不要先布完再补 stackup。

---

# 2. Layer 名称要表达角色

避免只保留：

`In1.Cu / In2.Cu / In3.Cu / In4.Cu`

在工程文档里给它们角色：

- `L2_GND_REF`
- `L3_SIG_MEM`
- `L4_PWR`
- `L5_GND_REF`

KiCad 内部层名受软件规则约束，但你的 layer-role-map 必须能让 reviewer 一眼看懂。

---

# 3. Net Class：定义“默认怎么走”

KiCad 官方文档说明 Net Class 可设置：

- clearance；
- track width；
- via size；
- differential pair width/gap 等。

但要特别记住：

> **Net Class 的 track width / via size 是默认/optimal routing 值，并不天然成为硬性 min/max DRC。**

手工改成别的宽度，未必自动报错。

因此：

- Net Class 用来组织规则与交互路由默认值；
- 真正需要“违反就报错”的限制，使用 Custom Rules。

官方文档：
https://docs.kicad.org/9.0/zh/pcbnew/pcbnew.html

---

# 4. 六层项目建议的 Net Group

示例，不是固定参数：

- `P0_CLOCK`
- `MEMORY_DATA`
- `MEMORY_CTRL`
- `ETHERNET_DIGITAL`
- `USB_DIFF`
- `POWER_HIGH_CURRENT`
- `ANALOG_SENSITIVE`
- `DEBUG`
- `GENERAL_IO`

规则表先写来源：

| Class | Width | Clearance | Via | Diff gap | Layer restriction | Source |
|---|---:|---:|---|---:|---|---|
| USB_DIFF | TBD | TBD | TBD | TBD | L1 preferred | USB/ST + board stackup |
| MEMORY_CLK | TBD | TBD | TBD | TBD | L1/L3 | MCU + SDRAM + SI budget |

所有 `TBD` 在 Source Freeze 前必须被关闭。

---

# 5. Custom Rules：让“设计意图”变成 DRC

适合的规则包括：

- 某 net 只允许特定 layer；
- 某 clock 最小 clearance；
- differential pair gap；
- target length / skew；
- 某区域禁止 via；
- BGA/connector 区局部 neck-down；
- 特定 net 的 via 类型或尺寸。

官方文档提供了 target length / skew、layer、clearance 等规则示例。

注意：

- 规则越多不代表越专业；
- 每条 rule 都应对应一个物理/制造原因；
- 不要把临时 workaround 写成永久规则而不记录。

---

# 6. Rule Area / Keepout 的价值

六层板建议主动建立：

- crystal quiet zone；
- switching regulator hot-loop exclusion；
- connector protection zone；
- SDRAM escape corridor；
- reference split no-cross zone；
- antenna / chassis / mounting keepout（如适用）。

这些区域表达的是**空间结构约束**，比在 Review 时靠肉眼记忆可靠。

---

# 7. Layer Transition Review 不能完全自动化

DRC 很擅长检查：

- clearance；
- connectivity；
- 规则长度；
- skew；
- allowed layer；

但它通常不会自动告诉你：

> “这根线从参考 L2 GND 换到参考 L4 PWR，而附近没有合适 reference-transfer path。”

因此 Part 6 仍保留人工 `reference-transition-map.md`。

自动化与人工 Review 的边界本身就是工程能力。

---

# 8. KiCad 检查流程

建议每次重大 routing milestone：

1. refill zones；
2. run DRC；
3. isolate critical net group；
4. hide signal layers，只看 reference plane；
5. 检查 split / void / antipad corridor；
6. 显示 signal + reference 两层；
7. 逐个 layer transition 看 return path；
8. 更新 Review 记录。

---

# 9. 本章任务

创建 V3 的 `kicad-rule-plan.md`（Part 7 可继续扩展）：

- Net classes；
- Custom rule candidates；
- Rule areas；
- Layer restrictions；
- 仍需人工 Review 的项目。

---

## 本章一句话

> **EDA 规则的任务是保存并执行设计意图，不是替你产生设计意图。**