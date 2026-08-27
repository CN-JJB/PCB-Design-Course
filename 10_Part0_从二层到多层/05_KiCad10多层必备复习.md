# 05｜KiCad 10 多层板必备复习：把“规则”变成工程约束

> 🎯 **本章目标**：不做 KiCad 菜单百科，只复习 Part 1 立即会用到的多层板功能，并明确“软件设置”和“真实板厂叠层”之间的关系。

本文按 **KiCad 10.0 官方文档（文档基于 9.0.9）** 编写。界面小版本可能变化，请以官方手册为准：

https://docs.kicad.org/9.0/zh/pcbnew/pcbnew.html

---

## 1. Board Setup 是 Part 1 的控制中心

进入：

```text
PCB Editor → File / Board Setup
```

后面最常用的部分：

- Board Editor Layers；
- Physical Stackup；
- Constraints；
- Pre-defined Sizes；
- Net Classes；
- Custom Rules；
- Violation Severity。

重要：**KiCad 允许你配置很多参数，但 KiCad 不会替板厂制造你的想象。**

真实 stackup 必须来自：

1. 你选定的板厂；
2. 你选择的板厚/铜厚/阻抗方案；
3. 板厂最终确认的介质结构。

---

## 2. Physical Stackup：先把“虚拟 PCB”变成真实结构

KiCad 10 官方手册说明，Physical Stackup 用来配置：

- copper layer count；
- dielectric layer；
- copper thickness；
- dielectric thickness；
- material；
- solder mask / silkscreen 等物理层信息。

官方文档还特别说明：stackup thickness 会影响 3D board thickness，并且层间厚度会参与含过孔网络的长度计算。

### Part 1 操作

在第一块四层板中：

```text
Board Setup
→ Board Stackup
→ Physical Stackup
→ Copper layers = 4
```

然后填入 Part 1 选定板厂的 stackup。

**不要用 KiCad 默认介质厚度直接做受控阻抗设计。**

---

## 3. Board Editor Layers：层名是给工程师看的“语义”

KiCad 允许把铜层指定为 signal / power plane / mixed 等类型。

官方文档强调：这个类型主要是用户参考；即便标成 power plane，KiCad 仍可允许你在铜层上放 tracks/zones。

所以：

> “软件里叫 Plane”不会自动让它成为完整参考平面。

真正决定参考质量的是你实际画出来的铜结构。

Part 1 推荐语义：

```text
F.Cu   = L1_SIG
In1.Cu = L2_GND
In2.Cu = L3_PWR
B.Cu   = L4_SIG
```

其中 L2 的课程目标是：**尽量保持整面连续 GND，不把它当免费布线层。**

---

## 4. Net Classes：不是“线宽分组”，而是网络意图分组

初学者常建：

```text
Default
Power
```

然后只设置 line width。

到了多层项目，更好的思路是按照**电气意图**分组，例如：

```text
DEFAULT
PWR_3V3
PWR_5V
CLOCK
USB_FS
SDIO
CAN
SENSITIVE_ANALOG
```

但注意：Part 1 不会一开始就给所有网络塞一堆未经验证的数值。

规则来自：

- board house manufacturing limits；
- actual stackup；
- interface requirements；
- MCU/peripheral documentation；
- current/thermal analysis。

---

## 5. Custom Rules：把“脑内规则”变成可检查规则

KiCad Custom Rules 很适合表达：

- 某网络的特殊 clearance；
- 某类网络允许/禁止的 via；
- 特定区域要求；
- 长度/拓扑相关检查中的部分约束。

但有一类规则仍然很难由 DRC 自动保证：

> **Return path continuity / reference-plane integrity。**

例如走线是否跨了平面开槽，很多时候仍需要：

- layer projection review；
- 3D/2D 目检；
- 专用 SI/field 工具；
- 人工 Design Review。

所以课程 Checklist 永远会分成两栏：

```text
Automated checks
Manual electromagnetic review
```

---

## 6. Import Settings：以后可以建立自己的板级模板

KiCad 10 官方文档支持从另一个 board 导入设置，包括：

- board layers / physical stackup；
- design constraints；
- predefined track/via sizes；
- net classes；
- custom rules；
- violation severity 等。

这意味着当 Part 1 完成以后，我们可以把经过验证的四层板设置做成课程模板：

```text
templates/
└── four-layer-stm32/
    └── board-template.kicad_pcb
```

以后不是从零重新输入，而是复用**有来源、被 Review 过**的规则。

---

## 7. 3D Viewer 的真正用途

3D Viewer 不只是“截图发朋友圈”。

它可以帮助检查：

- connector orientation；
- component height；
- mounting hole；
- board edge interference；
- 机械装配方向；
- 贴片正反面错误。

但它不能证明：

- SI 正确；
- 回流正确；
- 阻抗正确；
- DFM 完整。

每个工具只回答它擅长的问题。

---

## 8. 🛠️ 本章练习：创建一个空四层工程壳

暂时不放 MCU。

### Step 1

新建 KiCad project：

```text
stm32f407-v1
```

### Step 2

PCB Editor 中设置 4 copper layers。

### Step 3

将层语义记录成：

```text
L1 = Signal + Components
L2 = Solid GND reference
L3 = Power distribution
L4 = Secondary Signal + Components
```

### Step 4

Physical Stackup 暂时标记：

```text
TBD — waiting for selected manufacturer stackup
```

不要随便填“经典 0.2 / 1.2 / 0.2 mm”然后把它当真实生产数据。

### Step 5

建立初始 Net Classes，但不要填没有来源的高速参数：

```text
DEFAULT
POWER
CLOCK
USB_FS
CAN
SDIO
```

这就是工程纪律：**宁可 TBD，也不要伪精确。**

---

## 9. KiCad 复习检查

在进入 STM32F407 四层项目之前，你应该能：

- [ ] 解释 signal + return 形成闭合回路；
- [ ] 解释 reference plane 为什么重要；
- [ ] 不再用固定 MHz 定义高速；
- [ ] 会估算 flight time 与 edge time 的关系；
- [ ] 会从 ST 一手资料提取硬件约束；
- [ ] 会在 KiCad 10 设置 layer count 和 Physical Stackup；
- [ ] 知道 Net Class 数值必须有来源；
- [ ] 知道 DRC 无法替代 return-path review。

全部能解释后，先进入最后一关：

> [06｜实测案例：接地、过孔寄生与耦合](06_实测案例_接地过孔与耦合.md)

在那里你会用“同一原理图、不同 PCB 结构”的实测结果，把 reference plane、return path、GND via 和 loop coupling 串成一条完整因果链。完成第 6 关的 Design Review 后，再进入 Part 1。