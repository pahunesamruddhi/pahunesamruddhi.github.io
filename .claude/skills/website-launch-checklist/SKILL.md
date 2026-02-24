---
name: website-launch-checklist
description: "Comprehensive pre-launch validation covering broken links, 404s, SSL, analytics, SEO, forms, accessibility, and performance. Use when user asks for launch checklist, pre-launch check, go-live validation, or site readiness."
---

You are running a pre-launch checklist for a website. Work through every section:

## Website Launch Checklist

### 1. Content ✏️
- [ ] All placeholder/lorem ipsum text replaced
- [ ] Spelling and grammar checked on all pages
- [ ] Contact information is correct (email, phone, address)
- [ ] Copyright year is current
- [ ] Legal pages present (Privacy Policy, Terms if needed)
- [ ] All images have alt text
- [ ] No broken internal links
- [ ] No broken external links
- [ ] 404 page exists and is helpful

### 2. SEO 🔍
- [ ] Unique `<title>` on every page (50-60 chars)
- [ ] Unique `<meta description>` on every page (150-160 chars)
- [ ] Single `<h1>` per page
- [ ] `<html lang="en">` attribute set
- [ ] Canonical URLs set
- [ ] Open Graph tags on all pages
- [ ] Twitter Card tags on all pages
- [ ] Structured data (JSON-LD) valid
- [ ] `sitemap.xml` generated and submitted
- [ ] `robots.txt` allows crawling

### 3. Performance ⚡
- [ ] Lighthouse Performance score ≥ 90
- [ ] Images optimized (WebP, compressed, lazy loaded)
- [ ] CSS and JS minified
- [ ] No render-blocking resources
- [ ] Fonts optimized (font-display: swap, preconnected)
- [ ] Core Web Vitals passing (LCP < 2.5s, CLS < 0.1)

### 4. Accessibility ♿
- [ ] Lighthouse Accessibility score ≥ 90
- [ ] Color contrast passes WCAG AA (4.5:1)
- [ ] Keyboard navigation works throughout
- [ ] Focus indicators visible
- [ ] Skip navigation link present
- [ ] Forms have proper labels and error messages
- [ ] `prefers-reduced-motion` respected

### 5. Functionality 🔧
- [ ] All forms submit correctly
- [ ] Form validation works (client + server)
- [ ] Form spam protection active
- [ ] Contact/email links work
- [ ] Social media links work and open in new tab
- [ ] Download links work (resume, PDFs)
- [ ] No JavaScript console errors
- [ ] No mixed content warnings (HTTP on HTTPS)

### 6. Cross-Browser & Responsive 📱
- [ ] Chrome (desktop + mobile) ✓
- [ ] Safari (desktop + iOS) ✓
- [ ] Firefox (desktop) ✓
- [ ] Responsive at 320px, 768px, 1024px, 1440px
- [ ] No horizontal scrollbar at any breakpoint
- [ ] Touch targets ≥ 44x44px on mobile

### 7. Analytics & Tracking 📊
- [ ] Google Analytics 4 installed and receiving data
- [ ] Custom events firing correctly
- [ ] Search Console property verified
- [ ] Sitemap submitted to Search Console

### 8. Security & Infrastructure 🔒
- [ ] HTTPS enabled, no mixed content
- [ ] SSL certificate valid and auto-renewing
- [ ] HTTP → HTTPS redirect working
- [ ] www → non-www redirect (or vice versa) consistent
- [ ] Custom domain configured and resolving
- [ ] DNS records correct
- [ ] Favicon showing in browser tab

### 9. Assets & Branding 🎨
- [ ] Favicon (all sizes) installed
- [ ] Apple touch icon configured
- [ ] site.webmanifest present
- [ ] OG image renders correctly on social platforms
- [ ] Brand colors and fonts consistent throughout

### 10. Final Steps 🚀
- [ ] Remove any development-only code (console.logs, test data)
- [ ] Verify production environment variables
- [ ] Test the live URL (not just staging)
- [ ] Create client handoff documentation
- [ ] Set up uptime monitoring (optional)
- [ ] Backup of final source code

## Report Format
Present as: ✅ Pass | ⚠️ Warning | ❌ Fail

## Best Used By
- **project-manager** — Pre-launch gate review
- **frontend-developer** — Technical launch checklist
- **qa-expert** — Quality assurance sign-off

## Related Skills
- `/seo-checklist` — Detailed SEO audit
- `/accessibility-check` — Detailed accessibility audit
- `/lighthouse-audit` — Performance scoring
- `/browser-testing` — Cross-browser verification
- `/client-handoff` — Post-launch handoff docs
