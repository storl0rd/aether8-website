# Pursuit — Internal Engagement Pricing Guide
**Aether8 AI Consulting Inc. — Confidential, Not for Client Distribution**
**Version:** 1.0 | **Date:** April 6, 2026

---

## Overview

Pursuit is priced as a forward-deployed engagement — not a SaaS license. Clients are paying for
a production-grade AI sales research system configured around their ICP, their CRM, and their
workflow. Pricing reflects scope, not seat count.

This document covers:
1. Cost basis (COGS per prospect)
2. Engagement structure (3-phase model)
3. Fee schedule by phase and volume
4. Competitive anchoring (how to position the price)
5. Deal guidance — how to quote a client

---

## 1. Cost Basis (COGS)

### What happens per prospect in Pursuit

The Scout → Draft → Sync pipeline performs the following per target company:

| Step | Operation | Model / Tool |
|------|-----------|-------------|
| Scout: Scrape | Playwright headless scrape of up to 4 pages (homepage, /about, /team, /contact) | Chromium (CPU) |
| Scout: Enrich | LLM structured extraction → `EnrichedCompany` schema (name, industry, employee range, contacts with confidence scores) | LLM (~1,800 tok in / 400 tok out) |
| Draft: Generate | Personalized outreach draft using company intel + ICP context + optional call transcript | LLM (~2,500 tok in / 900 tok out) |
| Sync: Export | Push enriched record + draft to Close CRM or HubSpot | API call |

### LLM cost per prospect (variable — model-dependent)

| Model | Input ($/MTok) | Output ($/MTok) | Enrichment call | Draft call | Total/prospect |
|-------|---------------|-----------------|-----------------|------------|---------------|
| Claude 3.5 Haiku | $0.80 | $4.00 | $0.003 | $0.006 | **~$0.009** |
| Claude 3.5 Sonnet | $3.00 | $15.00 | $0.011 | $0.021 | **~$0.032** |
| GPT-4o Mini | $0.15 | $0.60 | $0.001 | $0.001 | **~$0.002** |
| GPT-4o | $2.50 | $10.00 | $0.008 | $0.014 | **~$0.022** |

**Default deployment model:** Claude 3.5 Sonnet for quality; Haiku can be swapped for cost-sensitive volume runs. LiteLLM makes this a config change.

### Infrastructure cost (monthly, shared across runs)

| Component | Stack | Monthly Cost |
|-----------|-------|-------------|
| App server (API + Celery workers) | DigitalOcean / Railway (2 vCPU, 4GB RAM) | ~$40 |
| PostgreSQL | Managed (DigitalOcean DB / Supabase) | ~$15-25 |
| Redis (Celery broker) | Upstash or managed | ~$10 |
| OTel / observability | Grafana Cloud free tier or Honeycomb | $0-30 |
| **Total infra** | | **~$65-105/mo** |

> Infra cost is absorbed into engagement pricing. At any meaningful prospect volume, infra is <1% of total cost.

### Blended COGS at scale (Sonnet, fully-loaded)

| Monthly Volume | LLM Cost | Infra (pro-rated) | Total COGS | COGS/Prospect |
|---------------|----------|-------------------|------------|---------------|
| 500 prospects | $16 | $85 | $101 | $0.20 |
| 2,000 prospects | $64 | $85 | $149 | $0.07 |
| 5,000 prospects | $160 | $85 | $245 | $0.05 |

**Key takeaway:** At any serious volume, COGS is negligible. Pricing is anchored to value delivered (displaced SDR time, pipeline quality), not to model cost. The margin is substantial — use it to price delivery confidence, not raw compute.

---

## 2. Engagement Structure — 3-Phase Model

### Phase 1: Discovery & Scoping (paid, fixed)

A bounded engagement to assess fit, define the ICP, and produce a deployment spec. This protects both parties — Aether8 doesn't commit engineering time on unqualified clients; the client gets a tangible deliverable before committing to deployment.

**Deliverables:**
- 60-90 min structured discovery call
- ICP definition document (industry, company size, revenue range, geography, target titles, disqualifying criteria)
- Scoring model spec (5-10 weighted criteria, 0-100 scale definition)
- CRM field mapping document (what goes where in HubSpot / Close)
- Deployment scope document (run frequency, prospect volume targets, success metrics)
- Go/no-go recommendation

**Fee:** **$1,500 — $2,500** (flat, non-refundable, credited toward Phase 2 if client proceeds)

**Timeline:** 5-7 business days from kickoff call to deliverables

---

### Phase 2: Deployment (one-time, fixed per scope)

Full deployment of the configured Pursuit instance. Includes environment provisioning, ICP model configuration, CRM integration, initial calibration run, and handoff.

**Deliverables:**
- Configured Pursuit instance (Docker stack, Postgres, Redis, OTel)
- ICP scoring model loaded with client-defined criteria and weights
- CRM integration live (Close or HubSpot — contacts, enrichment fields, draft notes pushed)
- Initial calibration run: 50-100 prospects reviewed together on a call, scoring adjustments made
- Runbook: how to submit new ICP targets, how to trigger runs, how to interpret scores
- 30-day support window post-launch (email/Slack, business hours)

**Fee:** By scope —

| Deployment Scope | Description | Fee |
|-----------------|-------------|-----|
| **Standard** | 1 ICP, HubSpot or Close CRM, standard enrichment (web scrape + LLM), CSV fallback | **$4,500 — $6,500** |
| **Extended** | 1-2 ICPs, choice of CRM, Pitch agent enabled (call transcript → qualification), custom scoring logic | **$8,000 — $12,000** |
| **Enterprise** | Multiple ICPs, Salesforce or multi-CRM, custom data sources, SLA, dedicated infra, SOC 2 review | **$15,000 — $25,000** |

Phase 1 fee credited toward Phase 2 (i.e., a Standard deployment becomes $3,000-$5,000 net after credit).

**Timeline:**
- Standard: 10-15 business days from Phase 1 deliverables approved
- Extended: 20-25 business days
- Enterprise: scoped separately

---

### Phase 3: Operating Retainer (monthly, recurring)

Ongoing operation of the Pursuit agent: running the pipeline, tuning the scoring model as the client's ICP evolves, CRM field updates, observability monitoring, and regular review calls.

This is where the recurring relationship lives. Phase 3 can be month-to-month or committed quarterly (10% discount).

| Retainer Tier | Included Monthly Volume | ICP Changes | Runs/Month | Support | Monthly Fee |
|--------------|------------------------|-------------|------------|---------|------------|
| **Maintain** | Up to 500 prospects | 1 | 1 | Email, 48h SLA | **$1,800/mo** |
| **Operate** | Up to 2,000 prospects | Unlimited | 4 (weekly) | Email + Slack, 24h SLA | **$3,500/mo** |
| **Scale** | Up to 5,000 prospects | Unlimited | Unlimited | Dedicated Slack, 4h SLA, bi-weekly call | **$6,500/mo** |
| **Custom** | 5,000+ prospects | Unlimited | Unlimited | Scoped SLA, monthly exec review | **Quote** |

**Overage:** Prospects above the tier limit are billed at a flat per-prospect rate:
- Maintain tier overage: $3.50/prospect
- Operate tier overage: $2.00/prospect
- Scale tier overage: $1.25/prospect

**Quarterly commitment discount:** 10% off monthly fee when billed quarterly upfront.

---

## 3. Total Engagement Economics

### Scenario A: Standard startup / scale-up (Close CRM, 1 ICP, weekly runs)

| Phase | Fee |
|-------|-----|
| Phase 1: Discovery | $1,500 |
| Phase 2: Standard Deployment (net after credit) | $3,000 — $5,000 |
| Phase 3: Operate retainer (month 1-12) | $3,500/mo |
| **Year 1 Total** | **~$47,000 — $49,000** |
| **Year 1 Monthly Equivalent** | **~$3,900/mo** |

### Scenario B: Mid-market (HubSpot, 2 ICPs, Pitch agent, weekly runs)

| Phase | Fee |
|-------|-----|
| Phase 1: Discovery | $2,500 |
| Phase 2: Extended Deployment (net after credit) | $6,500 — $9,500 |
| Phase 3: Scale retainer (month 1-12) | $6,500/mo |
| **Year 1 Total** | **~$87,000 — $90,000** |

### Scenario C: One-time campaign (no retainer)

Some clients want a single high-volume research run — e.g., pre-conference prospect list, entering a new vertical.

- Phase 1: $1,500 (discovery + target definition)
- Phase 2 (Standard): $4,500-$6,500
- One-time run (up to 1,000 prospects delivered): included in Phase 2 fee
- Additional runs: $2,000/run (up to 500 prospects), $3,500/run (up to 2,000 prospects)
- No retainer required

---

## 4. Competitive Price Anchoring

Use this section when a prospect compares Pursuit to B2BRocket, Apollo, or Clay.

### The DIY cost of one "Pursuit-quality" prospect

| Activity | Tool / Method | Cost Per Prospect |
|----------|--------------|------------------|
| Find a contact | Apollo (Pro, 1,200 credits/yr) | $0.08-0.25/record |
| Research the company | SDR manual (1-2 hrs @ $30-60/hr blended) | **$30-120/prospect** |
| Write a personalized first draft | SDR manual (20-40 min) | $10-40/prospect |
| Push to CRM | Manual data entry (10 min) | $5-15/prospect |
| **Total DIY cost** | | **$45-175/prospect** |

At the Operate retainer (2,000 prospects/month at $3,500/mo), **Pursuit delivers each qualified, researched, draft-ready prospect for $1.75** — against $45-175 for a human SDR doing the same work.

### Against B2BRocket

| | B2BRocket Growth ($99/mo) | Pursuit (Operate retainer) |
|--|--------------------------|---------------------------|
| Prospect volume | 200,000 contacts in DB | 2,000 researched/drafted/month |
| Research quality | Database record (name, email, company) | Web-scraped, LLM-enriched intel per prospect |
| Personalization | Template-based AI sequences | Per-prospect draft referencing specific company details |
| ICP model | Shared filters across all clients | Calibrated scoring model built for this client |
| CRM export | HubSpot, Zoho, Salesforce | HubSpot, Close (gap in B2BRocket) |
| Ramp time | 2-3 weeks for AI to "learn" | Day-1 ICP baked in from Phase 1 |
| Traceability | None | OTel traces — every score is explainable |
| Client | SDR team running volume outreach | Sales team prioritizing pipeline quality |

**Frame:** "B2BRocket gives your team a database and sequences. Pursuit gives your team a qualified, scored list with personalized drafts ready to review. These are different products for different problems."

### Against Apollo

Apollo is frequently used as a data source, not a competitor. Position accordingly:
> "Many Pursuit clients use Apollo for the contact database layer — Pursuit then takes those exports, runs web research, scores them against your ICP, and generates outreach drafts. Apollo finds people; Pursuit qualifies them."

### Against Clay

| | Clay ($185-495/mo) | Pursuit |
|--|-------------------|---------|
| Enrichment depth | 150+ providers, highly configurable | Web-first, LLM synthesis — no data vendor dependencies |
| Operations | Requires RevOps expertise to build and maintain | Forward-deployed — Aether8 configures and runs it |
| Outreach | No native outreach execution | Draft generation included |
| Traceability | Limited | OTel traced — every enrichment step logged |

**Frame:** "Clay is a powerful platform — if you have a RevOps engineer to operate it. Pursuit is deployed for you, runs for you, and is tuned to your ICP without requiring internal expertise."

---

## 5. Deal Guidance — How to Quote

### Step 1: Qualify before pricing

Questions to ask before presenting any numbers:

1. **Volume**: "How many net-new target accounts are you trying to research per month?"
2. **Current state**: "How are your reps doing research today — manually, Apollo, something else? How long does it take per prospect?"
3. **CRM**: "What CRM are you running? How important is the CRM data quality to you?"
4. **ICP clarity**: "Do you have a defined ICP, or is that something you're still working on?" (If undefined, Phase 1 is the starting point.)
5. **Budget signal**: "What do you currently spend on sales tools and SDR time that Pursuit would replace?"

### Step 2: Anchor to displaced cost

Before presenting Phase 1/2/3 fees, establish what they currently spend:
- If they have 2 SDRs spending 50% of time on research → 1 FTE equivalent → $60-100K/yr in loaded cost
- Pursuit Operate retainer at $3,500/mo = $42K/yr → ROI case is immediate

### Step 3: Start with Phase 1

Lead with Phase 1 as the entry point, not the full engagement. Reasons:
- Lower commitment for the client ($1,500-2,500 vs. $10K+)
- Produces tangible deliverables they keep regardless of whether they proceed
- Gives Aether8 time to assess whether the client's ICP is well-defined enough to deliver results
- Phase 1 fee is credited toward deployment — no cost penalty for proceeding

### Step 4: Size the retainer to their run cadence

- 1 run/month → Maintain ($1,800/mo)
- Weekly cadence or active growth phase → Operate ($3,500/mo)
- High-volume or multi-ICP → Scale ($6,500/mo) or custom quote

### Step 5: Offer a quarterly commitment

Propose quarterly billing with 10% discount when the client signals intent to commit long-term. This improves cash flow predictability for Aether8 and gives the client a concrete incentive to commit.

---

## 6. Discount Policy

| Scenario | Discount |
|----------|----------|
| Quarterly retainer commitment (pre-paid) | 10% off monthly rate |
| Annual retainer commitment (pre-paid) | 15% off monthly rate |
| Referral (client refers a closed deal) | 1 month retainer credit |
| Pilot / intro engagement (first client in a new vertical) | Phase 2 at cost + 30% (build the case study) |
| Non-profit or early-stage startup | Case-by-case — maximum 20% off |

**Floor rule:** Phase 2 (deployment) is never discounted below cost + 50%. The deployment is where the expertise investment is made.

---

## 7. Pricing Review Cadence

This document should be reviewed quarterly. Adjust based on:
- Actual LLM API cost changes (Anthropic/OpenAI pricing changes frequently)
- Infrastructure cost changes
- Market pricing signals (competitor pricing updates)
- Margin realization from closed deals (track actual time-to-deliver vs. fee)

---

*Prepared by Aether8 AI Consulting Inc. — Internal use only.*
*Do not share with prospects. Use the competitive anchoring section to guide verbal positioning.*
