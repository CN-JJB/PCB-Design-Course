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

### 2.3.1 Solder Joint Reliability：可焊不等于耐久

DFA 不只看“这颗料能不能贴上去”，还要看 joint 在真实 mission profile 下承受什么：

- thermal cycling；
- board flex；
- connector side load；
- vibration/shock；
- heavy-component inertia；
- depanel / assembly stress。

因此：

> **thermal relief、via-in-pad、paste aperture 都属于工艺 + 电气 + 机械的联合决策。**

课程禁止写成两个绝对规则：

~~~text
“所有 plane pad 都必须 thermal relief”
“所有 via-in-pad 都必须禁止”
~~~

Via-in-pad 如果被使用，必须明确 fill / cap / planarization / plating 与 assembly process。

### 2.3.1.1 制造术语陷阱：Via-in-Pad 不只是“把 Via 画进 Pad”

在 CAD 里把 via 中心放进 SMD pad 很容易，于是初学者会误以为：

> “这就是 via-in-pad。”

但很多板厂/装配语境里的 **VIP / VIPPO** 默认意味着额外工艺，例如：

~~~text
drill / plate
→ fill
→ planarize
→ cap plate
→ flat solderable pad
~~~

它解决的核心问题之一是：

- 小 pad 上的 solder 不再被 open via hole 吸走；
- BGA / fine-pitch pad 能保持平整焊接面；
- escape 可以直接从 pad 垂直下去。

### 📦 三种结构必须分清

| CAD 看起来 | 制造上其实是什么 | 主要风险 / 用途 |
|---|---|---|
| via 与 pad 重叠，孔保持 open | “via in a pad area”，未必是 VIPPO | solder wicking、paste loss、void；大 thermal pad 有时仍可接受 |
| filled + capped + plated flat | 真正常说的 VIP / VIPPO | fine-pitch BGA、紧凑 escape，成本更高 |
| QFN thermal pad 里一组小 thermal vias | thermal-via array | 是否填孔/塞孔取决于 stencil、void、assembly process，不自动要求 VIPPO |

### ⚠️ 不要把两条经验规则写成铁律

错误：

~~~text
所有 via-in-pad 都必须填孔
所有 thermal via 都必须开孔
~~~

正确流程：

~~~text
package pitch / pad size
+ solder paste volume
+ stencil design
+ assembly process
+ void requirement
+ fab capability
→ via fill / tent / cap decision
~~~

### Teardrop 与 Thermal Relief 也属于同一类“默认 checkbox 陷阱”

| 功能 | 主要解决什么 | 不要误解成 |
|---|---|---|
| Teardrop | drill breakout / annular-ring robustness、局部机械裕量 | 高速 SI 必选项 |
| Thermal relief | 降低焊接时 plane 吸热，尤其 THT / wave / hand solder 场景 | 所有 GND/Via 都必须加 |
| Solid connection | 降低电气/热阻，适合很多 via、thermal pad、reflow 场景 | 永远比 thermal spoke 好 |

### 工程实践来源（论坛讨论，不是规范）

- Electronics StackExchange, *What is the difference between “via-in-pad” and a via in a pad?*  
  https://electronics.stackexchange.com/questions/646593/what-is-the-difference-between-via-in-pad-and-a-via-in-a-pad
- Electronics StackExchange, *Why are there teardrops on PCB pads?*  
  https://electronics.stackexchange.com/questions/13205/why-are-there-teardrops-on-pcb-pads
- Electronics StackExchange, *Why thermal reliefs on vias?*  
  https://electronics.stackexchange.com/questions/14435/why-thermal-reliefs-on-vias

> 这里的作用是建立**制造语言识别能力**；最终工艺选择服从当前 fab/EMS capability 与 assembly requirement。


### 2.3.2 Connector Mechanical Load Path

对 USB、DC jack、board-edge connector、wire harness 等，Review 时画出：

~~~text
user / cable force
→ connector anchor
→ PCB
→ standoff / mounting hole
→ enclosure / chassis
~~~

如果主要载荷最终由 signal-pad solder fillet 承担，应视为可靠性 finding。

检查：

- shell/anchor pin；
- mounting hole proximity；
- board-edge leverage；
- strain relief；
- insertion/extraction cycle；
- enclosure support；
- cable torque；
- alignment tolerance。

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

### 2.4.1 Reworkability：Production 不是假设“永远不返修”

视频指出 tight component spacing 会让 probe、返修和更换器件变得困难。

课程不建立一个跨封装固定的“最小返修间距”，而要求 DFM/DFA Review 同时考虑：

- placement nozzle；
- AOI / X-ray line of sight；
- hot-air / soldering-iron access；
- tweezer access；
- nearby plastic connector heat sensitivity；
- tall-vs-short component shadowing；
- underfill / adhesive；
- rework fixture；
- risk of heating neighboring components。

所以元件间距由：

~~~text
package
+ assembly process
+ inspection
+ rework strategy
+ thermal sensitivity
+ board density
→ project spacing rule
~~~

“尽量留空间”是好直觉，但高密度产品不能靠一个固定 mm 数字解决。

## 2.5 Panel / Assembly Context

单板 DRC 可能完全通过，但拼板后仍可能有：

- connector interference；
- depanel stress；
- insufficient rail；
- tooling conflict；
- edge component damage。

所以 DFM/DFA 必须看实际制造流程。

### 2.5.1 Fiducial：不要背“2 个 + 1 mm Clearance”

视频建议至少两个 global fiducial、放在对角，并对 fine-pitch / BGA / QFN 考虑 local fiducial，同时给出 1 mm 周围 clearance 的经验值。

课程把它改写为：

> **Fiducial 的数量、尺寸、mask opening、keepout、位置与 local/global 策略必须由真实 assembly line / EMS 冻结。**

这是因为供应商规则会不同且会变化。

例如 JLCPCB 2026-05 的 Standard Assembly 指南当前推荐：

- 1 mm fiducial copper；
- solder-mask opening 为 exposed copper diameter 的 2×；
- board edge 上 3–4 个 fiducial；
- 并给出其自己的 board-edge clearance 规则。

而其 Economic/其他流程又可能由工厂自动补 fiducial / tooling / edge rail。

这些数字在本课程只能作为：

> **Supplier-specific current case**

不能写成 IPC 通用永恒规则。

### 2.5.2 Panelization / Depanelization 要在 Placement 之前考虑

视频强调：

- 小板 / 批量生产通常需要 panel；
- mouse-bite / V-score / tooling rail 会反向影响 layout；
- 错误 depaneling 会把机械应力送进 solder joint / connector。

课程落地为：

~~~text
EMS process
→ panel method
→ rail/tooling/fiducial
→ tab/V-score
→ component keepout
→ depanel stress path
→ inspection/rework
~~~

Review 时至少检查：

- panel size；
- rail / conveyor handling；
- tooling hole；
- global/local fiducial；
- V-score / tab route；
- component-to-break-line distance；
- connector overhang；
- MLCC / BGA / brittle component proximity；
- board support during depanel；
- depanel method；
- post-depanel inspection。

不要让 CM 在最后一刻“自己随便拼一个 panel”再倒逼 layout。

JLCPCB 当前公开的 edge-rail / tooling / panel 数字可以作为真实供应商案例，但每次下单前仍要重新确认当前 capability。

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
