# 11｜Reliability 与 Pre-compliance：不要把“72 小时烤机”当通用可靠性标准

> 可靠性验证必须从产品使用环境和失效机制出发，而不是复制一个固定温度、固定时长。

---

# 1. 先定义 Mission Profile

至少：

- operating temperature；
- storage；
- humidity；
- power cycles；
- duty cycle；
- vibration/shock；
- connector cycles；
- ESD exposure；
- surge/EFT；
- expected lifetime。

没有 mission profile，所谓“可靠性测试”没有裁判。

---

# 2. De-rating 也不是统一百分比

旧教材曾给：

- 电容 70–80% 电压；
- 电阻 50% 功率；
- junction 70% Tmax

这种统一比例。

这些可以是某些组织的内部政策，但不是跨器件、跨行业通用定律。

实际 derating 应来自：

- component type；
- manufacturer；
- temperature；
- failure mechanism；
- company/industry standard。

---

# 3. Environmental Test

可能包括：

- thermal cycling；
- high/low temperature operation；
- storage；
- damp heat；
- vibration；
- shock；
- power cycling；
- connector cycling；
- HALT/HASS（按体系）。

是否做、怎么做由：

> mission profile + regulatory/customer requirement + risk

决定。

---

# 4. EMC Pre-compliance

Part 4 已经建立 EMC 诊断方法。

量产前要把它变成：

- fixed test configuration；
- cable；
- firmware mode；
- worst-case load；
- orientation；
- measurement setup；
- pass/fail target；
- report。

如果不同 firmware workload 会改变 emissions：

> 测试 image 必须冻结。

---

# 5. ESD / EFT / Surge

测试等级来自：

- 产品标准；
- 客户要求；
- installation environment。

不能写：

> “工业板统一 ±8 kV。”

---

# 6. Thermal

测试：

- regulator；
- MCU/FPGA；
- DDR3；
- PHY；
- connector；
- inductor；
- protection。

条件：

- max workload；
- max input；
- worst ambient；
- enclosure。

室温裸板温升正常，不代表最终 enclosure 内正常。

---

# 7. Margin Test

工程验证阶段可以有意识做：

- input voltage margin；
- clock/frequency margin；
- SDRAM timing margin；
- temperature；
- load；
- cable；
- alternate part。

它不是为了“虐板”，而是找：

> 离失效边界还有多远。

---

# 8. Reliability Failure 必须回 ECO/CAPA

如果：

- thermal cycle 后 MLCC crack；
- vibration 后 connector fail；
- ESD 后 PHY reset；

需要：

- failure analysis；
- containment；
- corrective action；
- redesign/process update；
- revalidation。

不能只换一块“好的样机”继续测试。

---

# 9. Review

- [ ] mission profile
- [ ] product-specific standards identified
- [ ] test conditions有source
- [ ] pre-compliance configuration冻结
- [ ] worst-case firmware/load冻结
- [ ] thermal enclosure条件
- [ ] margin test有purpose
- [ ] failure进入CAPA/ECO
