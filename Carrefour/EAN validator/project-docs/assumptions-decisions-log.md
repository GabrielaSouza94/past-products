# Assumptions & Decisions Log

## EAN Validator System

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | EAN Validator System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Living Document |
| Purpose | Track assumptions made and decisions taken during project documentation |

---

## How to Use This Document

This document tracks:
- **Assumptions (A)**: Things we believe to be true but need client confirmation
- **Decisions (D)**: Choices made during documentation that affect scope/approach
- **Open Items (O)**: Items requiring client input before implementation

**Status Legend:**
- 🟡 Pending Confirmation
- 🟢 Confirmed
- 🔴 Rejected/Changed
- ⚪ Superseded

---

## Assumptions Register

### Technical Assumptions

| ID | Assumption | Rationale | Impact if Wrong | Status | Date |
|----|------------|-----------|-----------------|--------|------|
| A-T01 | GOLD database is accessible via internal API | Mentioned in context as internal validation source | Cannot implement internal validation layer | 🟡 Pending | - |
| A-T02 | GS1 Brazil provides API access for EAN validation | GS1 is the official EAN registry | Cannot implement external validation | 🟡 Pending | - |
| A-T03 | Mirakl supports webhook/callback for product validation | Required for integration | Major architecture change needed | 🟡 Pending | - |
| A-T04 | Simplus is an alternative/complementary EAN data source | Listed in systems but undefined | May need to add/remove integration | 🟡 Pending | - |
| A-T05 | EAN validation can intercept between Mirakl and Omnilogic | Based on ANATEL pattern | Integration point may differ | 🟡 Pending | - |
| A-T06 | Check digit validation follows standard GS1 algorithm | Industry standard | Validation logic incorrect | 🟡 Pending | - |
| A-T07 | BigQuery can be used for validated EAN cache | GCP infrastructure exists (per ANATEL) | Need different storage solution | 🟡 Pending | - |
| A-T08 | Batch processing is acceptable for catalog cleanup | Large volume expected | May need real-time processing | 🟡 Pending | - |

### Business Assumptions

| ID | Assumption | Rationale | Impact if Wrong | Status | Date |
|----|------------|-----------|-----------------|--------|------|
| A-B01 | Products without EAN will be excluded from catalog | UC-07 implies exclusion | Need alternative handling | 🟡 Pending | - |
| A-B02 | Sellers receive notification of EAN rejection | Standard UX practice | Poor seller experience | 🟡 Pending | - |
| A-B03 | Grace period not required for catalog cleanup | Not mentioned in context | Seller disruption risk | 🟡 Pending | - |
| A-B04 | EAN validation applies to all product categories | No exclusions mentioned | Scope may be narrower | 🟡 Pending | - |
| A-B05 | Failed products can be resubmitted after correction | Standard marketplace practice | Seller workflow affected | 🟡 Pending | - |
| A-B06 | Manual review process exists for edge cases | Not defined but implied | 100% automation not possible | 🟡 Pending | - |

### Data Assumptions

| ID | Assumption | Rationale | Impact if Wrong | Status | Date |
|----|------------|-----------|-----------------|--------|------|
| A-D01 | GOLD contains brand, model, description for products | Required for matching | Cannot validate product correspondence | 🟡 Pending | - |
| A-D02 | GS1 returns product attributes (brand, model, category) | Required for external matching | Limited validation possible | 🟡 Pending | - |
| A-D03 | EAN-13 is the primary format used | Most common in Brazil | Support additional formats | 🟡 Pending | - |
| A-D04 | Seller-provided data includes brand and model | Required for comparison | Matching criteria limited | 🟡 Pending | - |
| A-D05 | Historical catalog has significant EAN issues | Problem statement implies this | Cleanup scope may be smaller | 🟡 Pending | - |

---

## Decisions Register

### Architectural Decisions

| ID | Decision | Alternatives Considered | Rationale | Impact | Date |
|----|----------|------------------------|-----------|--------|------|
| D-A01 | Phase development: New Products first, then Catalog Cleanup | All at once | Lower risk, faster initial value | Defers catalog cleanup | - |
| D-A02 | Internal validation before external | External only | Reduces external API costs, faster response | Requires internal DB maintenance | - |
| D-A03 | Build validated EAN cache | Query Mirakl directly | Avoids duplicate lookups, better performance | Additional storage needed | - |
| D-A04 | Integration point after Omnilogic enrichment | Before Omnilogic | Matches ANATEL pattern, leverages existing flow | Depends on existing integration | - |

### Scope Decisions

| ID | Decision | Alternatives Considered | Rationale | Impact | Date |
|----|----------|------------------------|-----------|--------|------|
| D-S01 | MVP focuses on Milestones 1-2 (New Products) | All 5 milestones | Manageable scope, faster delivery | Catalog cleanup deferred | - |
| D-S02 | EAN format validation includes EAN-8, EAN-13, UPC-A, GTIN-14 | EAN-13 only | Comprehensive coverage | Slightly more complex logic | - |
| D-S03 | Product matching uses brand + model + category | Full attribute comparison | Core identifiers sufficient | May miss edge cases | - |
| D-S04 | Simplus treated as optional/future scope | Required integration | Role unclear, don't block progress | May need to add later | - |

### Process Decisions

| ID | Decision | Alternatives Considered | Rationale | Impact | Date |
|----|----------|------------------------|-----------|--------|------|
| D-P01 | Rejected products go to "Pending Correction" status | Immediate deletion | Seller-friendly, allows correction | Products remain in queue | - |
| D-P02 | Catalog cleanup runs in nightly batches | Real-time | Performance, system stability | Delayed cleanup | - |
| D-P03 | Manual review queue for no-match products | Auto-reject all | Reduces false positives | Operational overhead | - |

---

## Open Items (Requiring Client Input)

### Critical (Blocks Development)

| ID | Item | Question | Owner | Due | Resolution |
|----|------|----------|-------|-----|------------|
| O-C01 | Simplus Definition | What is Simplus and what role does it play in EAN validation? | Client | TBD | - |
| O-C02 | GOLD Access | How is GOLD database accessed? What is the schema? | Client | TBD | - |
| O-C03 | GS1 Integration | What GS1 API/service will be used? Is access available? | Client | TBD | - |
| O-C04 | Matching Criteria | What specific attributes determine EAN/product match? | Client | TBD | - |
| O-C05 | Catalog Cleanup Policy | What happens to existing products without EAN? | Client | TBD | - |

### Important (Blocks TRD)

| ID | Item | Question | Owner | Due | Resolution |
|----|------|----------|-------|-----|------------|
| O-I01 | Catalog Volume | How many products currently in catalog? | Client | TBD | - |
| O-I02 | Products Without EAN | What % of catalog lacks EAN? | Client | TBD | - |
| O-I03 | Daily Registrations | How many new products registered daily? | Client | TBD | - |
| O-I04 | SLA Requirements | What response time is acceptable for validation? | Client | TBD | - |
| O-I05 | Seller Notification | How should sellers be notified of failures? | Client | TBD | - |

### Nice to Have

| ID | Item | Question | Owner | Due | Resolution |
|----|------|----------|-------|-----|------------|
| O-N01 | Baseline Metrics | Current return rate for EAN-related issues? | Client | TBD | - |
| O-N02 | Priority Categories | Are some product categories higher priority? | Client | TBD | - |

---

## Change Log

| Date | Version | Change Description | Author |
|------|---------|-------------------|--------|
| - | 1.0 | Initial document creation | Gabriela Souza |

---

## Related Documents

- [Blueprint](../discovery-docs/ean-validator-blueprint.md) - Discovery document
- [PRD](./ean-validator-prd.md) - Product Requirements Document

---

*Living Document - Updated as assumptions are confirmed and decisions are made*
*Author: Gabriela Souza*
