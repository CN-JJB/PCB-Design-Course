# Reliability Validation Matrix

> 用于 Part 9 Production Release。不要把“做过一些可靠性测试”当作证据；每一项都必须绑定 mission profile、失效机制和判据。

## 1. Mission Profile

| Item | Requirement | Source | Notes |
|---|---|---|---|
| ambient temperature | TBD | | |
| humidity / condensation | TBD | | |
| vibration / shock | TBD | | |
| enclosure / airflow | TBD | | |
| duty cycle | TBD | | |
| power cycles | TBD | | |
| connector cycles | TBD | | |
| battery/storage | TBD | | |
| ESD/EFT/surge exposure | TBD | | |
| expected service life | TBD | | |

## 2. Validation Matrix

| ID | Requirement | Stress / Corner | Failure Mechanism | DUT Configuration | Method | Acceptance | Evidence | Result |
|---|---|---|---|---|---|---|---|---|
| REL-001 | | | | | | | | |
| REL-002 | | | | | | | | |
| REL-003 | | | | | | | | |

## 3. Suggested Coverage

### Thermal
- max ambient + max workload
- sealed enclosure
- regulator / MOSFET / MCU / capacitor hotspot
- long soak appropriate to requirement

### Power
- startup
- simultaneous subsystem startup
- low input / low battery
- fast load step
- brownout / recovery
- repeated power cycle

### Mechanical
- connector mate/unmate
- cable side load
- board flex / twist
- drop / vibration as required
- tall/heavy component support

### Environment
- humidity / condensation
- dust / contamination
- coating process if used
- corrosion / leakage monitoring

### Component Stress
- voltage/current/power/Tj
- capacitor DC bias / ripple / lifetime
- switching SOA / transient stress
- battery protection events

### PCB / Assembly
- critical solder joint inspection
- via-in-pad process verification if used
- laminate identity
- material substitution control

## 4. Finding Closure

For every failure:

~~~text
Stress
→ Symptom
→ Reproduction
→ Failure mechanism
→ Root cause
→ Fix
→ Side effect
→ Retest
→ ECO
→ Evidence
~~~

## 5. Release Decision

- [ ] All critical mission-profile corners covered
- [ ] Acceptance criteria defined before test
- [ ] Production-representative enclosure / mounting used where relevant
- [ ] Critical component derating reviewed
- [ ] Material / assembly process frozen
- [ ] All blocker/major findings closed or explicitly accepted
- [ ] Evidence paths recorded in release manifest
