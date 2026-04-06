# Aether8 Website — Task Tracker

## Active Sprint: Product Landing Pages + Portfolio Update
**Kickoff: April 5, 2026**

### Business Model Context
All three products are tailored AI deployments — not SaaS tiers. Every client gets a unique instance.
Pricing is always "Contact for Pricing." CTAs are "Talk to Us" / "Request a Demo."
No tiered plans, no feature gates, no "Start Free Trial" language.

---

### Phase 1 — Infrastructure
- [x] Create `vercel.json` with host-based rewrites for 3 subdomains
- [x] Add CNAME DNS records in Cloudflare for all three subdomains (proxied, → aether8.ai)
- [x] Add Cloudflare Redirect Rules: pursuit/showwalker/scrnr subdomains → aether8.ai/[product]/ (301)
- Note: Vercel Hobby plan — using Cloudflare Redirect Rules instead of host-based rewrites

### Phase 2 — Main Site Products Section Update
- [x] Replace single Pursuit teaser card with 3-product grid (Pursuit, Showwalker, Scrnr)
- [x] Pursuit card: Live badge + 3 feature bullets + "Talk to Us →" CTA linking to pursuit.aether8.ai
- [x] Showwalker card: Early Access badge + 3 teased features + "Request Access →" CTA
- [x] Scrnr card: Early Access badge + 3 teased benefits + "Join Waitlist →" CTA
- [x] Verify responsive layout (1-col mobile, 3-col desktop)

### Phase 3 — Pursuit Landing Page (full)
- [x] Nav: logo + Features/How It Works links + "Talk to Us" CTA
- [x] Hero: gradient headline, tagline, CTA, Live badge
- [x] Features: 3 glass-cards (Research, Outreach Drafts, CRM Export)
- [x] How It Works: 3-step flow
- [x] Pricing: single card — "Every deployment is built for you" + "Talk to Us" CTA
- [x] Footer: cross-product links (legibility fixed: slate-400/slate-600)
- [x] SEO: title, description via Layout.astro props
- [x] Close CRM featured as named integration in CRM-Ready Output card tags

### Phase 4 — Showwalker Landing Page
- [x] Nav + Hero with Early Access badge (fixed: was incorrectly showing green "Live")
- [x] Problem block: 500+ exhibitors / ~2 days / 1 click stats
- [x] How It Works: 3-phase flow (Extract, Discover, Score & Route)
- [x] Features 2x2 grid (Custom Scoring, Contact Enrichment, One-Click CRM Push, Any Portal)
- [x] Deployment/pricing CTA block
- [x] Footer: cross-product links
- [x] SEO
- [x] Purple hover glow on glass-cards

### Phase 5 — Scrnr Landing Page (waitlist)
- [x] Nav + Hero with waitlist CTA + Early Access badge
- [x] Problem statement card (contact decay stats)
- [x] 3 teased benefits with "Coming Soon" pills
- [x] Waitlist CTA block
- [x] Footer: cross-product links
- [x] SEO
- [x] Emerald hover glow on glass-cards
- [x] Waitlist form: name + email + business_type + notes
- [x] API endpoint: `src/pages/api/waitlist.ts` — Resend-powered (internal + confirmation emails)
- [x] RESEND_API_KEY configured in Vercel environment variables
- [x] End-to-end form test verified live at aether8.ai/scrnr/

### Phase 6 — QA & Deploy
- [x] `npm run build` — zero errors, 4 pages compiled
- [x] Design pass: badge fix, footer legibility, product-colored hover glows, connector line positioning
- [x] Em-dash removal across all 4 pages
- [x] Tech reference scrub (no Playwright/Serper/Apollo/ZoomInfo in visible copy)
- [x] Push to main → Vercel auto-deploy triggered
- [x] Cloudflare DNS: 3 proxied CNAMEs added
- [x] Cloudflare Redirect Rules: 3 rules deployed (301)
- [x] Subdomain smoke test: scrnr.aether8.ai → aether8.ai/scrnr/ verified live
- [x] All mailto CTAs verified
- [x] Visual QA pass: Syne font, glass depth, grain, shimmer, reduced-motion, form polish

### Phase 7 — Visual QA Polish (April 6)
- [x] Syne display font applied to all h1/h2/h3 across all pages
- [x] `body::before` grain intensity bumped (0.015 → 0.025)
- [x] `.glass-card` deepened: stronger gradient, inset shadow, webkit-backdrop-filter
- [x] `@media (prefers-reduced-motion)` block added to global.css
- [x] `.cta-primary` shimmer class added to global.css
- [x] Hero + pricing CTAs on Pursuit/Showwalker/Scrnr get `cta-primary`
- [x] Services section + About section: `reveal` class added to index.astro
- [x] Scrnr form: select background fixed (no white flash), hover states, success card
- [x] Syne font link added to Layout.astro

---

## Deferred / Future

### Sales Enablement
- [ ] Build Pursuit vs B2BRocket battle card (1-page PDF for sales conversations)
- [ ] Build Pursuit vs Apollo/Clay battle card
- [ ] Create case study template for first client deployment
- [ ] Research and apply to Close CRM partner/marketplace program

### IP & Legal
- [ ] Engage patent counsel on Showwalker provisional patent filing
      Note: B2BRocket patent claim researched — no USPTO filings found, zero IP risk

### Site Improvements
- [ ] Open Graph images per product page (currently using logo fallback)
- [ ] Add analytics to product pages (Vercel Analytics or Plausible)
- [ ] Sitemap updates to include product page paths
- [ ] Social proof / testimonials sections (once first customers confirm)

### Product
- [ ] Pursuit app: onboarding/auth flow once client engaged
- [ ] Showwalker: upgrade from "Early Access" → "Live" when first client deployed
- [ ] Scrnr waitlist: upgrade from mailto fallback to Beehiiv/Typeform if volume warrants

---

## Review

### Session: April 6, 2026 — Sprint Complete + Waitlist Live + Visual QA

**Competitive intelligence (B2BRocket):**
- Full review completed: b2brocket.ai pricing, features, patent claim investigated
- Patent claim: no USPTO filings found — zero IP risk
- Showwalker identified as genuine white space — no direct competitor
- Full report saved to tasks/competitive-intelligence-b2brocket.md

**Waitlist backend:**
- `src/pages/api/waitlist.ts` — Resend-powered serverless endpoint
- Validates name/email/business_type (7 B2C categories)
- Sends internal notification to hello@aether8.ai + confirmation to submitter
- `output: 'static'` + `export const prerender = false` for hybrid serverless
- RESEND_API_KEY added to Vercel env, redeploy triggered, end-to-end verified live
- Fixed: @astrojs/vercel@10 incompatible with Astro 5 → pinned to @astrojs/vercel@8
- Fixed: select element white flash — explicit inline background-color applied

**Visual QA pass:**
- Typography: Syne (display) + Inter (body) applied globally
- Motion: reduced-motion media query blocks all reveals and fades
- Glass depth: stronger gradient + inset shadow + webkit-backdrop-filter
- Shimmer: .cta-primary ::after hover shimmer on all primary CTAs
- Reveal: 10 total elements across index.astro
- All changes verified live at aether8.ai and aether8.ai/scrnr/
- Final commit: e6025d7 — "Visual QA pass — typography, glass depth, motion, and polish"

**Infrastructure:**
- Vercel Hobby plan: host-based rewrites not used
- Routing: Cloudflare proxied CNAMEs + 3 Redirect Rules (301) → aether8.ai/[product]/
- scrnr.aether8.ai → aether8.ai/scrnr/ confirmed redirecting
