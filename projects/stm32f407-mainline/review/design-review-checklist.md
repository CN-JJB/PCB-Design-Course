# STM32 Mainline｜Design Review Checklist

> 这不是“打勾就一定正确”的护身符。每一项都要能说明证据：Datasheet、计算、KiCad rule、Gerber、测量或人工审查。

## A. Requirements

- [ ] exact MCU / package 已冻结
- [ ] power input / output rails 定义
- [ ] debug / programming method 定义
- [ ] mechanical / connector access 定义
- [ ] 每项 requirement 有验收方式
- [ ] scope change 有记录

## B. Schematic

### MCU power
- [ ] VDD/VSS 全部核对
- [ ] VDDA/VREF+ 核对
- [ ] VCAP1/2 按器件文档
- [ ] VBAT 按器件文档
- [ ] local decoupling 数量/连接符合一手资料
- [ ] package bulk decoupling 有来源

### Regulator
- [ ] exact regulator MPN
- [ ] CIN/COUT 值/介质符合 datasheet
- [ ] enable state 明确
- [ ] thermal budget 已估算
- [ ] input source current capability 合理

### Clock / reset / boot
- [ ] HSE source/CL/footprint 有来源
- [ ] oscillator placement note 已写
- [ ] BOOT0 default state 明确
- [ ] NRST circuit reviewed

### Debug
- [ ] SWDIO/SWCLK/NRST/GND/VTREF
- [ ] header orientation / pin 1
- [ ] debug connector 可物理接近

## C. Stackup

- [ ] board house / stackup name
- [ ] 查询日期
- [ ] copper thickness
- [ ] dielectric thickness
- [ ] KiCad Physical Stackup 与制造选择一致
- [ ] L1 primary reference = L2 GND
- [ ] L2 不作为普通 routing layer
- [ ] L4 关键网络逐条检查 L3 reference
- [ ] impedance geometry（如有）来自当前 stackup/计算器

## D. Placement

### Mechanical
- [ ] board outline / mounting holes
- [ ] connector cable access
- [ ] reset/button access
- [ ] polarity / pin 1 可识别

### Power loops
- [ ] LDO CIN/COUT close to proper pins
- [ ] VCAP local
- [ ] each 100 nF has intended VDD region/pin group
- [ ] capacitor GND path quickly enters L2
- [ ] power path does not unnecessarily cross oscillator region

### Clock / debug
- [ ] HSE compact
- [ ] no unnecessary oscillator stub
- [ ] SWD header near accessible edge

## E. Routing

### Automated
- [ ] no unresolved DRC errors
- [ ] track width / clearance
- [ ] via size / drill
- [ ] copper-to-edge
- [ ] unconnected items

### Manual electromagnetic
- [ ] L2 continuous under critical L1 routes
- [ ] no critical signal across GND slot/void
- [ ] every critical layer change has reference-transition analysis
- [ ] Bottom critical routes checked against L3 split
- [ ] no unexplained long stub
- [ ] HSE current/field loop compact

## F. Power integrity basics

- [ ] current path from regulator to load is clear
- [ ] no thin accidental plane neck
- [ ] via count appropriate for expected current
- [ ] local/bulk decoupling are not treated as interchangeable
- [ ] test points do not create dangerous stubs on sensitive nodes

## G. Fabrication

- [ ] board thickness
- [ ] stackup/order match
- [ ] Gerber layer count correct
- [ ] In1 GND refill reviewed
- [ ] In2 power refill reviewed
- [ ] drill file reviewed
- [ ] Edge.Cuts closed
- [ ] mask openings
- [ ] silkscreen polarity / revision
- [ ] BOM ↔ footprint ↔ MPN match

## H. Bring-up

- [ ] visual inspection plan
- [ ] unpowered rail check
- [ ] current-limited first power-up
- [ ] 3V3 measurement
- [ ] NRST measurement
- [ ] SWD attach
- [ ] internal-clock minimal firmware
- [ ] HSE separate validation
- [ ] LED/button/UART staged test
- [ ] fault log template ready

## I. Evidence

Review 不允许只有“OK”。至少关键项能指向：

```text
source document / section
KiCad screenshot or rule
calculation
Gerber layer
measurement
fault log
```

## J. Review result

```text
Blocker:
Major:
Minor:
Accepted risk:
Reviewer:
Revision:
Date:
Decision: REWORK / READY FOR FAB / READY FOR BRING-UP
```