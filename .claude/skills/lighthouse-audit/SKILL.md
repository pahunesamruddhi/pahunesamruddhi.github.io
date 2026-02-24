---
name: lighthouse-audit
description: "Run Lighthouse audit and report Performance, Accessibility, SEO, and Best Practices scores. Use when user asks for Lighthouse audit, performance score, site audit, or web vitals check."
---

You are running a Lighthouse audit on a website. Follow this process:

## Audit Process

### Step 1: Identify Target
- Ask for the URL or local file path to audit
- Determine if this is a deployed site (use URL) or local development (use local server)

### Step 2: Run Lighthouse

For deployed sites, use the PageSpeed Insights API:
```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&category=PERFORMANCE&category=ACCESSIBILITY&category=SEO&category=BEST_PRACTICES&strategy=mobile"
```

For local sites, use Lighthouse CLI if available:
```bash
npx lighthouse URL --output=json --quiet --chrome-flags="--headless"
```

### Step 3: Report Format

Present results in this format:

**Lighthouse Report — [URL]**

| Category | Score | Grade |
|----------|-------|-------|
| Performance | XX/100 | 🟢/🟡/🔴 |
| Accessibility | XX/100 | 🟢/🟡/🔴 |
| Best Practices | XX/100 | 🟢/🟡/🔴 |
| SEO | XX/100 | 🟢/🟡/🔴 |

Grading: 🟢 90-100 | 🟡 50-89 | 🔴 0-49

### Step 4: Key Issues
List the top 5 opportunities for improvement with estimated savings.

### Step 5: Recommendations
For each issue, provide a specific, actionable fix.

## Manual Audit (Fallback)

If automated tools aren't available, manually check:
- **Performance**: Image sizes, render-blocking resources, font loading, compression
- **Accessibility**: Alt text, contrast, heading hierarchy, ARIA, keyboard nav
- **SEO**: Meta tags, structured data, mobile-friendly, HTTPS
- **Best Practices**: HTTPS, no console errors, proper image aspect ratios

## Best Used By
- **performance-optimizer** — Performance scoring and improvement
- **seo-specialist** — SEO score analysis
- **accessibility-auditor** — Accessibility score validation

## Related Skills
- `/asset-optimizer` — Fix image-related performance issues
- `/seo-checklist` — Address SEO findings
- `/accessibility-check` — Deep-dive on accessibility issues
