# Part 4 Fault Lab｜EMI / EMC 故障板

这批故障全部允许 DRC 通过。目标是训练你看 **电流路径和系统边界**，不是看红叉。

---

## Fault 01｜USB shield 直接通过一条长细线接 MCU GND

### 表面
DC 测量“接地正常”。

### 实际风险
shield/ESD/common-mode current 通过高电感路径进入数字核心。

### 修复
根据机壳/connector 结构重新定义 shield/chassis coupling，并降低入口处高频阻抗。

---

## Fault 02｜TVS 离 connector 很近，但地端绕很远

### 表面
满足“TVS 靠近接口”的经验规则。

### 实际风险
完整 discharge loop inductance 仍然很大。

### 训练点
只看器件距离会误判；必须画 `connector → TVS → reference → environment`。

---

## Fault 03｜TVS 放在 MCU 旁，connector 到 TVS 共享长线

ESD 电流先深入 PCB，再遇到保护支路。

修复重点：protection interception topology。

---

## Fault 04｜USB D+ 有 test stub，D- 没有

### 后果
pair asymmetry → differential-to-common-mode conversion 增加，同时出现 SI discontinuity。

---

## Fault 05｜USB CMC 被当作“EMC 必装件”

### 表面
BOM 很专业。

### 实际风险
原始 pair/reference 已经很差，CMC 只是掩盖问题；器件寄生还可能恶化通道。

### 实验
CMC fitted / bypass A/B，并同时检查 common-mode source。

---

## Fault 06｜CAN TVS 选型正确，但 transient path 穿 MCU 区

### 表面
器件 IEC rating 很高。

### 实际风险
大瞬态电流和系统地共享高阻抗铜段。

---

## Fault 07｜CANH/CANL protection footprint 不对称

一根线多 via/更长 pad path，导致 mode conversion 与 channel mismatch。

---

## Fault 08｜高速线跨 reference slot

### 后果
同时造成：
- return detour
- larger loop
- impedance discontinuity
- stronger coupling / EMI risk

这是 SI 与 EMC 共用的一类根因。

---

## Fault 09｜板边 via fence 机械复制 10 mm 间距

### 表面
“看起来很 EMC”。

### 实际问题
没有定义 target frequency、enclosure、seam 或具体 current path。

### 训练点
删除装饰性规则，只保留有物理用途的 stitching。

---

## Fault 10｜CHASSIS_GND 只是一个名字

PCB 画一圈 `CHASSIS_GND`，但整机无金属机壳、无 shield bonding，也没有明确 coupling network。

### 训练点
net name 不会自动创造 chassis。

---

## Fault 11｜Buck SW node 靠 USB connector 很近

### 结果
高 dv/dt 电场更容易耦合到 cable-facing structure。

### 修复
先从 floorplan 把 source 与 interface boundary 分开，而不是事后只加磁珠。

---

## Fault 12｜近场热点就被认定为正式辐射主因

### 错误
near-field hotspot ≠ formal far-field dominant source。

### 正确
结合 cable experiment、结构尺寸和正式测试数据归因。

---

## Fault 13｜一次整改同时加 20 个地孔 + CMC + 磁珠 + 电容

### 结果
测试变好，但没有人知道哪个修改有效。

### 修复
单变量 A/B 测试，建立可复用知识。

---

## Fault 14｜拔 USB 线后峰值下降，于是直接认定 USB PHY 有问题

### 实际可能
板内 clock/power noise 通过 connector/shield coupling 到 cable。

### 修复
继续追 `Source → Coupling → Antenna → Return`。

---

## Fault 15｜ESD 测试只记录“有没有复位”

### 缺失
- communication errors
- reset reason
- latch-up
- self recovery
- permanent damage

### 训练点
EMC immunity 是系统行为，不只是芯片有没有烧。

---

# Fault Lab 完成标准

每个 Fault 写：

```text
Symptom
Current path
Why DRC misses it
Physics
Proposed change
Possible side effect
A/B verification
Checklist item
```

如果解释仍然是“这样画不规范”，说明还没有学会。