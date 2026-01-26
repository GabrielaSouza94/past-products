# PRD - Products Without Offer Blocker

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | Products Without Offer Blocker |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Draft |

---

## Introduction

### Document Purpose

This PRD defines requirements for the Products Without Offer Blocker - a cost optimization solution that prevents products without valid offers from entering the enrichment pipeline.

### Project Scope

**In Scope:**

| Feature | Description |
|---------|-------------|
| Offer Validation | Validate price and stock presence |
| Registration Blocking | Block products without offers |
| Seller Notification | Clear feedback on rejection |
| Update Passthrough | Allow stock/price updates for existing products |
| Logging | Track blocked attempts |

**Out of Scope:**

| Item | Rationale |
|------|-----------|
| Offer quality validation | Only presence, not reasonableness |
| Price range validation | No min/max checks |
| Inventory management | Just validation |
| Historical catalog cleanup | New registrations only |

---

## Business Context

### Current State

```
[Seller] → [Mirakl] → [Omnilogic] → [EAN Lookup] → [VTEX] → [Published]
              ↓            💰           💰           💰
        (No gate)      (Cost)       (Cost)       (Cost)
```

Products without offers proceed through entire pipeline, incurring costs, but are never published.

### Problem Statement

> **Carrefour's operations team** needs a way to **block products without valid offers before pipeline processing** to **eliminate unnecessary enrichment costs** for products that cannot be sold.

### Business Objectives

| ID | Objective | Measurement |
|----|-----------|-------------|
| OBJ-01 | Reduce enrichment costs | Cost savings per blocked product |
| OBJ-02 | Block 100% of invalid registrations | Zero products without offers in pipeline |
| OBJ-03 | Maintain seller experience | Resubmission success rate |

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Products blocked without offers | 100% | Validation logs |
| Cost savings | TBD (pending baseline) | Monthly cost reduction |
| Seller resubmission rate | > 80% | After adding offers |
| False positive rate | < 1% | Valid products blocked |

---

## Product Requirements

### BR-01: Offer Presence Validation

**Priority:** Critical

**Description:**
Validate that product registration includes both price and stock values.

**Acceptance Criteria:**
- [ ] Validate price field is present
- [ ] Validate price is not null
- [ ] Validate price is greater than zero
- [ ] Validate price is numeric
- [ ] Validate stock field is present
- [ ] Validate stock is not null
- [ ] Validate stock is greater than zero
- [ ] Validate stock is numeric

**Business Rules:**
- BRL-01: Price MUST be present and numeric
- BRL-02: Price MUST be greater than zero
- BRL-03: Stock MUST be present and numeric
- BRL-04: Stock MUST be greater than zero
- BRL-05: Both price AND stock MUST be valid

---

### BR-02: Registration Blocking

**Priority:** Critical

**Description:**
Block product registrations that fail offer validation before pipeline processing.

**Acceptance Criteria:**
- [ ] Block registration before Mirakl processing
- [ ] Block before Omnilogic enrichment
- [ ] Block before EAN validation
- [ ] Block before VTEX registration
- [ ] Log blocked attempt with details

**Business Rules:**
- BRL-06: Blocked products MUST NOT enter Mirakl
- BRL-07: Blocked products MUST NOT incur enrichment costs
- BRL-08: Blocking MUST be synchronous

---

### BR-03: Seller Notification

**Priority:** High

**Description:**
Provide clear, actionable feedback to sellers when registration is blocked.

**Rejection Messages:**

| Code | Condition | Message |
|------|-----------|---------|
| REJ-01 | Missing price | "Price is required for product registration" |
| REJ-02 | Invalid price (zero) | "Price must be greater than zero" |
| REJ-03 | Invalid price (format) | "Price must be a valid number" |
| REJ-04 | Missing stock | "Stock quantity is required for product registration" |
| REJ-05 | Invalid stock (zero) | "Stock must be greater than zero" |
| REJ-06 | Invalid stock (format) | "Stock must be a valid number" |

**Acceptance Criteria:**
- [ ] Return specific rejection reason
- [ ] Message is clear and actionable
- [ ] Seller can understand what to fix
- [ ] Response includes all validation errors

**Business Rules:**
- BRL-09: Rejection reason MUST be specific
- BRL-10: Message MUST be actionable
- BRL-11: All validation errors MUST be returned

---

### BR-04: Update Passthrough

**Priority:** High

**Description:**
Allow stock and price updates for existing products without blocking.

**Acceptance Criteria:**
- [ ] Distinguish new registration from update
- [ ] Allow stock updates for existing products
- [ ] Allow price updates for existing products
- [ ] Updates proceed to normal processing

**Business Rules:**
- BRL-12: Updates MUST NOT be blocked
- BRL-13: Only new registrations require full validation
- BRL-14: Updates MUST be identified by product ID

---

### BR-05: Logging and Analytics

**Priority:** Medium

**Description:**
Log all blocked attempts for analysis and debugging.

**Log Schema:**

| Field | Description |
|-------|-------------|
| timestamp | When blocked |
| seller_id | Who submitted |
| product_data | Submitted payload |
| rejection_code | Why blocked |
| rejection_message | Full message |

**Acceptance Criteria:**
- [ ] Log all blocked attempts
- [ ] Include seller identification
- [ ] Include rejection reason
- [ ] Logs accessible for analysis
- [ ] Logs retained per policy

**Business Rules:**
- BRL-15: All blocks MUST be logged
- BRL-16: Logs MUST include rejection reason
- BRL-17: Logs MUST be queryable

---

## Use Cases

### UC-01: Product with Valid Offer

**Actor:** Seller
**Preconditions:** Seller submits product with price > 0 and stock > 0

**Flow:**
1. Seller submits product registration
2. System validates price (present, > 0, numeric)
3. System validates stock (present, > 0, numeric)
4. Both validations pass
5. Product proceeds to Mirakl
6. Normal pipeline continues

**Postconditions:** Product enters pipeline

---

### UC-02: Product with Price but No Stock

**Actor:** Seller
**Preconditions:** Seller submits product with valid price but stock = 0/null

**Flow:**
1. Seller submits product registration
2. System validates price (passes)
3. System validates stock (fails - zero/null)
4. System blocks registration
5. Seller receives: "Stock must be greater than zero"

**Postconditions:** Product blocked, seller notified

---

### UC-03: Product with Stock but No Price

**Actor:** Seller
**Preconditions:** Seller submits product with valid stock but price = 0/null

**Flow:**
1. Seller submits product registration
2. System validates price (fails - zero/null)
3. System blocks registration
4. Seller receives: "Price must be greater than zero"

**Postconditions:** Product blocked, seller notified

---

### UC-04: Product with No Offer Data

**Actor:** Seller
**Preconditions:** Seller submits product without price and stock

**Flow:**
1. Seller submits product registration
2. System validates price (fails - missing)
3. System validates stock (fails - missing)
4. System blocks registration
5. Seller receives both errors

**Postconditions:** Product blocked with multiple errors

---

### UC-05: Product with Invalid Characters

**Actor:** Seller
**Preconditions:** Seller submits product with "ABC" in price field

**Flow:**
1. Seller submits product registration
2. System validates price format (fails - not numeric)
3. System blocks registration
4. Seller receives: "Price must be a valid number"

**Postconditions:** Product blocked, seller notified

---

### UC-06: Stock Update for Existing Product

**Actor:** Seller
**Preconditions:** Product already in catalog, seller sends stock update

**Flow:**
1. Seller submits stock update (not new registration)
2. System identifies this as update (product ID exists)
3. System passes through without offer validation
4. Update proceeds normally

**Postconditions:** Update processed

---

## Non-Functional Requirements

| Category | Requirement | Target |
|----------|-------------|--------|
| Performance | Validation response time | < 100ms |
| Availability | System uptime | 99.9% |
| Scalability | Handle peak registration volume | TBD per current volume |
| Logging | Retention period | Per Carrefour policy |

---

## Business Rules Summary

| ID | Rule |
|----|------|
| BRL-01 | Price MUST be present and numeric |
| BRL-02 | Price MUST be greater than zero |
| BRL-03 | Stock MUST be present and numeric |
| BRL-04 | Stock MUST be greater than zero |
| BRL-05 | Both price AND stock MUST be valid |
| BRL-06 | Blocked products MUST NOT enter Mirakl |
| BRL-07 | Blocked products MUST NOT incur enrichment costs |
| BRL-08 | Blocking MUST be synchronous |
| BRL-09 | Rejection reason MUST be specific |
| BRL-10 | Message MUST be actionable |
| BRL-11 | All validation errors MUST be returned |
| BRL-12 | Updates MUST NOT be blocked |
| BRL-13 | Only new registrations require full validation |
| BRL-14 | Updates MUST be identified by product ID |
| BRL-15 | All blocks MUST be logged |
| BRL-16 | Logs MUST include rejection reason |
| BRL-17 | Logs MUST be queryable |

---

## Glossary

| Term | Definition |
|------|------------|
| Offer | Combination of price and stock for a product |
| Pipeline | Product registration workflow (Mirakl → Omnilogic → VTEX) |
| Enrichment | Product categorization and data enhancement |
| Blocking | Preventing registration from proceeding |

---

## Related Documents

- [Blueprint](../discovery-docs/offer-blocker-blueprint.md)
- [Solution Diagrams](./offer-blocker-solution-diagrams.md)
- [SOW](./offer-blocker-sow.md)
- [Assumptions Log](./assumptions-decisions-log.md)

---

*Document Version: 1.0*
*Author: Gabriela Souza*
