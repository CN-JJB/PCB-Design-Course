# 12｜EMC 预兼容测试体系：把“整改运气”变成可重复实验

> 近场探头只是工具之一。预兼容的核心是**建立可重复 baseline、单变量 A/B、频谱归因和证据链**。

## 12.1 先冻结测试配置

每次测试记录：

```text
PCB revision
firmware revision
clock tree
workload
power source
cable type/length
enclosure / shield state
instrument
probe / antenna / current clamp
RBW / VBW / detector
distance / orientation
date
```

没有这些信息，两个频谱图很难比较。

## 12.2 Source Inventory

列出所有可能源：

- oscillator；
- MCU / FPGA clock；
- memory clock；
- RMII / RGMII / USB；
- DC/DC switching；
- GPIO edge；
- SerDes reference clock。

然后建立“fundamental / harmonics / modulation / beat”假设。

## 12.3 四类低成本实验

### Source A/B

- slew / drive strength；
- clock frequency；
- regulator mode；
- workload。

### Path A/B

- cable；
- stitching / temporary bond；
- source resistor；
- filter / CMC。

### Antenna A/B

- cable orientation；
- enclosure；
- shield connection。

### Immunity A/B

- interface active / idle；
- firmware recovery；
- reset reason logging。

## 12.4 工具分层

### Level 1

- oscilloscope；
- DIY / commercial near-field probe；
- known-good cables；
- simple spectrum view。

### Level 2

- spectrum analyzer / receiver；
- current probe；
- LISN / CDN according to test need；
- TEM/GTEM or controlled fixture。

### Level 3

- calibrated pre-compliance / compliance setup；
- accredited lab。

## 12.5 Near Field 不能直接判合规

近场热点非常适合：

- 定位 source；
- 比较 layout A/B；
- 验证整改趋势。

但它不能单独证明远场 emission limit 已通过。

## 12.6 Evidence Log

| Test ID | Hypothesis | Change | Before | After | Interpretation | Confidence |
|---|---|---|---|---|---|---|

每个整改只能改变尽可能少的变量。

## 12.7 进入正式实验室前的 Gate

- [ ] 主要频谱峰有 source hypothesis；
- [ ] cable-dependent peak 已识别；
- [ ] 每个外部接口画过 ESD/common-mode current path；
- [ ] 至少完成一组 source/path A/B；
- [ ] Major EMC finding 有 mitigation；
- [ ] 测试配置与 firmware 可复现。
