# Statement of Work (SOW)

## EAN Validator System

---

## Cover Page

| Field | Value |
|-------|-------|
| Document Title | Statement of Work |
| Project Name | EAN Validator System |
| Client Name | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Draft |
| Scope | Phase 1: New Product Validation |

---

## 1. Executive Summary

This Statement of Work defines the engagement terms for developing the **EAN Validator System** for Carrefour Brasil's marketplace platform.

The project addresses a critical data quality challenge: products in the Carrefour marketplace catalog currently have optional and unvalidated EAN (barcode) codes, leading to incorrect product matching, catalog inconsistencies, and potential customer issues. ANATEL validation revealed the need for robust product data validation across the marketplace.

The solution introduces a comprehensive EAN validation system that ensures every product in the catalog has a valid, verified EAN code that correctly corresponds to the product being offered. The system validates EAN format, checks against internal and external registries, and verifies product attribute correspondence before allowing products into the catalog.

**Engagement Type:** Production
**Engagement Scope:** Phase 1 - New Product Validation (Milestones 1-2)

**Key Business Outcomes:**
- 100% of new products will have valid, verified EAN codes
- Product matching accuracy will improve significantly
- Catalog data quality will be enhanced
- Foundation established for full catalog cleanup (Phase 2)

---

## 2. Scope of Work

### 2.1 In Scope

**Core Deliverables - Phase 1:**

| Deliverable | Description |
|-------------|-------------|
| EAN Presence Validation | Block product registration without EAN code |
| EAN Format Validation | Validate format, length, and check digit |
| Internal EAN Lookup | Query GOLD database and validated cache |
| External EAN Lookup | Query GS1 registry for unmatched EANs |
| Product Matching Engine | Verify EAN corresponds to submitted product |
| Rejection Flow | Handle invalid products with seller notification |
| Approval Flow | Process valid products to catalog pipeline |
| Validated EAN Cache | Store validated EANs for future lookups |
| Manual Review Queue | Queue partial matches for human review |

**Supporting Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| Blueprint Document | Project understanding and gap analysis |
| PRD (Product Requirements) | Functional and non-functional requirements |
| Solution Diagrams | Architecture and process flow documentation |
| Assumptions & Decisions Log | Tracking document for project decisions |
| SOW (This Document) | Engagement terms and scope definition |

### 2.2 Out of Scope

The following items are explicitly excluded from Phase 1:

| Item | Rationale | Future Phase |
|------|-----------|--------------|
| Existing Catalog Cleanup | Higher complexity, requires cleanup policy | Phase 2 |
| EAN Testing for Existing Products | Depends on cleanup strategy | Phase 2 (M3) |
| EAN/Product Match for Catalog | Depends on M3 completion | Phase 2 (M4-M5) |
| Simplus Integration | Role unclear, pending clarification | Phase 2 or N/A |
| Manual EAN Assignment | Process undefined | Future |
| Seller Self-Service EAN Lookup | UX enhancement | Future |
| Multi-Marketplace Support | Single platform focus | Future |

### 2.3 Assumptions

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A01 | GOLD database accessible via API | Cannot implement internal validation |
| A02 | GS1 API access available | Cannot implement external validation |
| A03 | Mirakl supports validation hook | Integration architecture change |
| A04 | Check digit follows GS1 standard | Validation logic incorrect |
| A05 | BigQuery available for cache | Need alternative storage |
| A06 | Sellers can resubmit after rejection | Workflow affected |

See [Assumptions & Decisions Log](./assumptions-decisions-log.md) for complete register.

---

## 3. Deliverables

| # | Deliverable | Description | Format | Delivery |
|---|-------------|-------------|--------|----------|
| 1 | Blueprint | Project understanding and gap analysis | Markdown | Repository |
| 2 | PRD | Product requirements document | Markdown | Repository |
| 3 | Solution Diagrams | Architecture and process flows | Markdown + Mermaid | Repository |
| 4 | Assumptions Log | Decision tracking document | Markdown | Repository |
| 5 | SOW | Engagement terms (this document) | Markdown | Repository |
| 6 | Validation Service | EAN validation microservice | Cloud Application | GCP |
| 7 | Integration APIs | Webhook receiver, status updater | REST API | Cloud Endpoint |
| 8 | EAN Cache | Validated EAN data store | BigQuery | GCP |
| 9 | Review Queue | Manual review interface | Web Application | Cloud Deployment |
| 10 | Technical Documentation | API specs and deployment guide | Markdown | Repository |

### Acceptance Criteria Summary

**Documentation Deliverables:**
- Complete and accurate content
- Assumptions clearly documented
- Reviewed by Carrefour stakeholders

**Technical Deliverables:**
- All functional requirements from PRD implemented
- EAN format validation working correctly (all formats)
- Internal lookup operational (Cache + GOLD)
- External lookup operational (GS1)
- Product matching with configurable threshold
- Rejection flow with seller notification
- Manual review queue functional
- Performance meets SLA (< 5s P95)

---

## 4. Timeline & Milestones

### Phase Overview

| Phase | Milestone | Deliverables | Dependencies |
|-------|-----------|--------------|--------------|
| Discovery | Blueprint Complete | Blueprint, Gap Analysis | Client materials |
| Discovery | PRD Complete | PRD, Assumptions Log | Blueprint approval |
| Discovery | Solution Design Complete | Solution Diagrams, SOW | PRD approval |
| Build | Integration Ready | Webhook receiver, Mirakl integration | Solution approval |
| Build | Validation Core | Format validation, lookup services | Integration ready |
| Build | Matching Engine | Product comparison, scoring | Validation core |
| Build | Review System | Manual review queue, UI | Matching engine |
| Build | MVP Complete | Full system integrated | All components |
| Launch | Go-Live | Production deployment | MVP complete |
| Support | Stabilization | Bug fixes, tuning | Go-live |

### Milestone Definitions

**M1: Discovery Complete**
- Blueprint approved by Carrefour
- PRD approved by Carrefour
- Solution diagrams complete
- Critical assumptions confirmed
- Open questions resolved

**M2: Integration Ready**
- Mirakl webhook integration working
- GOLD database connection established
- GS1 API access confirmed
- Cache infrastructure deployed

**M3: Validation Core Complete**
- EAN format validation operational
- Check digit validation working
- Internal lookup (Cache + GOLD) functional
- External lookup (GS1) functional

**M4: Matching Engine Complete**
- Product attribute comparison working
- Fuzzy matching implemented
- Scoring algorithm operational
- Threshold configuration available

**M5: Review System Complete**
- Manual review queue functional
- Review interface deployed
- Approval/rejection workflow working
- Queue metrics available

**M6: MVP Complete**
- End-to-end validation working
- All use cases tested
- Performance requirements met
- Monitoring configured

**M7: Go-Live**
- Production deployment complete
- Monitoring and alerting active
- Runbook documentation available
- Support team trained

---

## 5. Team & Responsibilities

### RACI Matrix

| Activity | PM | Tech Lead | Dev | Carrefour PO | Carrefour Tech |
|----------|-------|-----------|-----|--------------|----------------|
| Requirements Definition | R | C | I | A | C |
| Architecture Design | C | R | C | I | A |
| GOLD Integration | I | R | R | I | A |
| GS1 Integration | I | R | R | I | C |
| Development | I | A | R | I | C |
| Matching Algorithm | C | R | R | C | I |
| Review Queue UI | C | A | R | C | I |
| Integration Testing | C | R | R | C | R |
| UAT Coordination | R | I | C | A | C |
| Deployment | I | R | R | I | A |
| Production Support | C | R | R | I | A |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Client Responsibilities

| Responsibility | Owner | Description |
|----------------|-------|-------------|
| GOLD API Access | Carrefour Tech | Provide and maintain GOLD database access |
| GS1 API Credentials | Carrefour Tech | Provide GS1 API access and credentials |
| Mirakl Configuration | Carrefour Tech | Configure webhook and status integrations |
| Matching Criteria Approval | Carrefour Product | Define and approve match thresholds |
| Review Queue Operations | Carrefour Catalog | Staff and operate manual review |
| UAT Execution | Carrefour QA | Execute user acceptance testing |
| Production Approval | Carrefour PO | Approve go-live |

---

## 6. Pricing & Payment Terms

### Engagement Pricing

| Component | Description | Type |
|-----------|-------------|------|
| Discovery Phase | Blueprint, PRD, Solution Design | Fixed Price |
| Build Phase | Development, Integration, Testing | Fixed Price |
| Launch & Support | Deployment, Stabilization | Fixed Price |

### Payment Schedule

| Milestone | Payment | Trigger |
|-----------|---------|---------|
| M1: Discovery Complete | Payment 1 | PRD Approval |
| M4: Matching Engine Complete | Payment 2 | Core functionality demo |
| M7: Go-Live | Payment 3 | Production deployment |

### Payment Terms

- Invoice issued upon milestone completion
- Payment due within agreed terms
- All pricing in agreed currency

---

## 7. Change Request Process

### Change Request Procedure

1. **Request Submission**
   - Requestor submits change request in writing
   - Includes description, rationale, priority

2. **Impact Assessment**
   - Team evaluates scope, timeline, cost impact
   - Assessment within 3 business days

3. **Approval**
   - Changes affecting scope/timeline require mutual approval
   - Minor clarifications approved by project leads

4. **Implementation**
   - Approved changes added to project plan
   - Documentation updated accordingly

### Change Categories

| Category | Impact | Approval Required |
|----------|--------|-------------------|
| Clarification | No impact | Project lead |
| Minor Enhancement | < 1 day effort | Project manager |
| Scope Change | > 1 day effort | Carrefour PO + PM |
| Major Change | New requirements | Executive sponsor |

### Expected Change Areas

| Area | Likelihood | Mitigation |
|------|------------|------------|
| Matching criteria adjustments | High | Configurable thresholds |
| Additional EAN formats | Medium | Extensible format handler |
| GS1 API changes | Low | Abstraction layer |
| Review queue enhancements | Medium | Modular design |

---

## 8. Terms & Conditions

### 8.1 Confidentiality

- All project information treated as confidential
- Seller data protected per privacy requirements
- EAN and product data handled securely

### 8.2 Intellectual Property

| Component | Ownership |
|-----------|-----------|
| Validation System Code | Carrefour |
| Matching Algorithm | Carrefour |
| Cache Data | Carrefour |
| Integration Patterns | Shared |
| Documentation | Carrefour |

### 8.3 Warranties

- Deliverables will meet documented requirements
- System will perform per PRD specifications
- Defects during warranty period will be corrected

### 8.4 Liability

- Liability limited to engagement value
- No liability for third-party API issues (GS1)
- Force majeure provisions apply

### 8.5 Termination

| Condition | Notice Period | Obligations |
|-----------|---------------|-------------|
| Mutual Agreement | Immediate | Settle completed work |
| Breach | 30 days cure period | Cure or terminate |
| Convenience | 30 days written notice | Payment for completed work |

### 8.6 Dispute Resolution

1. Project-level resolution (5 business days)
2. Management escalation (10 business days)
3. Executive escalation (15 business days)
4. Formal mediation if unresolved

---

## 9. Signatures

| Party | Name | Title | Signature | Date |
|-------|------|-------|-----------|------|
| Carrefour Brasil | | | | |
| Carrefour Brasil | | | | |
| Engagement Team | Gabriela Souza | Product Manager | | |

---

## Appendix A: Validation Requirements Summary

### EAN Format Support

| Format | Digits | Validation |
|--------|--------|------------|
| EAN-8 | 8 | Length + Check digit |
| UPC-A | 12 | Length + Check digit |
| EAN-13 | 13 | Length + Check digit |
| GTIN-14 | 14 | Length + Check digit |

### Rejection Codes

| Code | Reason | User Message |
|------|--------|--------------|
| REJ-01 | Missing EAN | "EAN code is required" |
| REJ-02 | Invalid format | "EAN format is invalid" |
| REJ-03 | Invalid check digit | "EAN check digit is incorrect" |
| REJ-04 | EAN not found | "EAN not found in registries" |
| REJ-05 | Product mismatch | "EAN does not match product" |

### Match Score Thresholds

| Score | Decision |
|-------|----------|
| ≥ 80% | Approve |
| 60-80% | Manual Review |
| < 60% | Reject |

---

## Appendix B: Integration Points

### Inbound (From Mirakl)

| Event | Trigger | Data |
|-------|---------|------|
| Product Registration | New product submitted | Product ID, EAN, attributes |
| Product Update | Product resubmitted | Product ID, EAN, attributes |

### Outbound (To Mirakl)

| Event | Trigger | Data |
|-------|---------|------|
| Approval | Validation passed | Product ID, status |
| Rejection | Validation failed | Product ID, status, reason |
| Review Queue | Partial match | Product ID, status |

### External APIs

| API | Purpose | Rate Limit |
|-----|---------|------------|
| GS1 | EAN registry lookup | TBD |
| GOLD | Internal product lookup | Internal |

---

## Appendix C: Performance Requirements

| Metric | Target | Measurement |
|--------|--------|-------------|
| Validation Response Time | < 5 seconds P95 | Latency monitoring |
| Throughput | 100 validations/minute | Load testing |
| Cache Hit Rate | > 50% | Cache metrics |
| System Availability | 99.5% | Uptime monitoring |
| Manual Review Backlog | < 24 hours | Queue age monitoring |

---

## Appendix D: Phase 2 Preview

Phase 2 will address existing catalog validation (Milestones 3-5):

| Milestone | Description | Complexity |
|-----------|-------------|------------|
| M3 | EAN testing for entire catalog | High (volume) |
| M4 | EAN/Product match for catalog | High (matching) |
| M5 | Full catalog cleanup | High (policy) |

**Prerequisites from Phase 1:**
- Validated EAN cache populated
- Matching algorithm tuned
- Review process established
- Cleanup policy defined

---

## Related Documents

- [Blueprint](../discovery-docs/ean-validator-blueprint.md) - Discovery document
- [PRD](./ean-validator-prd.md) - Product Requirements Document
- [Solution Diagrams](./ean-validator-solution-diagrams.md) - Architecture diagrams
- [Assumptions Log](./assumptions-decisions-log.md) - Decisions tracking

---

*Document Version: 1.0*
*Author: Gabriela Souza*
