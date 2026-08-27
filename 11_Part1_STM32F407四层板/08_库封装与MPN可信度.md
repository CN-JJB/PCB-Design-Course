# 08｜Library Provenance、封装验证与 MPN Traceability

> 一块板可以在 ERC/DRC 上完全正确，却因为 pin number、封装尺寸、Pin-1、exposed pad 或连接器机械图错误而整批报废。库文件不是“下载到就可信”。

## 1. 三个对象必须分开核对

```text
Symbol
Footprint
Exact MPN / Package
```

它们之间建立可追溯映射。

## 2. Symbol Review

至少检查：

- pin number；
- pin name；
- power pin；
- hidden pin；
- pin electrical type；
- NC / reserved；
- multi-unit device；
- datasheet revision。

## 3. Footprint Review

critical footprint 至少对照原始 mechanical drawing：

- package body；
- pitch；
- pad size；
- exposed pad；
- pin-1；
- courtyard；
- soldermask；
- paste；
- mounting hole；
- connector shell / keepout。

## 4. Library Source Hierarchy

推荐优先级：

1. 器件厂商官方 library / reference；
2. KiCad 官方库；
3. 可信第三方库；
4. 自建。

无论来源，**critical part 都必须自己复核**。

## 5. Third-party Library

Ultra Librarian / SnapEDA / 元器件平台的库可以提高效率，但不能把“能下载”当作 qualification。

记录：

```text
library source
download date
source part number
datasheet used for verification
local modifications
reviewer
```

## 6. Connector 是最高风险之一

连接器常同时包含：

- electrical pin；
- mechanical peg；
- shield tab；
- board edge；
- mating keepout；
- height；
- insertion direction。

3D 看起来像，不代表 footprint 正确。

## 7. MPN Traceability

BOM 中的 exact MPN 应能反查：

```text
schematic symbol
→ footprint
→ datasheet/package drawing
→ procurement item
```

任何 suffix 改变都要重新问：

- pinout 一样吗？
- package 一样吗？
- temperature / speed / voltage grade 一样吗？
- lifecycle / qualification 一样吗？

## 8. Library Gate

- [ ] MCU exact package verified
- [ ] regulator / PHY / memory package verified
- [ ] connectors against mechanical drawing
- [ ] polarity / pin-1 checked
- [ ] exposed pad / paste reviewed
- [ ] custom footprints peer-reviewed
- [ ] BOM exact MPN linked
- [ ] 3D/mechanical fit checked

## 9. 与 Part 9 的关系

Part 1 建立习惯；Part 9 把它升级成 fabrication / assembly release 的正式输入。
