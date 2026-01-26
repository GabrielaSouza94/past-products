# Blueprint - EAN Validator System

---

## Cover Page

| Field | Description |
|-------|-------------|
| Project Name | EAN Validator System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Document Status | DRAFT - Pending client confirmation |

---

## Project Overview

| Attribute | Value |
|-----------|-------|
| Project Name | EAN Validator System |
| Client | Carrefour Brasil |
| Engagement Type | Production |
| Client Readiness Level | Level 1 (Vision document with high-level features) |
| Primary Contact | TBD |
| Source Materials | Context document with problem description, use cases, acceptance criteria |

**Source Materials Received:**

| Material | Type | Notes |
|----------|------|-------|
| Context Document | Text | Problem context, milestones, use cases, acceptance criteria (Portuguese) |
| Product Registration Flowchart | External Link | Confluence documentation |
| EAN/GS1 References | External Links | Technical EAN documentation |

---

## Problem Statement (As Understood)

### What the client says:

> "Todo produto possui um código de barras / código identificador / EAN único, que permite a identificação do produto, seu título e detalhes de especificação. Esse código é global e o fabricante do produto é responsável pelo registro dele em alguma instituição emissora."

> "Durante o cadastro de um produto na Mirakl o campo EAN é disponibilizado para preenchimento, porém ele não é obrigatório, permitindo com que muitos produtos não tenham EAN cadastrado."

> "Ao inserir um EAN para determinado produto, o sistema de catálogo da Mirakl e do Carrefour também não identificam se o EAN inserido realmente corresponde ao produto que está sendo cadastrado."

### Our understanding:

Carrefour's marketplace has significant data quality issues with EAN (barcode) codes in the product catalog:

1. **Missing EAN Codes:** The EAN field is not mandatory during product registration, resulting in many products without proper identification codes.

2. **Unvalidated EAN Codes:** When sellers provide EAN codes, the system does not verify:
   - Whether the code is a legitimate, properly-formatted EAN
   - Whether the code actually belongs to the product being registered

3. **Product Matching Failures:** Incorrect EANs cause problems with product matching functionality, which should group different seller offers for the same product. Wrong EANs lead to:
   - Different products incorrectly grouped together
   - Same products not being matched (missed consolidation)
   - Customer confusion and potential fraud exposure

4. **Catalog Reliability:** The current catalog lacks reliability and consistency in EAN information, affecting:
   - Search and discovery accuracy
   - Product data quality
   - Customer trust

### Gaps:

- [ ] Volume of products currently without EAN in catalog (Q1)
- [ ] Volume of products with potentially incorrect EANs (Q2)
- [ ] Financial impact of product mismatches (Q3)
- [ ] Current daily volume of new product registrations (Q4)

---

## Client's Stated Vision

### Primary Objective

> "Criar um sistema de validação do EAN para todo o catálogo de produtos. Fazendo com que todos os produtos tenham EAN compatível com o que está sendo ofertado (produto com EAN correto)."

**Translation:** Create an EAN validation system for the entire product catalog, ensuring all products have an EAN compatible with what is being offered (product with correct EAN).

### Expected Milestones

| # | Milestone | Description | Scope |
|---|-----------|-------------|-------|
| 1 | Block Without EAN | Prevent registration of products without EAN | New Products |
| 2 | EAN Test (New) | Validate EAN legitimacy on new products | New Products |
| 3 | EAN Test (Catalog) | Test EAN legitimacy for existing catalog | Existing Catalog |
| 4 | EAN/Product Match (New) | Validate EAN corresponds to product | New Products |
| 5 | EAN/Product Match (Catalog) | Validate correspondence for entire catalog | Existing Catalog |

### Main Features (From Client)

| Feature | Description |
|---------|-------------|
| EAN Legitimacy Test | Test if the code is a legitimate barcode (valid format, check digit) |
| EAN/Product Validation | Validate if code belongs to the informed product (compare seller info vs. EAN registry) |
| Missing EAN Handling | Find missing code or create action flow for products without EAN |
| Registration Blocking | Block product registration without EAN |

### Acceptance Criteria (From Client)

| ID | Criterion | Priority |
|----|-----------|----------|
| AC01 | No new products allowed in catalog without EAN | Critical |
| AC02 | EAN only accepted if tested (verified as valid barcode format) | Critical |
| AC03 | Product only valid if EAN matches product information | Critical |
| AC04 | Validation must check internal bases first (GOLD, validated products) before external | High |
| AC05 | Validation must query multiple external bases if first doesn't match | High |
| AC06 | All catalog products must have tested and validated EAN | Critical |
| AC07 | Products with failed EAN test/validation must be excluded | Critical |
| AC08 | System must store validated EAN product characteristics for future lookups | High |

---

## Use Cases (From Client)

### New Product Registration

| UC | Scenario | Outcome |
|----|----------|---------|
| UC-01 | New product without EAN | Product rejected |
| UC-02 | New product with EAN that fails test | Product rejected |
| UC-03 | New product with EAN that passes test | Proceed to validation |
| UC-04 | New product with EAN + internal match found | Product approved |
| UC-05 | New product with EAN + external match found | Product approved |
| UC-06 | New product with EAN + no match found | Product rejected |

### Existing Catalog Cleanup

| UC | Scenario | Outcome |
|----|----------|---------|
| UC-07 | Catalog product without EAN | Product excluded (confirm with catalog team) |
| UC-08 | Catalog product with EAN that fails test | Mark as no-EAN (excluded) |
| UC-09 | Catalog product with EAN + internal match | Product validated |
| UC-10 | Catalog product with EAN + external match | Product validated |
| UC-11 | Catalog product with EAN + no match | Product excluded/flagged |

---

## Referenced Systems

| System | Role | Integration Type |
|--------|------|------------------|
| **Mirakl** | Marketplace platform, product registration | Primary integration |
| **GS1** | Global EAN/barcode registry and issuing organization | External validation |
| **GOLD** | Internal product database (pre-validated products) | Internal validation |
| **Simplus** | TBD - Role unclear | TBD |
| **Omnilogic** | Product categorization service | Existing integration |
| **VTEX** | E-commerce platform (product visibility) | Downstream system |

### Current Product Registration Flow (As Described)

```
[Seller] → [Mirakl API/Portal] → [MCM Module] → [Omnilogic] → [Categorization] → [Publication] → [VTEX]
```

**Where EAN Validation Would Fit:**

```
[Seller] → [Mirakl] → [EAN Validator] → [MCM] → [Omnilogic] → [Publication]
                          ↓
                    [GOLD/Internal]
                          ↓
                    [GS1/External]
```

---

## Source Material Summary

| Material | Type | Summary | Key Information |
|----------|------|---------|-----------------|
| Context Document | Discovery Input | Problem context, milestones, use cases | 5 milestones, 11 use cases, 8 acceptance criteria |
| Discovery Questionnaire | Checklist | Partial answers to discovery questions | Problem root understood, solution unclear |
| Confluence Link | External | Product registration flowchart | Reference for current flow |
| GS1/EAN Links | External | EAN technical documentation | Validation algorithms |

### Information Quality Assessment

| Area | Quality | Notes |
|------|---------|-------|
| Problem Statement | Good | Clear articulation of data quality issues |
| High-Level Vision | Good | Clear objective and milestone structure |
| Use Cases | Good | 11 use cases defined |
| Acceptance Criteria | Good | 8 criteria defined |
| Technical Solution | Low | Only mentions architecture components, no details |
| System Integrations | Moderate | Systems named but integration details missing |
| Timeline/Budget | Missing | Not provided |
| Metrics | Partial | Metrics named but no baseline data |

---

## Technical Approach (As Understood)

### EAN Validation Layers

**Layer 1: EAN Format Test (Legitimacy)**
- Verify EAN follows valid format (8, 12, 13, or 14 digits)
- Validate check digit using GS1 algorithm
- Reject malformed codes immediately

**Layer 2: Internal Database Lookup**
- Query GOLD database for existing validated products
- Query internal cache of previously validated EANs
- If match found, validate product characteristics

**Layer 3: External Database Lookup**
- Query GS1 database for EAN registration
- Query additional external sources if needed
- Compare product information from registry vs. seller submission

### Proposed Validation Flow

```
[Product with EAN]
       ↓
[Format Test] ─── FAIL ───→ [Reject Product]
       ↓ PASS
[Internal Lookup (GOLD)] ── MATCH ──→ [Validate Characteristics] ── MATCH ──→ [Approve]
       ↓ NO MATCH                                      ↓ MISMATCH
[Internal Cache Lookup] ── MATCH ───→ [Validate Characteristics] ── MATCH ──→ [Approve]
       ↓ NO MATCH                                      ↓ MISMATCH
[External Lookup (GS1)] ── MATCH ───→ [Validate Characteristics] ── MATCH ──→ [Approve]
       ↓ NO MATCH                                      ↓ MISMATCH
[Additional External] ─── MATCH ────→ [Validate Characteristics] ── MATCH ──→ [Approve]
       ↓ NO MATCH                                      ↓ MISMATCH
[Reject Product]                               [Reject Product]
```

### Client Considerations

> "O problema de usar a Mirakl como fonte de consulta após a verificação de todos os produtos do catálogo, é que o catálogo na Mirakl permite cadastrar um mesmo produto mais de uma vez. O EAN vai ficar repetido e a complexidade para varrer uma base muito grande vai ser maior."

**Translation:** Using Mirakl as a lookup source after verifying all catalog products is problematic because Mirakl allows registering the same product multiple times. EANs can be duplicated, and scanning a large database increases complexity.

**Proposed Solution:** Build an internal validated EAN cache to avoid repeated external lookups.

---

## Assumptions

| ID | Assumption | Source | Risk if Wrong |
|----|------------|--------|---------------|
| A01 | GOLD database contains pre-validated product data | Context doc | Internal lookup won't work |
| A02 | GS1 API is accessible for EAN validation | Context doc | Cannot validate externally |
| A03 | EAN validation can be integrated into product registration flow | Implied | Architecture rework |
| A04 | Mirakl supports blocking products during validation | Implied | Cannot enforce validation |
| A05 | Sellers can resubmit products after correction | Implied | Poor seller experience |
| A06 | Simplus system has relevant role in validation | Context doc | May not be needed |
| A07 | Existing catalog cleanup can run in batches | Implied | Performance issues |
| A08 | Project language is Portuguese (Brazilian) | Source material | Documentation/communication |

---

## Open Questions

### Tier 1: Critical (Blocks PRD)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q1 | Data | What is the current volume of products without EAN in the catalog? | Catalog cleanup scope |
| Q2 | Data | What is the estimated volume of products with incorrect EANs? | Validation effort estimation |
| Q3 | Business | What is the financial impact of product mismatches (returns, complaints)? | Business case |
| Q4 | Technical | What is the daily volume of new product registrations? | System capacity planning |
| Q5 | Technical | What exactly is Simplus and what role does it play? | Integration scope |
| Q6 | Technical | What is the GOLD database schema and how is it accessed? | Internal validation |
| Q7 | Business | What is the decision for products in catalog without EAN - exclude immediately or grace period? | Catalog cleanup strategy |
| Q8 | Technical | What GS1 API/service will be used for external validation? | External integration |

### Tier 2: Important (Needed for TRD)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q9 | Technical | What product characteristics should be compared for EAN/product matching? | Validation logic |
| Q10 | Technical | How is the Mirakl-to-Omnilogic integration currently implemented? | Integration point |
| Q11 | Technical | What are the SLA requirements for validation (response time)? | Performance requirements |
| Q12 | Operations | How should sellers be notified of EAN failures? | Communication flow |
| Q13 | Technical | What is the authentication mechanism for GS1 API? | Security architecture |
| Q14 | Data | What is the GOLD database update frequency? | Data freshness |

### Tier 3: Nice to Have

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q15 | UX | Can sellers preview EAN validation results before submission? | User experience |
| Q16 | Data | Historical data on EAN-related product returns? | Baseline metrics |
| Q17 | Operations | What is the current manual process for handling EAN issues? | Process improvement |

---

## Gap Analysis

```
Area                        Known    Gaps     Status
------------------------------------------------------------
Problem Statement           90%      10%      Good: Minor data gaps
Use Cases                   80%      20%      Good: Defined but need detail
Acceptance Criteria         80%      20%      Good: Defined, need clarification
Technical Solution          40%      60%      Warning: Proposal only, no specs
System Integrations         50%      50%      Warning: Systems named, no details
Data Sources                40%      60%      Critical: GOLD, GS1, Simplus unclear
Validation Logic            30%      70%      Critical: Matching criteria undefined
Timeline/Budget              0%     100%      Critical: Not provided
Current State Metrics       20%      80%      Warning: Baselines missing
```

### Visual Summary

| Area | Status |
|------|--------|
| Problem Understanding | Well defined |
| Use Cases | Defined, need refinement |
| Systems Landscape | Partially known |
| Technical Architecture | High-level only |
| Validation Logic | Needs specification |
| Data Sources | Need clarification |
| Timeline/Budget | Not provided |
| Success Metrics | Defined but no baseline |

---

## Contradictions & Clarifications Needed

| Issue | Observation | Sources | Resolution Needed |
|-------|-------------|---------|-------------------|
| Simplus Role | Listed in systems but not explained | Context doc | Q5: What is Simplus? |
| Catalog Cleanup Treatment | UC-07 says "Produto excluído (Oficializar tratativa com catálogo)" | Use cases | Q7: Confirm exclusion policy |
| Multiple External Sources | AC05 requires multiple external bases, only GS1 mentioned | Acceptance criteria | Q8: Which external sources? |
| Validation vs. Match | Use cases reference "match interno/externo" but criteria unclear | Use cases | Q9: What constitutes a match? |

---

## Metrics (From Client)

**Primary Metrics:**

| Metric | Description | Baseline |
|--------|-------------|----------|
| Products without EAN | Count of catalog products missing EAN | TBD |
| Products with altered EAN | Products that had EAN changed after validation | TBD |
| Estimated loss | Proportional value based on sales/returns of rejected products | TBD |

**Success Metrics (Inferred):**

| Metric | Target | Measurement |
|--------|--------|-------------|
| New products with valid EAN | 100% | Registration logs |
| Catalog cleanup completion | 100% | Catalog audit |
| False rejection rate | < 5% | Manual review sample |
| Validation response time | < 5s | P95 latency |

---

## Next Steps

### Immediate Actions

1. **Send Open Questions to Carrefour Team**
   - Priority: Tier 1 questions (Q1-Q8)
   - Format: Structured questionnaire in Portuguese
   - Expected response: 1 week

2. **Request Additional Materials**
   - GOLD database documentation
   - GS1 API documentation and access
   - Simplus system overview
   - Current catalog statistics (EAN coverage)

3. **Schedule Follow-up Sessions**
   - Technical deep-dive for integration architecture
   - Business stakeholder session for catalog cleanup policy
   - Data analysis session for current state metrics

### After Client Response

1. Update Blueprint with answers
2. Resolve assumptions and contradictions
3. Proceed to PRD development for Milestone 1-2
4. Create technical discovery tasks for TRD

### Discovery Sessions Recommended

| Session | Purpose | Attendees | Duration |
|---------|---------|-----------|----------|
| Architecture Review | Map current integrations, define EAN Validator position | Tech leads | 2 hours |
| Validation Logic Definition | Define matching criteria and thresholds | Product + Tech | 2 hours |
| Catalog Cleanup Strategy | Define policy for existing products | Product + Catalog team | 1.5 hours |
| External Integration | GS1 and other external sources | Tech + Vendor | 1 hour |

---

## Appendix A: EAN Technical Reference

### EAN Format Specifications

| Type | Digits | Description |
|------|--------|-------------|
| EAN-8 | 8 | Short format for small products |
| EAN-13 | 13 | Standard format (most common) |
| UPC-A | 12 | North American format |
| GTIN-14 | 14 | Trade item identification |

### Check Digit Algorithm (GS1)

The last digit of an EAN is a check digit calculated as follows:
1. Sum digits in odd positions × 1
2. Sum digits in even positions × 3
3. Total = sum of (1) and (2)
4. Check digit = (10 - (Total mod 10)) mod 10

**Example:** EAN 590123412345**2**
- Valid check digit ensures basic format integrity
- Does NOT validate product ownership or characteristics

### Validation Hierarchy

```
┌───────────────────────────────────────────────────────────────┐
│                     EAN VALIDATION PYRAMID                     │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Level 3: Product Characteristic Match                        │
│    ┌─────────────────────────────────────────────────────┐   │
│    │ Compare: Brand, Model, Description, Category, etc.  │   │
│    │ Sources: GS1 registry, Internal cache               │   │
│    └─────────────────────────────────────────────────────┘   │
│                                                               │
│  Level 2: EAN Ownership Verification                          │
│    ┌─────────────────────────────────────────────────────┐   │
│    │ Verify: EAN is registered and belongs to claimed     │   │
│    │         manufacturer in official registries          │   │
│    └─────────────────────────────────────────────────────┘   │
│                                                               │
│  Level 1: Format Validation                                   │
│    ┌─────────────────────────────────────────────────────┐   │
│    │ Check: Valid length, numeric only, check digit       │   │
│    └─────────────────────────────────────────────────────┘   │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## Appendix B: Referenced Links

| Reference | URL | Purpose |
|-----------|-----|---------|
| Product Registration Flowchart | https://c4br.atlassian.net/wiki/spaces/Prod/pages/2803826764 | Current flow |
| VTEX Marketplace Docs | https://help.vtex.com/pt/tutorial/acoes-para-a-operacao-de-marketplaces-vtex--2SdIflvwywiOqCpczKCfev | Marketplace operations |
| EAN Information | https://e-tailize.com/blog/what-is-an-ean-code-and-why-do-you-need-one/ | EAN overview |
| GS1 Check Digit | https://www.gs1.org/services/how-calculate-check-digit-manually | Validation algorithm |
| GS1 Brazil GTIN | https://gs1br.org/codigos-e-padroes/padroes-de-identificacao/Paginas/GTIN.aspx | Brazilian EAN standards |
| VTEX Marketplace API | https://developers.vtex.com/docs/api-reference/marketplace-apis#overview | API reference |

---

## Related Documents

- PRD (Pending) - To be created after Blueprint approval
- TRD (Pending) - To be created after PRD approval

---

*Document Version: 0.1 - DRAFT*
*Author: Gabriela Souza*
