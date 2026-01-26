# Assumptions & Decisions Log

## Products Without Offer Blocker

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | Products Without Offer Blocker |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Living Document |

---

## Assumptions Register

### Technical Assumptions

| ID | Assumption | Rationale | Impact if Wrong | Status |
|----|------------|-----------|-----------------|--------|
| A-T01 | Seller API can be intercepted before Mirakl | Need early gate | Different integration approach | 🟡 Pending |
| A-T02 | Product and offer data sent together | Context document implies | Separate flows needed | 🟡 Pending |
| A-T03 | Price and stock fields are clearly identifiable | Standard e-commerce | Field mapping needed | 🟡 Pending |
| A-T04 | Webhook/callback mechanism available | Common integration pattern | Polling/batch alternative | 🟡 Pending |
| A-T05 | Validation can run synchronously | Real-time blocking | Async with status check | 🟡 Pending |

### Business Assumptions

| ID | Assumption | Rationale | Impact if Wrong | Status |
|----|------------|-----------|-----------------|--------|
| A-B01 | Zero price means "no price" not "free" | Context implies | May block valid free items | 🟡 Pending |
| A-B02 | Zero stock means "no stock" not "backorder" | Context implies | May block pre-orders | 🟡 Pending |
| A-B03 | All product categories require offers | Not specified | Category exceptions needed | 🟡 Pending |
| A-B04 | Sellers understand offer requirements | Assumed | Education needed | 🟡 Pending |
| A-B05 | Blocked products can be resubmitted | Standard practice | Workflow impact | 🟡 Pending |

---

## Decisions Register

### Scope Decisions

| ID | Decision | Alternatives | Rationale | Date |
|----|----------|--------------|-----------|------|
| D-S01 | Block before any pipeline processing | Block after Mirakl | Maximum cost savings | - |
| D-S02 | Require both price AND stock | Either price OR stock | Both needed for sale | - |
| D-S03 | Allow stock updates for existing products | Block all updates | UC-06 requirement | - |
| D-S04 | Reject invalid characters immediately | Sanitize input | Data quality | - |

### Technical Decisions

| ID | Decision | Alternatives | Rationale | Date |
|----|----------|--------------|-----------|------|
| D-T01 | Synchronous validation | Async with queue | Immediate feedback | - |
| D-T02 | Return specific rejection reasons | Generic "invalid" | Seller experience | - |
| D-T03 | Log all blocked attempts | No logging | Analytics and debugging | - |

---

## Open Items

### Critical

| ID | Item | Question | Owner | Resolution |
|----|------|----------|-------|------------|
| O-C01 | Integration Point | Where exactly can we intercept? | Carrefour Tech | TBD |
| O-C02 | Cost Baseline | Cost per product through pipeline? | Carrefour Finance | TBD |
| O-C03 | Volume Baseline | Products registered without offers? | Carrefour Data | TBD |

### Important

| ID | Item | Question | Owner | Resolution |
|----|------|----------|-------|------------|
| O-I01 | Zero-Price Scenarios | Are free products valid? | Carrefour Product | TBD |
| O-I02 | Pre-order Scenarios | Can stock be zero for pre-orders? | Carrefour Product | TBD |
| O-I03 | Error Messages | What language/format for sellers? | Carrefour UX | TBD |

---

## Related Documents

- [Blueprint](../discovery-docs/offer-blocker-blueprint.md)
- [PRD](./offer-blocker-prd.md)
- [Solution Diagrams](./offer-blocker-solution-diagrams.md)
- [SOW](./offer-blocker-sow.md)

---

*Living Document - Updated as assumptions are confirmed*
*Author: Gabriela Souza*
