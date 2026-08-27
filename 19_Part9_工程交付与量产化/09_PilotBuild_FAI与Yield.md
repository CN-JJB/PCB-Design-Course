# 09｜Pilot Build、FAI 与 Yield：小批量不是“多做几块样板”

## 9.1 Pilot Build 的目的

验证的不只是电路：

- fabrication repeatability；
- assembly；
- programming；
- fixture；
- test limits；
- work instruction；
- supply chain；
- rework；
- packaging。

## 9.2 First Article Inspection

首件检查应覆盖：

- mechanical；
- component identity；
- orientation；
- solder；
- key dimensions；
- programming；
- basic electrical；
- critical interfaces。

## 9.3 Yield

至少区分：

```text
fabrication yield
assembly yield
first-pass test yield
retest pass
rework pass
final yield
```

只看“最后都修好了”会掩盖生产问题。

## 9.4 Defect Pareto

每个失败分类：

- solder short/open；
- wrong/missing component；
- orientation；
- programming；
- fixture/contact；
- component failure；
- design margin；
- process variation；
- documentation error。

做 Pareto 后优先处理高频且可消除的原因。

## 9.5 Test Limit Guardband

Production limit 不应等于 datasheet absolute max/min。

要考虑：

- measurement uncertainty；
- fixture variation；
- process variation；
- functional margin。

## 9.6 Stop-the-Line Criteria

提前定义什么情况下停止继续生产：

- safety risk；
- destructive failure；
- repeated critical defect；
- wrong BOM；
- wrong revision；
- systematic test failure。

## 9.7 Pilot Exit Gate

- [ ] FAI passed；
- [ ] first-pass yield 有记录；
- [ ] top defects 有 owner；
- [ ] fixture false-fail 已评估；
- [ ] work instruction 已更新；
- [ ] ECO 已关闭或明确接受；
- [ ] production release inputs 完整。
