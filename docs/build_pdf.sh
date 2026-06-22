#!/usr/bin/env bash
# Render a Markdown doc to PDF with the preferred academic look.
# Engine: typst (lightweight).  Font: Libertinus Serif, 11pt.
#
# Usage:  ./build_pdf.sh phd_meeting_brief.md        # -> phd_meeting_brief.pdf
#         ./build_pdf.sh                             # rebuilds phd_meeting_brief.md
#
# Notes:
#  - Markdown tables take column widths from the dash counts in the separator
#    row; keep them proportional (e.g. |-----|----------|--------|--------|).
#  - Block code (the ASCII tree) is shrunk to 7.5pt so wide lines don't overflow;
#    inline `code` stays full size.
set -euo pipefail

src="${1:-phd_meeting_brief.md}"
out="${src%.md}.pdf"

pandoc "$src" -o "$out" \
  --pdf-engine=typst \
  -V mainfont="Libertinus Serif" \
  -V monofont="DejaVu Sans Mono" \
  -V fontsize=11pt \
  --include-in-header=<(cat <<'TYP'
#set page(margin: (x: 1.6cm, y: 1.9cm))
#show raw.where(block: true): set text(size: 7.5pt)
TYP
)

echo "Built $out"
