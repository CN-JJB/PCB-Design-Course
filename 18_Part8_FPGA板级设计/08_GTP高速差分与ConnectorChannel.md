# 08｜GTP 高速差分：不要把 SerDes 当普通 LVDS

> CSG325 的 XC7A35T 可以引出 GTP。GTP 的意义不是让课程追求超高速，而是训练你区分 **SelectIO differential** 与 **multi-gigabit transceiver channel**。

---

# 1. 两种差分完全不同

## SelectIO LVDS

- 由 HR I/O Bank 提供；
- 受 VCCO / IOSTANDARD；
- 速率与资源由 SelectIO 决定；
- pin 名属于普通 I/O pair。

## GTP

- 专用 transceiver；
- 独立 TX/RX datapath；
- 独立 reference clock；
- 独立 analog supplies；
- 适合多 Gb/s serial channel。

不要把 GTP_TXP/N 配成普通 LVDS IOSTANDARD。

---

# 2. GTP 主要 PCB 对象

- MGTPTXP/N
- MGTPRXP/N
- MGTREFCLKP/N
- MGTAVCC
- MGTAVTT
- MGTVCCAUX
- related GND / calibration

---

# 3. Channel 不只是 100 Ω

高速串行 channel 还要看：

- insertion loss；
- return loss；
- via stub；
- connector；
- AC coupling；
- reference plane；
- differential/common-mode conversion；
- lane-to-lane crosstalk；
- refclk jitter。

所以“100 Ω”只是必要条件之一。

---

# 4. AC Coupling

AC coupling capacitor 放 TX 还是 RX 侧、具体值、是否已经在 module/connector 内，都要按接口协议 / GTP guide / endpoint 设计确定。

不要机械写：

> “所有 GTP 每根线串 100 nF。”

---

# 5. Reference Clock

GTP REFCLK 是专用 differential clock input。

必须：

- 用 dedicated MGTREFCLK pair；
- 控制 channel；
- 记录 source jitter；
- 保持 supply/refclk return 安静。

---

# 6. Via Stub

multi-Gb/s 下 via stub 的影响明显高于 MCU SDRAM/RMII。

如果 channel 必须换层：

- via geometry；
- unused barrel；
- backdrill 是否必要；
- connector launch

都要进入 channel budget。

但课程不写：

> “GTP 必须 backdrill。”

是否需要取决于：

- data rate；
- board thickness；
- stub length；
- channel loss budget；
- simulation/measurement。

---

# 7. Connector

V1 GTP teaching lane 可以预留：

- SMA；
- board-to-board high-speed connector；
- module edge interface

中的一种实验出口。

目标是可以：

- loopback；
- PRBS；
- eye/BER；
- connector A/B。

---

# 8. GTP Power

MGT analog rails 必须单独进入：

- regulator/filter；
- decoupling；
- plane；
- sequencing；
- measurement。

不要把它们并入 noisy 1.0 V digital core 后就结束。

---

# 9. Review

- [ ] GTP balls 确认 bonded
- [ ] TX/RX polarity/map 已核
- [ ] REFCLK dedicated
- [ ] analog rails 独立 Review
- [ ] channel stackup/impedance 有来源
- [ ] connector launch 有模型/资料
- [ ] AC coupling 有协议/guide 来源
- [ ] via stub 风险已量化
- [ ] loopback/BER test plan 已准备


# 增补｜把 GTP 变成真正的 Channel Engineering

## A. Channel Definition

一条 lane 应写成：

```text
FPGA TX package
→ launch via
→ PCB trace
→ AC coupling
→ connector
→ cable/backplane
→ connector
→ PCB
→ RX package
```

每段都要有 model / assumption。

## B. 需要看的不只有 100 Ω

至少建立概念：

- insertion loss；
- return loss；
- mode conversion；
- crosstalk；
- via stub；
- connector discontinuity；
- reference-clock jitter；
- channel loss budget。

具体 limit 必须来自目标 line rate / device guide / protocol，而不是本课程发明。

## C. S-parameter Workflow

```text
connector .sNp
+ PCB/via model
+ cable .sNp
→ channel model
→ inspect IL/RL
→ time-domain / eye tool
→ compare hardware
```

每个 Touchstone 文件记录 vendor、part number、fixture/port definition 与 revision。

## D. Via Stub / Backdrill Gate

只有当 channel analysis 说明 stub 影响不可接受时才引入 backdrill/HDI；同时记录：

- target layer；
- remaining stub；
- drill tolerance；
- fab capability；
- cost。

## E. AC Coupling

记录：

- TX/RX 哪一侧要求；
- device guideline；
- capacitor value / package；
- placement；
- footprint discontinuity；
- receiver common-mode requirement。

## F. Reference Clock

GTP refclk 单独 review：

- exact clock-capable/transceiver pins；
- source standard；
- termination；
- jitter requirement；
- power supply；
- routing；
- measurement。
