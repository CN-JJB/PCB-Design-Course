# V3 Stackup Decision Record

Status: `DRAFT`

## Manufacturer Candidate

- Manufacturer:
- Stackup ID:
- Query date:
- Finished thickness:
- Outer / inner copper:
- Material / Tg:

## Candidate Comparison

| Candidate | Layer roles | L1 ref | inner signal ref | L6 ref | PWR split risk | Impedance layers | Margin | Result |
|---|---|---|---|---|---|---|---|---|
| A | | | | | | | | |
| B | | | | | | | | |

## Signal–Reference Pair Map

> 先填这个表，再决定“L3 是高速层”或“L4 是 power layer”。层号不是 reference 的证据。

| Signal layer | Candidate reference(s) | Dielectric H | Primary reference judgment | Continuous? | Transition to next layer | Evidence |
|---|---|---:|---|---|---|---|
| L1 | L2 | | | | | |
| L3 | L2 / L4 | | | | | |
| L4 | L3 / L5 | | | | | |
| L6 | L5 | | | | | |

## Why This Is 6 Layers, Not a Copied Textbook Pattern

- [ ] actual fab stackup geometry has been read, not inferred from a generic diagram
- [ ] no assumption that L1/L2/L3 form a tightly coupled triplet unless H confirms it
- [ ] pair-coupling / asymmetry is reflected in layer-role assignment
- [ ] every critical layer has an explicit reference plane
- [ ] inner power polygons do not sit in the dominant field region of critical traces unless intentionally modeled
- [ ] stackup symmetry / copper balance has been reviewed with fab

### Practitioner Debate Context

The following threads are used only to stress-test the decision:

- https://electronics.stackexchange.com/questions/676466/6-layer-stack-up-optimal-core-prepreg-thinkness-and-coupling-to-gnd
- https://electronics.stackexchange.com/questions/576750/6-layer-stackup-where-to-put-the-power-planes
- https://electronics.stackexchange.com/questions/427747/best-layer-stack-strategy-for-a-6-layer-pcb-with-mostly-smd-components

Decision rule:

> If a forum recommendation cannot be translated into actual H / reference / routing / transition geometry for this fab stackup, it does not enter the frozen design.


## Manufacturing Model Identity

| Item | Frozen value | Source | Recheck before order | Result |
|---|---|---|---|---|
| Fab stackup template ID | | | yes | |
| Calculator material family | | | yes | |
| Order material / Tg option | | | yes | |
| Outer finished copper | | | yes | |
| Inner finished copper | | | yes | |
| Soldermask model | | | yes | |
| Fabricator allowed to adjust width? | | CAM agreement | yes | |
| Fabricator allowed to adjust dielectric? | | CAM agreement | yes | |

## Impedance Acceptance Plan

| Structure | Target | Tolerance | Coupon | TDR/report | Acceptance owner |
|---|---:|---:|---|---|---|
| USB | | | | | |
| Ethernet | | | | | |
| Memory / clock | | | | | |

Freeze rule:

> Calculator model、订单材料、stackup ID 和 CAM 权限只要有一项变化，就 reopen impedance calculation，而不是只改文档版本号。


## Controlled Impedance

| Net class | Layer | Target | Tolerance | Width | Gap | Calculator/source | CAM confirm |
|---|---|---|---|---|---|---|---|
| USB | | | | | | | |
| Ethernet | | | | | | | |
| Memory clock | | | | | | | |

## Freeze / Reopen Conditions

- stackup ID changes
- copper weight changes
- MCU/package changes
- PHY/SDRAM changes
- layer role changes
- controlled-impedance target changes

Decision: `TBD`