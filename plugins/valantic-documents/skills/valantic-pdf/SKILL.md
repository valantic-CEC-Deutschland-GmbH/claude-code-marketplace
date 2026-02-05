---
name: valantic-pdf
description: Generate branded PDF documents (reports, whitepapers, proposals) following Valantic's Liquid Brand Design with correct colors, typography, and layout.
---

# Valantic PDF Generation

## When to Use

Activate this skill when the user asks to create a PDF document — reports, whitepapers, proposals, or data sheets — that should follow Valantic branding.

## PDF Standards

### Page Layout

- **Page Size**: A4 (210mm × 297mm)
- **Margins**: Top 25mm, Bottom 20mm, Left 25mm, Right 20mm
- **Header**: Running header in uppercase, e.g., "WHITEPAPER | TOPIC NAME"
- **Footer**: Page number right-aligned, optional Valantic logo left

### Typography

- **Font**: Calibre (embed in PDF) with Segoe UI fallback
- **H1**: Calibre Light (300), 24pt, Coral `#FF5757`
- **H2**: Calibre Light (300), 18pt, Coral `#FF5757`
- **H3**: Calibre Semibold (600), 14pt, Dark `#1A1A1A`
- **H4**: Calibre Semibold (600), 12pt, Dark `#1A1A1A`
- **Body**: Calibre Regular (400), 10pt, Primary `#333333`, line-height 1.6
- **Pull Quotes**: Calibre Regular Italic, 12pt, Coral `#FF5757`

### Color Usage

- Accent borders on callout boxes: 4pt left border
  - Highlight: Coral `#FF5757` with `#fff5f5` background
  - Info: Blue `#4A9EFF` with `#f0f8ff` background
  - Warning: Orange `#FF9800` with `#fff8f0` background
- Table headers: `#F8F8F8` background, Semibold text
- Chart primary: Coral, secondary: `#999999`

### Cover Page

- Top section: Valantic gradient (315°, Coral → Peach)
- Title: White, Calibre Light, 36pt
- Subtitle: White, Calibre Regular, 18pt
- Author/date block below gradient section

### Table of Contents

- Section numbers in Coral
- Page numbers right-aligned with dot leaders
- Max 2 levels of nesting

## Implementation

Use `reportlab` or `weasyprint` for PDF generation:

```python
# ReportLab example
from reportlab.lib.colors import HexColor

CORAL = HexColor('#FF5757')
PURPLE = HexColor('#4C26B7')
PEACH = HexColor('#FFCCAA')
TEXT_PRIMARY = HexColor('#333333')
TEXT_DARK = HexColor('#1A1A1A')
```

## Checklist

- [ ] A4 page size with correct margins
- [ ] Cover page with gradient header
- [ ] Fonts embedded (Calibre preferred, Segoe UI fallback)
- [ ] Heading hierarchy: H1/H2 Coral Light, H3/H4 Dark Semibold
- [ ] Running header on all pages (except cover)
- [ ] Callout boxes with correct border colors
- [ ] Charts use Coral as primary data color
