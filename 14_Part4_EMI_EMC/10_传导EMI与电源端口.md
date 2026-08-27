# 10｜传导 EMI 与电源端口：噪声不只会“从天线飞出去”

> 辐射只是 EMC 的一部分。开关电源、数字回流和外部线缆还会把噪声沿导体带出系统。

## 10.1 两条基本路径

### Differential-Mode Conducted Noise

噪声主要以正负导体之间的差模电压/电流存在。

### Common-Mode Conducted Noise

多个导体相对 chassis / environment 同向运动。其回路往往经过寄生电容、屏蔽、地和外壳。

滤波器对 DM / CM 的作用不同，因此“多加一颗磁珠”不是统一答案。

## 10.2 开关电源为什么常成为源

重点看：

- hot loop；
- SW node dv/dt；
- diode / FET di/dt；
- input capacitor loop；
- transformer / inductor parasitic coupling；
- layout 到 chassis / cable 的寄生电容。

## 10.3 LISN 的角色

正式 conducted-emissions 测试会使用由适用标准定义的网络和测试配置。LISN 的工程作用之一是提供受控的测量阻抗与测试端口。

本课程不把某个 LISN 参数写成所有产品通用要求；必须按适用标准和端口类型确定。

## 10.4 输入滤波器不是“越大越好”

滤波器要检查：

- source / load impedance；
- regulator stability；
- damping；
- inrush；
- DCR / thermal；
- DM / CM path；
- layout parasitic。

## 10.5 PCB Review

从输入连接器开始画：

```text
Cable
→ protection
→ filter
→ bulk
→ regulator
→ load
→ return
→ chassis/environment
```

任何一段如果跨越长距离、形成大 loop 或在保护/滤波前把噪声扩散到全板，后面再堆器件效果都可能有限。

## 10.6 预兼容 A/B

- regulator mode / switching frequency A/B；
- filter fitted / bypassed；
- cable length/orientation A/B；
- chassis bond A/B；
- source slew / workload A/B；
- near-field hotspot ↔ conducted peak 相关性。

## 10.7 Review

- [ ] 已区分 DM / CM；
- [ ] 输入端口噪声路径可画出；
- [ ] 滤波器有 source/load/stability 依据；
- [ ] cable / chassis 参与已检查；
- [ ] 结论来自 A/B 或正式测试，而非“装了滤波器所以会过”。
