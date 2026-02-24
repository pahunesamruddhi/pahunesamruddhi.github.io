---
name: browser-testing
description: "Cross-browser compatibility testing matrix and responsive breakpoint validation. Use when user asks for browser testing, cross-browser check, responsive testing, or device testing."
---

You are running cross-browser and responsive testing. Follow this checklist:

## Browser Testing Matrix

### Desktop Browsers (must test)
| Browser | Engine | Priority | Key Quirks |
|---------|--------|----------|------------|
| Chrome (latest) | Blink | P0 | Reference browser |
| Safari (latest) | WebKit | P0 | Flexbox gaps, backdrop-filter, font rendering |
| Firefox (latest) | Gecko | P1 | Scroll behavior, font smoothing |
| Edge (latest) | Blink | P2 | Same as Chrome generally |

### Mobile Browsers (must test)
| Browser | Platform | Priority | Key Quirks |
|---------|----------|----------|------------|
| Safari iOS | iPhone | P0 | 100vh issue, position:fixed, rubber banding |
| Chrome Android | Android | P0 | Address bar height, font boosting |
| Samsung Internet | Android | P2 | Dark mode, older feature support |

## Responsive Breakpoints

Test at these widths:
| Width | Device Class | Test Focus |
|-------|-------------|------------|
| 320px | Small phone (iPhone SE) | Minimum viable layout |
| 375px | Standard phone (iPhone) | Primary mobile |
| 428px | Large phone (iPhone Pro Max) | Wide mobile |
| 768px | Tablet portrait (iPad) | Tablet layout switch |
| 1024px | Tablet landscape / small laptop | Desktop transition |
| 1280px | Laptop | Standard desktop |
| 1440px | Desktop | Design reference |
| 1920px | Full HD | Large screen behavior |

## Testing Checklist (per browser/breakpoint)

### Layout
- [ ] No horizontal overflow/scrollbar
- [ ] Grid/Flexbox layouts render correctly
- [ ] Images scale and don't overflow containers
- [ ] Navigation is usable (hamburger on mobile, full on desktop)
- [ ] Footer stays at bottom of page

### Typography
- [ ] Fonts load correctly (web fonts with fallbacks)
- [ ] Text is readable at all sizes (min 16px body)
- [ ] Line lengths stay readable (45-75 characters)
- [ ] No text overflow or truncation

### Interactions
- [ ] Hover states work (desktop) / touch states work (mobile)
- [ ] Click/tap targets are adequate size (44x44px minimum)
- [ ] Forms are usable (inputs, selects, textareas)
- [ ] Animations run smoothly (60fps)
- [ ] Scroll behavior works (smooth scroll, parallax)

### Media
- [ ] Images load (WebP with fallbacks for older browsers)
- [ ] Videos play (if applicable)
- [ ] SVGs render correctly
- [ ] Favicons display in browser tab

### Functionality
- [ ] JavaScript features work (no console errors)
- [ ] Forms submit correctly
- [ ] Links work (internal and external)
- [ ] Analytics tracking fires

## Known Cross-Browser Issues

| Issue | Affected | Workaround |
|-------|----------|------------|
| `100vh` includes address bar | iOS Safari | Use `100dvh` or JS fallback |
| `gap` in Flexbox | Safari <14.1 | Use margins as fallback |
| `backdrop-filter` | Firefox (partial) | Provide solid fallback |
| Smooth scroll | Safari (partial) | CSS `scroll-behavior` + JS polyfill |
| `:has()` selector | Firefox <121 | Use JS or alternative selectors |

## Best Used By
- **frontend-developer** — Cross-browser implementation
- **qa-expert** — Quality assurance testing
- **accessibility-auditor** — Accessibility across browsers

## Related Skills
- `/lighthouse-audit` — Automated testing scores
- `/accessibility-check` — Accessibility across browsers
- `/website-launch-checklist` — Pre-launch browser verification
