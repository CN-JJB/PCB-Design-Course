# 10｜IBIS 与板级 SI 仿真入门：让“串阻值”从猜测变成假设验证

> IBIS 不是晶体管级 SPICE。它以 I/O buffer 的外部行为模型帮助板级工程师分析驱动、互连、终端和接收端波形。

## 10.1 本课程为什么需要 IBIS

我们已经反复强调：

> “22 Ω / 33 Ω”不能成为跨器件的魔法数字。

IBIS 给出一种更好的工程链：

```text
Device model
→ package
→ transmission line
→ termination
→ receiver
→ waveform
→ prototype measurement
```

## 10.2 一个最小 IBIS 模型里你应该识别什么

至少知道：

- component / pin mapping；
- model selector；
- I/O model type；
- pullup / pulldown；
- rising / falling waveform；
- package R / L / C；
- voltage / temperature corner。

不要假设“文件能导入”就代表选对了 pin model。

## 10.3 Corner 思维

同一个输出缓冲器在不同：

- process；
- voltage；
- temperature；
- drive strength / slew setting

下表现可能不同。

因此仿真不是为了得到一条“真波形”，而是为了检查设计在合理 corner 下是否仍有 margin。

## 10.4 教学实验：Source Termination A/B

建立一个点对点时钟：

```text
MCU/FPGA IBIS driver
→ package
→ PCB line
→ optional Rs
→ receiver
```

比较：

- Rs = 0 Ω；
- 一个偏小的串阻；
- 一个接近 source-match 的串阻；
- 一个过大的串阻。

观察：

- overshoot / undershoot；
- settling；
- receiver crossing；
- edge rate；
- delay。

## 10.4.1 从 point-to-point 升级到 branched + coupled topology

视频中的完整案例不是只扫一个 Rs，而是同时建模：

~~~text
IBIS transmitter
→ coupled trace section
→ tee
→ branch A / branch B
→ two IBIS receivers

adjacent quiet victim
→ coupled trace section
→ victim receiver
~~~

这能同时回答：

- branch imbalance 会怎样改变 reflection timing；
- Rs 对 repeated bounce 的抑制程度；
- H / spacing 对 crosstalk 的影响；
- stackup 变化如何同时改变 Z0 与 field confinement。

建议学生做仿真时也采用 **single-variable ablation**：

1. baseline；
2. only topology change；
3. only Rs；
4. only stackup；
5. pairwise combinations；
6. all changes。

这样才能知道“为什么变好”，而不是只保存一张最终漂亮波形。

完整实验参数与教材修正见：[11｜仿真案例：支路、源端串联终端与 Stackup](11_仿真案例_支路终端与Stackup.md)。


## 10.4.2 进阶：不要只 sweep Rs，也可以 sweep system Z0

如果不是协议固定 impedance 的接口，可以做一个 architecture experiment：

~~~text
Z0 = 30 Ω / 40 Ω / 50 Ω / 60 Ω / 70 Ω
→ 每个 Z0 重新生成合法 PCB geometry
→ 每个 Z0 重新优化 source / load termination
→ 比较
   waveform
   power
   crosstalk
   routing width
   manufacturing margin
~~~

注意最重要的一点：

> **不能只把 simulator 里的 Z0 数字从 50 改成 70，却保持 PCB geometry、crosstalk coupling 和 termination 不变。**

因为真实 Z0 变化通常意味着 W/H/Dk 变化，而这些变化会同步影响：

- coupling；
- delay；
- loss；
- routing density。

所以这是“system trade-off sweep”，不是单参数魔法旋钮。


## 10.5 仿真输入必须可追溯

保存：

| Input | Source |
|---|---|
| IBIS file | vendor + revision |
| pin/model | exact I/O |
| stackup | board freeze |
| Z0 / delay | field solver / fab |
| load | receiver / connector / probe |
| termination | schematic BOM option |
| topology / branch lengths | layout / extracted geometry |
| corner | explicit |

## 10.6 仿真不能替代什么

IBIS 不自动替你证明：

- EMC compliance；
- PDN；
- connector / cable model正确；
- PCB stackup实际值；
- probe loading；
- firmware timing；
- production variation。

## 10.7 与实测闭环

推荐形成：

```text
Simulation hypothesis
→ choose termination options
→ reserve footprint
→ manufacture
→ scope measurement
→ compare trend
→ update model / constraint
```

如果仿真和实测不一致，先检查：

1. probe；
2. source slew；
3. actual stackup；
4. load；
5. model pin / corner；
6. hidden cable / connector / stub。

## 10.8 Part 2 新毕业 Gate

完成 Part 2 后至少能解释：

- 为什么一个网络需要/不需要 transmission-line treatment；
- 为什么 termination 必须结合 source / line / load；
- S11 / S21 分别看什么；
- IBIS 能回答什么、不能回答什么；
- 为什么最终要回到测量。

## 参考资料

- IBIS Open Forum 官方规范与模型说明；
- MCU / FPGA 厂商 IBIS model；
- 具体接口与器件 hardware design guide。
