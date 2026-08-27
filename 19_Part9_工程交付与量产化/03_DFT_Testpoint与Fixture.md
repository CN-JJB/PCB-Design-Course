# 03｜DFT、Testpoint 与 Fixture：测试能力必须在 PCB 设计时购买

## 3.1 DFT 是什么

Design for Testability 的目标不是“多放测试点”，而是让关键故障能够：

- 被激励；
- 被观察；
- 被定位；
- 被自动判定。

## 3.2 测试分层

### Bring-up Test

工程师调试用，允许示波器/飞线/手工操作。

### Production Test

目标是快、重复、低歧义。

### Diagnostic Test

当 production fail 时帮助定位返修。

三者测试点需求不同。

## 3.3 Testpoint Inventory

对每个测试点记录：

| Net | Purpose | Access | Expected | Instrument | Production? |
|---|---|---|---|---|---|
| 3V3 | rail | pogo/probe | TBD | DMM | yes |
| NRST | reset | probe | digital | scope | maybe |
| SWDIO/TCK | programming | fixture | protocol | programmer | yes |
| UART | log | header/pogo | serial | fixture | maybe |

## 3.4 Pogo Fixture 约束

PCB 阶段就要考虑：

- pad size；
- pitch；
- probe travel；
- board support；
- datum；
- connector height；
- bottom-side component conflict；
- ground / power current；
- programming interface；
- operator ergonomics。

## 3.5 Boundary / Functional Test

并非每块板都需要 ICT。

根据产品量与复杂度选择：

- continuity/basic rail；
- functional test；
- boundary scan/JTAG；
- memory test；
- interface loopback；
- RF/SerDes production test；
- calibration。

## 3.6 Fault Coverage

测试计划写：

```text
fault
→ stimulus
→ observation
→ pass/fail limit
→ diagnostic resolution
```

“LED 会亮”通常不是足够的 production coverage。

## 3.7 Fixture Version

Fixture 自己也是工程产品：

- fixture hardware revision；
- firmware；
- script；
- limits；
- calibration；
- maintenance。

测试失败时必须区分 DUT 与 fixture。
