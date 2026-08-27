# 04｜BOM Lifecycle、Alternate 与 AVL：原理图上的“10 kΩ”不是采购对象

## 4.1 BOM 的最小身份

每行至少考虑：

- reference；
- exact MPN；
- manufacturer；
- description；
- package；
- value；
- rating；
- tolerance；
- lifecycle；
- approved alternates；
- DNP/variant；
- source / note。

## 4.2 哪些料不能随便替

高风险通常包括：

- MCU / FPGA；
- PHY；
- memory；
- oscillator / crystal；
- connector；
- protection器件；
- regulator；
- magnetics；
- high-capacitance MLCC；
- precision analog；
- safety-critical parts。

## 4.3 Alternate Qualification

不是“参数差不多”。

建立 equivalence matrix：

| Parameter | Original | Alternate | Requirement | Result |
|---|---|---|---|---|
| footprint | | | exact | |
| pinout | | | exact | |
| voltage/current | | | ≥ req | |
| timing | | | | |
| capacitance/ESR | | | | |
| thermal | | | | |
| qualification | | | | |

## 4.4 AVL / AML

Approved Vendor / Manufacturer List 解决：

> 哪些制造商/料号经过批准。

采购渠道解决：

> 从哪里买。

不要混成一列。

## 4.5 PCN / EOL

建立 lifecycle 流程：

```text
PCN/EOL received
→ affected BOM
→ inventory exposure
→ alternate
→ engineering review
→ sample qualification
→ ECO
```

## 4.6 MLCC 特别提醒

同样写“10 µF 0805 X7R”的不同 MPN，DC bias / ESR / voltage rating 可能显著不同。

高影响电容必须按 exact MPN 管理，而不是只按 value/package。

## 4.7 BOM Risk Register

| MPN | Risk | Why | Alternate | Inventory | Action |
|---|---|---|---|---|---|

Part 5 / 7 / 8 的 BOM review 最终统一进入这一格式。


## 4.8 Battery 不能只作为一行 Generic BOM

如果产品包含 battery，BOM / AVL 至少扩展：

| Field | Why |
|---|---|
| exact cell/pack MPN | certification / transport / replacement |
| manufacturer | traceability |
| chemistry | charger / safety |
| Vmax/Vnom/Vmin | regulator |
| capacity + test condition | runtime |
| max continuous/pulse current | load |
| protection/BMS | fault behavior |
| connector/drawing | mechanical |
| UN 38.3 Test Summary | lithium transport evidence |
| applicable safety report | certification |
| replacement/spare status | lifecycle |

### Alternate Battery Qualification

Battery alternate 绝不能只满足：

> “同样 3.7 V、2000 mAh、尺寸差不多。”

替代电池可能同时改变：

- charge voltage；
- NTC；
- protection threshold；
- max current；
- swelling envelope；
- connector；
- certification report；
- UN 38.3 identity。

因此 battery alternate 应按**新关键器件**重新 qualification。

详见：[Part 1｜10 电池供电产品](../11_Part1_STM32F407四层板/10_电池供电产品_选型安全认证与可维修性.md)。

