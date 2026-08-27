# 02｜DFM 与 DFA：能画出来，不等于能稳定生产

## 2.1 两个概念分开

- **DFM**：Design for Manufacturability，面向 PCB fabrication；
- **DFA**：Design for Assembly，面向 SMT / THT / mechanical assembly。

DRC 只是输入，不是结论。

## 2.2 DFM Review

至少检查：

- trace / space；
- drill / finished hole；
- annular ring；
- aspect ratio；
- copper-to-edge；
- soldermask sliver；
- via type；
- controlled impedance；
- stackup；
- board outline / route / V-score；
- panelization；
- copper balance；
- fiducial；
- tooling hole；
- fab notes。

## 2.3 DFA Review

重点：

- footprint land pattern；
- polarity / pin-1；
- component orientation；
- courtyard；
- nozzle / placement access；
- reflow compatibility；
- tombstone risk；
- thermal pad / paste window；
- via-in-pad；
- bottom-side heavy components；
- connector mechanical load；
- hand-solder / rework access。

## 2.4 Footprint Provenance

每个 critical footprint 保存：

```text
MPN
package drawing revision
land pattern source
custom modification
3D/mechanical check
assembly feedback
```

库里“有这个 footprint”不是验证。

## 2.5 Panel / Assembly Context

单板 DRC 可能完全通过，但拼板后仍可能有：

- connector interference；
- depanel stress；
- insufficient rail；
- tooling conflict；
- edge component damage。

所以 DFM/DFA 必须看实际制造流程。

## 2.6 Manufacturer Feedback Loop

板厂/贴片厂提出的修改不能只在聊天记录里。

每条反馈进入：

```text
Finding
→ source
→ accept / reject
→ design impact
→ ECO if required
```

## 2.7 Gate

- [ ] fab capability 已冻结；
- [ ] critical footprints 已核对原始 mechanical drawing；
- [ ] panel/assembly process 已考虑；
- [ ] impedance / via process 有明确供应商确认；
- [ ] 所有 manufacturer waiver 有记录。
