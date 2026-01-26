# Statement of Work (SOW)

## ANATEL Homologation Validation System

---

## Cover Page

| Field | Value |
|-------|-------|
| Document Title | Statement of Work |
| Project Name | ANATEL Homologation Validation System |
| Client Name | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Complete |

---

## 1. Executive Summary

This Statement of Work defines the engagement terms for developing the **ANATEL Homologation Validation System** for Carrefour Brasil's marketplace platform.

The project addresses a critical regulatory compliance requirement: ANATEL (Brazilian National Telecommunications Agency) mandates that all marketplaces must validate and display homologation licenses for telecommunications products. Non-compliance exposes Carrefour to regulatory penalties and legal liability for selling non-certified products.

The solution introduces a validation layer that intercepts product registrations, validates ANATEL licenses through a 3-layer verification process, and either approves products for publication or rejects them with clear guidance for sellers to correct and resubmit.

**Engagement Type:** Production
**Engagement Scope:** MVP 1 - Product Registration Validation

---

## 2. Scope of Work

### 2.1 In Scope

**Core Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| Omnilogic Integration (CM21) | Endpoint to receive enriched product data after categorization |
| Category Filtering System | Configurable filter to identify homologable product categories |
| Product Identification Logic | Brand/model matching to identify products requiring licenses |
| 3-Layer License Validation | Validation against ANATEL database (exists, active, matches) |
| Mirakl Rejection Flow | Status update and rejection reason communication to sellers |
| Audit Logging | Comprehensive logging of all validation decisions |

**Supporting Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| Blueprint Document | Project understanding and gap analysis |
| PRD (Product Requirements) | Functional and non-functional requirements |
| Solution Diagrams | Architecture and process flow documentation |
| SOW (This Document) | Engagement terms and scope definition |

### 2.2 Out of Scope

The following items are explicitly excluded from this engagement:

| Item | Rationale | Future Phase |
|------|-----------|--------------|
| License Expiration Monitoring | Not required for MVP | Phase 2 |
| Automatic Seller Notifications | Manual process sufficient for MVP | Phase 2 |
| Category Management UI | Manual configuration for MVP | Phase 2 |
| Periodic Pending Item Purge | Will evaluate based on volume | Phase 2 |
| Seller Reporting to ANATEL | Separate regulatory milestone | Milestone 4 |
| Existing Product Audit | Requires separate effort | Future |
| Milestones 2-5 (Other Regulatory) | Out of current scope | Future |

### 2.3 Assumptions

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A01 | ANATEL database is accessible via BigQuery | Cannot validate licenses |
| A02 | Omnilogic provides enriched data before validation | Incomplete product data |
| A03 | Mirakl rejection flow supports custom rejection reasons | Cannot communicate to sellers |
| A04 | BigQuery crawler is operational and updating every 48 hours | Stale license data |
| A05 | Carrefour provides initial list of homologable categories | Incorrect filtering |
| A06 | Sellers can view rejection reasons in Mirakl | Poor seller experience |

---

## 3. Deliverables

| # | Deliverable | Description | Format | Delivery Method |
|---|-------------|-------------|--------|-----------------|
| 1 | Blueprint | Project understanding and gap analysis | Markdown | Repository |
| 2 | PRD | Product requirements document | Markdown | Repository |
| 3 | Solution Diagrams | Architecture and process flows | Markdown + Mermaid | Repository |
| 4 | SOW | Engagement terms (this document) | Markdown | Repository |
| 5 | Validation System | Deployed validation service | Cloud Application | GCP |
| 6 | Integration APIs | CM21/CM22/CM23 endpoints | REST API | Cloud Endpoint |
| 7 | ANATEL Data Sync | Crawler service for license data | Cloud Function | GCP |
| 8 | Technical Documentation | API specs and deployment guide | Markdown | Repository |

### Acceptance Criteria Summary

Each deliverable must meet the following criteria:

**Documentation Deliverables:**
- Complete and accurate content
- No placeholders or TBD items without justification
- Reviewed and approved by Carrefour stakeholders

**Technical Deliverables:**
- All functional requirements from PRD implemented
- 3-layer validation working correctly
- Integration with Omnilogic and Mirakl operational
- Audit logging capturing all validation decisions
- Performance meets SLA requirements (< 5s response time)

---

## 4. Timeline & Milestones

### Phase Overview

| Phase | Milestone | Deliverables | Dependencies |
|-------|-----------|--------------|--------------|
| Discovery | Blueprint Complete | Blueprint, Gap Analysis | Client materials received |
| Discovery | PRD Complete | PRD, Solution Diagrams | Blueprint approval |
| Build | Integration Ready | CM21/CM22/CM23 APIs | PRD approval |
| Build | Validation Core Complete | Category filter, Validator | Integration Ready |
| Build | MVP Complete | Full system deployed | Validation Core |
| Launch | Go-Live | Production deployment | MVP Complete |
| Support | Stabilization | Bug fixes, monitoring | Go-Live |

### Milestone Definitions

**M1: Discovery Complete**
- Blueprint approved by Carrefour
- PRD approved by Carrefour
- Solution diagrams complete
- Open questions resolved

**M2: Integration Ready**
- CM21 endpoint operational
- Omnilogic integration tested
- CM22/CM23 status endpoints working

**M3: Validation Core Complete**
- Category filtering operational
- Product identification logic working
- 3-layer validation implemented
- BigQuery integration functional

**M4: MVP Complete**
- Mirakl rejection flow working
- End-to-end testing passed
- Audit logging operational
- Performance requirements met

**M5: Go-Live**
- Production deployment complete
- Monitoring and alerting configured
- Runbook documentation available

---

## 5. Team & Responsibilities

### RACI Matrix

| Activity | Product Manager | Tech Lead | Developer | Carrefour PO | Carrefour Tech |
|----------|-----------------|-----------|-----------|--------------|----------------|
| Requirements Definition | R | C | I | A | C |
| Architecture Design | C | R | C | I | C |
| Development | I | A | R | I | C |
| Integration Testing | C | R | R | C | R |
| UAT Coordination | R | I | C | A | C |
| Deployment | I | R | R | I | A |
| Production Support | C | R | R | I | A |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### Client Responsibilities

| Responsibility | Owner | Description |
|----------------|-------|-------------|
| Category List | Carrefour Product | Provide and maintain list of homologable categories |
| BigQuery Access | Carrefour Tech | Ensure crawler and database are operational |
| Omnilogic Coordination | Carrefour Tech | Coordinate integration requirements |
| Mirakl Configuration | Carrefour Tech | Configure rejection flow and status codes |
| UAT Execution | Carrefour QA | Execute user acceptance testing |
| Production Approval | Carrefour PO | Approve go-live |

---

## 6. Pricing & Payment Terms

### Engagement Pricing

| Component | Description | Type |
|-----------|-------------|------|
| Discovery Phase | Blueprint, PRD, Solution Design | Fixed Price |
| Build Phase | Development and Integration | Fixed Price |
| Launch & Support | Deployment and Stabilization | Fixed Price |

### Payment Schedule

| Milestone | Payment | Trigger |
|-----------|---------|---------|
| M1: Discovery Complete | Payment 1 | PRD Approval |
| M3: Validation Core Complete | Payment 2 | Core functionality demo |
| M5: Go-Live | Payment 3 | Production deployment |

### Payment Terms

- Invoice issued upon milestone completion
- Payment due within agreed terms
- All pricing in agreed currency

---

## 7. Change Request Process

### Change Request Procedure

1. **Request Submission**
   - Requestor submits change request in writing
   - Change request includes description, rationale, and priority

2. **Impact Assessment**
   - Team evaluates scope, timeline, and cost impact
   - Assessment provided within 3 business days

3. **Approval**
   - Changes affecting scope/timeline require mutual written approval
   - Minor clarifications can be approved by project leads

4. **Implementation**
   - Approved changes incorporated into project plan
   - Documentation updated accordingly

### Change Categories

| Category | Impact | Approval Required |
|----------|--------|-------------------|
| Clarification | No impact | Project lead |
| Minor Enhancement | < 1 day effort | Project manager |
| Scope Change | > 1 day effort | Carrefour PO + PM |
| Major Change | New requirements | Executive sponsor |

---

## 8. Terms & Conditions

### 8.1 Confidentiality

- All project information treated as confidential
- No disclosure to third parties without written consent
- ANATEL regulatory requirements are public information

### 8.2 Intellectual Property

| Component | Ownership |
|-----------|-----------|
| Validation System Code | Carrefour |
| Solution Architecture | Carrefour |
| Integration Patterns | Shared |
| Documentation | Carrefour |

### 8.3 Warranties

- Deliverables will meet documented requirements
- System will perform according to PRD specifications
- Defects identified during warranty period will be corrected

### 8.4 Liability

- Liability limited to engagement value
- No liability for regulatory penalties outside scope
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

## Appendix A: Regulatory Context

### ANATEL Compliance Requirements

| Milestone | Requirement | Regulatory Deadline |
|-----------|-------------|---------------------|
| 1 | Remove non-homologated product listings | Per ANATEL mandate |
| 2 | Mandatory homologation code in registration | Per ANATEL mandate |
| 3 | Validate codes against ANATEL database | Per ANATEL mandate |
| 4 | Report non-compliant sellers | Per ANATEL mandate |

### Referenced Regulations

- Resolution 715: Homologation regulations
- Act 7280: Telecom product certification requirements
- Federal Prosecutor's position on marketplace liability

---

## Appendix B: Technical References

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| CM21 | POST /api/mcm/products/synchronization | Receive product from Omnilogic |
| CM22 | GET /api/mcm/products/synchronization/{ID} | Check sync status |
| CM23 | GET /api/mcm/products/synchronization/{ID}/report | Get detailed report |
| CM51 | POST /api/mcm/products/export | Mirakl export trigger |

### Data Sources

| Source | Purpose | Update Frequency |
|--------|---------|------------------|
| BigQuery (br-digitalcomm-prod) | ANATEL license cache | Every 48 hours |
| ANATEL Portal | Official homologation database | Source of truth |

---

## Related Documents

- [Blueprint](../discovery-docs/anatel-blueprint.md) - Discovery document
- [PRD](./anatel-prd.md) - Product Requirements Document
- [Solution Diagrams](./anatel-solution-diagrams.md) - Architecture diagrams

---

*Document Version: 1.0*
*Author: Gabriela Souza*
