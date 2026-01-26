# PRD - ANATEL Homologation Validation System

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | ANATEL Homologation Validation System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Complete |
| Scope | MVP 1: Product Registration Validation |

---

## Introduction

### Document Purpose

This Product Requirements Document (PRD) defines the business needs, functional requirements, and scope for the ANATEL Homologation Validation System - a regulatory compliance solution for Carrefour's marketplace.

This document serves as the foundation for:
- Technical design (TRD)
- Development planning
- Client alignment and approval
- Quality assurance and acceptance testing

**Relationship to Other Documents:**
- **Blueprint:** Provides strategic context and regulatory requirements (see `discovery-docs/anatel-blueprint.md`)
- **TRD:** Will define HOW to implement these requirements

### Project Scope

**In Scope for MVP 1:**

| Feature | Status | Description |
|---------|--------|-------------|
| Omnilogic Integration | Active | Build CM21 endpoint for product synchronization |
| Category Filtering | Active | Filter products by homologable categories |
| Product Identification | Active | Identify if product requires ANATEL license |
| License Validation | Active | Validate license against ANATEL database |
| Rejection Flow | Active | Configure Mirakl rejection for invalid products |

**Out of Scope (Future Phases):**

| Feature | Phase | Rationale |
|---------|-------|-----------|
| License Expiration Monitoring | Future | Not required for MVP |
| Automatic Seller Notification | Future | Manual process for now |
| Category List Management UI | Future | Manual configuration for MVP |
| Periodic Pending Item Purge | Future | Will evaluate based on volume |
| Seller Reporting to ANATEL | Milestone 4 | Separate regulatory milestone |

### Audience

| Audience | Usage |
|----------|-------|
| Carrefour Product Team | Requirements validation, business rules definition |
| Carrefour Tech Team | Technical feasibility review |
| Carrefour Legal/Compliance | Regulatory alignment verification |
| Engineering Team | Development reference |
| QA Team | Test case development |

---

## Business Context

### Background / Current State

Carrefour Brasil operates a marketplace using the Mirakl platform, integrated with Omnilogic for product categorization and enrichment. Currently:

```
[Seller] → [Mirakl] → [Omnilogic] → [Published Product]
                          ↓
              (No ANATEL validation)
```

**Current Challenges:**
1. **Regulatory Non-Compliance:** Telecom products listed without valid ANATEL homologation
2. **Legal Liability:** Marketplace legally responsible for unauthorized product sales
3. **Piracy Risk:** Counterfeit telecom products sold without verification
4. **Regulatory Penalties:** Risk of fines and sanctions from ANATEL

### Problem Statement

> **Carrefour's marketplace compliance team** needs a way to **validate ANATEL homologation licenses for telecommunications products** to ensure **regulatory compliance and avoid legal liability**. Currently, products are listed without license verification, exposing Carrefour to regulatory penalties and enabling the sale of non-compliant products.

### Business Objectives

| ID | Objective | Measurement | Target |
|----|-----------|-------------|--------|
| OBJ-01 | Block 100% of non-compliant telecom products | Products rejected without valid license | 100% |
| OBJ-02 | Achieve regulatory compliance | ANATEL audit results | Full compliance |
| OBJ-03 | Maintain seller experience | Resubmission success rate | TBD |
| OBJ-04 | Minimize false rejections | Valid products incorrectly rejected | < 5% |

### Success Metrics

| Metric | Target | Measurement Method | Timeline |
|--------|--------|-------------------|----------|
| Products Validated | 100% of homologable products | Validation logs | Ongoing |
| Invalid License Rejection Rate | 100% | Rejection count vs invalid attempts | Ongoing |
| False Positive Rate | < 5% | Manual review sample | Monthly |
| Seller Resubmission Success | > 80% | Resubmission completion rate | Ongoing |
| System Availability | 99.5% | Monitoring | Ongoing |

---

## Users & Personas

| Persona | Description | Goals | Pain Points |
|---------|-------------|-------|-------------|
| **Marketplace Seller** | Third-party seller listing telecom products | Register products quickly, understand compliance requirements | Unclear rejection reasons, complex license requirements |
| **Catalog Operations** | Internal team managing product listings | Ensure compliance, process rejections efficiently | Manual validation, volume of non-compliant products |
| **Compliance Team** | Legal/regulatory compliance oversight | Achieve ANATEL compliance, avoid penalties | Lack of automated validation, audit preparation |
| **Omnilogic System** | Categorization and enrichment service | Process products, return enriched data | Integration complexity |

---

## Product Requirements

### BR-01: Omnilogic Integration Endpoint (CM21)

**Priority:** Critical
**Persona:** Omnilogic System

**Description:**
Build an endpoint (CM21) to receive product data from Omnilogic after categorization and enrichment, enabling ANATEL validation before returning to Mirakl.

**Business Value:**
Enables validation at the correct point in the product flow where category and enrichment data are available.

**User Story:**
As the validation system, I need to receive enriched product data from Omnilogic so that I can perform ANATEL license validation with complete product information.

**Acceptance Criteria:**
- [ ] Endpoint receives product payload from Omnilogic
- [ ] Endpoint returns trackingId for async status lookup
- [ ] System supports CM22 (status check) and CM23 (report) endpoints
- [ ] Integration is asynchronous to match existing Omnilogic flow
- [ ] Failed validations are logged with details

**Business Rules:**
- BRL-01: Validation MUST occur after Omnilogic enrichment
- BRL-02: System MUST return trackingId within SLA
- BRL-03: All requests MUST be logged for audit

**Dependencies:**
- Depends on: None (foundational requirement)
- Blocking: BR-02, BR-03, BR-04

**Technical Reference:**
- CM21: POST {{URL}}/api/mcm/products/synchronization
- CM22: GET {{URL}}/api/mcm/products/synchronization/{ID}
- CM23: GET {{URL}}/api/mcm/products/synchronization/{ID}/report

---

### BR-02: Category Filtering

**Priority:** Critical
**Persona:** Catalog Operations

**Description:**
Filter products by configurable category list to determine which products require ANATEL validation. Only products in homologable categories should be validated.

**Business Value:**
Prevents unnecessary validation of products that don't require ANATEL licenses (e.g., furniture, clothing).

**User Story:**
As a catalog operations manager, I want only telecom-related products to be validated so that non-telecom products are not incorrectly blocked.

**Acceptance Criteria:**
- [ ] System maintains configurable list of homologable categories
- [ ] Products not in homologable categories bypass validation
- [ ] Products in homologable categories proceed to validation
- [ ] Category list can be updated without code deployment
- [ ] Category filtering is logged for audit

**Business Rules:**
- BRL-04: Only products in configured categories MUST be validated
- BRL-05: Category list MUST be configurable
- BRL-06: Non-homologable products MUST pass through unchanged

**Dependencies:**
- Depends on: BR-01 (Omnilogic Integration)
- Blocking: BR-03

**Client Responsibility:**
- Provide initial list of homologable categories
- Maintain category list over time

---

### BR-03: Product Identification (Homologable Detection)

**Priority:** Critical
**Persona:** Catalog Operations

**Description:**
Identify whether a product within a homologable category actually requires an ANATEL license, using brand/manufacturer and model data.

**Business Value:**
Ensures accurate identification of products requiring licenses, reducing false positives.

**User Story:**
As a catalog operations manager, I want the system to correctly identify which products need ANATEL licenses so that we don't incorrectly reject valid products.

**Acceptance Criteria:**
- [ ] System uses brand/manufacturer data for identification
- [ ] System uses model data for identification
- [ ] System handles inconsistent product naming from sellers
- [ ] System matches against ANATEL database product types
- [ ] Identification logic is configurable

**Business Rules:**
- BRL-07: Products MUST be identified using brand and model
- BRL-08: System MUST handle naming inconsistencies
- BRL-09: Unidentifiable products MUST be flagged for review

**Dependencies:**
- Depends on: BR-01, BR-02
- Blocking: BR-04

---

### BR-04: License Validation (3-Layer)

**Priority:** Critical
**Persona:** Compliance Team

**Description:**
Validate ANATEL licenses using a three-layer validation approach against the internal ANATEL database.

**Business Value:**
Ensures comprehensive validation that meets ANATEL regulatory requirements.

**User Story:**
As a compliance team member, I want products validated against the ANATEL database so that we only sell properly licensed telecommunications products.

**Validation Layers:**

| Layer | Validation | Check |
|-------|------------|-------|
| 1 | License Exists | Verify license code exists in ANATEL database |
| 2 | License Active | Verify license status = "vigente" (active) |
| 3 | License Match | Verify license belongs to correct product |

**Acceptance Criteria:**
- [ ] Layer 1: Validate license exists in internal ANATEL database
- [ ] Layer 2: Validate license status is "vigente" (active)
- [ ] Layer 3: Validate license matches product (type, model, manufacturer)
- [ ] All three layers must pass for product to be approved
- [ ] Failed validation returns specific layer failure
- [ ] Validation results are logged for audit

**Business Rules:**
- BRL-10: All three validation layers MUST pass
- BRL-11: License status MUST be "vigente" to be valid
- BRL-12: License MUST match product brand/model
- BRL-13: Validation failures MUST specify which layer failed

**Data Source:**
- BigQuery: br-digitalcomm-prod.br_digitalcomm_anatel_homologados.produtos
- Updates: Every 2 days via crawler

**Dependencies:**
- Depends on: BR-01, BR-02, BR-03
- Blocking: BR-05

---

### BR-05: Mirakl Rejection Flow

**Priority:** Critical
**Persona:** Marketplace Seller

**Description:**
Configure the Mirakl rejection flow to move products with invalid/missing licenses to "pending" status, allowing sellers to correct and resubmit.

**Business Value:**
Provides a path for sellers to correct license issues without permanently blocking products.

**User Story:**
As a marketplace seller, I want to understand why my product was rejected and have the ability to fix the issue and resubmit.

**Acceptance Criteria:**
- [ ] Invalid products are moved to "aguardando alteração" (pending) status
- [ ] Rejection reason includes specific validation failure
- [ ] Seller can view rejection reason in Mirakl
- [ ] Seller can update license and resubmit
- [ ] Resubmitted products go through validation again
- [ ] Successful resubmission moves product to published

**Business Rules:**
- BRL-14: Invalid products MUST be moved to pending status
- BRL-15: Rejection reason MUST be provided to seller
- BRL-16: Resubmission MUST trigger re-validation

**Dependencies:**
- Depends on: BR-01, BR-02, BR-03, BR-04
- Blocking: None

---

### BR-06: License Field Requirement

**Priority:** High
**Persona:** Marketplace Seller

**Description:**
Require sellers to provide ANATEL homologation code in product registration for products in homologable categories.

**Business Value:**
Ensures license data is captured at registration time for validation.

**User Story:**
As a marketplace seller, I want to know that I need to provide my ANATEL license code when registering telecom products.

**Acceptance Criteria:**
- [ ] License field is required for homologable products
- [ ] Clear error message if license field is empty
- [ ] License field accepts standard ANATEL code format
- [ ] License code is displayed in product listing (per ANATEL requirement)

**Business Rules:**
- BRL-17: License field MUST be required for homologable products
- BRL-18: Empty license field MUST trigger rejection
- BRL-19: License code MUST be displayed in product listing

**Dependencies:**
- Depends on: BR-02
- Blocking: BR-04

---

## Use Cases / Business Scenarios

### UC-01: Product Rejected by Omnilogic

**Actor:** Omnilogic System
**Preconditions:** Product submitted for categorization

**Main Flow:**
1. Omnilogic rejects product (no category identified)
2. Product returns to seller as rejected
3. No ANATEL validation performed

**Postconditions:** Product rejected, not validated

---

### UC-02: Product Not in Homologable Category

**Actor:** Validation System
**Preconditions:** Product categorized by Omnilogic

**Main Flow:**
1. System receives product from Omnilogic
2. System checks product category
3. Category not in homologable list
4. Product bypasses validation
5. Product proceeds to publish

**Postconditions:** Product published without ANATEL validation

---

### UC-03: Homologable Product with Valid License

**Actor:** Marketplace Seller
**Preconditions:** Seller submits telecom product with license

**Main Flow:**
1. Seller registers product with license code
2. Omnilogic categorizes and enriches product
3. System identifies product as homologable
4. System validates license (all 3 layers pass)
5. Product proceeds to publish
6. License code displayed in listing

**Postconditions:** Product published with valid license

---

### UC-04: Homologable Product with Invalid License

**Actor:** Marketplace Seller
**Preconditions:** Seller submits telecom product with invalid license

**Main Flow:**
1. Seller registers product with license code
2. Omnilogic categorizes and enriches product
3. System identifies product as homologable
4. System validates license (one or more layers fail)
5. System rejects product with specific failure reason
6. Product moved to "pending" status
7. Seller receives rejection notification

**Alternate Flow:**
- **A1:** Seller corrects license and resubmits → Return to step 2

**Postconditions:** Product rejected, pending seller correction

---

### UC-05: Homologable Product with Missing License

**Actor:** Marketplace Seller
**Preconditions:** Seller submits telecom product without license

**Main Flow:**
1. Seller registers product without license code
2. Omnilogic categorizes and enriches product
3. System identifies product as homologable
4. System detects missing license field
5. System rejects product with "missing license" reason
6. Product moved to "pending" status

**Postconditions:** Product rejected, pending license submission

---

## Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|-------------|--------|-------------|
| Performance | Validation response time | < 5 seconds | P95 latency |
| Performance | Throughput | Handle current Mirakl volume | Requests per second |
| Availability | Uptime | 99.5% | Monitoring |
| Data | ANATEL database freshness | < 48 hours | Crawler logs |
| Security | Data encryption | TLS 1.2+ in transit | Certificate validation |
| Logging | Audit trail | 100% of validations logged | Log audit |
| Logging | Log retention | Per Carrefour policy | Storage monitoring |

---

## Business Rules Summary

| Rule ID | Rule | Rationale |
|---------|------|-----------|
| BRL-01 | Validation MUST occur after Omnilogic enrichment | Requires category data |
| BRL-02 | System MUST return trackingId within SLA | Async integration |
| BRL-03 | All requests MUST be logged for audit | Compliance |
| BRL-04 | Only products in configured categories MUST be validated | Efficiency |
| BRL-05 | Category list MUST be configurable | Maintainability |
| BRL-06 | Non-homologable products MUST pass unchanged | User experience |
| BRL-07 | Products MUST be identified using brand and model | Accuracy |
| BRL-08 | System MUST handle naming inconsistencies | Seller variations |
| BRL-09 | Unidentifiable products MUST be flagged | Manual review |
| BRL-10 | All three validation layers MUST pass | Compliance |
| BRL-11 | License status MUST be "vigente" | ANATEL requirement |
| BRL-12 | License MUST match product brand/model | Accuracy |
| BRL-13 | Validation failures MUST specify failed layer | Debugging |
| BRL-14 | Invalid products MUST move to pending status | Seller experience |
| BRL-15 | Rejection reason MUST be provided | Transparency |
| BRL-16 | Resubmission MUST trigger re-validation | Compliance |
| BRL-17 | License field MUST be required for homologable products | Data capture |
| BRL-18 | Empty license field MUST trigger rejection | Compliance |
| BRL-19 | License code MUST display in product listing | ANATEL requirement |

---

## Assumptions & Dependencies

### Assumptions

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A01 | ANATEL database is reliable and accessible | Cannot validate |
| A02 | Omnilogic provides enrichment before validation | Incomplete data |
| A03 | Mirakl rejection flow works as expected | Cannot block products |
| A04 | BigQuery crawler updates every 2 days | Stale data |
| A05 | Brand/model matching is sufficient | False positives |
| A06 | Sellers can resubmit after fixing license | Poor experience |

### Dependencies

| Dependency | Owner | Status | Risk if Unavailable |
|------------|-------|--------|---------------------|
| ANATEL database (BigQuery) | Portal Seller Team | Available | Cannot validate licenses |
| Omnilogic integration | Omnilogic | Available | Cannot receive enriched data |
| Mirakl rejection API | Mirakl | Available | Cannot reject products |
| Homologable category list | Carrefour | Required | Incorrect filtering |

---

## Risks

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---------|------|------------|--------|------------|
| RSK-01 | ANATEL database unavailable | Low | High | Implement fallback/queue |
| RSK-02 | False positive rejections | Medium | High | Brand/model matching refinement |
| RSK-03 | Seller confusion on rejection | Medium | Medium | Clear error messages |
| RSK-04 | Volume spike on launch | Medium | Medium | Load testing |
| RSK-05 | Category list incomplete | Medium | High | Thorough initial review |
| RSK-06 | Omnilogic integration issues | Low | High | Integration testing |

---

## Glossary

| Term | Definition |
|------|------------|
| ANATEL | Agência Nacional de Telecomunicações - Brazilian telecommunications regulatory agency |
| Homologation | Official certification/approval by ANATEL |
| Vigente | Active/valid status for ANATEL license |
| Omnilogic | Third-party service for product categorization and enrichment |
| Mirakl | Marketplace platform used by Carrefour |
| CM21/22/23 | API endpoints for product synchronization |
| BigQuery | Google Cloud data warehouse storing ANATEL database |
| Seller | Third-party merchant listing products on marketplace |

---

## Approvals

| Name | Role | Signature | Date |
|------|------|-----------|------|
| TBD | Carrefour Product Owner | | |
| TBD | Carrefour Compliance | | |
| Gabriela Souza | Product Manager | | |

---

## Appendices

### Appendix A: Validation Flow Diagram

```
[Product from Omnilogic]
         |
         v
[Check Homologable Category] --NO--> [Pass Through to Mirakl]
         |
        YES
         |
         v
[Identify Product Type]
         |
         v
[Check License Field] --EMPTY--> [Reject: Missing License]
         |
      PRESENT
         |
         v
[Validation Layer 1: License Exists?] --NO--> [Reject: License Not Found]
         |
        YES
         |
         v
[Validation Layer 2: Status = Vigente?] --NO--> [Reject: License Inactive]
         |
        YES
         |
         v
[Validation Layer 3: Matches Product?] --NO--> [Reject: License Mismatch]
         |
        YES
         |
         v
[Approve: Proceed to Mirakl Publish]
```

### Appendix B: ANATEL Database Fields

| Field | Description | Usage |
|-------|-------------|-------|
| Tipo de produto | Product type (e.g., Smartphone) | Product identification |
| Modelo do produto | Product model | License matching |
| Nome Comercial | Commercial name | Product identification |
| Fabricante | Manufacturer | License matching |
| N° processo SEI | SEI process number | Not used |
| Status da homologação | Homologation status | Validation Layer 2 |
| Data da homologação | Homologation date | Reference only |

### Appendix C: MVP 1 User Stories

1. Build CM21 endpoint for Omnilogic communication
2. Verify product belongs to homologable categories
3. Perform homologable product identification
4. Verify license field contains a code
5. Configure Mirakl payload for pending status
6. Spike: Test Mirakl rejection flow
7. Spike: Test product update after license fix

---

## Related Documents

- [Blueprint](../discovery-docs/anatel-blueprint.md) - Discovery document
- [Context](../client-docs/Context) - Original problem context
- [Proposed Solution](../client-docs/proposed%20solution) - Technical solution proposal

---

*Document Version: 1.0*
*Author: Gabriela Souza*
