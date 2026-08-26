# STM32F407 V2｜PI Rail Budget

> 这张表故意把未知数写成 `TBD`。工程里最危险的不是不知道，而是把不知道的参数当成默认值。

| Rail | Source | Nominal | Main loads | Avg current | Fast ΔI assumption | Allowed ΔV | Teaching Ztarget | Requirement source |
|---|---|---:|---|---:|---:|---:|---:|---|
| +3V3 | LDO | 3.3 V | STM32 + peripherals | TBD | TBD | TBD | ΔV/ΔI | system estimate |
| VDDA | filtered +3V3 | 3.3 V | ADC/analog | TBD | TBD | device/system | n/a for now | ST AN4488 |
| VCAP1/2 | MCU internal regulator node | device-defined | MCU core node | n/a | n/a | device-defined | do not invent | ST AN4488 / datasheet |
| +5V | external input | 5 V | regulator / interface | TBD | TBD | TBD | optional | system |

---

## 1. +3V3 Budget Procedure

1. 从实际 firmware/peripheral plan 估算平均电流；
2. 用示波器/功耗资料修正 transient assumption；
3. 定义系统允许的 rail disturbance；
4. 计算教学级：

```text
Ztarget ≈ ΔV_allowed / ΔI_transient
```

5. 在 Review 中注明：这不是 ST 官方 F407 频域 sign-off limit；
6. 把测量结果反哺下一版预算。

---

## 2. Regulator Budget

记录：

```text
Input voltage min/max:
Output voltage:
Rated current:
Estimated board current:
Dropout/headroom:
Power dissipation:
θJA / actual copper assumption:
Junction-temperature estimate:
Input capacitor requirement:
Output capacitor requirement:
```

“额定 600 mA”只属于其中一个字段。

---

## 3. Capacitor Inventory

| Ref | Rail | Nominal C | Package | Dielectric | Voltage rating | Effective C @ Vrail | ESR/Model | Role | Source |
|---|---|---:|---|---|---:|---:|---|---|---|
| TBD | 3V3 | 100 nF | TBD | X7R | TBD | TBD | vendor | VDD local | ST + vendor |
| TBD | 3V3 | 4.7–10 µF class | TBD | TBD | TBD | TBD | vendor | package bulk | ST |
| TBD | VDDA | 100 nF | TBD | TBD | TBD | TBD | vendor | analog local | ST |
| TBD | VDDA | 1 µF | TBD | TBD | TBD | TBD | vendor | analog local | ST |
| TBD | VCAP | 2.2 µF class | TBD | ceramic | TBD | TBD | low ESR | internal regulator | ST |

---

## 4. Validation Log

| Test | Location | Load condition | Probe method | BW | Result | Target | Status |
|---|---|---|---|---|---|---|---|
| 3V3 startup | TP3V3 | power-on | short ground | full | TBD | TBD | TBD |
| 3V3 ripple | MCU local | workload | ground spring | 20 MHz + full comparison | TBD | TBD | TBD |
| 3V3 load step | MCU local | workload transition | ground spring | full | TBD | TBD | TBD |
| VDDA noise | TPVDDA | ADC active | ground spring | defined | TBD | TBD | TBD |

---

## 5. Rules

- 器件 requirement 不用教学公式替换；
- 教学 Ztarget 必须标注假设；
- 大容量 MLCC 必查 DC bias；
- 测量结果必须记录探头方法；
- rail budget 是活文档，会随项目升级修订。
