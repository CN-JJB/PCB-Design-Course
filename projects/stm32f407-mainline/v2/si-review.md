# V2 Signal Integrity Review

> Review 目标：不是“规则都设了”，而是每个关键互连都能解释为什么这样设计。

---

## A. Transmission-Line Screening

- [ ] 关键网络已建立 source / load / topology
- [ ] 已估算关键走线 flight time
- [ ] 已记录 edge-rate 或 protocol 依据
- [ ] 没用固定 MHz 门槛替代判断

### Notes

- 

---

## B. Stackup / Impedance

- [ ] 当前 fab stackup 名称与查询日期已记录
- [ ] controlled-impedance geometry 来自对应 stackup 求解
- [ ] 关键线宽没有无意义突变
- [ ] connector / ESD / via / pad transition 已人工检查

### Notes

- 

---

## C. Reflection / Termination

- [ ] 快速点对点输出已评估 source termination
- [ ] 串联电阻靠 source
- [ ] 没有多余 branch / test stub
- [ ] 终端阻值没有凭习惯直接填 22/33 Ω

### Notes

- 

---

## D. Return Path / Reference Plane

- [ ] 每条 critical net 都能指出 reference plane
- [ ] 不跨 plane slot/split
- [ ] 关键 signal via 都能解释 return transition
- [ ] via anti-pad cluster 没切断回流通道
- [ ] connector 区域的 reference / shield / ESD return 已检查

### Notes

- 

---

## E. Crosstalk

- [ ] 已识别 high-slew aggressor
- [ ] 已识别 sensitive victim
- [ ] 最长 parallel runs 已审查
- [ ] high-risk nets 没只用 manufacturing minimum spacing
- [ ] pair-to-pair 与 intra-pair geometry 分开管理

### Notes

- 

---

## F. Differential / USB

- [ ] USB mode 明确为 FS/HS 中的具体一种
- [ ] DP/DM geometry 与 stackup 对应
- [ ] pair 没跨 reference split
- [ ] ESD 靠 connector
- [ ] VBUS 没和 DP/DM 长距离并行
- [ ] transition 对称
- [ ] skew target 有来源
- [ ] 没为了“0 skew”制造密集蛇形

### Notes

- 

---

## G. Measurement Readiness

- [ ] source / receiver 至少有合理测量方法
- [ ] 探测不会引入很长 ground loop
- [ ] 高速路径没有为了测量增加明显 stub
- [ ] Bring-up 计划包含 source/load 波形比较

### Notes

- 

---

## Review Decision

- [ ] PASS — 可进入下一阶段
- [ ] PASS WITH ACTIONS — 带明确整改项进入
- [ ] FAIL — 关键 SI 风险未解释

### Open Actions

| ID | Problem | Physical reason | Fix | Owner | Status |
|---|---|---|---|---|---|
| SI-01 | | | | | |

---

## 最后一问

随机点一根 critical net，设计者能否在 2 分钟内回答：

> source 在哪？load 在哪？reference 是谁？为什么这个 width/gap？回流怎么走？换层怎么办？最可能的反射/串扰点在哪？怎么测？

如果不能，这根线还没有真正 Review 完。