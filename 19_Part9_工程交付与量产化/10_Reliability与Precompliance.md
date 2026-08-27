# 10｜Reliability 与 Pre-compliance：一次上电成功不代表产品会稳定工作

## 10.1 Reliability 从使用场景开始

先定义：

- temperature；
- humidity；
- vibration/shock；
- power cycles；
- connector cycles；
- ESD/EFT/surge exposure；
- duty cycle；
- expected lifetime。

没有 mission profile，就没有“可靠性够不够”的统一答案。

## 10.2 HALT/HASS 与常规验证要区分

不同产品会使用不同加速或筛选方法。本课程只要求建立：

> **应力 → 失效机制 → 测试 → 判据 → 证据**

而不是背某套固定温度/小时数。

## 10.3 Thermal

记录：

- ambient；
- workload；
- enclosure；
- airflow；
- hotspot；
- junction estimate；
- component rating；
- margin。

## 10.4 Power Cycling / Connector

典型问题：

- inrush；
- brownout；
- hot-plug；
- connector wear；
- ground-first / ground-last；
- latch-up / reset；
- flash corruption。

## 10.4.1 Protection Validation：从“器件存在”升级成“故障可恢复”

量产 release 前，保护器件不能只在 BOM 里“存在”。

至少形成：

| Threat | Trigger | Expected protection | Safe state | Recovery | Evidence |
|---|---|---|---|---|---|
| overload | controlled current fault | fuse/eFuse/current limit | no thermal damage | defined | test log |
| hot-plug | repeated plug-in | inrush control | source remains stable | automatic | scope |
| brownout | rail ramp/droop | reset/BOR/supervisor | outputs safe | reboot | log |
| firmware lockup | forced hang | watchdog | outputs safe | reboot | log |
| external ESD | pre-compliance | TVS/current steering | no permanent damage | defined criterion | report |

保护验证的毕业标准不是：

> “故障后还能重新上电。”

而是：

> **fault detection、safe state、recovery 和 evidence 都被定义。**

基础架构见：[Part 1｜09 产品级保护电路](../11_Part1_STM32F407四层板/09_产品级保护电路_从接口到SafeState.md)。


## 10.4.2 Battery Reliability 需要独立 Mission Profile

Battery-powered product 额外记录：

- ambient / cell temperature；
- charge temperature；
- pulse-current profile；
- depth of discharge；
- charge cycles；
- storage duration / SoC；
- mechanical shock / swelling；
- connector / holder cycles；
- charger fault；
- pack protection event；
- battery replacement event。

验证重点：

~~~text
new battery
aged battery
cold battery
low-SoC battery
worst pulse load
~~~

都必须满足 system rail / BOR / safe-state requirement。

对 lithium product，还要把：

> **transport evidence + safety report + exact MPN traceability**

作为 production release evidence，而不是采购附件。

详见：[Part 1｜10 电池供电产品](../11_Part1_STM32F407四层板/10_电池供电产品_选型安全认证与可维修性.md)。


## 10.5 EMC Pre-compliance

复用 Part 4：

- source inventory；
- cable experiment；
- near-field；
- conducted path；
- ESD/EFT/surge preparation；
- reproducible configuration。

## 10.6 Reliability Finding

每条记录：

```text
stress
symptom
reproduction
root cause
fix
side effect
retest
ECO
```

## 10.7 进入量产前

所有 blocker/major reliability issue 必须：

- close；
- accept with rationale；
- or explicitly gate release。
