---
name: accessibility-check
description: "WCAG 2.1 accessibility audit using axe-core/pa11y patterns, generating a compliance report with severity levels. Use when user asks for accessibility audit, WCAG check, a11y review, or compliance report."
---

You are performing a WCAG 2.1 AA accessibility audit. Work through each category:

## Accessibility Checklist

### 1. Perceivable
- [ ] All images have meaningful `alt` text (decorative images have `alt=""`)
- [ ] Color contrast ≥ 4.5:1 for normal text, ≥ 3:1 for large text
- [ ] Color is not the only means of conveying information
- [ ] Text can be resized to 200% without loss of content
- [ ] Content is readable at 400% zoom (no horizontal scrolling at 320px width)
- [ ] Media has captions/transcripts if applicable

### 2. Operable
- [ ] All interactive elements reachable via keyboard (Tab/Shift+Tab)
- [ ] Visible focus indicators on all focusable elements
- [ ] No keyboard traps (can Tab away from any element)
- [ ] Skip navigation link present (skip to main content)
- [ ] Touch targets ≥ 44x44px on mobile
- [ ] No content flashes more than 3 times per second
- [ ] Page has descriptive `<title>`

### 3. Understandable
- [ ] `<html lang="en">` (or appropriate language) set
- [ ] Form inputs have associated `<label>` elements
- [ ] Error messages are descriptive and linked to fields (`aria-describedby`)
- [ ] Required fields clearly indicated (not by color alone)
- [ ] Consistent navigation across pages
- [ ] No unexpected context changes on input

### 4. Robust
- [ ] Valid HTML (no duplicate IDs, proper nesting)
- [ ] ARIA roles used correctly (not overriding semantic HTML)
- [ ] Custom widgets follow WAI-ARIA Authoring Practices
- [ ] Content works with assistive technologies
- [ ] `role`, `aria-label`, `aria-describedby` used appropriately

### 5. Automated Testing

If tools are available:
```bash
# pa11y
npx pa11y URL --standard WCAG2AA

# axe-core via CLI
npx @axe-core/cli URL
```

### 6. Manual Testing Checklist
- Navigate entire site using only keyboard
- Test with screen reader (VoiceOver: Cmd+F5 on Mac)
- Check with browser zoom at 200% and 400%
- Enable high contrast mode and verify readability
- Test with `prefers-reduced-motion` enabled

## Report Format

| Issue | Severity | WCAG Criterion | Location | Fix |
|-------|----------|---------------|----------|-----|
| Missing alt text | Critical | 1.1.1 | image.html | Add descriptive alt |
| Low contrast | Serious | 1.4.3 | nav links | Darken text color |

Severity levels: Critical → Serious → Moderate → Minor

## Best Used By
- **accessibility-auditor** — Full WCAG compliance audit
- **frontend-developer** — Fixing accessibility issues
- **qa-expert** — Quality assurance testing

## Related Skills
- `/lighthouse-audit` — Automated accessibility scoring
- `/browser-testing` — Cross-browser accessibility verification
- `/website-launch-checklist` — Pre-launch accessibility gate
