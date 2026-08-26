# STM32F407 V2｜Power Integrity Design Review

## Review metadata

- Revision:
- Reviewer:
- Date:
- Stackup:
- Regulator:
- PCB screenshot/commit:

---

## 1. Power Tree

- [ ] 所有 rail 有明确 source
- [ ] 所有主要 consumer 已列出
- [ ] 平均电流有估算/测量来源
- [ ] 瞬态假设与平均电流分开记录
- [ ] regulator headroom / dropout 已核对
- [ ] regulator thermal budget 已核对

### Findings

| Severity | Finding | Evidence | Action |
|---|---|---|---|
|  |  |  |  |

---

## 2. STM32F407 Official Decoupling

- [ ] VDD package bulk 满足 ST AN4488
- [ ] 每个 VDD pin 的 100 nF 已映射
- [ ] VDDA 100 nF + 1 µF 已满足
- [ ] VCAP1/2 电容值/ESR/连接符合 ST 文档
- [ ] VBAT/VREF 按实际模式处理

> 这里的值属于器件厂商 requirement，不是经验规则。

---

## 3. Local Loop Review

至少选 5 个关键电容，逐个画：

```text
Cap+ → VDD pin → internal load → VSS pin → GND → Cap-
```

| Cap | Load pin/group | Power path | Ground path | Mounting risk | Fix |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

- [ ] 无“电容很近但 GND 绕远”的假近布局
- [ ] 无多个 local decoupler 不必要共享长窄 neck
- [ ] GND vias 与 local capacitors 几何合理

---

## 4. Capacitor Reality Check

- [ ] 所有大容量 Class 2 MLCC 有具体料号
- [ ] 记录 voltage rating
- [ ] 记录 dielectric
- [ ] 检查 operating-voltage 下 effective capacitance
- [ ] regulator 输出电容稳定性要求已核对
- [ ] 没有无来源的“十倍值电容农场”

---

## 5. PDN Budget

- [ ] 3V3 allowed ΔV 有来源/假设
- [ ] transient ΔI 有来源/假设
- [ ] teaching Ztarget 已计算
- [ ] 明确这不是 STM32F407 官方频域 sign-off target
- [ ] 未来 H7/FPGA 需要升级到更正式 PIA 的风险已记录

---

## 6. Planes / Distribution

### L2 GND

- [ ] 连续完整
- [ ] MCU VSS 不通过长串联 top trace 才落地
- [ ] decoupling GND 没有共享窄瓶颈

### L3 Power

- [ ] 3V3 无明显 narrow neck
- [ ] split 边界清楚
- [ ] Bottom 关键网络没有无意跨 split
- [ ] local load 与 source 之间没有被 keepout/via wall 严重掐窄

---

## 7. Ground Bounce / SSN

- [ ] 多个 VSS 连接方式已审
- [ ] 并行 IO 大量同时切换场景已记录
- [ ] 不把 `V=L·di/dt` 的教学例子当器件实测值
- [ ] 若有异常 threshold/jitter/noise，有测量计划区分 SI/PI 原因

---

## 8. Switching Converter Fault Lab

若当前正式 V2 不使用 Buck，本节对 Fault Lab 评分：

- [ ] 已识别 input switching-current loop
- [ ] CIN placement 正确
- [ ] CIN ground return 正确
- [ ] SW copper 不无意义扩大
- [ ] FB/quiet analog 远离 SW/inductor noisy region
- [ ] 对照具体器件 recommended layout

---

## 9. Measurement Integrity

- [ ] TP3V3 + nearby GND
- [ ] TPVDDA + nearby GND
- [ ] 记录 probe type
- [ ] 记录 BW limit
- [ ] 记录 AC/DC coupling
- [ ] 记录 probe point 和 ground point
- [ ] 至少一次 long-ground vs ground-spring 对比
- [ ] SW-node measurement（如有）使用低电感探测与足够带宽

---

## 10. Fault Lab Results

| Fault | Root cause | Why DRC misses it | Measurement | Fix | Checklist added? |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## 11. Exit Gate

### Blocker

- [ ] 无违反 ST VCAP/decoupling requirement 的项
- [ ] 无明显 regulator mandatory-cap violation
- [ ] 无关键 rail 断颈/孤岛
- [ ] 测量方案不会依赖长探头地线做最终判定

### Should Fix

- [ ] 关键 MLCC DC-bias 未核对
- [ ] power testability 不足
- [ ] local loop 可明显缩短
- [ ] 无来源经验值仍存在

### Open Risks

1.
2.
3.

---

## Review 结论

- [ ] PASS
- [ ] PASS WITH ACTIONS
- [ ] REWORK REQUIRED

理由：
