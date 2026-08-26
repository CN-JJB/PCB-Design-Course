# 10｜Bring-up 与验证计划：第一次上电不要“一把梭”

> 好的 Bring-up 不是把 USB、CAN、SDIO 全插上然后祈祷，而是按风险分层，把失败范围逐步缩小。

---

# 10.1 上电前检查

不通电先做：

- PCB revision 与 release package 一致；
- MCU orientation；
- regulator orientation；
- USB-C / microSD / CAN connector solder quality；
- shorts / solder bridges；
- 5V ↔ GND resistance；
- 3V3 ↔ GND resistance；
- VCAP node 是否符合预期；
- DNP / optional parts 是否按 bring-up config 装配。

---

# 10.2 第一次供电：限流

推荐使用可调电源或受控 USB power source。

流程：

1. 不插 SD card；
2. 不接 CAN bus；
3. 不接其他外部 cable；
4. 电流限制设置为合理保护值；
5. 上电；
6. 观察 input current；
7. 测 5V / 3V3 / VCAP；
8. 检查 regulator / MCU 是否异常升温。

异常立即断电。

---

# 10.3 Power Rail 验证

记录：

| Rail | No-load-ish | MCU active | USB active | SD write | Limit |
|---|---:|---:|---:|---:|---:|
| 5V | | | | | |
| 3V3 | | | | | |
| VCAP | only per device requirement | | | | |

还要记录：

- ripple measurement setup；
- probe type；
- ground spring；
- bandwidth setting；
- test point。

Part 3 的“测量完整性”必须真的执行。

---

# 10.4 SWD 是第一条数字生命线

在测试 USB/CAN/SDIO 前：

- SWD connect；
- read device ID；
- erase/program；
- reset；
- halt/run；
- option bytes / boot config 确认；
- UART debug 如果有，先输出最简单 heartbeat。

如果 SWD 都不稳定，不要继续调高级接口。

---

# 10.5 Clock Bring-up

逐步确认：

1. HSI boot；
2. HSE startup；
3. PLL lock；
4. system clock；
5. 48 MHz domain；
6. USB clock；
7. SDIO clock target。

示波器测 HSE 时注意：

- probe capacitance 会影响 oscillator；
- 不要直接用巨大 ground loop；
- 优先使用适合的 active/passive probe 方法；
- 必要时通过 MCO 输出间接验证时钟。

---

# 10.6 USB Bring-up

按顺序：

### Stage 1

- VBUS present；
- CC attach behavior 正常；
- device 上电。

### Stage 2

- 最小 USB device firmware；
- host 能识别；
- descriptor 正确；
- repeated plug/unplug。

### Stage 3

- 长时间枚举；
- data transfer；
- suspend/resume if required；
- 不同 host/cable A-B test。

### Stage 4

如果失败，再测：

- DP/DM waveform；
- pair symmetry；
- VBUS droop；
- ESD part loading；
- connector solder；
- clock accuracy。

不要第一步就拿示波器猜所有问题。

---

# 10.7 CAN Bring-up

先用最简单的两节点环境：

```text
V2 ↔ known-good CAN adapter/node
```

确认：

- termination topology；
- CANH/CANL idle levels；
- dominant/recessive；
- bitrate；
- error counters；
- TX/RX logic；
- long-run frames。

然后再逐步：

- 更长 cable；
- multi-node；
- endpoint / non-endpoint config；
- ESD/EMC pretest。

---

# 10.8 microSD / SDIO Bring-up

必须结合 ES0182。

建议：

1. low clock initialization；
2. 1-bit mode basic read；
3. 4-bit mode；
4. filesystem read；
5. write；
6. continuous read/write stress；
7. different card vendors/capacities；
8. temperature / supply margin if product requires。

Firmware constraints 里明确：

- hardware flow control 不按普通路径启用；
- NEGEDGE 避免；
- BYPASS / clock relationship 对照当前 errata；
- DMA / bandwidth stress 实测。

如果写卡失败，不要立即认为是 PCB SI；先区分：

- silicon errata/config；
- filesystem/software；
- power transient；
- signal waveform；
- connector/contact。

---

# 10.9 联合压力测试

单接口都工作以后，才做：

```text
USB transfer
+ CAN traffic
+ SD continuous write
+ CPU load
```

这是为了暴露：

- 3V3 transient；
- shared ground noise；
- DMA/resource interaction；
- thermal rise；
- crosstalk/common-mode；
- regulator margin。

很多综合板问题只在多模块同时活动时出现。

---

# 10.10 EMC / ESD 预兼容验证

至少做可重复 baseline：

- near-field scan；
- USB cable A/B；
- CAN cable A/B；
- ferrite/CMC population A/B；
- source-series resistor A/B；
- operating-mode comparison；
- ESD gun test only if lab/safety conditions and procedure allow。

正式 IEC/FCC/CISPR 测试仍然要去合适实验室。

---

# 10.11 Bug Log 模板

```text
ID:
Board revision:
Firmware revision:
Symptom:
Reproduction rate:
Operating mode:
Measurement setup:
Evidence:
Hypothesis:
Single-variable experiment:
Result:
Root cause:
Fix:
Regression test:
```

不要用：

> “偶尔 USB 不行，重启就好了。”

作为工程记录。

---

# 10.12 Bring-up 的 stop conditions

遇到以下情况立即停：

- 3V3 明显过压/欠压；
- regulator/MCU 异常过热；
- VCAP 不符合器件要求；
- current draw 远超 budget；
- USB VBUS 出现危险反灌；
- CAN connector 保护器件异常发热；
- SD card socket/rail 短路。

不要为了“看看能不能跑”继续通电。

---

# 10.13 本章交付

创建：

- `projects/stm32f407-mainline/v2/bringup-test-plan.md`
- `projects/stm32f407-mainline/v2/validation-matrix.md`

验证矩阵至少包含：

| Feature | Basic | Stress | SI | PI | EMC | Pass criteria | Evidence |
|---|---|---|---|---|---|---|---|
| Power | | | | | | | |
| SWD | | | | | | | |
| USB | | | | | | | |
| CAN | | | | | | | |
| SDIO | | | | | | | |

---

## 本章任务

写出“USB 不枚举”的诊断树，至少覆盖：

- power；
- clock；
- firmware；
- CC/connector；
- DP/DM；
- ESD device；
- solder；
- host/cable。

并规定每一步用什么证据排除。