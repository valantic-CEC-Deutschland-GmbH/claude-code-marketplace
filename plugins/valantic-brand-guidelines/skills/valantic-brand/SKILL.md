---
name: valantic-brand
description: Applies Valantic's "Liquid Brand Design" system, including specific visual routes (A, B, C), official colors, typography, and office/web standards.
---

# Valantic Brand Styling

## Overview

To access Valantic's official brand identity resources, use this skill. This includes the **Liquid Brand Design** system, which adapts the visual language to specific target groups while maintaining the **One Firm** identity.

**Keywords**: Liquid Brand Design, Route A, Route B, Route C, valantic gradient, Segoe UI, Calibre, visual identity, One Firm

---

## 1. Liquid Brand Design Strategy

The Valantic brand operates on a flexible **Liquid Brand Design** model. This allows for distinct visual communication depending on the target group and touchpoint.

### Visual Routes (The A–B–C System)

Select the appropriate route based on the audience and message intensity.

#### Route A: Restrained & Elegant

- **Attributes**: Restrained, elegant, informative, serious
- **Target Audience**: Conservative industries (Banking, Insurance), high-probity services (Finance, Legal, Data Privacy)
- **Use Cases**: Invoices, data sheets, formal reporting
- **Visual Style**: Standard layouts, minimal distraction

#### Route B: Self-Confident & Human (Standard)

- **Attributes**: Self-confident, activating, human, approachable
- **Status**: **Default choice** (covers ~80% of use cases)
- **Target Audience**: Agile customers (IT, Automotive, Manufacturing), internal communications
- **Use Cases**: Project updates, team presentations, general communication
- **Visual Style**: Circular portrait mask ("Route B Shape") emphasizing the human element

#### Route C: Dynamic & Expressive

- **Attributes**: Dynamic, present, expressive, bold
- **Target Audience**: Marketing, start-ups, recruiting (talent acquisition)
- **Use Cases**: Fairs, events, zeitgeist-sensitive industries (e-commerce, tourism)
- **Visual Style**: Irregular "Valantic V" polygon mask with high visual energy

---

## 2. Design Tokens & Colors

### Primary Brand Colors

- **Valantic Coral**: `#FF5757` — primary accent for headings, links, and highlights
- **Purple Heart**: `#4C26B7` — secondary anchor (deep blue-purple, used sparingly)
- **Peach**: `#FFCCAA` — secondary accent, primarily used in gradients

### Utility Colors

- **Info Blue**: `#4A9EFF` — informational callouts and tips
- **Warning Orange**: `#FF9800` — warnings and important notices

### Text Colors

- **Primary Text**: `#333333` — body text
- **Dark Text**: `#1A1A1A` — emphasized text, subheadings
- **Light Background**: `#F8F8F8` — intro sections, table headers

### The Valantic Gradient

The gradient adds depth and recognition without overwhelming content.

- **Colors**: Valantic Coral (`#FF5757`) → Peach (`#FFCCAA`)
- **Angle**: `315°` (top-left to bottom-right)
- **Usage**: Shapes, active elements, selected icons

---

## 3. Typography System

### Digital & Web Standard

- **Font Family**: Calibre
- **Fallbacks**: Segoe UI, Helvetica, Arial, sans-serif
- **Weights**:
  - H1/H2 (Section Titles): Light (300) — CORAL color
  - H3/H4 (Subsections): Semibold/Bold (600) — BLACK color
  - Body: Regular (400)

### Heading Hierarchy

| Level | Color | Weight | Example |
|-------|-------|--------|---------|
| H1 | `#FF5757` Coral | 300 (Light) | Main document titles |
| H2 | `#FF5757` Coral | 300 (Light) | Section headings |
| H3 | `#1A1A1A` Black | 600 (Semibold) | Subsection headings |
| H4 | `#1A1A1A` Black | 600 (Semibold) | Detail headings |

### Special Text Styles

- **Pull Quotes**: Coral (`#FF5757`), italic
- **Person Names**: Coral (`#FF5757`), bold
- **Running Header**: Black, uppercase

### Office & Presentation Standard (PowerPoint / Word)

When proprietary fonts are unavailable, use **Segoe UI**.

- **Rule**: **Do not use Segoe UI Bold** (poor proportions on Windows)
- **Correct Usage**: Use **Segoe UI Semibold** for headings and emphasized text

---

## 4. Iconography & Imagery

### Icon Style

- **Source**: Microsoft Stock Icons (Thin style)
- **Coloring**:
  - Default: Valantic Coral (`#FF5757`)
  - Route-specific: Purple Heart (`#4C26B7`) for formal contexts
  - Highlights: Apply the valantic gradient (315°) selectively

### Generative Image Workflow

- **Requirement**: Header images (especially Route C) must use **Generative Fill** to extend the canvas horizontally
- **Goal**: Prevent cropping of faces or subjects when applying irregular Valantic masks

---

## 5. Technical Implementation Details

### CSS Variables (Web)

```css
:root {
  /* Primary Brand Colors */
  --valantic-coral: #FF5757;
  --valantic-purple: #4C26B7;
  --valantic-peach: #FFCCAA;

  /* Utility Colors */
  --valantic-info: #4A9EFF;
  --valantic-warning: #FF9800;

  /* Text Colors */
  --text-primary: #333333;
  --text-dark: #1A1A1A;
  --bg-light: #F8F8F8;

  /* Gradient */
  --valantic-gradient: linear-gradient(
    315deg,
    #FF5757 0%,
    #FFCCAA 100%
  );

  /* Typography */
  --font-primary: "Calibre", "Segoe UI", Helvetica, Arial, sans-serif;
}

h1, h2 {
  color: var(--valantic-coral);
  font-weight: 300;
}

h3, h4 {
  color: var(--text-dark);
  font-weight: 600;
}

p {
  color: var(--text-primary);
  line-height: 1.6;
}

a {
  color: var(--valantic-coral);
  text-decoration: none;
}

.pull-quote, blockquote.highlight {
  color: var(--valantic-coral);
  font-style: italic;
}

.author-name {
  color: var(--valantic-coral);
  font-weight: 600;
}

.highlight-box {
  border-left: 4pt solid var(--valantic-coral);
  background: #fff5f5;
  padding: 12pt 12pt 12pt 15pt;
}

.info-box {
  border-left: 4pt solid var(--valantic-info);
  background: #f0f8ff;
  padding: 12pt 12pt 12pt 15pt;
}

.warning-box {
  border-left: 4pt solid var(--valantic-warning);
  background: #fff8f0;
  padding: 12pt 12pt 12pt 15pt;
}

th {
  background: var(--bg-light);
  font-weight: 600;
}

.chart-primary { fill: var(--valantic-coral); }
.chart-secondary { fill: #999999; }
```

## List Formatting (Presentations)

- Levels 1–3: Standard bullets
- Level 4:
  - Bold Coral (Route B / C)
  - Black (Route A)
    Used as subheadings within lists

---

## 6. Quick Reference

### Color Palette

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Valantic Coral | `#FF5757` | 255, 87, 87 | H1/H2 headings, links, quotes, accents |
| Purple Heart | `#4C26B7` | 76, 38, 183 | Secondary brand, formal contexts |
| Peach | `#FFCCAA` | 255, 204, 170 | Gradient end, soft backgrounds |
| Info Blue | `#4A9EFF` | 74, 158, 255 | Info callouts |
| Warning Orange | `#FF9800` | 255, 152, 0 | Warning callouts |
| Text Primary | `#333333` | 51, 51, 51 | Body text |
| Text Dark | `#1A1A1A` | 26, 26, 26 | H3/H4 headings, bold text |
| Background Light | `#F8F8F8` | 248, 248, 248 | Intro boxes, table headers |

### Element Quick Reference

| Element | Color | Weight | Style |
|---------|-------|--------|-------|
| H1, H2 | Coral `#FF5757` | 300 | Normal |
| H3, H4 | Black `#1A1A1A` | 600 | Normal |
| Body | Gray `#333333` | 400 | Normal |
| Pull Quote | Coral `#FF5757` | 400 | Italic |
| Author Name | Coral `#FF5757` | 600 | Normal |
| Links | Coral `#FF5757` | - | No underline |
| Chart Bars | Coral `#FF5757` | - | Primary data |
