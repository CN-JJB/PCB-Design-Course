# STM32F407 V1｜Power / Clock / Boot / Debug Plan

## 1. Power tree

~~~text
5V_IN
  ↓
Protection / input network: TBD
  ↓
AP2112K-3.3 teaching candidate
  ↓
3V3_MAIN
  ├─ MCU VDD
  ├─ VDDA branch
  ├─ LEDs
  └─ expansion allowance
~~~

## 2. Regulator budget

| Item | Value | Source |
|---|---:|---|
| Vin min/max | TBD | system |
| Vout | 3.3 V | system |
| estimated avg current | TBD | system-spec |
| design max current | TBD | system-spec |
| dropout/headroom | TBD | regulator DS |
| power dissipation | TBD | calculation |
| thermal assumption | TBD | PCB/layout |
| junction estimate | TBD | calculation |
| CIN requirement | TBD | DS |
| COUT requirement | TBD | DS |

Gate 2 不能只写“LDO 额定 600 mA”。

## 3. MCU supply checklist

- [ ] all VDD/VSS pins accounted for
- [ ] local decoupling mapped to pins
- [ ] package bulk planned
- [ ] VDDA/VSSA strategy
- [ ] VCAP1/2 exact requirement
- [ ] VBAT default state
- [ ] PVD/BOR firmware assumptions documented if relevant

## 4. Clock plan

| Stage | Source | Target | Why |
|---|---|---:|---|
| Bring-up 1 | internal RC | safe baseline | remove HSE variable |
| Bring-up 2 | HSE | TBD exact | project clock |
| PLL/SYSCLK | TBD | within device requirement | firmware plan |

### HSE selection

- exact part: TBD
- frequency: TBD
- load capacitance / oscillator mode: TBD
- tolerance/temperature: TBD
- startup requirement: TBD
- PCB keep-local rule: yes

## 5. Boot / Reset / Debug

| Signal | Default / strategy | Verification |
|---|---|---|
| BOOT0 | known Flash-boot default | DMM / schematic |
| NRST | manual + SWD accessible | scope / debugger |
| SWDIO | dedicated debug | ST-LINK |
| SWCLK | dedicated debug | ST-LINK |
| VTREF | 3V3 target reference | DMM |
| GND | low-impedance return | continuity |
| UART | console | terminal |

## 6. Gate 2 Pass

- [ ] regulator thermal budget exists
- [ ] MCU supply pins reviewed
- [ ] internal-clock first bring-up decided
- [ ] HSE requirement defined
- [ ] BOOT/RESET/SWD/UART usable
- [ ] no blocker TBD before schematic

通过后进入：[schematic-review.md](schematic-review.md)
