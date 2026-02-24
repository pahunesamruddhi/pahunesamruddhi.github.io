---
name: asset-optimizer
description: "Bulk image compression, WebP/AVIF conversion, responsive srcset generation, and asset optimization. Use when user asks to optimize images, compress assets, convert to WebP, or generate responsive images."
---

You are optimizing website assets for performance. Follow this process:

## Asset Audit

### Step 1: Inventory
- List all images with format, dimensions, and file size
- Identify oversized images (>200KB for web, >50KB for icons/thumbnails)
- Check for missing responsive variants

### Step 2: Image Optimization

**Format conversion priority:**
1. AVIF (best compression, growing support)
2. WebP (excellent compression, broad support)
3. Optimized JPEG/PNG (fallback)

**Using CLI tools:**
```bash
# Install if needed
brew install webp libavif

# Convert to WebP
cwebp -q 80 input.png -o output.webp

# Convert to AVIF
avifenc input.png output.avif --min 20 --max 40

# Optimize JPEG
jpegoptim --max=85 --strip-all image.jpg

# Optimize PNG
optipng -o5 image.png
```

**Using Sharp (Node.js):**
```bash
npx sharp-cli --input "assets/*.{png,jpg}" --output "assets/optimized/" --webp
```

### Step 3: Responsive Images

Generate srcset variants at common breakpoints:
- 320w (mobile)
- 640w (tablet)
- 960w (desktop)
- 1280w (large desktop)
- 1920w (full HD, only for hero images)

Implement with `<picture>` element:
```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description" loading="lazy" width="800" height="600">
</picture>
```

### Step 4: Additional Optimizations
- Add `loading="lazy"` to all below-fold images
- Add `fetchpriority="high"` to LCP image
- Set explicit `width` and `height` to prevent CLS
- Inline small SVGs instead of loading as files
- Use CSS `background-image` only when semantic `<img>` isn't appropriate

## Quality Checks
- All images under 200KB (under 100KB preferred)
- WebP versions exist for all raster images
- All `<img>` tags have width, height, and alt attributes
- Hero/LCP images are preloaded, not lazy-loaded

## Best Used By
- **performance-optimizer** — Image performance optimization
- **frontend-developer** — Responsive image implementation
- **ui-designer** — Asset preparation

## Related Skills
- `/lighthouse-audit` — Measure image performance impact
- `/favicon-og-generator` — Optimized favicon and OG images
- `/browser-testing` — Cross-browser image format support
