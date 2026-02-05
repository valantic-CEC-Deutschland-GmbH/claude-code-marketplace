---
name: valantic-pptx
description: Create branded PowerPoint presentations following Valantic's Liquid Brand Design system with proper slide layouts, colors, and typography.
---

# Valantic PPTX Generation

## When to Use

Activate this skill when the user asks to create a PowerPoint presentation, slide deck, or `.pptx` file that should follow Valantic branding.

## Presentation Standards

### Slide Layout Structure

1. **Title Slide**: Full gradient background (Coral → Peach, 315°), white text, Valantic logo placement top-right
2. **Section Divider**: Coral accent bar left, section title in Coral Light (300), subtitle in Dark Text
3. **Content Slide**: White background, heading in Coral, body in Primary Text (`#333333`)
4. **Two-Column Slide**: Equal columns with thin Coral divider line
5. **Closing Slide**: Gradient background matching title slide, contact information

### Typography (PowerPoint)

- **Font**: Segoe UI (Calibre not available in Office)
- **Title**: Segoe UI Semibold, 28pt, Coral `#FF5757`
- **Subtitle**: Segoe UI Regular, 18pt, Dark `#1A1A1A`
- **Body**: Segoe UI Regular, 14pt, Primary `#333333`
- **Captions**: Segoe UI Regular, 10pt, `#666666`
- **NEVER use Segoe UI Bold** — use Semibold instead

### Visual Route Selection

Choose the route based on the audience (default to Route B):

- **Route A**: Minimal graphics, formal layout, Purple Heart accents
- **Route B**: Circular portrait masks, human imagery, Coral accents (default)
- **Route C**: Dynamic V-shaped masks, bold imagery, gradient fills

### Slide Dimensions

- Standard: 16:9 (33.867cm × 19.05cm)
- Margins: 1.5cm on all sides

### Color Usage in Slides

- Chart primary color: Coral `#FF5757`
- Chart secondary: `#999999`
- Table headers: Light Background `#F8F8F8` with Semibold text
- Accent elements: Use gradient sparingly

## Implementation

Use `python-pptx` to generate presentations programmatically. Reference template files in `templates/` directory if available.

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# Valantic brand colors
CORAL = RGBColor(0xFF, 0x57, 0x57)
PURPLE = RGBColor(0x4C, 0x26, 0xB7)
PEACH = RGBColor(0xFF, 0xCC, 0xAA)
TEXT_PRIMARY = RGBColor(0x33, 0x33, 0x33)
TEXT_DARK = RGBColor(0x1A, 0x1A, 0x1A)
BG_LIGHT = RGBColor(0xF8, 0xF8, 0xF8)
```

## Checklist

- [ ] Route selected (A/B/C) — default B
- [ ] Segoe UI Semibold for headings (never Bold)
- [ ] Coral for H1/H2, Dark for H3/H4
- [ ] 16:9 aspect ratio
- [ ] Gradient used only on title/closing slides
- [ ] Charts use Coral as primary data color
