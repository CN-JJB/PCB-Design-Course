# Part 6 Fault Lab｜六层与 Stackup 故障板

每个场景按 `Symptom → Current/field path → Root cause → Fix → Side effect → Verification` 分析。

## Fault 01｜“H7 所以必须六层”
没有 layer-count evidence，只按 MCU 名字选层数。

## Fault 02｜“六层一定比四层 EMI 好”
新增两层却让两个 signal layer 紧邻、reference 很远。

## Fault 03｜L3 写着 Signal，所以默认参考 L2
真实 dielectric 显示 L4 coupling 更强，但 Review 完全没看厚度。

## Fault 04｜Bottom 高速线参考 split power plane
L5 不是 GND，L6 关键网络跨越两个 rail island。

## Fault 05｜GND→GND 换层没有 stitching path
signal via 很短，return 却绕到远处地孔。

## Fault 06｜GND→PWR 换层只加 GND via
reference net 不同，GND via 无法直接把回流送进 power plane。

## Fault 07｜“旁边放 100 nF”但电容安装回路很长
reference transfer 仍然高电感。

## Fault 08｜Power plane 被切成漂亮拼图
信号 corridor 恰好跨 split。

## Fault 09｜为了 plane 对称而牺牲 reference adjacency
几何看起来对称，电磁结构却不适合关键网络。

## Fault 10｜把板厂 3.5 mil capability 当项目默认规则
所有 routing 都踩 manufacturing edge，良率/成本/可维护性变差。

## Fault 11｜Stackup 改了但 impedance width 没重算
KiCad 仍保留旧 width/gap。

## Fault 12｜Net Class 写了 0.15 mm 就以为 DRC 会禁止 0.10 mm
未用 Custom Rule，手工改线宽没有触发预期错误。

## Fault 13｜Via forest 把 GND plane 打成 antipad slot
escape 成功，return path 失败。

## Fault 14｜为了少一个 via 让 clock 绕远
“少换层”被错误当成唯一优化指标。

## Fault 15｜六层仍挤到必须大量跨 reference
项目拒绝比较八层，因为“六层已经够高级”。

## Fault 16｜复制开发板 stackup
没有确认自己的板厂、铜厚、板厚、接口与布局是否相同。

## Fault 17｜Part 6 就把 SDRAM 规则写成 DDR3 规则
把 DQS/fly-by 等概念错误套到普通 SDR SDRAM。

## Fault 18｜H7 power scheme 直接复制博客
没有核对 exact package / AN4938 / datasheet / errata。

## Fault 19｜GND plane 上随手走普通信号
为了省局部 routing，破坏全局 reference infrastructure。

## Fault 20｜Stackup source 没记录查询日期
几个月后板厂页面更新，团队无法知道设计基于哪个版本。