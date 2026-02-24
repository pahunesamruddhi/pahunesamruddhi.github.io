---
name: design-token-extractor
description: "Extract design tokens from Figma or CSS into reusable CSS variables, JSON, or JS format. Use when user asks to extract design tokens, create design variables, standardize design values, or export from Figma."
---

You are extracting and organizing design tokens from existing CSS or design files.

## What Are Design Tokens

Design tokens are the atomic values that define a design system:
- **Colors**: Brand, semantic, surface, text colors
- **Typography**: Font families, sizes, weights, line heights
- **Spacing**: Margin/padding values, gap sizes
- **Borders**: Widths, styles, radii
- **Shadows**: Box shadows, text shadows
- **Transitions**: Durations, easing functions
- **Breakpoints**: Responsive width thresholds

## Extraction Process

### Step 1: Audit Existing CSS
- Find all CSS custom properties (`:root` variables)
- Identify hardcoded values that should be tokens
- Look for repeated values across rules
- Catalog all colors, sizes, and fonts used

### Step 2: Organize into Token Categories

**Primitive tokens** (raw values):
```css
:root {
  --color-black: #000000;
  --color-orange-500: #ff5500;
  --font-size-16: 1rem;
  --space-4: 4px;
}
```

**Semantic tokens** (purpose-based):
```css
:root {
  --color-bg-primary: var(--color-black);
  --color-accent: var(--color-orange-500);
  --color-text-primary: var(--color-white);
  --font-size-body: var(--font-size-16);
  --space-component-padding: var(--space-4);
}
```

**Component tokens** (component-specific):
```css
:root {
  --card-bg: var(--color-bg-primary);
  --card-radius: var(--radius-standard);
  --card-shadow: var(--shadow-card);
  --button-bg: var(--color-accent);
}
```

### Step 3: Export Formats

**CSS Custom Properties** (default for static sites):
```css
:root { --color-accent: #ff5500; }
```

**JSON** (for build tools, CMS, multi-platform):
```json
{
  "color": {
    "accent": { "value": "#ff5500", "type": "color" }
  }
}
```

**JavaScript/TypeScript** (for JS frameworks):
```js
export const tokens = {
  color: { accent: '#ff5500' },
  spacing: { sm: '8px', md: '16px' }
};
```

### Step 4: Documentation

Create a token reference showing:
- Token name
- Value (visual swatch for colors)
- Where it's used
- Light/dark mode variants (if applicable)

## Best Practices
- Name tokens by purpose, not appearance (`--color-accent` not `--color-orange`)
- Use a consistent naming convention (kebab-case for CSS, camelCase for JS)
- Layer tokens: primitive → semantic → component
- Keep the token set minimal — don't tokenize everything
- Document every token's intended use

## Best Used By
- **ui-designer** — Design system token management
- **frontend-developer** — Token implementation
- **motion-designer** — Animation token values

## Related Skills
- `/lighthouse-audit` — Verify tokens don't increase CSS size
- `/browser-testing` — Cross-browser CSS variable support
- `/client-handoff` — Design token documentation for handoff
