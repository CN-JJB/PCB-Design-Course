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
