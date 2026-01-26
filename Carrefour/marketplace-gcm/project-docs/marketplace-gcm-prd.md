# PRD - CSM (Catalog Management System)

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | CSM - Catalog Management System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza|
| Version | 0.1 |
| Status | Draft - Pending Client Validation |
| Scope | Milestone 1: Catalog Management |

---

## Introduction

### Document Purpose

This Product Requirements Document (PRD) defines the business needs, functional requirements, and scope for the CSM (Catalog Management System) platform - Milestone 1: Catalog Management.

This document serves as the foundation for:
- Technical design (TRD)
- Development planning
- Client alignment and approval
- Quality assurance and acceptance testing

**Relationship to Other Documents:**
- **Blueprint:** Provides strategic context and client understanding (see `discovery-docs/marketplace-gcm-blueprint.md`)
- **TRD:** Will define HOW to implement these requirements (to be created)

### Project Scope

**In Scope for Milestone 1 (Catalog Management):**

| Feature | Status | Description |
|---------|--------|-------------|
| Product Registration | Active | Register new products via CSM API |
| Catalog Editing | Active | Edit existing product information |
| Offer Registration | Active | Create and manage product offers |
| API Endpoint Redirection | Active | Redirect seller/integrator calls from Mirakl to CSM |
| Monitoring & Control | Active | Enable visibility and control over catalog operations |

**Out of Scope (Future Phases):**

| Feature | Phase | Rationale |
|---------|-------|-----------|
| Product Deletion | Phase 2 | ON HOLD - Pending process definition |
| Product Data Validation | Phase 2 | ON HOLD - Until internal catalog creation |
| Internal 3P Catalog | Phase 3 | Future scope per solution roadmap |
| Seller Management | Milestone 2 | Separate milestone |
| Order Management | Milestone 3 | Separate milestone |
| Financial Management | Milestone 4 | Separate milestone |
| Promotions Management | Milestone 5 | Separate milestone |

### Audience

| Audience | Usage |
|----------|-------|
| Carrefour Product Team | Requirements validation, business rules definition |
| Carrefour Tech Team | Technical feasibility review |
| Engineering Team | Development reference |
| QA Team | Test case development |
| Stakeholders | Project scope alignment |

---

## Business Context

### Background / Current State

Carrefour Brasil operates a marketplace powered by the Mirakl platform. The current architecture:

```
[Sellers/Integrators] ---> [Mirakl API] ---> [Carrefour Marketplace]
                               ^
                               |
                    (No Carrefour visibility
                     or control layer)
```

**Current Challenges:**
1. **No Visibility:** Sellers and integrators call Mirakl APIs directly - Carrefour cannot monitor or validate operations
2. **No Control:** Unable to implement custom validations or business rules
3. **Limited Evolution:** Mirakl is a generic platform that cannot accommodate Carrefour-specific needs
4. **Increased Costs:** Generic solution creates operational inefficiencies

### Problem Statement

> **Marketplace sellers and integrators** need a way to **register and manage catalog products** that gives **Carrefour visibility and control** over these operations. Currently, all API calls go directly to Mirakl, preventing Carrefour from validating data, monitoring operations, or evolving the platform according to business needs.

### Business Objectives

| ID | Objective | Measurement | Status |
|----|-----------|-------------|--------|
| OBJ-01 | Gain visibility over all catalog operations | 100% of product registrations pass through CSM | TBD - Baseline needed |
| OBJ-02 | Enable custom validation rules | Number of validation rules implemented | TBD - Rules to be defined |
| OBJ-03 | Improve product registration success rate | % products published without blocks on first attempt | TBD - Baseline needed |
| OBJ-04 | Reduce products stuck in registration funnel | % reduction in stuck products | TBD - Baseline needed |

**Note:** Quantified targets pending client input on current baselines and expected improvements.

### Success Metrics

| Metric | Target | Measurement Method | Timeline |
|--------|--------|-------------------|----------|
| API Redirection Coverage | 100% | CSM logs vs Mirakl direct calls | Post-launch Week 4 |
| Product Registration Volume | Maintain current volume | Daily registration count | Ongoing |
| First-Attempt Success Rate | TBD% improvement | Registration funnel analytics | Post-launch Month 1 |
| Stuck Products Reduction | TBD% reduction | Funnel stage monitoring | Post-launch Month 1 |
| API Response Time | Equal or better than Mirakl | Latency monitoring | Ongoing |

**Metrics from Client (Milestone 1):**
- Products registered and published without blocks on first attempt
- Products stuck at different stages of the registration funnel

---

## Users & Personas

| Persona | Description | Goals | Pain Points |
|---------|-------------|-------|-------------|
| **Marketplace Seller** | Third-party sellers who list products on Carrefour marketplace | Register products quickly, manage offers, update catalog | API documentation complexity, unclear rejection reasons, no visibility into status |
| **Integration Partner** | Third-party platforms that integrate with Carrefour marketplace on behalf of multiple sellers | Bulk product registration, automated catalog sync, reliable API | Rate limiting, inconsistent responses, migration effort for new endpoints |
| **Catalog Operations (Carrefour)** | Internal team managing marketplace catalog quality | Monitor registrations, enforce quality standards, resolve issues | No visibility into current operations, manual intervention required |
| **Product Team (Carrefour)** | Internal team defining catalog standards and validations | Define validation rules, evolve platform capabilities | Cannot implement rules in current Mirakl setup |

---

## Product Requirements

### BR-01: API Endpoint Redirection

**Priority:** Critical
**Persona:** All users (Sellers, Integrators, Carrefour teams)

**Description:**
All catalog management API calls currently directed to Mirakl must be redirected to CSM. CSM will act as the control layer, processing requests and forwarding them to Mirakl for execution.

**Business Value:**
Establishes the foundation for all CSM capabilities by routing traffic through Carrefour-controlled infrastructure.

**User Story:**
As a Carrefour product manager, I want all seller/integrator catalog API calls to pass through CSM so that we have visibility and control over marketplace operations.

**Acceptance Criteria:**
- [ ] CSM exposes endpoints that mirror Mirakl catalog management APIs
- [ ] Sellers/integrators can call CSM endpoints using existing API patterns
- [ ] CSM successfully forwards requests to Mirakl and returns responses
- [ ] All API calls are logged for monitoring purposes
- [ ] API response times are equal to or better than direct Mirakl calls
- [ ] Backward compatibility is maintained for existing integrations

**Business Rules:**
- BRL-01: All catalog management API calls MUST pass through CSM
- BRL-02: Existing Mirakl API contracts MUST be maintained for backward compatibility
- BRL-03: CSM MUST log all API requests and responses

**Dependencies:**
- Depends on: None (foundational requirement)
- Blocking: BR-02, BR-03, BR-04

**Client Responsibility:**
- Provide complete inventory of Mirakl API endpoints currently in use
- Communicate endpoint migration to sellers/integrators
- Provide Mirakl API credentials for CSM integration

---

### BR-02: Product Registration

**Priority:** Critical
**Persona:** Marketplace Seller, Integration Partner

**Description:**
Enable sellers and integrators to register new products in the Carrefour marketplace catalog through CSM endpoints.

**Business Value:**
Core functionality for marketplace operations. Enables controlled product onboarding with future validation capabilities.

**User Story:**
As a marketplace seller, I want to register my products through the CSM API so that they can be listed on Carrefour's marketplace.

**Acceptance Criteria:**
- [ ] Sellers can submit product registration requests via CSM API
- [ ] Product data is validated against required fields (per Mirakl schema)
- [ ] Successful registrations are forwarded to Mirakl
- [ ] Sellers receive confirmation with product ID upon successful registration
- [ ] Failed registrations return clear error messages with rejection reasons
- [ ] Registration status is logged and queryable
- [ ] Batch product registration is supported

**Business Rules:**
- BRL-04: Product registration MUST include all mandatory fields per Mirakl schema
- BRL-05: Each product MUST be associated with a valid seller account
- BRL-06: Product registration responses MUST include status and any error details

**Dependencies:**
- Depends on: BR-01 (API Endpoint Redirection)
- Blocking: BR-03 (Catalog Editing)

**Client Responsibility:**
- Confirm mandatory product fields
- Define error message standards (language, format)

**Reference:**
- Mirakl API: https://help.mirakl.net/help/api-doc/seller/mmp.html

---

### BR-03: Catalog Editing

**Priority:** Critical
**Persona:** Marketplace Seller, Integration Partner

**Description:**
Enable sellers and integrators to update existing product information in the catalog through CSM endpoints.

**Business Value:**
Allows sellers to maintain accurate product information, improving catalog quality and customer experience.

**User Story:**
As a marketplace seller, I want to update my product information through the CSM API so that my listings remain accurate and current.

**Acceptance Criteria:**
- [ ] Sellers can update product attributes via CSM API
- [ ] Partial updates are supported (only changed fields required)
- [ ] Updates are validated before forwarding to Mirakl
- [ ] Sellers receive confirmation upon successful update
- [ ] Failed updates return clear error messages
- [ ] Update history is logged for audit purposes
- [ ] Concurrent update handling (optimistic locking or similar)

**Business Rules:**
- BRL-07: Only the seller who owns the product CAN update it
- BRL-08: Certain fields MAY be immutable after initial registration (TBD by client)
- BRL-09: All catalog edits MUST be logged with timestamp and user ID

**Dependencies:**
- Depends on: BR-01 (API Endpoint Redirection), BR-02 (Product Registration)
- Blocking: None

**Client Responsibility:**
- Define which fields are immutable after registration
- Confirm update validation rules

---

### BR-04: Offer Registration

**Priority:** Critical
**Persona:** Marketplace Seller, Integration Partner

**Description:**
Enable sellers and integrators to create and manage product offers (pricing, availability, shipping) through CSM endpoints.

**Business Value:**
Offers are the commercial representation of products. Controlled offer management enables pricing visibility and future promotional capabilities.

**User Story:**
As a marketplace seller, I want to create and update offers for my products so that customers can see pricing and availability on the marketplace.

**Acceptance Criteria:**
- [ ] Sellers can create offers linked to registered products
- [ ] Offer data includes: price, quantity, shipping options, availability
- [ ] Offers are validated before forwarding to Mirakl
- [ ] Sellers can update existing offers
- [ ] Sellers can deactivate offers without deleting
- [ ] Bulk offer creation/update is supported
- [ ] Offer status changes are logged

**Business Rules:**
- BRL-10: An offer MUST be linked to a valid, registered product
- BRL-11: An offer MUST have a valid price (> 0)
- BRL-12: Offer quantity MUST be a non-negative integer
- BRL-13: Only the seller who owns the product CAN create/update offers

**Dependencies:**
- Depends on: BR-01 (API Endpoint Redirection), BR-02 (Product Registration)
- Blocking: None

**Client Responsibility:**
- Confirm offer data schema
- Define pricing validation rules (min/max, currency)

**Reference:**
- Mirakl API OF01: https://help.mirakl.net/help/api-doc/seller/mmp.html#OF01

---

### BR-05: Monitoring Dashboard

**Priority:** High
**Persona:** Catalog Operations (Carrefour), Product Team (Carrefour)

**Description:**
Provide Carrefour internal teams with visibility into catalog operations, including registration volumes, success rates, and funnel metrics.

**Business Value:**
Enables data-driven decisions about catalog quality and identifies bottlenecks in the product registration process.

**User Story:**
As a Carrefour catalog operations manager, I want to monitor product registration activity so that I can identify issues and measure success rates.

**Acceptance Criteria:**
- [ ] Dashboard displays real-time registration volume
- [ ] Dashboard shows success/failure rates by time period
- [ ] Dashboard displays products stuck at each funnel stage
- [ ] Dashboard allows filtering by seller, product category, time range
- [ ] Data is exportable for further analysis
- [ ] Alerting for anomalies (spike in failures, unusual volume)

**Business Rules:**
- BRL-14: Dashboard access MUST be restricted to authorized Carrefour users
- BRL-15: Dashboard data MUST refresh at minimum every 5 minutes

**Dependencies:**
- Depends on: BR-01, BR-02, BR-03, BR-04 (requires logging data)
- Blocking: None

**Client Responsibility:**
- Define user access levels and permissions
- Confirm required dashboard metrics

---

### BR-06: Product Deletion (Phase 2)

**Priority:** Medium
**Persona:** Marketplace Seller
**Status:** ON HOLD - Phase 2

**Description:**
Enable sellers to remove products from the catalog through CSM endpoints.

**Business Value:**
Allows sellers to manage product lifecycle, removing discontinued or out-of-stock items.

**Note:** This requirement is ON HOLD pending definition of:
- Current manual deletion process
- Impact analysis on seller operations
- Expected gains from automation

**Placeholder Acceptance Criteria:**
- [ ] Sellers can request product deletion via API
- [ ] Deletion is soft-delete (recoverable) vs hard-delete (TBD)
- [ ] Linked offers are handled appropriately
- [ ] Deletion is logged for audit

**Client Responsibility:**
- Provide current manual deletion process details
- Define deletion policy (soft vs hard delete)
- Confirm impact on related entities (offers, orders)

---

### BR-07: Product Data Validation (Phase 2)

**Priority:** Medium
**Persona:** Product Team (Carrefour)
**Status:** ON HOLD - Phase 2

**Description:**
Implement custom validation rules for product data before forwarding to Mirakl.

**Business Value:**
Ensures catalog quality by enforcing Carrefour-specific standards beyond Mirakl's basic validations.

**Note:** This requirement is ON HOLD until internal 3P catalog creation (Part 3 of solution roadmap). Validators will be implemented progressively following the product roadmap.

**Placeholder Acceptance Criteria:**
- [ ] Validation rules are configurable without code changes
- [ ] Validation failures return clear, actionable error messages
- [ ] Validation rules can be A/B tested before enforcement
- [ ] Validation history is logged

**Client Responsibility:**
- Define validation rules by product category
- Provide validation criteria for each rule
- Define enforcement policy (block vs warn)

---

## Use Cases / Business Scenarios

### UC-01: Seller Registers New Product

**Actor:** Marketplace Seller
**Preconditions:** Seller has valid API credentials, seller account is active

**Main Flow:**
1. Seller sends product registration request to CSM API
2. CSM validates request format and required fields
3. CSM logs the request
4. CSM forwards request to Mirakl
5. Mirakl processes registration and returns response
6. CSM logs the response
7. CSM returns success confirmation with product ID to seller

**Alternate Flows:**
- **A1:** If product already exists → Return duplicate error with existing product ID
- **A2:** If seller wants batch registration → Process multiple products in single request

**Error Flows:**
- **E1:** If required fields missing → Return validation error with list of missing fields
- **E2:** If Mirakl returns error → Return error to seller with details
- **E3:** If Mirakl unavailable → Return service unavailable, retry logic

**Postconditions:** Product is registered in Mirakl catalog, registration logged in CSM

---

### UC-02: Seller Updates Product Information

**Actor:** Marketplace Seller
**Preconditions:** Product exists, seller owns the product

**Main Flow:**
1. Seller sends update request with product ID and changed fields
2. CSM validates seller ownership
3. CSM validates update data
4. CSM logs the request
5. CSM forwards update to Mirakl
6. Mirakl processes update and returns response
7. CSM logs the response
8. CSM returns success confirmation to seller

**Alternate Flows:**
- **A1:** If partial update → Only process provided fields

**Error Flows:**
- **E1:** If seller does not own product → Return authorization error
- **E2:** If immutable field update attempted → Return validation error
- **E3:** If product not found → Return not found error

**Postconditions:** Product information updated in Mirakl, update logged in CSM

---

### UC-03: Seller Creates Offer

**Actor:** Marketplace Seller
**Preconditions:** Product exists and is active, seller owns the product

**Main Flow:**
1. Seller sends offer creation request with product ID and offer details
2. CSM validates product exists and seller owns it
3. CSM validates offer data (price, quantity, availability)
4. CSM logs the request
5. CSM forwards offer to Mirakl
6. Mirakl processes offer and returns response
7. CSM logs the response
8. CSM returns success confirmation with offer ID

**Alternate Flows:**
- **A1:** If bulk offer creation → Process multiple offers in single request
- **A2:** If offer exists → Update existing offer

**Error Flows:**
- **E1:** If product not found → Return product not found error
- **E2:** If invalid price → Return validation error
- **E3:** If seller does not own product → Return authorization error

**Postconditions:** Offer created in Mirakl, offer logged in CSM

---

### UC-04: Carrefour Monitors Catalog Activity

**Actor:** Catalog Operations (Carrefour)
**Preconditions:** User has dashboard access

**Main Flow:**
1. User accesses CSM monitoring dashboard
2. System displays real-time registration metrics
3. User filters by date range, seller, or category
4. System updates display with filtered data
5. User exports data if needed

**Alternate Flows:**
- **A1:** If user sets up alert → System notifies on threshold breach

**Error Flows:**
- **E1:** If no data available → Display empty state with explanation

**Postconditions:** User has visibility into catalog operations

---

## Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|-------------|--------|-------------|
| Performance | API response time | < Mirakl latency + 200ms | P95 latency monitoring |
| Performance | Throughput | Match current Mirakl volume | Requests per second |
| Availability | Uptime | 99.5% | Monitoring dashboard |
| Availability | Mirakl dependency handling | Graceful degradation | Error rate during Mirakl outage |
| Security | API authentication | Match Mirakl auth model | Security audit |
| Security | Data encryption | TLS 1.2+ in transit | Certificate validation |
| Scalability | Concurrent requests | TBD (pending volume data) | Load testing |
| Logging | Request/response logging | 100% coverage | Log audit |
| Logging | Log retention | TBD (per Carrefour policy) | Storage monitoring |
| Monitoring | Real-time metrics | < 5 min delay | Dashboard refresh |

**Note:** Specific scalability targets pending client input on transaction volumes (Q4 from Blueprint).

---

## Business Rules

| Rule ID | Rule | Rationale |
|---------|------|-----------|
| BRL-01 | All catalog management API calls MUST pass through CSM | Core requirement for visibility |
| BRL-02 | Existing Mirakl API contracts MUST be maintained | Backward compatibility |
| BRL-03 | CSM MUST log all API requests and responses | Audit and monitoring |
| BRL-04 | Product registration MUST include all mandatory fields | Data quality |
| BRL-05 | Each product MUST be associated with a valid seller | Data integrity |
| BRL-06 | Registration responses MUST include status and errors | Seller experience |
| BRL-07 | Only product owner CAN update product | Authorization |
| BRL-08 | Certain fields MAY be immutable (TBD) | Data integrity |
| BRL-09 | All edits MUST be logged with timestamp and user | Audit trail |
| BRL-10 | Offer MUST be linked to valid product | Data integrity |
| BRL-11 | Offer MUST have valid price (> 0) | Business logic |
| BRL-12 | Offer quantity MUST be non-negative | Business logic |
| BRL-13 | Only product owner CAN manage offers | Authorization |
| BRL-14 | Dashboard access restricted to authorized users | Security |
| BRL-15 | Dashboard data refresh minimum every 5 minutes | Usability |

---

## Assumptions & Dependencies

### Assumptions

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A01 | Mirakl API contracts will remain stable during CSM development | API mapping rework |
| A02 | Sellers will migrate to CSM endpoints as communicated | Adoption delays |
| A03 | CSM authentication will match current Mirakl auth model | Additional auth development |
| A04 | Mirakl contract includes necessary API access | Legal/licensing issues |
| A05 | Current Mirakl performance is acceptable baseline | Performance requirements change |
| A06 | Portuguese is the primary language for error messages | Localization needed |
| A07 | Internal catalog (Part 3) is not required for Phase 1 | Scope creep if required |

### Dependencies

| Dependency | Owner | Status | Risk if Unavailable |
|------------|-------|--------|---------------------|
| Mirakl API endpoint inventory | Carrefour | Pending | Cannot map all endpoints |
| Mirakl API credentials | Carrefour | Pending | Cannot test integration |
| Seller communication plan | Carrefour | Pending | Adoption issues |
| Validation rules definition | Carrefour | Pending (Phase 2) | Phase 2 delayed |
| Transaction volume data | Carrefour | Pending | Scaling decisions impacted |

---

## Exclusions

| Exclusion | Rationale | Future Phase? |
|-----------|-----------|---------------|
| Product Deletion | ON HOLD - Process definition pending | Phase 2 |
| Product Validation | ON HOLD - Until internal catalog | Phase 2 |
| Internal 3P Catalog | Per solution roadmap | Phase 3 |
| Seller Management | Separate milestone | Milestone 2 |
| Order Management | Separate milestone | Milestone 3 |
| Financial Management | Separate milestone | Milestone 4 |
| Promotions Management | Separate milestone | Milestone 5 |
| UI/Admin Portal | Focus on API layer | Future consideration |
| Mobile app | API-first approach | Future consideration |

---

## Risks

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---------|------|------------|--------|------------|
| RSK-01 | Mirakl API changes during development | Low | High | Monitor Mirakl release notes, abstract API layer |
| RSK-02 | Seller/integrator migration resistance | Medium | High | Clear communication, migration support, parallel operation period |
| RSK-03 | Performance degradation due to proxy layer | Medium | Medium | Performance testing, optimization, caching strategies |
| RSK-04 | Incomplete API endpoint inventory | Medium | High | Early discovery, phased rollout |
| RSK-05 | Mirakl rate limiting affects CSM | Medium | Medium | Implement queuing, rate limit handling |
| RSK-06 | Scope creep from undefined Phase 2 items | Medium | Medium | Clear phase boundaries, change control |
| RSK-07 | Data loss during Mirakl unavailability | Low | High | Queue requests, retry logic, alerting |

---

## Glossary

| Term | Definition |
|------|------------|
| CSM | Catalog Management System - Carrefour's catalog management system |
| Mirakl | Third-party marketplace platform currently used by Carrefour |
| 3P | Third-party (refers to marketplace sellers, not Carrefour-owned products) |
| Seller | Third-party merchant who lists products on Carrefour marketplace |
| Integrator | Third-party platform that integrates with marketplace on behalf of sellers |
| Offer | Commercial representation of a product (price, quantity, availability) |
| Catalog | Collection of products available on the marketplace |
| Product Registration | Process of adding a new product to the catalog |
| Endpoint Redirection | Routing API calls from Mirakl to CSM |

---

## Approvals

| Name | Role | Signature | Date |
|------|------|-----------|------|
| TBD | Carrefour Product Owner | | |
| TBD | Carrefour Tech Lead | | |
| Gabriela Souza | Product Manager | | |

---

## Open Items (From Blueprint)

The following items from the Blueprint require resolution:

### Critical (Blocking Full PRD Completion)

| ID | Question | Impact |
|----|----------|--------|
| Q2 | Expected timeline for each milestone | Resource planning |
| Q3 | Other applications in marketplace architecture | Integration scope |
| Q4 | Transaction volume (products, offers per day) | Scaling decisions |

### Important (Needed for TRD)

| ID | Question | Impact |
|----|----------|--------|
| Q7 | Complete Mirakl API endpoint inventory | API mapping |
| Q8 | Authentication model details | Security architecture |
| Q10 | SLA requirements | Infrastructure decisions |

---

## Appendices

### Appendix A: Product Registration Funnel

```
[API Request Received]
        |
        v
[Request Validation] -----> [Validation Error] --> [Return Error]
        |
        v (Pass)
[Log Request]
        |
        v
[Forward to Mirakl]
        |
        v
[Mirakl Processing] -----> [Mirakl Error] --> [Log & Return Error]
        |
        v (Success)
[Log Response]
        |
        v
[Return Success + Product ID]
```

### Appendix B: Milestone 1 Metrics (As Provided by Client)

**Success Metrics:**
- Products registered and published without blocks on first attempt
- Products stuck at different stages of the registration funnel

**Complementary Information Needed:**
- Details of product registration funnel (stages, status, flow)
- Types of validation currently performed and missing criteria
- Manual product deletion funnel and service details

---

