---
name: seo-checklist
description: "Comprehensive SEO audit covering meta tags, OG/Twitter cards, structured data, sitemap.xml, robots.txt, and on-page factors. Use when user asks for SEO audit, meta tag review, or search optimization check."
---

You are running an SEO checklist audit. Work through each section systematically:

## SEO Checklist

### 1. Meta Tags (per page)
- [ ] `<title>` — Unique, 50-60 chars, includes primary keyword
- [ ] `<meta name="description">` — Unique, 150-160 chars, compelling
- [ ] `<meta name="viewport">` — `width=device-width, initial-scale=1.0`
- [ ] `<html lang="en">` — Language attribute set
- [ ] `<link rel="canonical">` — Self-referencing canonical URL

### 2. Open Graph Tags (per page)
- [ ] `og:title` — Page title for social sharing
- [ ] `og:description` — Description for social sharing
- [ ] `og:image` — 1200x630px image, absolute URL
- [ ] `og:url` — Canonical page URL
- [ ] `og:type` — "website" for homepage, "article" for posts
- [ ] `og:site_name` — Site name

### 3. Twitter Card Tags (per page)
- [ ] `twitter:card` — "summary_large_image" recommended
- [ ] `twitter:title` — Title for Twitter
- [ ] `twitter:description` — Description for Twitter
- [ ] `twitter:image` — Image URL (same as OG or Twitter-specific)

### 4. Structured Data
- [ ] Organization/Person schema (JSON-LD)
- [ ] WebSite schema with SearchAction (if applicable)
- [ ] BreadcrumbList schema (for multi-page sites)
- [ ] Article/CreativeWork schema (for case studies/blog)
- [ ] JSON-LD is valid (no syntax errors)

### 5. Content & Headings
- [ ] Single H1 per page
- [ ] Logical heading hierarchy (H1 → H2 → H3, no skips)
- [ ] Descriptive, keyword-rich headings
- [ ] All images have descriptive alt text
- [ ] Internal links between related pages
- [ ] No broken links (404s)

### 6. Technical SEO
- [ ] `sitemap.xml` exists and lists all public pages
- [ ] `robots.txt` exists and allows crawling
- [ ] HTTPS enabled (no mixed content)
- [ ] Mobile-friendly (responsive design)
- [ ] Page load time < 3 seconds
- [ ] No duplicate content (canonicals set)
- [ ] 404 page exists and is helpful

### 7. Performance (SEO-impacting)
- [ ] Core Web Vitals passing (LCP < 2.5s, CLS < 0.1)
- [ ] Images optimized (WebP, lazy loading)
- [ ] No render-blocking resources
- [ ] Text content loads without JavaScript (for crawlability)

## Report Format

Present findings as:
- ✅ Passing items
- ⚠️ Warnings (improvable)
- ❌ Failing items (must fix)

Include specific recommendations for each failing item.

## Best Used By
- **seo-specialist** — Comprehensive SEO auditing
- **content-strategist** — Content-SEO alignment
- **frontend-developer** — Implementation of SEO fixes

## Related Skills
- `/lighthouse-audit` — Automated SEO scoring
- `/favicon-og-generator` — OG image creation
- `/website-launch-checklist` — Pre-launch SEO gate
