# Part 9 Fault Lab｜Engineering Release / Production

> 这一组错误的特点：PCB 电路可能完全正确，甚至样板已经正常工作，但量产仍然会出严重事故。

---

# A. Design Freeze / Configuration

## Fault 01｜只冻结 Gerber，不冻结 BOM/FW/Test
同一 Gerber 被搭配了不同 BOM 或不同固件，产品配置失去唯一性。

## Fault 02｜Gerber 手工修了一根线
工厂那版能工作，但 source PCB 没有修正；下一次重新输出又复发。

## Fault 03｜PnP CSV 手工改角度但没记录
下次重新导出恢复旧角度。

## Fault 04｜Hardware Rev 与 Git commit 混为一谈
产品标签写 Rev A，但无法知道具体 source state。

## Fault 05｜Freeze 后偷偷改 silk，不升任何 revision
制造资料 hash 已变，但 release manifest 不变。

## Fault 06｜BOM Rev 变化但 Assembly Drawing 仍旧版本
DNP/variant 发生冲突。

---

# B. DFM / DFA / DFT

## Fault 07｜板厂能做 0.15 mm drill，所以全板都用最小孔
忽略成本、良率、可靠性与 vendor portability。

## Fault 08｜把 JLCPCB 当前 edge rail 数字写成公司永久标准
换 EMS 后工艺条件完全不同。

## Fault 09｜QFN 一律要求 100% X-ray
没有风险/成本/过程能力分析。

## Fault 10｜BGA 一律 via-in-pad
工艺升级没有必要，成本与返修难度增加。

## Fault 11｜测试点最后一天才加
关键 rail/接口没有 probe access。

## Fault 12｜为了测试给 GTP/USB 增加长 stub
DFT 破坏 SI。

## Fault 13｜拼板 depanelization 线紧贴 MLCC
试产后出现 flex crack。

---

# C. BOM / AVL / Supply

## Fault 14｜替代 MLCC 只比较 10 µF / 0805 / 10 V
忽略 DC bias / ESR / height / reliability。

## Fault 15｜晶振只比较频率
startup、ESR、load cap、drive level 全部变化。

## Fault 16｜PHY 同封装同 pin 就直接替代
register/strap/analog/network behavior 未验证。

## Fault 17｜采购发现缺货后现场换 LDO
可能改变 stability、dropout、thermal 与 PCB pin behavior。

## Fault 18｜DNP 通过删除 BOM 行实现
PnP/assembly drawing/variant 无法一致。

## Fault 19｜Alternate 写进 BOM 但没有 Validation
Candidate 被误当 Approved。

## Fault 20｜关键 IC 已 NRND/EOL，Pilot 后才发现
量产计划无法持续。

---

# D. Fabrication / Assembly Package

## Fault 21｜Edge.Cuts 丢失但 Gerber ZIP 仍发出
CAM 系统可能无法正确识别 outline。

## Fault 22｜Drill 与 copper 来自不同 PCB commit
孔与 pad 偏移。

## Fault 23｜Stackup 改了，阻抗 table 没更新
制造商按新 stackup 做旧 geometry。

## Fault 24｜Fab note 写“50 Ω”，没有 layer/net/tolerance
要求不可执行。

## Fault 25｜只检查 KiCad PCB，不检查 generated Gerber
输出配置错误没被发现。

## Fault 26｜Top/Bottom PnP rotation convention 未验证
极性器件被旋转。

## Fault 27｜BOM Variant=STD，PnP 却来自 DEBUG variant
装配配置分裂。

## Fault 28｜Golden Sample 代替 Assembly Drawing
样品返修/旧版状态变成事实标准。

---

# E. Programming / Serialization

## Fault 29｜生产文件叫 final.hex，没有 hash
无法证明烧录的是哪一版。

## Fault 30｜Debug firmware 当 Production image
watchdog/security/test mode 状态错误。

## Fault 31｜Serial Number 只贴标签，不进 test database
返修/RMA 无法追到生产批次。

## Fault 32｜MAC 地址人工复制
出现重复网络身份。

## Fault 33｜FPGA JTAG image 正确，但 SPI Flash image 是旧版
上电自动启动与开发调试行为不一致。

## Fault 34｜Calibration data schema 改了但 FW compatibility 未更新
旧板加载新格式后读错。

---

# F. Test / Fixture

## Fault 35｜FCT 只输出 PASS/FAIL
产线无法做 defect Pareto。

## Fault 36｜Fixture pogo 坏了，整批产品被判 FAIL
夹具没有 self-test / golden board。

## Fault 37｜为了提高 yield 临时放宽 test limit
没有 ECO/Test Revision。

## Fault 38｜功能测试只测“能开机”
接口/内存/网络/负载缺陷逃逸。

## Fault 39｜示波器/仪器 calibration 已过期
测量证据失效。

## Fault 40｜高速 probe testpoint 改变 channel
测试结构本身制造 failure。

---

# G. Pilot / Yield

## Fault 41｜100 片里 80 片一次过、20 片返修后全过，报告写 Yield=100%
掩盖 FPY=80%。

## Fault 42｜只统计 scrap，不统计 rework
过程问题被隐藏。

## Fault 43｜FAI = 第一块能亮
没有对 BOM、方向、尺寸、工艺、程序逐项核对。

## Fault 44｜Pilot top defect 连续发生，但因为都能返修所以放量
把返修能力当生产能力。

## Fault 45｜一次同时改 stencil、pad、温度曲线和器件
即使改善也无法确定根因。

---

# H. ECO / Traceability / Supplier

## Fault 46｜换晶振不改 PCB，所以不走 ECO
影响 clock/EMC/firmware startup，却不可追溯。

## Fault 47｜供应商静默换 PCB material
阻抗/可靠性发生变化。

## Fault 48｜Deviation 没有 expiry
临时替代变成永久隐性配置。

## Fault 49｜无法回答某个 RMA Serial 用的 BOM/FW/Test Rev
unit genealogy 不完整。

## Fault 50｜量产后只归档 Gerber ZIP
没有 source/BOM/firmware/test/quality evidence，下一版无法复现。

---

# 使用方式

每个 Fault 填写：

| Field | Answer |
|---|---|
| Symptom / Escape | |
| Why prototype did not catch it | |
| Configuration item affected | |
| Manufacturing/Test impact | |
| Root cause evidence | |
| Containment | |
| ECO/CAPA | |
| Validation | |
| Traceability update | |
| New release rule | |

最终目标：

> **量产事故不是靠记忆“以后小心”，而是反馈进 Release System。**
