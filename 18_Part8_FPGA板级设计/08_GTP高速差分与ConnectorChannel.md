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

# 6.1 Backdrill 不是“高速板必选项”：先算 Stub，再看制造代价

这批资料补上了一个以前很容易讲虚的部分：**residual stub 到底要控制到什么程度，以及它和 HDI 成本是什么关系。**

Sierra 的 backdrill 文章给出的制造目标是 residual stub 尽量 **< 10 mil**，并给出具体 oversize、depth tolerance、copper clearance 等 DFM 项。

但课程不把 `10 mil` 写成所有 SerDes 的硬规则，因为真正约束来自：

~~~text
data rate / spectral content
+ via geometry
+ stub electrical length
+ channel loss budget
+ connector/package
~~~

### 先做三个方案，不要直接选最贵的

| 方案 | 优点 | 代价 / 风险 |
|---|---|---|
| Through via + 选靠近端部的 routing layer | 最便宜 | layer assignment 受限制 |
| Through via + backdrill | 去掉无用 barrel，工艺相对成熟 | 增加工序、残桩公差、keepout |
| Blind / buried / microvia | stub 最容易控制、escape 更灵活 | sequential lamination、yield、成本显著上升 |

### HDI 成本数据怎么用？

本批 6L 制造资料给出了额外 lamination、blind/buried via、VIP 等相对成本案例。它们适合说明：

> **HDI 的成本主要来自额外工艺循环和良率，不是“多打几个小孔”这么简单。**

但这些百分比和美元数字属于特定厂商/数量/时间的报价案例，不能写进课程当永久价格表。

### Review Gate

只有同时满足以下条件，才进入 backdrill / HDI 决策：

- 当前 through-via stub 已进入 channel risk；
- 调整 layer assignment 不能合理解决；
- 仿真/估算表明 transition 是真实瓶颈；
- 板厂明确给出 residual-stub capability；
- 成本/交期进入项目预算。

### 来源

- Sierra Circuits, *What is PCB Back Drilling?*  
  https://www.protoexpress.com/blog/back-drilling-pcb-design-and-manufacturing/
- Highleap, *The True Blind Buried Via PCB Cost Breakdown*  
  https://hilelectronic.com/blind-buried-via-pcb-cost/
- PCBELEC, *What Affects 6 Layer PCB Cost?*  
  https://www.pcbelec.com/blog/pcb-cost-and-budgeting/what-affects-6-layer-pcb-cost-a-complete-pricing-breakdownfor-engineers-and-buyers.html


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

# 7.1 Vendor Loss Budget 案例：为什么“100 Ω 对了”仍然可能完全不能用？

Intel/Altera 的 P-Tile PCB 指南提供了一个很好的 SerDes 教学案例：

高速通道的验收目标不是：

~~~text
Zdiff = 100 Ω
→ PASS
~~~

而是完整 channel budget：

~~~text
package
+ PCB trace loss
+ via / connector loss
+ edge-finger transition
+ reflections / mode conversion
→ insertion-loss / return-loss budget
~~~

资料集记录的 P-Tile Gen4 示例在 8 GHz 给出了明确的 end-to-end / package / PCB loss allocation。**这些数值只属于对应 Intel 器件与规范环境，不能复制给 Artix-7 GTP。**

我们真正要学的是：

> **Vendor 会把“通道能不能工作”写成 loss budget，而不是只写 100 Ω。**

### 🎮 Layer Count 反推题

如果一个接口要求：

- 很低的 insertion loss；
- 很短 residual via stub；
- edge finger / connector 有特定 void；
- 需要 backdrill 或 blind via；

那么“能不能用四层”就不再是审美问题，而是：

~~~text
channel budget
→ transition count
→ via technology
→ reference architecture
→ required layer count
~~~

这也是为什么某些 PCIe/SerDes 设计会自然进入 6L/8L+，不是因为“高速都必须八层”。

### 来源

- Intel/Altera, *P-Tile PCB Design Guidelines*  
  https://www.intel.com/content/www/us/en/docs/programmable/683864/current/p-tile-pcb-design-guidelines.html
- TI SNLA426, *High-Speed PCB Layout for PCIe Gen 5*  
  https://www.ti.com/lit/an/snla426/snla426.pdf


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
