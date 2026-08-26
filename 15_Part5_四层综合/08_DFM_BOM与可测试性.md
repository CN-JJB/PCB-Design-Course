# 08｜DFM、BOM 与可测试性：能画出来不等于能稳定制造和调试

> 到这一章，电气设计已经基本完成。现在要把“工程样板”变成“别人也能做出来、装出来、测出来”的硬件。

---

# 8.1 DFM 不是最后一分钟跑一次 DRC

DFM（Design for Manufacturability）至少包含：

- PCB fabrication；
- SMT assembly；
- hand assembly / rework；
- inspection；
- test；
- mechanical integration；
- component sourcing。

DRC 只是其中一小部分。

---

# 8.2 PCB Fabrication Review

冻结：

- layer count；
- board thickness；
- copper weight；
- stackup；
- minimum trace/space；
- via drill / finished hole；
- annular ring；
- soldermask expansion；
- impedance control；
- surface finish；
- board outline tolerance。

所有这些参数要来自**实际目标板厂当前 capability**。

不要从去年截图抄参数。

---

# 8.3 Controlled Impedance Release

USB differential geometry 如果要求板厂控阻抗：

交付时至少明确：

```text
Layer: L1
Reference: L2 GND
Target: [current USB requirement]
Trace width: [solver/fab confirmed]
Pair spacing: [solver/fab confirmed]
Copper: [stackup]
Dielectric: [stackup]
Tolerance: [fabricator capability / project requirement]
```

如果板厂会二次调整线宽：

- 需要知道他们是否会回改；
- 最终生产 stackup 是否与 KiCad 记录一致；
- release note 要记录实际值。

---

# 8.4 Via Review

检查：

- drill 是否在标准工艺范围；
- small via 是否不必要地增加成本；
- GND via 是否有足够 annular ring；
- USB/SDIO 不存在多余 via；
- power via 不成为 current bottleneck；
- thermal via 是否会吸锡/需要 tenting。

V2 不需要为了“看起来高级”使用 blind/buried via。

---

# 8.5 Soldermask / Silkscreen

检查：

- USB-C fine pads 的 mask 是否符合 connector footprint；
- microSD connector mechanical pads；
- TVS/CMC pin 1 / orientation；
- LQFP100 pin 1 清楚；
- silkscreen 不压 exposed pad；
- testpoint labels 可读；
- CANH/CANL / polarity 不会标反；
- USB role / power warning 明确。

---

# 8.6 Footprint 不能只相信库

每个关键器件至少人工核对：

- package name；
- body size；
- pitch；
- pin 1；
- exposed pad；
- recommended land pattern；
- connector shell tabs；
- keepout / insertion area；
- 3D mechanical envelope。

高风险对象：

- USB-C connector；
- microSD socket；
- CAN terminal；
- LQFP100；
- ESD arrays；
- CAN transceiver；
- regulator。

---

# 8.7 BOM 不是元件名称列表

一个工程 BOM 至少应该包含：

```text
RefDes
Qty
Value / Function
Manufacturer
MPN
Package
Voltage/current/temp rating
DNP status
Approved alternate
Lifecycle / availability note
Source / datasheet
```

对关键器件还要记录：

- MLCC DC bias；
- TVS capacitance / working voltage；
- CAN transceiver fault/common-mode capability；
- regulator thermal/package；
- USB-C connector cycle rating；
- microSD socket detect mechanism。

---

# 8.8 DNP 是设计的一部分

V2 会有很多“可调”位置：

- USB source-series resistor；
- SDIO_CLK source resistor；
- CAN termination；
- optional CMC；
- shield/chassis option；
- LED/debug options。

每个 DNP 必须说明：

```text
Default population:
When to populate:
Allowed values:
What measurement decides:
Impact if wrongly populated:
```

否则生产只会问：

> “这个到底贴不贴？”

---

# 8.9 Testability：测试点不是越多越好

## 必备 power points

- GND；
- 5V；
- 3V3；
- NRST。

## Bring-up points

- SWDIO；
- SWCLK；
- UART TX/RX；
- CAN TX/RX logic；
- SDIO_CLK；
- optional USB measurement pads（必须控制 stub）。

## Bus points

CANH/CANL 可以在 connector / dedicated test pads 测。

不要为了“方便测”给 USB D+/D- 拉出 30 mm stub。

---

# 8.10 Fixture 思维

如果以后要做 10 块、100 块：

- 测试点最好单面可访问；
- pogo pad pitch 可夹具化；
- 不要全部藏在 connector 下；
- boot/reset 可 fixture 控制；
- firmware programming path 固定；
- serial number / test result 能追踪。

即使 V2 只是教学板，也应该第一次接触这个思维。

---

# 8.11 Assembly Review

问：

- USB-C shell tabs 是否需要手焊/通孔回流；
- microSD socket 是否遮挡 AOI；
- connector 重件是否适合 reflow；
- 小 0402 是否离板边/V-cut 太近；
- polarity/orientation 是否清楚；
- rework iron 能否接触；
- testpoint 是否被高器件挡住。

---

# 8.12 BOM Risk Review

至少标出：

### A 类：不能轻易替代

- MCU；
- USB connector；
- CAN transceiver；
- regulator；
- microSD socket；
- ESD array。

### B 类：参数匹配后可替代

- MLCC；
- resistors；
- LEDs；
- crystals（仍需 CL/ESR/tolerance 验证）。

### C 类：generic

- jumpers；
- some headers。

---

# 8.13 本章交付

创建：

- `projects/stm32f407-mainline/v2/dfm-checklist.md`
- `projects/stm32f407-mainline/v2/bom-risk-register.md`
- `projects/stm32f407-mainline/v2/testpoint-plan.md`

---

## 本章任务

选 5 个关键器件，打开 datasheet 的 recommended land pattern，和 KiCad footprint 一项项核对。

不要只检查 pad 数量，要检查机械 envelope 和插拔空间。