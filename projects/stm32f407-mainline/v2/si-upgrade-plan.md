# STM32F407 V2 — Signal Integrity Upgrade Plan

> V2 不是“重新画一块更复杂的板”，而是把 V1 中关键互连升级为**可解释、可审查、可测量**的 SI 设计。

---

## 目标

完成 Part 2 后，V2 至少具备：

- USB FS device path；
- 至少 3 根经过 transmission-line screening 的单端快速网络；
- source termination 预留；
- 关键网络 reference-plane map；
- layer-transition return-path review；
- crosstalk parallel-run review；
- SI measurement points；
- 独立 SI Design Review。

---

## Upgrade 1 — USB FS

### 必做

- 使用 STM32F407 embedded FS PHY；
- 明确 USB mode 为 Full-Speed device；
- connector / ESD / VBUS sensing 原理图按当前 ST 文档核对；
- ESD 放在 connector 侧；
- DP/DM 使用统一 differential geometry；
- DP/DM 不跨 plane split；
- VBUS 不与 DP/DM 长距离贴近；
- pair transition 保持对称。

### 资料

ST AN4879：
https://www.st.com/resource/en/application_note/an4879-usb-hardware-design-guidelines-for-stm32-microcontrollers-stmicroelectronics.pdf

---

## Upgrade 2 — Source Termination Reserve

优先评估：

- `SDIO_CK`
- `SPI_SCK`
- 任何向板外 connector 输出的快速 clock/data

要求：

- resistor footprint 靠 source；
- default DNP / 0 Ω / 实际值必须在 BOM Notes 里有状态；
- 不写“统一 33 Ω”；
- 未来用测量/IBIS/仿真选择。

---

## Upgrade 3 — Reference Plane Review

为每个关键 net/group 记录：

```text
Layer
Reference plane
Plane continuity
Layer transitions
Return transition
Risk / action
```

V2 默认快速线优先 L1 / L2-GND 环境。

---

## Upgrade 4 — Crosstalk Review

检查：

- clocks/high-slew outputs；
- reset/interrupt 等 sensitive victims；
- 长平行段；
- TX/RX 长并行；
- 与 HSE、SW node 的距离。

禁止用“全板 3W”替代风险分析。

---

## Upgrade 5 — Measurement Access

至少规划：

- SPI/SDIO clock source-side probe point；
- receiver-side 可探测位置；
- USB 不额外增加长 stub test point；
- ground spring 可接的近地位置。

---

## V2 交付物

- `si-net-inventory.md`
- `si-routing-constraints.md`
- `si-review.md`
- Fault Lab before/after
- KiCad 工程（待可验证环境中提交）
- Gerber review snapshot
- Bring-up / measurement notes

---

## 通过条件

不是“DRC = 0”。

而是：

> 给任意一条 critical net，都能说清 source、load、edge/protocol、Z0 requirement、reference、return path、termination、spacing 和测量方法。