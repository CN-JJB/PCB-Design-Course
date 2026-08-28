# 06｜Fabrication Package：板厂真正需要的是受控制造定义

## 6.1 最小输出

根据供应商能力，常见 fabrication package 包括：

- copper / mask / silkscreen fabrication data；
- drill；
- board outline；
- fabrication drawing / notes；
- stackup；
- impedance requirement；
- material / finish requirement；
- route / V-score information；
- netlist/verification data（如 IPC-D-356）；
- ODB++ / IPC-2581（如果双方流程支持）。

不要假设所有工厂都使用同一格式组合。

## 6.2 Gerber Review

独立 viewer 检查：

1. board outline；
2. 每层 copper；
3. soldermask；
4. silkscreen；
5. drill；
6. slot；
7. NPTH/PTH；
8. layer alignment。

## 6.3 Stackup Note

至少写：

```text
layer count
overall thickness
copper
material family
controlled impedance structures
target/tolerance
approved fab adjustment policy
coupon/TDR requirement
```

### 6.3.1 Material Identity 与 Substitution Control

“FR-4”不是足够完整的 reliability specification。

按产品需要冻结：

- approved laminate family / exact material；
- Tg；
- Td；
- Z-axis expansion / CTE；
- moisture behavior；
- CAF requirement；
- lead-free reflow compatibility；
- Dk / Df or controlled-impedance relevance；
- copper thickness / construction；
- applicable certification。

**Higher Tg 不是自动更可靠。**

材料选择必须回到具体 failure mechanism。

Fab substitute material 前应满足：

~~~text
property equivalence
→ impedance/process impact review
→ reliability impact review
→ approval / ECO when required
~~~

而不是由工厂在量产时静默换成“差不多的 FR-4”。

## 6.4 Drill Review

区分：

- plated；
- non-plated；
- slot；
- via；
- mechanical hole；
- special via process。

## 6.5 Fabrication Drawing

关键机械信息不要只藏在 CAD：

- dimensions；
- tolerances；
- datum；
- hole notes；
- finish；
- special edge / bevel；
- controlled depth / backdrill（如有）。

## 6.6 Netlist Cross-check

如生产流程支持，使用独立 netlist / electrical verification 数据帮助发现 CAM 处理或文件错误。

## 6.7 Release Gate

- [ ] 从冻结 commit 生成；
- [ ] Jobset / CLI 可重复；
- [ ] Gerber viewer 已人工复核；
- [ ] stackup 与 fab 已确认；
- [ ] drill / slots 已确认；
- [ ] package hash / manifest 已生成。
