# 07｜V1 Design Review 与 Bring-up：板子回来才是真正考试

> 🎯 **本章目标**：建立第一次上电流程，不用“插 USB 看冒不冒烟”作为调试方法；把每一次异常记录成下一版 PCB 的设计知识。

---

## 1. Bring-up 的原则：一次只验证一个假设

坏流程：

```text
焊完全部器件
→ 直接接 5V
→ 下载完整固件
→ 什么都不工作
→ 不知道从哪查
```

好流程：

```text
机械/焊接检查
→ 不上电测短路
→ 限流上电
→ 验证 3V3
→ 验证 reset
→ 验证 SWD
→ 验证最小程序
→ 验证时钟
→ LED
→ UART
→ 逐个外设
```

每一步只增加一个新的未知量。

---

## 2. 上电前：Visual Inspection

显微镜/放大镜检查：

- MCU pin bridge；
- polarity；
- LDO orientation；
- capacitor tombstone；
- connector pinout；
- missing component；
- solder ball；
- damaged trace/pad。

特别检查：

```text
5V ↔ GND
3V3 ↔ GND
VCAP nodes
```

有没有明显焊桥。

---

## 3. 不上电电阻检查

万用表测：

- 5V to GND；
- 3V3 to GND；
- 必要敏感 rail。

不要简单规定：

> “低于 X Ω 就一定短路。”

因为不同芯片/电容/保护器件在万用表测试下表现不同。

正确方式：

- 与同类正常板/设计预期比较；
- 观察读数是否随电容充电变化；
- 明显接近硬短路时不要直接满电流上电。

---

## 4. 第一次上电：使用可调电源与限流

如果实验条件允许：

1. 不先接昂贵主机；
2. 使用 current-limited bench supply；
3. 从保守 current limit 开始；
4. 观察输入电流；
5. 同时测 3V3 rail。

如果电流立即触发限制：

> 断电，查短路/器件方向/焊接，不要连续“试试看”。

---

## 5. Power Rail Check

按顺序：

```text
5V_IN
→ LDO VIN
→ 3V3_MAIN
→ MCU VDD
→ VDDA
→ VCAP1
→ VCAP2
```

VCAP 是内部 regulator 节点，期望值必须查 STM32 datasheet，而不是当作普通 3V3 输出。

记录：

| Node | Expected | Measured | Result |
|---|---:|---:|---|
| 5V_IN | supply setting | | |
| 3V3_MAIN | regulator target | | |
| VDDA | per schematic | | |
| VCAP1 | datasheet expectation | | |
| VCAP2 | datasheet expectation | | |

---

## 6. Reset Check

测 NRST：

- 上电后是否处于正常高状态；
- 按 reset button 是否正确拉低；
- 松开是否恢复；
- ST-LINK 是否能控制 reset（取决于连接方式）。

如果 SWD 连不上，NRST 是第一批检查对象之一。

---

## 7. SWD：不要一上来怪“芯片坏了”

按层次查：

1. target 3V3 正常；
2. VTREF 正确；
3. GND connected；
4. SWDIO continuity；
5. SWCLK continuity；
6. NRST；
7. BOOT configuration；
8. pinout/orientation；
9. soldering；
10. 最后才怀疑 MCU 本体。

### 第一段程序

只做：

```text
minimal clock configuration
LED toggle
```

不要第一段固件就初始化十个外设。

---

## 8. Clock Bring-up

### Stage A：内部时钟

先用 internal oscillator 让 MCU 稳定运行。

目的：把“MCU 核心/供电/SWD”与“HSE network”分开验证。

### Stage B：HSE

再切换到 external clock source。

如果切换失败：

- crystal part/CL；
- capacitor value；
- solder；
- OSC pin routing；
- firmware clock config；
- probe loading

逐项排查。

注意：直接拿普通长地线探头测晶体节点可能严重加载振荡器。测量方法本身会改变被测系统，仪器章节会专门讲。

---

## 9. UART / LED / Button

依次验证：

### LED

- GPIO direction；
- polarity；
- resistor；
- actual active-high/low。

### Button

- pull state；
- debounce 暂时软件处理；
- input transition。

### UART

- TX/RX 是否交叉正确；
- GND common；
- logic voltage；
- baud/clock config。

UART 是极好的 bring-up 通道，因为它能在 SWD 之外提供第二种观察方式。

---

## 10. Fault Log：错误必须变成资产

每个问题使用固定格式：

```markdown
## Fault F-001
Symptom:
Reproduction:
Measurements:
Hypothesis:
Root cause:
Fix on current board:
PCB fix for next revision:
Checklist item added:
```

例如：

```text
Symptom: SWD intermittent
Root cause: header GND contact / routing issue
Next PCB: revise header + ground access
Checklist: debug connector must include adjacent solid GND return
```

不要只修好后忘记。

---

## 11. V1 Final Design Review

### Architecture

- [ ] Requirements 全部可追踪；
- [ ] 功能没有偷偷 scope creep。

### Power

- [ ] regulator thermal budget；
- [ ] VDD/VDDA/VCAP/VBAT；
- [ ] decoupling current loops；
- [ ] test points。

### Stackup

- [ ] 真实板厂 stackup；
- [ ] L2 solid GND；
- [ ] L4 reference awareness。

### Placement

- [ ] HSE；
- [ ] SWD access；
- [ ] VCAP；
- [ ] local decoupling；
- [ ] connector/mechanical。

### Routing

- [ ] critical nets reference reviewed；
- [ ] no accidental L2 signal routes；
- [ ] Bottom critical routes reviewed against L3；
- [ ] no unexplained stubs。

### Fabrication

- [ ] DRC；
- [ ] Gerber Viewer；
- [ ] drill；
- [ ] board outline；
- [ ] BOM/footprint。

### Bring-up

- [ ] current-limited power-up plan；
- [ ] SWD；
- [ ] internal clock；
- [ ] HSE；
- [ ] UART/LED/button。

---

## 12. Part 1 毕业问题

你应该能不看答案解释：

1. 为什么 V1 关键快速网络优先放 L1？
2. L2 为什么不能因为“差一根线”就拿来走 signal？
3. 为什么 local decoupling 不能只在原理图上检查？
4. 为什么 AP2112 的 600 mA 额定信息不能替代热设计？
5. 为什么 Bottom signal 必须检查 L3 power reference？
6. 为什么 Gerber Viewer 是设计流程的一部分？
7. 为什么第一次固件只做最小 bring-up？

全部能解释，你才真正完成“第一块四层板”的认知闭环。

下一阶段 Part 2 会拿 V1 里的真实网络开始学 **Signal Integrity**：传输线、反射、端接、回流切换、串扰与差分。