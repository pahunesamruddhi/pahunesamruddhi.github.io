---
name: favicon-og-generator
description: "Generate favicons (all sizes), OG images, Twitter card images, and Apple touch icons. Use when user asks for favicon setup, OG image creation, social sharing images, or Apple touch icons."
---

You are generating favicons and social sharing images for a website.

## Favicon Setup

### Required Sizes
| File | Size | Purpose |
|------|------|---------|
| `favicon.ico` | 32x32 | Legacy browsers |
| `favicon-16x16.png` | 16x16 | Browser tabs |
| `favicon-32x32.png` | 32x32 | Browser tabs (Retina) |
| `apple-touch-icon.png` | 180x180 | iOS home screen |
| `android-chrome-192x192.png` | 192x192 | Android home screen |
| `android-chrome-512x512.png` | 512x512 | Android splash screen |

### HTML Head Tags
```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#000000">
```

### site.webmanifest
```json
{
  "name": "Site Name",
  "short_name": "Site",
  "icons": [
    { "src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#000000",
  "background_color": "#000000",
  "display": "standalone"
}
```

### Generation Tools
- **realfavicongenerator.net** — Upload SVG/PNG, generates all sizes + HTML
- **CLI**: `npx sharp-cli` to resize from source image
- **SVG favicon**: Modern browsers support `<link rel="icon" type="image/svg+xml" href="/favicon.svg">`

## Open Graph Images

### Specifications
| Platform | Recommended Size | Min Size | Ratio |
|----------|-----------------|----------|-------|
| Facebook/OG | 1200x630px | 600x315px | 1.91:1 |
| Twitter (large) | 1200x628px | 300x157px | ~2:1 |
| Twitter (summary) | 240x240px | 144x144px | 1:1 |
| LinkedIn | 1200x627px | 200x200px | 1.91:1 |

### HTML Tags
```html
<!-- Open Graph -->
<meta property="og:image" content="https://example.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Description of image">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://example.com/twitter-image.png">
<meta name="twitter:image:alt" content="Description of image">
```

### OG Image Design Guidelines
- Brand name/logo prominently displayed
- Clear, readable text (large font, high contrast)
- Consistent visual style across all pages
- Test at small sizes (appears as thumbnail in feeds)
- Use absolute URLs (required for social platforms)
- Image file size under 1MB

## Verification
- [ ] Favicon shows in browser tab
- [ ] Apple touch icon works on iOS "Add to Home Screen"
- [ ] OG image renders in Facebook Sharing Debugger
- [ ] Twitter Card renders in Twitter Card Validator
- [ ] site.webmanifest is valid JSON and accessible

## Best Used By
- **seo-specialist** — Social sharing optimization
- **ui-designer** — Favicon and OG image design
- **frontend-developer** — Meta tag implementation

## Related Skills
- `/seo-checklist` — Meta tag completeness
- `/asset-optimizer` — Image optimization
- `/website-launch-checklist` — Pre-launch favicon/OG verification
