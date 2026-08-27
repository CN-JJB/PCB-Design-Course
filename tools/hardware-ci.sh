#!/usr/bin/env bash
set -euo pipefail

mkdir -p ci-reports

echo "KiCad:"
kicad-cli version

found=0

while IFS= read -r -d '' sch; do
  found=1
  safe="$(echo "$sch" | tr '/ ' '__')"
  echo "::group::ERC $sch"
  kicad-cli sch erc --exit-code-violations -o "ci-reports/${safe}.erc.rpt" "$sch"
  echo "::endgroup::"
done < <(find projects -type f -name '*.kicad_sch' -print0)

while IFS= read -r -d '' pcb; do
  found=1
  safe="$(echo "$pcb" | tr '/ ' '__')"
  echo "::group::DRC $pcb"
  kicad-cli pcb drc --exit-code-violations --schematic-parity -o "ci-reports/${safe}.drc.rpt" "$pcb"
  echo "::endgroup::"
done < <(find projects -type f -name '*.kicad_pcb' -print0)

if [[ "$found" -eq 0 ]]; then
  echo "No KiCad schematic/PCB source is committed yet."
  echo "CI infrastructure is ready; project status remains Engineering Draft."
fi
