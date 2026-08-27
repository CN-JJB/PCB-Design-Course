# 05｜Clock：不是把 100 MHz 振荡器接到任意 GPIO

> FPGA 时钟 pin、clock region、MMCM/PLL 与普通 GPIO 的关系，比 MCU 外部晶振更“架构化”。

---

# 1. Clock-capable pin

7 Series 有：

- MRCC
- SRCC
- differential clock-capable pins

系统 oscillator / external clock 应优先进入适合的 clock-capable input。

不要先选一个 PCB 最好走的普通 GPIO，再想办法让逻辑“用它当时钟”。

---

# 2. Clock Source Baseline

Artix-7 V1：

- 100 MHz LVCMOS oscillator，system clock；
- optional differential GTP refclk footprint；
- JTAG TCK 作为 debug clock，不是 system clock。

---

# 3. Clock Tree

~~~text
Oscillator
→ clock-capable pin
→ input buffer
→ MMCM / PLL / BUFG
→ clock regions
→ user logic
~~~

PCB 只负责最前面的 physical path，但 pin 选择会影响后面的 clocking architecture。

---

# 4. Bank Voltage

如果 oscillator 输出 3.3 V LVCMOS，而 chosen clock pin 所在 Bank 是 1.8 V：

这是硬件冲突。

所以 clock planning 也必须进入 Bank matrix。

---

# 5. Differential Ref Clock

GTP refclk 是专用 MGT reference clock pins。

不要：

- 拿普通 LVDS clock pin 代替；
- 通过普通 fabric pin 再“转给 GTP”。

专用 refclk 有自己的 pin / supply / routing requirement。

---

# 6. Clock SI

对 system oscillator：

- source/load 明确；
- reference plane 连续；
- 尽量短；
- 少 via/stub；
- series damping footprint 可按 evidence 预留；
- 不靠近 switching regulator SW node。

---

# 7. Clock 与 BGA Escape

BGA fanout 时不能把：

- MRCC/SRCC；
- GTP refclk；
- DDR CK/DQS

当普通 ball 先随便逃出去。

这些资源必须优先定义逃线方向和 layer。

---

# 8. Review

- [ ] system clock 使用合法 clock-capable pin
- [ ] Bank VCCO 与 oscillator level 匹配
- [ ] GTP refclk 用 dedicated MGT pins
- [ ] clock route reference 连续
- [ ] 无不必要 stub
- [ ] clock pin assignment 已进 XDC
- [ ] oscillator phase-noise/jitter target 有来源
- [ ] probe access 不破坏主路径
