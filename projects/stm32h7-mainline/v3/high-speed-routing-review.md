
# V3 High-Speed Routing Review

> Review unit = complete electrical channel, not a routing screenshot. Fill one row per critical net/group.

## 1. Screening / Interface

| Group | Interface / Function | Edge / Data Source | Topology | Why High-Speed | Evidence |
|---|---|---|---|---|---|
| FMC_SDCLK | | | | | |
| FMC_DQ/DQM | | | | | |
| FMC_ADDR_CTRL | | | | | |
| RMII_REF_CLK | | | | | |
| ETH_MDI | | | | | |
| USB | | | | | |

## 2. Stackup / Reference / Impedance

| Group | Routing Layer | Reference | H | Target Z | Width / Gap | Geometry Source | Continuous Ref? |
|---|---|---|---:|---:|---|---|---|
| | | | | | | | |

## 3. Crosstalk / Routing Density

| Group | Aggressor / Victim | Min S/H | Longest Parallel Length | Edge Rate | Noise Budget / Reason | Solver / Evidence |
|---|---|---:|---:|---|---|---|
| | | | | | | |

3H / 3W may be used only as screening geometry. PASS requires a project noise/timing reason.

## 4. Via / Reference Transition

| Group | Via Count | Start→End Layer | Drill Span | Unused Stub | Return Transition | Pad / Antipad Review | Result |
|---|---:|---|---|---|---|---|---|
| | | | | | | | |

Review questions:

- Is the via required?
- Is barrel length minimized by layer choice?
- Is a small via being chosen for capacitance/density rather than the false assumption that smaller diameter always means lower inductance?
- Are nearby GND/reference vias placed because a return transition is actually required?
- Do antipads create a reference-plane neck or slot?
- For differential vias, are P/N and return structures symmetric?

## 5. Differential / Timing

### Intra-pair

| Pair | P delay | N delay | Skew | Requirement Source | Local discontinuity compensation | Result |
|---|---:|---:|---:|---|---|---|
| | | | | | | |

### Inter-pair / Clock-to-Data / Lane-to-Lane

| Group | Relationship | Electrical Delay Budget | Package Delay Included? | PCB Budget | Result |
|---|---|---|---|---|---|
| | | | | | |

Do not force every differential lane to identical copper length unless the interface timing model actually requires it.

## 6. Channel Discontinuities

| Group | Package | Connector | ESD / Magnetics | Neck-down | Layer Change | Test Access | Evidence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 7. SI / EMC Evidence

- DRC report:
- reference-plane overlay:
- length / delay report:
- IBIS / channel simulation:
- TDR / VNA:
- oscilloscope / eye:
- near-field / pre-compliance:
- unresolved assumptions:

## 8. Gate

- [ ] no critical signal crosses unexplained reference discontinuity
- [ ] impedance geometry comes from current stackup
- [ ] crosstalk spacing has a budget, not only a rule of thumb
- [ ] via transitions include return-path review
- [ ] unused stubs are identified from actual drill span
- [ ] differential intra-pair skew has a source
- [ ] lane-to-lane / clock-data timing has a separate source
- [ ] connector / package / protection discontinuities are included
- [ ] evidence path recorded

Decision:

- [ ] PASS
- [ ] PASS WITH ACTIONS
- [ ] FAIL
