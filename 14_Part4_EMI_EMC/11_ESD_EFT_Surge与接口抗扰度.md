# 11｜ESD、EFT、Surge：三个瞬态问题不要混成“抗静电”

> 三者都属于 immunity 问题，但能量、波形、耦合方式、端口与保护策略不同。

## 11.1 ESD

ESD 常与用户可触及点、连接器、外壳和极快边沿相关。

PCB 第一问题仍是：

> 放电电流从哪里进入，经过什么保护，最后在哪里闭合？

## 11.2 EFT / Burst

Electrical Fast Transient / Burst 是一串快速瞬态脉冲，常与开关感性负载、继电器/接触器等环境相关。

它与单次 ESD 不同，课程应特别训练：

- 外部长线；
- I/O / power port coupling；
- filter / common-mode path；
- reset / latch-up / communication recovery；
- firmware logging。

## 11.3 Surge

Surge 通常具有更高能量和更长时间尺度，常与电源/长线端口、开关过电压或雷击相关瞬态有关。

这意味着保护器件不仅要看：

- clamp voltage；
- capacitance；

还要看：

- pulse energy；
- current rating；
- coordination；
- series impedance；
- fuse / GDT / MOV / TVS 等系统级组合；
- creepage / clearance 与安全边界（如适用）。

## 11.4 不能只问“TVS 放多近”

正确问题是：

1. surge/ESD/EFT 从哪个端口进入？
2. 保护前的 current path 多长、多大 loop？
3. return 去哪里？
4. protection 后还有什么 residual stress？
5. 保护器件是否影响 SI / normal operation？
6. 失效模式是什么？

## 11.5 Immunity Failure Classification

不要只写 PASS / FAIL。

记录：

```text
no effect
temporary communication error
self-recovering reset
latched fault
data corruption
manual intervention required
permanent damage
```

## 11.6 Standards Discipline

测试等级、耦合网络、波形与判据必须来自目标产品适用的当前标准版本。

本课程只建立方法，不把固定 kV 数字作为所有产品统一规则。

## 11.7 工程输出

为每个外部端口建立：

| Port | Threat | Entry path | Protection | Return | Functional criterion | Evidence |
|---|---|---|---|---|---|---|
| USB | ESD | connector | TBD | TBD | TBD | TBD |
| CAN | ESD/EFT | cable | TBD | TBD | TBD | TBD |
| Power | EFT/Surge | input | TBD | TBD | TBD | TBD |

## 参考标准入口

- IEC 61000-4-2：ESD immunity；
- IEC 61000-4-4：EFT / burst immunity；
- IEC 61000-4-5：surge immunity。

实际产品必须核对当前 edition、产品标准与测试实验室方案。
