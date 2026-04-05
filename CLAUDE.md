# Aether8 Website

Landing page for Aether8 AI Consulting Inc. (aether8.ai).

## Stack
- Astro v5.17.3, Tailwind CSS v4 (`@import "tailwindcss"` syntax in global.css)
- Font: Avenir stack (set in `src/styles/global.css`)
- Deploy: Vercel on push to `main`

## Dev
- `npm run dev` → port 4321
- Main page: `src/pages/index.astro`
- Logo: `public/logofinal-transparent.png`

## Current Sections
- Hero: animated logo with glow, rotating rings, particles, shimmer
- Services: 3-card grid (Tailored AI Solutions, Forward-Deployed Engineering, SRE)
- Products: 3-card grid — Pursuit (Live), Showwalker (Early Access), Scrnr (Early Access)
- About: stats (0 Hallucinations, Infinite Scalability, 100% Traceable) + features
- Contact: CTA with mailto:hello@aether8.ai
- Nav: SERVICES | PRODUCTS | ABOUT | CONTACT

## Product Subdomains
- pursuit.aether8.ai → src/pages/pursuit/index.astro
- showwalker.aether8.ai → src/pages/showwalker/index.astro
- scrnr.aether8.ai → src/pages/scrnr/index.astro
- Routed via vercel.json host-based rewrites

## Style
- Body text: slate-400, text-base for readability
- PURSUIT section: gradient wordmark, "Early Access" amber badge
- All animations use CSS + Astro client-side scripts

## Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way"
- If a fix feels hacky: "Knowing everything I know now, implement the elagant solution"
- Skip this for simple, obvious fixes - dont over-engineer
- Challenge your own work before presenting it

## Task Management
1 **Plan First**: Write plan to "tasks/todo.md" with checkable items
2 **Verify Plan**: Check in before starting implementation
3 **Track Progress**: Mark items complete as you go
4 **Explain Changes**: High-level summary at each step
5 **Document Results**: Add review sections to "tasks/todo.md"
6 **Capture Lessons**: Updates "tasks/lessons.md" after correctioms

## Business Model
- **Not SaaS. Tailored AI Deployments.** Each product (Pursuit, Showwalker, Scrnr) is a foundational platform — not a fixed feature set. Every client gets a unique instance scoped and configured to their workflow, ICP, and stack.
- **No pricing tiers on the site.** Always "Contact for Pricing" or "Talk to Us." Pricing reflects the engagement scope, not a seat count. Never show tiered plans or feature gates.
- **AI coding collapses time-to-feature.** A new capability can be built in days. Position products as flexible, evolvable platforms — not rigid tools.
- **The differentiation is tailored delivery.** Generic SaaS is commoditised. Aether8's value is that the product is built for the client — their data, their workflows, their team.
- **CTAs reflect this.** Prefer "Talk to Us", "Request a Demo", "Get Started" — never "Sign Up Free" or "Pick a Plan."

## Core Principles
- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes, no temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.
