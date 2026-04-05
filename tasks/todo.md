# Aether8 Website — Task Tracker

## Active Sprint: Product Landing Pages + Portfolio Update
**Kickoff: April 5, 2025**

### Business Model Context
All three products are tailored AI deployments — not SaaS tiers. Every client gets a unique instance.
Pricing is always "Contact for Pricing." CTAs are "Talk to Us" / "Request a Demo."
No tiered plans, no feature gates, no "Start Free Trial" language.

---

### Phase 1 — Infrastructure
- [x] Create `vercel.json` with host-based rewrites for 3 subdomains
- [ ] Add `pursuit.aether8.ai`, `showwalker.aether8.ai`, `scrnr.aether8.ai` as custom domains in Vercel dashboard (manual)
- [ ] Add CNAME DNS records at registrar for all three subdomains (manual)

### Phase 2 — Main Site Products Section Update
- [x] Replace single Pursuit teaser card with 3-product grid (Pursuit, Showwalker, Scrnr)
- [x] Pursuit card: Live badge + 3 feature bullets + "Talk to Us →" CTA linking to pursuit.aether8.ai
- [x] Showwalker card: Early Access badge + 3 teased features + "Request Access →" CTA
- [x] Scrnr card: Early Access badge + 3 teased benefits + "Join Waitlist →" CTA
- [x] Verify responsive layout (1-col mobile, 3-col desktop)

### Phase 3 — Pursuit Landing Page (full)
- [x] Nav: logo + "← aether8.ai" + "Talk to Us" CTA
- [x] Hero: gradient headline, tagline, CTA, Live badge
- [x] Features: 3 glass-cards (Research, Outreach Drafts, CRM Export)
- [x] How It Works: 3-step flow
- [x] Pricing: single card — "Every deployment is built for you" + "Talk to Us" CTA
- [x] Footer: cross-product links
- [x] SEO: title, description via Layout.astro props

### Phase 4 — Showwalker Landing Page (teaser)
- [x] Nav + Hero with Early Access badge
- [x] Value prop + 3 teased features (Coming Soon aesthetic)
- [x] Early access CTA block
- [x] Footer
- [x] SEO

### Phase 5 — Scrnr Landing Page (teaser/waitlist)
- [x] Nav + Hero with waitlist CTA
- [x] Problem statement card (contact decay stats)
- [x] 3 teased benefits
- [x] Waitlist CTA block
- [x] Footer
- [x] SEO

### Phase 6 — QA & Deploy
- [x] `npm run build` — zero errors, 4 pages compiled
- [ ] `npm run dev` — manual visual check at /pursuit/, /showwalker/, /scrnr/
- [ ] Test responsive at 375px, 768px, 1280px for each page
- [ ] Verify all mailto CTAs open correctly
- [ ] Verify cross-product footer links
- [ ] Push to main → Vercel auto-deploy
- [ ] Confirm subdomain rewrites resolve correctly post-deploy

---

## Deferred / Future
- [ ] Waitlist backend (Beehiiv embed or serverless form) — using mailto for now
- [ ] Analytics per subdomain (Vercel Analytics or Plausible)
- [ ] Sitemap updates for subdomain URLs
- [ ] Pursuit app onboarding / authentication flow on subdomain
- [ ] Social proof / testimonials sections (once first customers confirm)

---

## Review

### Session: [Date] — [Summary]
_Add review notes here after each work session._
