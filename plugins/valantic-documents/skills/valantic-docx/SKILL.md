---
name: valantic-docx
description: Generate branded Word documents (proposals, reports, specifications) following Valantic's Liquid Brand Design with correct styles, colors, and formatting.
---

# Valantic DOCX Generation

## When to Use

Activate this skill when the user asks to create a Word document — proposals, specifications, reports, or business documents — that should follow Valantic branding.

## Document Standards

### Page Setup

- **Page Size**: A4 (210mm × 297mm)
- **Margins**: Top 2.5cm, Bottom 2cm, Left 2.5cm, Right 2cm
- **Header**: Company name or document type, Segoe UI Regular 9pt
- **Footer**: Page number centered or right-aligned

### Typography (Word)

- **Font**: Segoe UI (Calibre not standard in Word)
- **Heading 1**: Segoe UI Semibold, 20pt, Coral `#FF5757`
- **Heading 2**: Segoe UI Semibold, 16pt, Coral `#FF5757`
- **Heading 3**: Segoe UI Semibold, 13pt, Dark `#1A1A1A`
- **Heading 4**: Segoe UI Semibold, 11pt, Dark `#1A1A1A`
- **Body / Normal**: Segoe UI Regular, 11pt, Primary `#333333`, 1.15 line spacing
- **NEVER use Segoe UI Bold** — use Semibold instead

### Style Definitions

Define these Word styles programmatically:

| Style Name | Font | Size | Color | Weight |
|-----------|------|------|-------|--------|
| Heading 1 | Segoe UI | 20pt | `#FF5757` | Semibold |
| Heading 2 | Segoe UI | 16pt | `#FF5757` | Semibold |
| Heading 3 | Segoe UI | 13pt | `#1A1A1A` | Semibold |
| Heading 4 | Segoe UI | 11pt | `#1A1A1A` | Semibold |
| Normal | Segoe UI | 11pt | `#333333` | Regular |
| Quote | Segoe UI | 11pt | `#FF5757` | Italic |
| Author | Segoe UI | 11pt | `#FF5757` | Semibold |

### Table Formatting

- Header row: `#F8F8F8` background, Segoe UI Semibold
- Body rows: Alternating white / `#FAFAFA`
- Border: Thin (0.5pt) `#DDDDDD`
- No outer border emphasis

### Cover Page

- Top: Valantic logo (if available)
- Title: Segoe UI Semibold, 28pt, Coral
- Subtitle/description: Segoe UI Regular, 14pt, Dark
- Author, date, version info block
- Optional: Coral accent line (2pt) separating title from metadata

## Implementation

Use `python-docx` for document generation:

```python
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

CORAL = RGBColor(0xFF, 0x57, 0x57)
TEXT_DARK = RGBColor(0x1A, 0x1A, 0x1A)
TEXT_PRIMARY = RGBColor(0x33, 0x33, 0x33)
```

## Checklist

- [ ] A4 page size with correct margins
- [ ] Word styles defined (Heading 1-4, Normal, Quote)
- [ ] Segoe UI Semibold for headings (never Bold)
- [ ] Heading colors: H1/H2 Coral, H3/H4 Dark
- [ ] Table formatting with light header background
- [ ] Cover page with title and metadata
- [ ] Header/footer configured
