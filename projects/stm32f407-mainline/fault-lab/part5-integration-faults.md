# Part 5 Fault Lab｜四层综合板：模块都对，为什么整板还是会翻车？

> Part 5 故障不再是单一 SI/PI/EMC 题，而是“集成错误”。每题都要求你画 signal / return / power / transient path，并设计一个单变量验证实验。

---

## Fault 1｜USB 走线很好，但 USB-C 放在 MCU 对角线另一端

**错误：** 为了外观对称，把 connector 放到最远板边。

**后果：** pair 变长、穿多个功能区、ESD/route placement 被动。

**问题：** 这是 routing 问题还是 placement 问题？

**修复：** 回到 floorplan，而不是用更多 via/蛇形补救。

---

## Fault 2｜CC1 处理了，CC2 忘了

Type-C 可翻转。

**症状：** 插头某一方向工作，翻转后不工作。

**训练点：** connector system ≠ 传统单方向 USB connector。

---

## Fault 3｜CAN transceiver 支持 CAN FD，于是产品写“支持 CAN FD”

**错误：** 忽略 STM32F407 内部 controller 是 classic CAN 2.0B。

**训练点：** system capability 由最弱/实际实现链路决定，不由某一颗器件营销标题决定。

---

## Fault 4｜CAN 120 Ω 永久焊死

**症状：** 本板放在总线中间时等效终端过多，波形/幅度恶化。

**训练点：** termination 是 topology property，不是 board identity。

---

## Fault 5｜CAN TVS 在 connector 边，但 CMC/termination 绕线让 H/L 严重不对称

**后果：** common-mode conversion 增加，EMC 可能反而变差。

**训练点：** protection BOM 与 signal geometry 必须一起 Review。

---

## Fault 6｜SDIO_CLK 最短，但 series resistor 放在 microSD 端

**错误：** source termination 位置逻辑错误。

**症状：** 源端 launch 仍可能产生 reflection/ringing。

**训练点：** 先识别 source，再决定 termination topology。

---

## Fault 7｜SDIO 六根线全部精确等长，但用了大量紧密蛇形

**后果：** routing 更长、self-coupling/neighbor coupling 增加、CLK 被迫绕路。

**训练点：** timing budget 优先于“数字看起来整齐”。

---

## Fault 8｜SDIO 读卡正常，连续写卡偶发 corruption，第一反应改线

**可能根因：** ES0182 hardware flow control / clock mode / underrun limitation、firmware/DMA、power transient、SI。

**训练点：** silicon errata 必须进入诊断树。

---

## Fault 9｜microSD local cap 在 socket 旁，但 3V3 通过一条长窄 neck 供电

**症状：** 写卡时 3V3 droop，USB/MCU 可能受扰。

**训练点：** local C 不能替代 upstream distribution impedance。

---

## Fault 10｜USB ESD 离接口很近，但 TVS GND 经细长线跨板回地

**症状：** ESD 残压高、system ground 被注入更深。

**训练点：** “距离”不等于完整 low-inductance discharge path。

---

## Fault 11｜为了方便测 USB，拉出 25 mm DP/DM test stub

**后果：** impedance discontinuity / reflection / asymmetry。

**训练点：** testability 也必须服从 SI。

---

## Fault 12｜L2 GND 为救一根 GPIO 被切出长 slot

**后果：** USB/SDIO return detour；EMC 风险增加。

**训练点：** 一根低价值 GPIO 不应该破坏全板 reference infrastructure。

---

## Fault 13｜AP2112/类似 LDO 电流没超额定，但板子持续写 SD 时很烫

**根因：** `(VIN-VOUT)×I` thermal loss，而不是纯电流 rating。

**训练点：** rated current ≠ thermal capability。

---

## Fault 14｜所有单接口测试都 PASS，USB+CAN+SD 同时运行时 USB reset

可能链路：

- 3V3 transient；
- shared ground impedance；
- DMA/resource interaction；
- crosstalk/common-mode；
- thermal。

**训练点：** 综合压力测试是独立验证阶段。

---

## Fault 15｜DRC PASS，于是直接下单

遗漏：

- CC role；
- CAN termination topology；
- SDIO errata；
- regulator thermal；
- protection path；
- footprint mechanical；
- Gerber output。

**训练点：** DRC 只覆盖规则数据库能表达的那部分世界。

---

## Fault 16｜Gerber 改过线宽，KiCad source 没同步

**症状：** 下一版从旧 source 重新输出，改动丢失。

**训练点：** source-of-truth / release traceability。

---

## Fault 17｜USB cable 插上后 SWD header 无法插下载器

**训练点：** electrical PASS 但 mechanical/testability FAIL。

---

## Fault 18｜一次 EMC 整改同时装 CMC、换 TVS、加 8 个地孔、改 source R

**结果：** 峰值下降，但不知道哪个改动有效，也不知道副作用来源。

**训练点：** single-variable experiment + evidence log。

---

# 每题统一作业模板

```text
Symptom:
Which domain first appears relevant:
Signal path:
Return path:
Power path:
Transient/common-mode path:
Why DRC may miss it:
Hypotheses ranked:
Single-variable experiment:
Evidence:
Root cause:
KiCad fix:
Regression test:
New checklist item:
```

完成 18 题以后，你会发现：真正的工程能力不是“记住 18 个答案”，而是学会同一套诊断流程。