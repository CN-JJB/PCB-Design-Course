# 07｜Assembly Package：让贴片厂知道“装什么、装哪、怎么装”

## 7.1 常见输出

- BOM；
- position / centroid；
- assembly drawing；
- polarity / pin-1 information；
- variant / DNP；
- stencil note；
- special process note；
- programming / serialized parts instructions（若在装配阶段）。

## 7.2 BOM ↔ Position 一致性

Release 前自动/人工检查：

- BOM ref 是否都存在；
- position ref 是否都存在；
- DNP 是否一致；
- side 是否正确；
- rotation convention 是否与供应商兼容。

## 7.3 Rotation 是高风险接口

不同 EDA / assembly house 对 rotation 可能有不同 convention。

第一次生产必须：

- 用 sample components 核对；
- 看 assembly preview；
- 重点检查 IC / diode / connector；
- 将工厂反馈固化进流程。

## 7.4 Stencil / Paste

对：

- QFN exposed pad；
- BGA；
- fine-pitch；
- large thermal pad；
- mixed component size

需要单独 review paste aperture，而不是完全依赖默认 solder paste expansion。

## 7.5 Special Components

记录：

- moisture sensitivity；
- baking；
- hand insert；
- press-fit；
- connector torque；
- adhesive；
- selective solder；
- heat-sensitive part。

## 7.6 Assembly First Article

首件至少检查：

- polarity；
- orientation；
- solder joint；
- BGA/QFN process evidence（按需要）；
- connector alignment；
- mechanical fit；
- short/open；
- programming access。

## 7.7 Assembly Release Checklist

输出必须绑定：

```text
PCB revision
BOM revision
variant
position file
assembly drawing
DNP list
special notes
```
