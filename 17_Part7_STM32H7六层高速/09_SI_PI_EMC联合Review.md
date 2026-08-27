# 09｜STM32H743 V3：SI / PI / EMC 联合 Design Review

> 到 Part 7，不能再把 SI、PI、EMC 当成三份独立清单。真正的高速板问题往往是同一条电流路径，从三个视角同时暴露。

---

# 1. 联合 Review 的基本单位不是“网络名”

先从能量与电流路径开始：

~~~text
driver → interconnect → receiver/load
→ local return → supply replenishment
→ boundary / cable / environment
~~~

同一个问题可能同时属于 SI、PI、EMC。

---

# 2. SDRAM：三种视角

## SI

检查 SDCLK edge、address/control skew、DQ 双向质量、via/stub、reference transition、source damping 与 meander coupling。

## PI

检查 MCU I/O simultaneous switching、SDRAM VDD/VDDQ local decoupling、VSS/VSSQ return、3V3 distribution neck-down、package/plane inductance。

## EMC

检查 SDCLK loop、并行 bus simultaneous switching、reference discontinuity、bus 与 connector/cable 的距离、clock 到板边的关系。

---

# 3. Ethernet：三个电气世界

## RMII digital side

50 MHz REF_CLK、LVCMOS edge、reference plane、pin direction、crosstalk。

## MDI analog differential side

differential impedance、pair symmetry、magnetics topology、common-mode、PHY analog supply。

## Cable / chassis side

isolation boundary、shield、ESD、cable-side termination、chassis/system return。

只检查“MDI 是 100 Ω”不算完整 Review。

---

# 4. Power：用 current loop 标注图审

至少画出 MCU VDD loop、SDRAM VDDQ loop、PHY analog loop 与 Buck hot loop，再把它们叠加在 floorplan 上。

---

# 5. Reference Plane Overlay

对 SDCLK、DQ、Address/Control、RMII_REF_CLK、RMII data/control、MDI、USB DP/DM 每一段标：

- signal layer
- reference layer
- reference net
- via transition
- local stitching/coupling
- split crossing

如果答案只是“看起来下面是 GND”，Review 不通过。

---

# 6. 串扰和 SSN

串扰同时看 spacing、reference height、parallel length、edge rate、victim sensitivity 与 aggressor count。

多个 I/O 同时翻转时，公共 return/package/via/plane inductance 造成 ground bounce：

V = L · di/dt

这就是 output speed 不能无脑最高的原因之一。

---

# 7. Connector Boundary

USB 与 Ethernet 都连接外部 cable。

必须问：

- common-mode current 从哪里进？
- TVS/magnetics/shield 导向哪里？
- discharge path 是否穿 MCU ground？
- connector zone 是否侵入 SDRAM timing zone？
- chassis coupling 是否有真实结构？

---

# 8. Severity

## Blocker

不修不能 release，例如 SDCLK 跨 reference split、FMC/RMII pin collision、VCAP 错接、REF_CLK direction 错、MDI topology 错。

## Major

first-spin 前强烈建议修，例如 SDRAM via forest、PHY supply 穿 SW node 区。

## Minor

可接受但必须记录风险。

---

# 9. 本章产出

填写 projects/stm32h7-mainline/v3/joint-review.md：

| Issue | Domain | Current path | Evidence | Severity | Fix | Validation |
|---|---|---|---|---|---|---|

通过条件：

- [ ] SDRAM timing 有 ns→cycle→PCB budget
- [ ] timing group 有 reference map
- [ ] 3V3_SDRAM/3V3_PHY 有 current-loop review
- [ ] RMII 与 MDI 分开审
- [ ] connector/chassis path 有图
- [ ] Blocker 全关闭
- [ ] Major 未关闭项有风险接受
- [ ] DRC PASS 没被当 Review PASS
