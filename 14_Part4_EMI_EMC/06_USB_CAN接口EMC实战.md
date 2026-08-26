# 06｜USB / CAN 接口 EMC 实战：把 V2 真正改成“对外界有边界”的板

## 1. 为什么选 USB + CAN

它们代表两类不同问题：

- **USB FS**：差分数据 + 屏蔽连接器 + 用户频繁插拔 + ESD
- **CAN**：长电缆 + 工业瞬态 + 共模环境 + 终端/保护

同一套“接口三件套”不能机械复制。

---

# A. USB FS

## 2. USB 的 EMC 边界

按信号流看：

```text
STM32F407 USB PHY
→ D+/D-
→ optional series/CM control
→ ESD protection
→ receptacle
→ cable
```

同时还有：

```text
USB shield
→ chassis / shield strategy
```

以及：

```text
VBUS
→ sensing / power path / protection
```

三条路径不能混成“USB 口四根线”。

---

## 3. USB Layout Review

### Differential path
- pair geometry 保持对称
- protection package 两线寄生接近
- 避免一根线额外打 via / 走 test stub
- reference structure 连续

### ESD
- connector-side transient 优先经过 protection
- TVS discharge path 低电感
- 不把 ESD current 引进 MCU core area

### Shield
- shield connection 有 chassis/enclosure 依据
- shield mechanical tabs 被明确建模，不留悬空的未知铜

### VBUS
- 按 ST AN4879 和具体 USB role 处理 sensing/power
- 避免 VBUS 噪声与 D+/D- 长距离耦合

---

## 4. USB CMC 要不要放

对于 Full-Speed V2，不把 CMC 当默认必装件。

策略：

1. 先把 pair symmetry / return / shield / ESD 做对
2. 如果预兼容测试发现 cable common-mode 风险，再评估 CMC
3. 需要时使用接口适配的低寄生器件，并验证 signal integrity

如果一颗 CMC 能“神奇地”救回很多 dB，反而要追问：

> 原始 common-mode 是在哪里产生的？

---

# B. CAN

## 5. CAN 为什么更关注 immunity

工业 CAN 电缆可能面对：

- ESD
- EFT
- surge
- ground potential difference
- strong common-mode noise

因此 CAN 接口设计要从“通信能跑”升级到“外界瞬态不会直接打进逻辑区”。

---

## 6. CAN Connector Zone

一个可审查的顺序：

```text
connector
→ TVS / transient protection
→ optional common-mode choke
→ termination / split termination（按网络拓扑决定）
→ transceiver
→ MCU logic
```

具体 protection / CMC / termination 顺序要结合器件厂商 reference design；教材不把它固定成所有 CAN 的唯一序列。

---

## 7. CAN CMC 的意义

CMC 可以提高共模阻抗、减少共模噪声进入/离开电缆。

但它会增加：

- cost
- parasitic
- possible saturation / transient behavior considerations
- failure mode complexity

所以 V2 推荐：

> **留可替换 footprint，而不是不加思考永久装上。**

---

## 8. CAN Ground / Shield

CAN 的 shield、signal ground/reference、chassis 取决于线束和整机系统。

如果连接器提供 shield pin：

- 明确它接到哪里
- 不要默认接 MCU GND
- 不要悬空却又在 PCB 上留大片耦合铜

---

## 9. V2 修改任务

在项目目录形成两个 Review 图：

### USB EMC overlay
标出：
- D+/D-
- ESD path
- shield path
- VBUS path
- reference plane

### CAN EMC overlay
标出：
- CANH/CANL
- TVS discharge path
- optional CMC
- termination
- connector/chassis relationship

每个图至少指出一个“DRC 完全看不见”的风险。

---

## 本章 Review

- [ ] USB protection 不破坏 pair symmetry
- [ ] USB shield strategy 明确
- [ ] CAN transient path 在进入逻辑区前被处理
- [ ] CMC 是测量/系统驱动的选项，不是装饰
- [ ] USB 与 CAN 没有共用一份机械 checklist