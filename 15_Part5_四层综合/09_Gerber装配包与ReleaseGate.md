# 09｜Gerber、装配包与 Release Gate：真正交给板厂的不是 KiCad Editor 画面

> 制造只认识你交付的文件。PCB Editor 里看起来完美，但 Gerber、drill、BOM、坐标或装配说明错了，做出来的就是错板。

---

# 9.1 Release Package 最少包含什么

建议 V2 release directory：

```text
release/v2-r01/
├── README_release.md
├── gerber/
├── drill/
├── fabrication/
├── assembly/
│   ├── BOM.csv
│   ├── CPL.csv
│   └── assembly-notes.md
├── drawings/
├── reports/
│   ├── DRC.txt
│   └── review-summary.md
└── checksums.txt
```

课程仓库不要求你现在真的生成全部二进制/制造文件，但目录和 release discipline 要先建立。

---

# 9.2 Gerber 输出前的“冻结动作”

先记录：

- Git commit SHA；
- board revision；
- schematic revision；
- BOM revision；
- stackup revision；
- DRC result；
- open waivers；
- target fab；
- date。

之后不要一边输出一边继续改 PCB。

如果改：

> revision 重开，重新跑 release gate。

---

# 9.3 Gerber 层检查

至少：

- F.Cu；
- In1.Cu / L2 GND；
- In2.Cu / L3 Power；
- B.Cu；
- F.Mask / B.Mask；
- F.Silk / B.Silk；
- Edge.Cuts；
- paste layers if assembly requires；
- fabrication drawing layers as required。

不要因为“KiCad 默认勾了”就自动全交。

---

# 9.4 Drill Review

检查：

- PTH / NPTH 是否区分；
- mounting hole 是否正确 plated；
- connector shell tabs；
- via drill；
- slot / oval hole；
- microSD/USB mechanical pins；
- drill origin / units。

很多机械翻车都发生在这里。

---

# 9.5 Gerber Viewer 必须独立检查

不要只在 PCB Editor 看。

使用：

- KiCad Gerber Viewer；
- 或板厂 viewer；
- 最好再用第二工具交叉查看关键层。

重点检查：

### Edge
- board outline closed；
- no duplicate contour；
- cutout correct。

### Copper
- L2 GND 连续；
- L3 power islands 正确；
- no unexpected isolated copper；
- USB/SDIO/CAN path 和 editor 一致。

### Mask
- fine-pitch pad openings；
- exposed copper；
- testpoint mask opening。

### Silk
- pin 1；
- connector labels；
- no text on pads。

---

# 9.6 Impedance Fabrication Note

如果 USB pair 需要 controlled impedance：

fabrication note 里记录：

```text
Controlled pair:
Layer/reference:
Target impedance:
Nominal w/s:
Stackup ID:
Fabricator adjustment allowed? Y/N / communicate
Coupon requirement:
```

不要只在 KiCad 里设置了 differential width，就认为板厂知道你的意图。

---

# 9.7 Assembly Package Review

BOM 和 CPL / position file 必须互相一致。

检查：

- RefDes 数量；
- DNP；
- rotation；
- package；
- top/bottom side；
- pin 1；
- USB-C / microSD / IC orientation；
- alternate parts；
- hand-assembly parts。

---

# 9.8 Assembly Notes 要写什么

例如：

```text
R_CAN_TERM: DNP by default; populate only for endpoint validation.
R_USB_DP/DM: default 0 Ω / tuning placeholder per current design decision.
R_SDCLK: default candidate value; final value may be tuned after waveform validation.
CMC_CAN: DNP by default unless EMC validation requires it.
Shield option: see chassis/shield design note.
```

这样生产不会靠猜。

---

# 9.9 Release Gate Checklist

## Electrical

- [ ] ERC PASS / waived findings recorded
- [ ] DRC PASS / waivers recorded
- [ ] power tree reviewed
- [ ] VCAP reviewed
- [ ] USB reviewed
- [ ] CAN reviewed
- [ ] SDIO reviewed

## SI

- [ ] USB pair geometry/reference checked
- [ ] SDIO_CLK topology checked
- [ ] critical via transitions checked
- [ ] no major uncontrolled stubs

## PI

- [ ] decoupling loops checked
- [ ] 3V3 bottlenecks checked
- [ ] regulator thermal budget reviewed
- [ ] microSD transient path reviewed

## EMC/ESD

- [ ] connector-side protection paths checked
- [ ] USB/CAN cable boundary reviewed
- [ ] reference slots checked
- [ ] shield/chassis strategy documented

## DFM

- [ ] fab capability checked
- [ ] footprints checked
- [ ] mechanical clearance checked
- [ ] assembly orientation checked

## Release Files

- [ ] Gerber viewed
- [ ] Drill viewed
- [ ] BOM/CPL cross-check
- [ ] fab note complete
- [ ] release commit recorded

---

# 9.10 一个很重要的工程习惯：Release 不等于“最新版”

正确：

```text
v2-r01
commit: abc1234
BOM: r01
Gerber: generated from abc1234
```

错误：

```text
V2_final_final2_REAL.zip
```

Git 的价值在这里开始非常明显。

---

# 9.11 本章交付

创建：

- `projects/stm32f407-mainline/v2/release-gate.md`
- `projects/stm32f407-mainline/v2/release-package-structure.md`

等真实 KiCad 工程可验证后，再把实际 Gerber/DRC/BOM/CPL 按此流程生成。

---

## 本章任务

假设板厂反馈：

> “USB 90 Ω 需要把线宽从 0.18 mm 调到 0.20 mm。”

写出完整变更流程：

1. 谁批准；
2. KiCad 是否同步；
3. rule matrix 怎么改；
4. release revision 怎么变；
5. Gerber 怎么重出；
6. 如何防止 fab 文件和 source 不一致。