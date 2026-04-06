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

### Phase 6 — QA & Deploy
- [x] `npm run build` — zero errors, 4 pages compiled
- [x] Design pass: badge fix, footer legibility, product-colored hover glows, connector line positioning
- [x] Em-dash removal across all 4 pages
- [x] Tech reference scrub (no Playwright/Serper/Apollo/ZoomInfo in visible copy)
- [x] Push to main → Vercel auto-deploy triggered
- [x] Cloudflare DNS: 3 proxied CNAMEs added
- [x] Cloudflare Redirect Rules: 3 rules deployed (301)
- [ ] Visual QA at 375px, 768px, 1280px for each page (post-deploy)
- [ ] Verify all mailto CTAs open correctly
- [ ] Verify subdomain redirects resolve (pursuit/showwalker/scrnr → correct pages)

---

## Deferred / Future
- [ ] Waitlist backend (Beehiiv embed or serverless form) — using mailto for now
- [ ] Analytics per product page (Vercel Analytics or Plausible)
- [ ] Sitemap updates to include product page paths
- [ ] Social proof / testimonials sections (once first customers confirm)
- [ ] Open Graph images per product (currently using logo fallback)
- [ ] Pursuit app: onboarding/auth flow once client engaged
- [ ] Showwalker: upgrade from "Early Access" → "Live" when first client deployed
- [ ] Scrnr: build out actual waitlist signup (not just mailto)

---

## Review

### Session: April 6, 2026 — Sprint Complete, Subdomain DNS Live

**What was built:**
- Full sprint delivered: 4-page site (main + 3 product pages) committed to main and deployed via Vercel
- Showwalker completely rewritten after content correction (tradeshow intel agent, not meeting tool)
- Design pass: Showwalker badge corrected (green Live → amber Early Access), product-colored card hover glows, footer legibility bump, step connector line fix
- Em-dashes and underlying tech references scrubbed from all pages

**DNS/Infrastructure (April 6):**
- Vercel Hobby plan confirmed — host-based rewrites not used
- Cloudflare DNS: added 3 proxied CNAMEs (pursuit, showwalker, scrnr → aether8.ai)
- Cloudflare Redirect Rules: 3 rules deployed at edge (301 redirects to aether8.ai/[product]/)
- Traffic flow: subdomain → Cloudflare edge → 301 → aether8.ai/[product]/ → Vercel

**Pending verification:**
- Visual QA on live URLs post-deploy
- Subdomain redirect smoke test
