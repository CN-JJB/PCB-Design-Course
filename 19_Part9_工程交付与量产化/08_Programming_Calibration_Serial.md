# 08｜Programming、Calibration 与 Serial Number：功能软件也是生产资料

## 8.1 Programming Package

生产烧录至少冻结：

- firmware / bitstream binary；
- version；
- hash；
- target hardware revision；
- programmer；
- interface；
- voltage；
- fuse/option-byte policy；
- verification method。

## 8.2 不要只保存 IDE 工程

生产需要的是：

> **可识别、可验证、不可歧义的 build artifact。**

例如：

```text
firmware-v1.4.2.bin
sha256
source commit
toolchain
build configuration
```

## 8.3 FPGA

额外记录：

- bitstream；
- configuration flash image；
- Vivado version；
- XDC / generated IP revision；
- security/key policy（如使用）。

## 8.4 Calibration

如果产品需要校准，明确：

- calibration stimulus；
- equipment；
- reference standard；
- algorithm；
- acceptance；
- calibration data location；
- re-calibration policy。

## 8.5 Serial Number

序列号体系要回答：

- 谁分配；
- 是否唯一；
- 写在哪里；
- 标签如何对应；
- MES/数据库如何记录；
- 返修后是否保留；
- PCB SN / unit SN / firmware ID 如何关联。

## 8.6 Production Log

每台设备至少能追溯：

```text
serial
hardware rev
BOM variant
firmware/bitstream
test station
test result
date
lot
operator/automation ID
```

## 8.7 安全边界

密钥、证书、私有生产凭据不能提交到公开仓库。公开课程只保存流程和占位规范。
