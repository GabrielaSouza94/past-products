# PRD - EAN Validator System

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | EAN Validator System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 0.1 |
| Status | Draft - Pending Client Validation |
| Scope | Phase 1: New Product Validation |

**Note:** This PRD contains assumptions that require client confirmation. See [Assumptions & Decisions Log](./assumptions-decisions-log.md) for details.

---

## Introduction

### Document Purpose

This Product Requirements Document (PRD) defines the business needs, functional requirements, and scope for the EAN Validator System - a product catalog data quality solution for Carrefour's marketplace.

**Phase 1 Scope:** This document focuses on new product validation (Milestones 1-2). Existing catalog cleanup (Milestones 3-5) will be addressed in Phase 2.

This document serves as the foundation for:
- Technical design (TRD)
- Development planning
- Client alignment and approval
- Quality assurance and acceptance testing

**Relationship to Other Documents:**
- **Blueprint:** Provides strategic context and gap analysis (see `discovery-docs/ean-validator-blueprint.md`)
- **Assumptions Log:** Tracks assumptions made (see `project-docs/assumptions-decisions-log.md`)
- **TRD:** Will define HOW to implement these requirements

### Project Scope

**Phase 1 - In Scope (This Document):**

| Milestone | Feature | Status |
|-----------|---------|--------|
| M1 | Block product registration without EAN | Active |
| M2 | EAN format validation (legitimacy test) | Active |
| M2 | Internal EAN lookup (GOLD database) | Active |
| M2 | External EAN lookup (GS1) | Active |
| M2 | EAN/Product characteristic matching | Active |
| M2 | Rejection flow with seller notification | Active |
| - | Validated EAN cache | Active |

**Phase 2 - Out of Scope (Future):**

| Milestone | Feature | Phase | Rationale |
|-----------|---------|-------|-----------|
| M3 | EAN testing for existing catalog | Phase 2 | Higher complexity |
| M4 | EAN/Product match for existing catalog | Phase 2 | Depends on M3 |
| M5 | Full catalog cleanup | Phase 2 | Requires cleanup policy |
| - | Simplus integration | Phase 2 | Role unclear (see O-C01) |
| - | Manual EAN entry for missing codes | Future | Process TBD |

### Audience

| Audience | Usage |
|----------|-------|
| Carrefour Product Team | Requirements validation, business rules |
| Carrefour Catalog Team | Cleanup policy input |
| Engineering Team | Development reference |
| QA Team | Test case development |
| Sellers | Understand new requirements |

---

## Business Context

### Background / Current State

Carrefour Brasil operates a marketplace on the Mirakl platform where third-party sellers register products. Currently:

```
[Seller] → [Mirakl] → [MCM] → [Omnilogic] → [VTEX]
              ↓
        (EAN optional, not validated)
```

**Current Challenges:**

| Issue | Impact |
|-------|--------|
| EAN field not mandatory | Products without unique identifier |
| No EAN format validation | Invalid/malformed codes accepted |
| No EAN ownership verification | Codes may not belong to claimed product |
| No product matching validation | Wrong products grouped together |
| Catalog data quality issues | Customer confusion, potential returns |

### Problem Statement

> **Carrefour's catalog team** needs a way to **ensure all products have valid, correctly-associated EAN codes** to maintain **catalog data quality and accurate product matching**. Currently, EAN codes are optional and unvalidated, leading to product mismatches, catalog inconsistencies, and potential customer issues.

### Business Objectives

| ID | Objective | Measurement | Target |
|----|-----------|-------------|--------|
| OBJ-01 | Prevent products without EAN from entering catalog | Products blocked without EAN | 100% |
| OBJ-02 | Ensure all EAN codes are valid format | Format validation pass rate | 100% |
| OBJ-03 | Verify EAN corresponds to correct product | Match validation pass rate | 100% |
| OBJ-04 | Maintain validated EAN database | Cache hit rate for lookups | > 50% |
| OBJ-05 | Minimize false rejections | Manual review rate | < 5% |

### Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Products blocked without EAN | 100% | Registration logs |
| EAN format validation rate | 100% of submissions | Validation logs |
| Successful EAN/product matches | > 95% | Match logs |
| False positive rejection rate | < 5% | Manual review sample |
| Validation response time | < 5 seconds | P95 latency |
| Cache utilization | > 50% of lookups | Cache metrics |

---

## Users & Personas

### Primary Personas

| Persona | Description | Goals | Pain Points |
|---------|-------------|-------|-------------|
| **Marketplace Seller** | Third-party vendor registering products | Register products quickly, understand requirements | Unclear rejection reasons, EAN lookup effort |
| **Catalog Operations** | Internal team managing product catalog | Ensure data quality, process rejections | Manual validation burden, inconsistent data |

### Secondary Personas

| Persona | Description | Interaction |
|---------|-------------|-------------|
| **Customer** | End buyer on marketplace | Receives correct product matching their search |
| **Compliance Team** | Quality oversight | Reviews validation metrics and exceptions |

---

## Product Requirements

### BR-01: Mandatory EAN Field

**Priority:** Critical
**Milestone:** M1
**Reference:** Assumption A-B04

**Description:**
Block registration of any product that does not have an EAN code provided.

**Business Value:**
Ensures every product in the catalog has an identifier for matching and tracking.

**User Story:**
As a catalog operations manager, I want products without EAN to be rejected so that all catalog products have proper identification.

**Acceptance Criteria:**
- [ ] Product registration fails if EAN field is empty
- [ ] Clear error message displayed: "EAN code is required"
- [ ] Seller can correct and resubmit
- [ ] Validation occurs before any other processing
- [ ] Logging captures all blocked attempts

**Business Rules:**
- BRL-01: EAN field MUST be provided for all product registrations
- BRL-02: Empty, null, or whitespace-only EAN values MUST be rejected
- BRL-03: Rejection MUST occur early in the registration flow

**Dependencies:**
- None (foundational requirement)
- Blocking: BR-02

---

### BR-02: EAN Format Validation

**Priority:** Critical
**Milestone:** M2
**Reference:** Assumption A-T06

**Description:**
Validate that the provided EAN code follows valid format specifications and passes check digit verification.

**Business Value:**
Prevents obviously invalid codes from entering the system, reducing downstream validation costs.

**User Story:**
As a catalog operations manager, I want EAN codes validated for correct format so that only legitimate codes enter the system.

**Validation Logic:**

| Format | Length | Structure | Check Digit |
|--------|--------|-----------|-------------|
| EAN-8 | 8 digits | Numeric only | GS1 algorithm |
| EAN-13 | 13 digits | Numeric only | GS1 algorithm |
| UPC-A | 12 digits | Numeric only | GS1 algorithm |
| GTIN-14 | 14 digits | Numeric only | GS1 algorithm |

**Acceptance Criteria:**
- [ ] Validate EAN length (8, 12, 13, or 14 digits)
- [ ] Validate numeric-only characters
- [ ] Validate check digit using GS1 algorithm
- [ ] Reject with specific error: "Invalid EAN format" or "Invalid check digit"
- [ ] Log validation results with details

**Business Rules:**
- BRL-04: EAN MUST be 8, 12, 13, or 14 digits
- BRL-05: EAN MUST contain only numeric characters
- BRL-06: EAN MUST pass GS1 check digit validation
- BRL-07: Invalid format MUST be rejected before lookup

**Dependencies:**
- Depends on: BR-01
- Blocking: BR-03

---

### BR-03: Internal EAN Lookup

**Priority:** Critical
**Milestone:** M2
**Reference:** Assumptions A-T01, A-D01

**Description:**
Query internal databases (GOLD, validated EAN cache) to find matching EAN before querying external sources.

**Business Value:**
Reduces external API calls, improves response time, leverages existing validated data.

**User Story:**
As the validation system, I need to check internal sources first so that we minimize external API usage and costs.

**Lookup Hierarchy:**
1. Validated EAN Cache (previously validated products)
2. GOLD Database (pre-validated internal products)

**Acceptance Criteria:**
- [ ] Query validated EAN cache first
- [ ] If not found, query GOLD database
- [ ] Return product attributes if found (brand, model, category)
- [ ] Log lookup results (source, match/no-match)
- [ ] Proceed to external lookup only if no internal match

**Business Rules:**
- BRL-08: Internal sources MUST be queried before external
- BRL-09: Cache lookup MUST occur before GOLD lookup
- BRL-10: Internal match MUST proceed to product verification (BR-05)
- BRL-11: No internal match MUST trigger external lookup (BR-04)

**Data Requirements (GOLD):**
- EAN code
- Brand/Manufacturer
- Model/SKU
- Product category
- Product description

**Dependencies:**
- Depends on: BR-02
- Blocking: BR-04, BR-05

**Open Item:** O-C02 - GOLD database access specification required

---

### BR-04: External EAN Lookup

**Priority:** Critical
**Milestone:** M2
**Reference:** Assumptions A-T02, A-D02

**Description:**
Query external EAN registries (GS1) to validate EAN ownership and retrieve product information.

**Business Value:**
Enables validation of new products not yet in internal databases.

**User Story:**
As the validation system, I need to query external registries when internal lookup fails so that we can validate new products.

**Acceptance Criteria:**
- [ ] Query GS1 API if no internal match found
- [ ] Return product attributes if found (brand, model, category)
- [ ] Handle API errors gracefully (retry, fallback)
- [ ] Log external lookup results
- [ ] If match found, proceed to product verification

**Business Rules:**
- BRL-12: External lookup MUST only occur after internal lookup fails
- BRL-13: GS1 MUST be the primary external source
- BRL-14: API failures MUST be logged and handled gracefully
- BRL-15: External match MUST proceed to product verification (BR-05)
- BRL-16: No external match MUST trigger rejection (BR-06)

**Error Handling:**
| Error | Action |
|-------|--------|
| API timeout | Retry once, then queue for manual review |
| API rate limit | Queue for later processing |
| API unavailable | Queue for manual review |
| No match found | Proceed to rejection flow |

**Dependencies:**
- Depends on: BR-03 (no internal match)
- Blocking: BR-05, BR-06

**Open Item:** O-C03 - GS1 API access and specification required

---

### BR-05: EAN/Product Characteristic Matching

**Priority:** Critical
**Milestone:** M2
**Reference:** Assumption A-D04, Decision D-S03

**Description:**
Compare product information provided by seller against information returned from EAN lookup to verify correspondence.

**Business Value:**
Ensures the EAN code actually belongs to the product being registered, preventing mismatches.

**User Story:**
As a catalog operations manager, I want EAN codes verified against product details so that products are correctly identified.

**Matching Criteria:**

| Attribute | Weight | Match Type |
|-----------|--------|------------|
| Brand/Manufacturer | High | Fuzzy match (similarity > 80%) |
| Model/SKU | High | Fuzzy match (similarity > 80%) |
| Category | Medium | Exact or parent category match |

**Acceptance Criteria:**
- [ ] Compare brand from seller vs. lookup result
- [ ] Compare model from seller vs. lookup result
- [ ] Compare category from seller vs. lookup result
- [ ] Calculate overall match score
- [ ] Accept if match score >= threshold (80%)
- [ ] Reject if match score < threshold
- [ ] Log match details for audit

**Business Rules:**
- BRL-17: Brand comparison MUST use fuzzy matching
- BRL-18: Model comparison MUST use fuzzy matching
- BRL-19: Match threshold MUST be configurable (default 80%)
- BRL-20: Match MUST consider normalized text (lowercase, no special chars)
- BRL-21: Partial match (brand OR model) MUST trigger manual review

**Match Decision Matrix:**

| Brand Match | Model Match | Category Match | Decision |
|-------------|-------------|----------------|----------|
| Yes | Yes | Yes | Approve |
| Yes | Yes | No | Approve (log warning) |
| Yes | No | Yes | Manual Review |
| No | Yes | Yes | Manual Review |
| No | No | * | Reject |

**Dependencies:**
- Depends on: BR-03 or BR-04 (lookup result)
- Blocking: BR-06, BR-07

**Open Item:** O-C04 - Confirm matching criteria with client

---

### BR-06: Product Rejection Flow

**Priority:** High
**Milestone:** M2
**Reference:** Assumption A-B02, Decision D-P01

**Description:**
Handle products that fail validation by setting appropriate status and notifying sellers.

**Business Value:**
Provides clear feedback to sellers, enabling correction and resubmission.

**User Story:**
As a marketplace seller, I want to understand why my product was rejected so that I can correct and resubmit.

**Rejection Reasons:**

| Code | Reason | Message to Seller |
|------|--------|-------------------|
| REJ-01 | Missing EAN | "EAN code is required for product registration" |
| REJ-02 | Invalid format | "EAN code format is invalid. Please verify the code" |
| REJ-03 | Invalid check digit | "EAN code check digit is incorrect. Please verify the code" |
| REJ-04 | EAN not found | "EAN code not found in registries. Please verify the code" |
| REJ-05 | Product mismatch | "EAN code does not match product details. Please verify brand/model" |

**Acceptance Criteria:**
- [ ] Set product status to "Pending Correction"
- [ ] Store rejection reason and code
- [ ] Seller can view rejection reason in Mirakl
- [ ] Seller can correct and resubmit product
- [ ] Resubmission triggers full validation again
- [ ] Log all rejections with details

**Business Rules:**
- BRL-22: Rejected products MUST move to "Pending Correction" status
- BRL-23: Rejection reason MUST be specific and actionable
- BRL-24: Sellers MUST be able to view rejection details
- BRL-25: Resubmission MUST trigger complete re-validation

**Dependencies:**
- Depends on: BR-01, BR-02, BR-04, BR-05
- Blocking: None

---

### BR-07: Product Approval Flow

**Priority:** High
**Milestone:** M2

**Description:**
Handle products that pass all validation stages by updating status and storing validated data.

**Business Value:**
Completes the validation cycle and populates the validated EAN cache.

**User Story:**
As a marketplace seller, I want my validated product to proceed to publication so that I can start selling.

**Acceptance Criteria:**
- [ ] Set product status to approved/validated
- [ ] Store EAN and product attributes in validated cache
- [ ] Product proceeds to Omnilogic categorization
- [ ] Log approval with validation details
- [ ] Display validation success to seller

**Business Rules:**
- BRL-26: Approved products MUST proceed to next pipeline stage
- BRL-27: Approved EAN MUST be added to validated cache
- BRL-28: Cache entry MUST include all retrieved attributes

**Dependencies:**
- Depends on: BR-05 (successful match)
- Blocking: None

---

### BR-08: Validated EAN Cache

**Priority:** High
**Milestone:** M2
**Reference:** Assumption A-T07, Decision D-A03

**Description:**
Maintain a cache of previously validated EAN codes and their associated product attributes.

**Business Value:**
Reduces external API calls, improves validation speed, builds internal knowledge base.

**User Story:**
As the validation system, I need to cache validated EANs so that future lookups are faster and cheaper.

**Cache Schema:**

| Field | Type | Description |
|-------|------|-------------|
| ean_code | String | Primary key |
| brand | String | Manufacturer/brand name |
| model | String | Model/SKU identifier |
| category | String | Product category |
| description | String | Product description |
| source | String | Where validated (GOLD, GS1, etc.) |
| validated_at | Timestamp | When validation occurred |
| validation_count | Integer | Times this EAN was validated |

**Acceptance Criteria:**
- [ ] Cache populated on successful validation
- [ ] Cache queried before GOLD on all lookups
- [ ] Cache entries include source and timestamp
- [ ] Cache supports high-volume queries
- [ ] Cache data can be exported for analysis

**Business Rules:**
- BRL-29: Cache MUST be queried first in internal lookup
- BRL-30: Cache MUST store validation source
- BRL-31: Cache MUST support upsert operations
- BRL-32: Cache data MUST be persistent (not lost on restart)

**Dependencies:**
- Depends on: BR-05, BR-07
- Blocking: None (enables performance optimization)

---

### BR-09: Manual Review Queue

**Priority:** Medium
**Milestone:** M2
**Reference:** Assumption A-B06, Decision D-P03

**Description:**
Queue products with partial matches or edge cases for manual review by catalog team.

**Business Value:**
Reduces false positive rejections, handles edge cases gracefully.

**User Story:**
As a catalog operations manager, I want edge cases queued for review so that valid products aren't incorrectly rejected.

**Queue Triggers:**
- Partial match (brand matches but model doesn't, or vice versa)
- External API failures
- Match score between 60-80%

**Acceptance Criteria:**
- [ ] Products meeting queue criteria moved to review status
- [ ] Review queue accessible to catalog team
- [ ] Reviewers can approve or reject with reason
- [ ] Approved products proceed to pipeline
- [ ] Rejected products go to seller notification
- [ ] Queue metrics tracked (volume, age, resolution rate)

**Business Rules:**
- BRL-33: Partial matches MUST go to manual review
- BRL-34: API failures MUST go to manual review
- BRL-35: Reviewers MUST have approve/reject capability
- BRL-36: Review decisions MUST be logged

**Dependencies:**
- Depends on: BR-05
- Blocking: None

---

## Use Cases / Business Scenarios

### UC-01: New Product Without EAN

**Actor:** Marketplace Seller
**Preconditions:** Seller attempts to register product without EAN

**Main Flow:**
1. Seller submits product registration without EAN
2. System detects missing EAN field
3. System rejects product immediately
4. Seller receives error: "EAN code is required"
5. Product status set to "Pending Correction"

**Postconditions:** Product rejected, seller notified

---

### UC-02: New Product with Invalid EAN Format

**Actor:** Marketplace Seller
**Preconditions:** Seller submits product with malformed EAN

**Main Flow:**
1. Seller submits product with EAN "12345" (invalid length)
2. System validates EAN format
3. Format validation fails (wrong length)
4. System rejects product
5. Seller receives error: "EAN code format is invalid"

**Postconditions:** Product rejected, seller notified

---

### UC-03: New Product with Valid EAN - Internal Match

**Actor:** Marketplace Seller
**Preconditions:** Seller submits product with valid EAN that exists in cache/GOLD

**Main Flow:**
1. Seller submits product with valid EAN
2. System validates EAN format (passes)
3. System queries validated cache (found)
4. System compares product attributes
5. Match score >= 80%
6. Product approved, proceeds to Omnilogic
7. Cache entry updated with validation count

**Postconditions:** Product approved, cache updated

---

### UC-04: New Product with Valid EAN - External Match

**Actor:** Marketplace Seller
**Preconditions:** Seller submits product with valid EAN not in internal sources

**Main Flow:**
1. Seller submits product with valid EAN
2. System validates EAN format (passes)
3. System queries validated cache (not found)
4. System queries GOLD (not found)
5. System queries GS1 API (found)
6. System compares product attributes
7. Match score >= 80%
8. Product approved, proceeds to Omnilogic
9. EAN added to validated cache

**Postconditions:** Product approved, cache populated

---

### UC-05: New Product with Valid EAN - No Match Found

**Actor:** Marketplace Seller
**Preconditions:** Seller submits product with EAN not found in any source

**Main Flow:**
1. Seller submits product with valid EAN format
2. System validates EAN format (passes)
3. System queries validated cache (not found)
4. System queries GOLD (not found)
5. System queries GS1 API (not found)
6. System rejects product
7. Seller receives error: "EAN code not found in registries"

**Postconditions:** Product rejected, seller notified

---

### UC-06: New Product with Valid EAN - Product Mismatch

**Actor:** Marketplace Seller
**Preconditions:** Seller submits product with EAN that doesn't match product details

**Main Flow:**
1. Seller submits product with valid EAN
2. System validates EAN format (passes)
3. System queries sources (EAN found)
4. System compares product attributes
5. Match score < 60% (significant mismatch)
6. System rejects product
7. Seller receives error: "EAN code does not match product details"

**Postconditions:** Product rejected, seller notified

---

### UC-07: New Product with Valid EAN - Partial Match (Manual Review)

**Actor:** Marketplace Seller, Catalog Operations
**Preconditions:** Seller submits product with EAN that partially matches

**Main Flow:**
1. Seller submits product with valid EAN
2. System validates EAN format (passes)
3. System queries sources (EAN found)
4. System compares product attributes
5. Match score between 60-80%
6. Product queued for manual review
7. Catalog team reviews product
8. Team approves or rejects with reason

**Alternate Flows:**
- **A1:** Team approves → Product proceeds to Omnilogic
- **A2:** Team rejects → Seller notified with reason

**Postconditions:** Product approved or rejected by human decision

---

## Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|-------------|--------|-------------|
| Performance | Validation response time | < 5 seconds P95 | Latency monitoring |
| Performance | Throughput | 100 validations/minute | Load testing |
| Availability | System uptime | 99.5% | Monitoring |
| Data | Cache freshness | No expiration | Configuration |
| Data | GOLD sync frequency | Real-time or near-real-time | TBD per A-T01 |
| Security | API authentication | TLS 1.2+, API keys | Certificate validation |
| Logging | Audit trail | 100% of validations | Log analysis |
| Logging | Log retention | Per Carrefour policy | Storage monitoring |

---

## Business Rules Summary

| Rule ID | Rule | Requirement |
|---------|------|-------------|
| BRL-01 | EAN field MUST be provided | BR-01 |
| BRL-02 | Empty EAN MUST be rejected | BR-01 |
| BRL-03 | Rejection MUST occur early in flow | BR-01 |
| BRL-04 | EAN MUST be 8, 12, 13, or 14 digits | BR-02 |
| BRL-05 | EAN MUST be numeric only | BR-02 |
| BRL-06 | EAN MUST pass check digit validation | BR-02 |
| BRL-07 | Invalid format MUST reject before lookup | BR-02 |
| BRL-08 | Internal sources MUST be queried first | BR-03 |
| BRL-09 | Cache MUST be queried before GOLD | BR-03 |
| BRL-10 | Internal match MUST proceed to verification | BR-03 |
| BRL-11 | No internal match MUST trigger external lookup | BR-03 |
| BRL-12 | External lookup only after internal fails | BR-04 |
| BRL-13 | GS1 MUST be primary external source | BR-04 |
| BRL-14 | API failures MUST be handled gracefully | BR-04 |
| BRL-15 | External match MUST proceed to verification | BR-04 |
| BRL-16 | No external match MUST trigger rejection | BR-04 |
| BRL-17 | Brand comparison MUST use fuzzy matching | BR-05 |
| BRL-18 | Model comparison MUST use fuzzy matching | BR-05 |
| BRL-19 | Match threshold MUST be configurable | BR-05 |
| BRL-20 | Match MUST use normalized text | BR-05 |
| BRL-21 | Partial match MUST trigger manual review | BR-05 |
| BRL-22 | Rejected products MUST go to "Pending Correction" | BR-06 |
| BRL-23 | Rejection reason MUST be specific | BR-06 |
| BRL-24 | Sellers MUST see rejection details | BR-06 |
| BRL-25 | Resubmission MUST trigger re-validation | BR-06 |
| BRL-26 | Approved products MUST proceed to next stage | BR-07 |
| BRL-27 | Approved EAN MUST be cached | BR-07 |
| BRL-28 | Cache entry MUST include all attributes | BR-07 |
| BRL-29 | Cache MUST be queried first | BR-08 |
| BRL-30 | Cache MUST store validation source | BR-08 |
| BRL-31 | Cache MUST support upsert | BR-08 |
| BRL-32 | Cache data MUST be persistent | BR-08 |
| BRL-33 | Partial matches MUST go to manual review | BR-09 |
| BRL-34 | API failures MUST go to manual review | BR-09 |
| BRL-35 | Reviewers MUST have approve/reject capability | BR-09 |
| BRL-36 | Review decisions MUST be logged | BR-09 |

---

## Assumptions & Dependencies

### Assumptions

See [Assumptions & Decisions Log](./assumptions-decisions-log.md) for complete register.

**Key Assumptions for Phase 1:**

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A-T01 | GOLD database accessible via API | Cannot implement internal lookup |
| A-T02 | GS1 API available for validation | Cannot implement external lookup |
| A-T05 | Integration point after Omnilogic | Architecture may change |
| A-D01 | GOLD contains brand, model, description | Cannot validate matches |
| A-D02 | GS1 returns product attributes | Limited external validation |

### Dependencies

| Dependency | Owner | Status | Risk if Unavailable |
|------------|-------|--------|---------------------|
| GOLD database access | Carrefour Tech | TBD | Cannot validate internally |
| GS1 API access | Carrefour Tech | TBD | Cannot validate externally |
| Mirakl integration hook | Carrefour Tech | TBD | Cannot intercept registrations |
| BigQuery (for cache) | Carrefour Tech | Available (per ANATEL) | Need alternative storage |

---

## Risks

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---------|------|------------|--------|------------|
| RSK-01 | GS1 API access issues | Medium | High | Confirm access early |
| RSK-02 | GOLD data incomplete | Medium | High | Data audit before build |
| RSK-03 | High false positive rate | Medium | High | Tune matching thresholds |
| RSK-04 | Seller backlash | Medium | Medium | Clear communication, support |
| RSK-05 | Performance issues | Low | Medium | Load testing, caching |
| RSK-06 | Fuzzy matching inaccuracy | Medium | Medium | Algorithm tuning, manual review |

---

## Glossary

| Term | Definition |
|------|------------|
| EAN | European Article Number - global product barcode standard |
| GTIN | Global Trade Item Number - umbrella term for EAN/UPC codes |
| GS1 | Global Standards 1 - organization managing EAN/barcode standards |
| Check Digit | Final digit of EAN calculated using GS1 algorithm for validation |
| GOLD | Internal Carrefour product database with pre-validated products |
| Mirakl | Marketplace platform used by Carrefour |
| MCM | Mirakl Catalog Manager - product catalog module |
| Omnilogic | Third-party service for product categorization |
| Fuzzy Matching | Approximate string matching allowing for minor differences |
| Simplus | TBD - System mentioned but role undefined |

---

## Approvals

| Name | Role | Signature | Date |
|------|------|-----------|------|
| TBD | Carrefour Product Owner | | |
| TBD | Carrefour Catalog Lead | | |
| Gabriela Souza | Product Manager | | |

---

## Appendices

### Appendix A: Validation Flow Diagram

```
[Product Submitted]
        ↓
[BR-01: EAN Present?] ─── NO ───→ [REJ-01: Missing EAN]
        ↓ YES
[BR-02: Valid Format?] ─── NO ───→ [REJ-02/03: Invalid Format]
        ↓ YES
[BR-03: Cache Lookup] ─── FOUND ───→ [BR-05: Match Check]
        ↓ NOT FOUND                          ↓
[BR-03: GOLD Lookup] ─── FOUND ────→ [BR-05: Match Check]
        ↓ NOT FOUND                          ↓
[BR-04: GS1 Lookup] ─── FOUND ─────→ [BR-05: Match Check]
        ↓ NOT FOUND                          ↓
[REJ-04: Not Found]              [Score >= 80%?]
                                    ↓         ↓
                              YES → [BR-07: Approve]
                                    ↓
                              60-80% → [BR-09: Manual Review]
                                    ↓
                              < 60% → [REJ-05: Mismatch]
```

### Appendix B: GS1 Check Digit Algorithm

```
EAN-13 Example: 590123412345X (find X)

Position:  1  2  3  4  5  6  7  8  9  10 11 12 13
Digits:    5  9  0  1  2  3  4  1  2  3  4  5  X
Weight:    1  3  1  3  1  3  1  3  1  3  1  3  -

Sum = (5×1)+(9×3)+(0×1)+(1×3)+(2×1)+(3×3)+(4×1)+(1×3)+(2×1)+(3×3)+(4×1)+(5×3)
    = 5 + 27 + 0 + 3 + 2 + 9 + 4 + 3 + 2 + 9 + 4 + 15
    = 83

Check digit = (10 - (83 mod 10)) mod 10
            = (10 - 3) mod 10
            = 7

Full EAN: 5901234123457
```

---

## Related Documents

- [Blueprint](../discovery-docs/ean-validator-blueprint.md) - Discovery document
- [Assumptions Log](./assumptions-decisions-log.md) - Assumptions and decisions tracking

---

*Document Version: 0.1 - DRAFT*
*Author: Gabriela Souza*
