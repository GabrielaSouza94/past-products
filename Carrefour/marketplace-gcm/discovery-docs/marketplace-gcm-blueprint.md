# Blueprint - CSM (Catalog Management System)

---

## Cover Page

| Field | Description |
|-------|-------------|
| Project Name | CSM - Catalog Management System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza|
| Document Status | DRAFT - Pending client confirmation |

---

## Project Overview

| Attribute | Value |
|-----------|-------|
| Project Name | CSM - Catalog Management System |
| Client | Carrefour Brasil |
| Engagement Type | Production |
| Client Readiness Level | Level 1 (Vision document with high-level features) |
| Primary Contact | TBD |
| Source Materials | Product description (discovery session), Mirakl API documentation |

**Source Materials Received:**

| Material | Type | Notes |
|----------|------|-------|
| Product Description | Text | Provided in discovery session (Portuguese) |
| Mirakl API Reference | External Link | https://help.mirakl.net/help/api-doc/seller/mmp.html#OF01 |

---

## Problem Statement (As Understood)

### What the client says:

> "A arquitetura dos sistemas que compõem o marketplace do Carrefour faz uso da plataforma Mirakl, que atua como a aplicação que controla o marketplace do Carrefour. Porém por ser um serviço contratado, de uma aplicação pronta e genérica, várias necessidades de evolução para otimizar o marketplace não são atendidas, prejudicando o Carrefour, trazendo gastos e prejudicando a evolução dos produtos digitais."

> "Atualmente a Mirakl possui os endpoints de controle do catálogo de produtos e a documentação da API deles é repassada para os sellers e integradoras. Assim os Sellers realizam as chamadas diretamente pelos endpoints da Mirakl, impossibilitando o conhecimento ou validação de qualquer informação pelo Carrefour."

### Our understanding:

Carrefour currently uses Mirakl as their marketplace management platform. As a contracted, off-the-shelf solution, Mirakl cannot accommodate Carrefour's specific evolution needs, resulting in:

1. **Lack of Control:** Sellers and integrators call Mirakl APIs directly - Carrefour has no visibility or validation capability over these operations
2. **Evolution Blocked:** Platform-specific improvements cannot be implemented
3. **Increased Costs:** Generic solution generates unnecessary expenses
4. **Digital Product Hindrance:** Inability to evolve digital products according to business needs

### Gaps:

- [ ] Quantification of current costs attributed to Mirakl limitations (Q1)
- [ ] Specific examples of blocked evolution needs (Q2)
- [ ] Volume of transactions/products currently managed through Mirakl (Q3)

---

## Client's Stated Vision

### Primary Objective

> "Construir um mecanismo de gestão do marketplace que substitua a Mirakl e toda a comunicação realizada com outras aplicações parte da arquitetura do marketplace. Absorvendo a gestão de catálogo, sellers, pedidos, promoções, e trazendo consigo as melhorias necessárias pelas áreas e outras aplicações envolvidas com a arquitetura do marketplace Carrefour."

**Translation:** Build a marketplace management mechanism that replaces Mirakl and all communication with other applications in the marketplace architecture. Absorbing catalog management, sellers, orders, promotions, and bringing necessary improvements for business areas and other applications involved in Carrefour's marketplace architecture.

### Expected Milestones

| # | Milestone | Description | Detail Level |
|---|-----------|-------------|--------------|
| 1 | Catalog Management | Product registration, offers, catalog editing, validations | High |
| 2 | Seller Management | Store registration and updates | Low |
| 3 | Order Management | TBD | Minimal |
| 4 | Financial Management | TBD | Minimal |
| 5 | Promotions Management | TBD | Minimal |

### Milestone 1 Breakdown (Catalog Management)

| Feature | Status | Notes |
|---------|--------|-------|
| Product Registration + Catalog Editing | Active | Core functionality |
| Offer Registration | Active | Core functionality |
| Product Deletion | ON HOLD | Pending definition of how it will work |
| Product Data Validation | ON HOLD | Until second phase (internal catalog creation) |

### Technical Approach (3-Part Solution)

**Part 1: Endpoint Redirection**
- Redirect catalog management endpoints from Mirakl to CSM
- CSM acts as a proxy/controller layer
- Sellers and integrators call CSM instead of Mirakl directly
- CSM then calls Mirakl APIs internally
- Enables monitoring and control of catalog operations

**Part 2: Product Validators**
- Create validation mechanisms for products being registered
- Validators implemented progressively following product roadmap
- Ensures feature evolution accompanies CSM evolution

**Part 3: Internal 3P Catalog**
- Build Carrefour's own internal 3P product catalog
- Future official and unique marketplace catalog
- Houses validated data and currently active products

### Referenced Systems

- Mirakl (current marketplace platform)
- Seller API integrations
- Third-party integrators
- Other applications in marketplace architecture (not specified)

---

## Source Material Summary

| Material | Type | Summary | Key Information |
|----------|------|---------|-----------------|
| Product Description | Discovery Input | Comprehensive problem/solution overview | Problem context, 5 milestones, 3-part solution |
| Mirakl API Docs | External Reference | Seller marketplace API documentation | Endpoint reference for OF01 (offers) |

### Information Quality Assessment

| Area | Quality | Notes |
|------|---------|-------|
| Problem Statement | Good | Clear articulation of pain points |
| High-Level Vision | Good | Clear objective and milestone structure |
| Milestone 1 Detail | Moderate | Features listed, metrics defined |
| Milestones 2-5 Detail | Low | Names only, no specifications |
| Technical Architecture | Low | General approach, no diagrams or specs |
| Timeline/Budget | Missing | Not provided |

---

## Assumptions

| ID | Assumption | Source | Risk if Wrong |
|----|------------|--------|---------------|
| A01 | Milestone 1 (Catalog) is the first priority | Implied by detail level | Resource reallocation |
| A02 | CSM will initially act as proxy to Mirakl, not full replacement | Part 1 solution description | Architecture rework |
| A03 | Sellers will migrate to new CSM endpoints | Solution approach | Adoption blockers |
| A04 | Backward compatibility with current integrations is required | Implied | Breaking changes |
| A05 | Mirakl contract will be maintained during transition | Implied | Legal/cost issues |
| A06 | Internal 3P catalog (Part 3) is future scope, not MVP | Part 3 description | Scope creep |
| A07 | Validation rules will be defined by business areas | Part 2 description | Delays in validation implementation |
| A08 | Project language is Portuguese (Brazilian) | Source material | Documentation/communication |

---

## Open Questions

### Tier 1: Critical (Blocks PRD)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q1 | Business | What are the quantified costs/losses attributed to current Mirakl limitations? | Business case, prioritization |
| Q2 | Scope | What is the expected timeline for each milestone? | Resource planning, phasing |
| Q3 | Technical | What other applications are part of the marketplace architecture that integrate with Mirakl? | Integration scope, dependencies |
| Q4 | Technical | What is the expected transaction volume (products, offers, orders per day/month)? | Architecture decisions, scaling |
| Q5 | Priority | What is the priority order of Milestones 2-5? Are they sequential or can they be parallelized? | Roadmap planning |
| Q6 | Scope | What specific improvements are requested by business areas that Mirakl cannot provide? | Feature prioritization |

### Tier 2: Important (Needed for TRD)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q7 | Technical | What is the complete inventory of Mirakl API endpoints currently used by sellers/integrators? | API mapping, development scope |
| Q8 | Technical | What authentication/authorization model is used with Mirakl? Will CSM maintain the same? | Security architecture |
| Q9 | Data | What is the data migration strategy for existing catalog data? | Data engineering, timeline |
| Q10 | Technical | What are the SLA requirements for the new CSM APIs? | Infrastructure decisions |
| Q11 | Operations | How many sellers and integrators currently use the Mirakl APIs? | Change management scope |
| Q12 | Technical | What monitoring/observability exists today? What is required for CSM? | Operations, DevOps |

### Tier 3: Nice to Have

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q13 | Research | What feedback have sellers provided about current product registration process? | UX improvements |
| Q14 | Data | Historical data on products blocked at different funnel stages? | Baseline metrics |
| Q15 | Process | What is the current manual product deletion process that needs automation? | Feature specification |

---

## Gap Analysis

```
Area                        Known    Gaps     Status
------------------------------------------------------------
Problem Statement           80%      20%      Warning: 3 questions (Q1, Q2, Q6)
Technical Architecture      30%      70%      Critical: 5 questions (Q3, Q7, Q8, Q10, Q12)
Milestone 1 Scope          60%      40%      Warning: Needs validation rules detail
Milestones 2-5 Scope       10%      90%      Critical: Names only, no specifications
Timeline/Budget             0%      100%     Critical: Not provided (Q2)
User/Stakeholder Mapping   20%      80%      Important: Sellers, integrators mentioned but not detailed
Success Metrics            30%      70%      Warning: M1 metrics only
```

### Visual Summary

| Area | Status |
|------|--------|
| Business Case | Needs quantification |
| Scope Definition | Milestone 1 partially defined, 2-5 need detail |
| Technical Architecture | High-level approach only, needs elaboration |
| Timeline | Not provided |
| Resources/Budget | Not provided |

---

## Contradictions

| Issue | Observation | Sources | Resolution Needed |
|-------|-------------|---------|-------------------|
| Product Deletion | Listed as feature but marked "ON HOLD until definition" | Milestone 1 features | Q15: Clarify current process and requirements |
| Product Validation | Listed as feature but "ON HOLD until second phase" | Milestone 1 features | Clarify if this is Part 2 of solution or separate |
| Scope of CSM | "Replace Mirakl" vs. "Proxy to Mirakl" in Part 1 | Objective vs. Part 1 solution | Clarify: Is goal full replacement or controlled integration? |

---

## Next Steps

### Immediate Actions

1. **Send Open Questions to Carrefour Team**
   - Priority: Tier 1 questions (Q1-Q6)
   - Format: Structured questionnaire in Portuguese
   - Expected response: 1 week

2. **Request Additional Materials**
   - Current Mirakl API endpoint inventory
   - Marketplace architecture diagram
   - Seller/integrator communication examples

3. **Schedule Follow-up Sessions**
   - Technical deep-dive for architecture review
   - Business stakeholder session for priorities and success metrics
   - Milestone 2-5 scoping sessions

### After Client Response

1. Update Blueprint with answers
2. Resolve assumptions and contradictions
3. Proceed to PRD development for Milestone 1
4. Create technical discovery tasks for TRD

### Discovery Sessions Recommended

| Session | Purpose | Attendees | Duration |
|---------|---------|-----------|----------|
| Architecture Review | Map current integrations, define CSM position | Tech leads | 2 hours |
| Milestone 1 Deep-Dive | Detailed catalog management requirements | Product + Tech | 2 hours |
| Milestones 2-5 Scoping | High-level requirements for remaining milestones | Product owners | 1.5 hours |
| Seller Experience | Understand seller pain points and needs | Product + Seller ops | 1 hour |

---

## Appendix: Milestone 1 Metrics (As Provided)

**Success Metrics:**
- Products registered and published without blocks on first attempt
- Products stuck at different stages of the registration funnel

**Complementary Information Needed:**
- Details of product registration funnel (stages, status, flow)
- Types of validation currently performed and missing criteria
- Manual product deletion funnel and service details
- Research with sellers on deletion process
- Impact study and expected gains

---

## Related Documents

- [PRD - Milestone 1](../project-docs/marketplace-gcm-prd.md) - Product Requirements Document

---

*Document Version: 0.1 - DRAFT*
*Author: Gabriela Souza*
