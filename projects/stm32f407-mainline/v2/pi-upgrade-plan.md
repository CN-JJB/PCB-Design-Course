# STM32F407 V2｜Power Integrity Upgrade Plan

## 目标

把 V1 的“电源能工作”升级成 V2 的“电源设计可解释、可 Review、可测量”。

---

## A. 器件级要求

### STM32F407

- VDD：按 ST AN4488，package bulk + 每 VDD pin 本地 100 nF；
- VDDA：按 ST AN4488 的 100 nF + 1 µF；
- VCAP1/VCAP2：严格按器件内部 regulator 要求；
- VBAT/VREF：按实际使用模式和 ST 文档处理。

### 3V3 regulator

- input capacitor：按 regulator datasheet；
- output capacitor：按 regulator datasheet；
- 检查 output-cap ESR / total C 稳定性要求；
- 做 DC current + thermal budget，而不是只看额定电流数字。

---

## B. Layout 升级

- 每颗关键 local decoupler 建立“所属 VDD pin / pin group”关系；
- 审查 VDD 去程 + VSS 回流完整 loop；
- GND via 靠近 capacitor ground pad；
- 避免多个 decoupler 共享长窄 neck；
- L2 保持完整 GND；
- L3 3V3 避免 bottleneck；
- power split 与 Bottom 关键网络联合 Review；
- 增加 TP3V3 / TPVDDA 与邻近 GND test access。

---

## C. BOM 升级

对大容量 Class 2 MLCC 记录：

- exact manufacturer part number；
- package；
- dielectric；
- voltage rating；
- nominal C；
- effective C @ operating rail；
- source/model link。

不再只写 `10uF 0603`。

---

## D. PDN 教学预算

V2 不做高端 SoC 级完整 PIA，但建立：

- 3V3 nominal；
- allowed transient disturbance（教学/系统设计值）；
- estimated transient ΔI；
- teaching Ztarget；
- 关注频率范围；
- 明确“估算”与“芯片厂商要求”的区别。

---

## E. Measurement

### 必测

- 3V3 startup；
- 3V3 local ripple / droop under workload；
- VDDA noise（如果模拟功能启用）。

### 方法

- low-inductance ground spring / short loop；
- 记录 BW limit；
- 记录 AC/DC coupling；
- 记录 probe point + ground point；
- 同一测点比较不同 probe ground 方式。

---

## F. Buck 专项训练

V2 主 rail 不强行换未经验证的 Buck。

Fault Lab 独立加入一个 switching-converter block，训练：

- input capacitor placement；
- high di/dt loop；
- SW node area；
- feedback routing；
- low-inductance measurement。

---

## G. Exit Criteria

- [ ] MCU decoupling inventory complete
- [ ] VCAP / VDDA official requirements checked
- [ ] all critical loops manually reviewed
- [ ] major MLCC DC-bias checked
- [ ] 3V3 distribution no obvious narrow bottleneck
- [ ] PI test points added
- [ ] PI measurement plan written
- [ ] Part 3 Fault Lab ≥ 4 faults analyzed
- [ ] PI Review has no unexplained “rule of thumb” numbers
