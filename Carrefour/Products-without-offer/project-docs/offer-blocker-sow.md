# Statement of Work (SOW)

## Products Without Offer Blocker

---

## Cover Page

| Field | Value |
|-------|-------|
| Document Title | Statement of Work |
| Project Name | Products Without Offer Blocker |
| Client Name | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Status | Draft |

---

## 1. Executive Summary

This Statement of Work defines the engagement terms for developing the **Products Without Offer Blocker** for Carrefour Brasil's marketplace platform.

The project addresses a cost optimization challenge: products registered without valid offers (price and stock) currently proceed through the entire enrichment pipeline, incurring costs from Omnilogic, EAN validation, and VTEX registration, despite never being published or generating revenue.

The solution introduces a validation gate that blocks product registrations without valid offers BEFORE they enter the costly pipeline, eliminating unnecessary enrichment expenses while providing clear feedback to sellers.

**Engagement Type:** Production
**Engagement Scope:** Offer Validation and Blocking

**Key Business Outcomes:**
- Eliminate enrichment costs for unsellable products
- Block 100% of products without valid offers
- Clear seller communication for corrections
- Measurable cost savings

---

## 2. Scope of Work

### 2.1 In Scope

**Core Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| Offer Validator Service | Validate price and stock presence |
| Registration Gate | Block products before pipeline |
| Seller Notification | Clear rejection messages |
| Update Passthrough | Allow updates for existing products |
| Validation Logging | Track blocked attempts |

**Supporting Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| Blueprint | Project understanding |
| PRD | Product requirements |
| Solution Diagrams | Architecture documentation |
| Assumptions Log | Decision tracking |
| SOW | This document |

### 2.2 Out of Scope

| Item | Rationale |
|------|-----------|
| Price reasonableness checks | Only presence validation |
| Stock level recommendations | Only presence validation |
| Historical catalog cleanup | New registrations only |
| Seller education portal | Communication only |

### 2.3 Assumptions

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A01 | Can intercept before Mirakl | Different integration |
| A02 | Offer data sent with product | Separate flow handling |
| A03 | Zero means "no offer" | May block valid cases |
| A04 | Sellers can resubmit | Workflow impact |

---

## 3. Deliverables

| # | Deliverable | Description | Format | Delivery |
|---|-------------|-------------|--------|----------|
| 1 | Blueprint | Discovery document | Markdown | Repository |
| 2 | PRD | Requirements | Markdown | Repository |
| 3 | Solution Diagrams | Architecture | Markdown + Mermaid | Repository |
| 4 | Assumptions Log | Decisions | Markdown | Repository |
| 5 | SOW | This document | Markdown | Repository |
| 6 | Validator Service | Cloud application | Cloud Run | GCP |
| 7 | Integration | API endpoint | REST | Cloud |
| 8 | Logging | Validation logs | Firestore | GCP |
| 9 | Documentation | Technical docs | Markdown | Repository |

### Acceptance Criteria

**Documentation:**
- Complete content
- Reviewed by stakeholders

**Technical:**
- Price validation working
- Stock validation working
- Blocking before pipeline
- Seller notification working
- Logging operational
- < 100ms response time

---

## 4. Timeline & Milestones

| Phase | Milestone | Deliverables | Dependencies |
|-------|-----------|--------------|--------------|
| Discovery | Blueprint Complete | Blueprint, PRD | Client materials |
| Discovery | Design Complete | Diagrams, SOW | Blueprint approval |
| Build | Integration Ready | API endpoint | Design approval |
| Build | Validation Complete | Validator logic | Integration ready |
| Build | MVP Complete | Full system | Validation complete |
| Launch | Go-Live | Production | MVP complete |
| Support | Stabilization | Tuning | Go-live |

### Milestone Definitions

**M1: Discovery Complete**
- Blueprint approved
- PRD approved
- Integration point confirmed

**M2: Integration Ready**
- API endpoint deployed
- Seller API routing confirmed
- Logging infrastructure ready

**M3: MVP Complete**
- All validation rules working
- Seller notifications working
- Logging operational
- Performance verified

**M4: Go-Live**
- Production deployment
- Monitoring active
- Support ready

---

## 5. Team & Responsibilities

### RACI Matrix

| Activity | PM | Tech Lead | Dev | Carrefour PO | Carrefour Tech |
|----------|-------|-----------|-----|--------------|----------------|
| Requirements | R | C | I | A | C |
| Architecture | C | R | C | I | A |
| Development | I | A | R | I | C |
| Testing | C | R | R | C | R |
| Deployment | I | R | R | I | A |
| Support | C | R | R | I | A |

### Client Responsibilities

| Responsibility | Owner |
|----------------|-------|
| Integration point access | Carrefour Tech |
| Seller API routing | Carrefour Tech |
| Error message approval | Carrefour Product |
| UAT execution | Carrefour QA |
| Go-live approval | Carrefour PO |

---

## 6. Pricing & Payment Terms

### Engagement Pricing

| Component | Description | Type |
|-----------|-------------|------|
| Discovery | Blueprint, PRD, Design | Fixed Price |
| Build | Development, Integration | Fixed Price |
| Launch | Deployment, Stabilization | Fixed Price |

### Payment Schedule

| Milestone | Trigger |
|-----------|---------|
| M1: Discovery Complete | PRD Approval |
| M3: MVP Complete | Functionality Demo |
| M4: Go-Live | Production Deployment |

---

## 7. Change Request Process

### Categories

| Category | Impact | Approval |
|----------|--------|----------|
| Clarification | None | Project lead |
| Minor | < 1 day | PM |
| Scope Change | > 1 day | PO + PM |
| Major | New requirements | Executive |

---

## 8. Terms & Conditions

### Intellectual Property

| Component | Ownership |
|-----------|-----------|
| Validator Code | Carrefour |
| Documentation | Carrefour |

### Warranties

- Deliverables meet requirements
- Defects corrected during warranty

### Termination

| Condition | Notice |
|-----------|--------|
| Mutual | Immediate |
| Breach | 30 days |
| Convenience | 30 days |

---

## 9. Signatures

| Party | Name | Title | Signature | Date |
|-------|------|-------|-----------|------|
| Carrefour Brasil | | | | |
| Engagement Team | Gabriela Souza | Product Manager | | |

---

## Appendix A: Validation Rules

| Field | Rule | Rejection Code |
|-------|------|----------------|
| Price | Must be present | REJ-01 |
| Price | Must be > 0 | REJ-02 |
| Price | Must be numeric | REJ-03 |
| Stock | Must be present | REJ-04 |
| Stock | Must be > 0 | REJ-05 |
| Stock | Must be numeric | REJ-06 |

---

## Appendix B: Performance Requirements

| Metric | Target |
|--------|--------|
| Response Time | < 100ms |
| Availability | 99.9% |
| Throughput | Per current volume |

---

## Related Documents

- [Blueprint](../discovery-docs/offer-blocker-blueprint.md)
- [PRD](./offer-blocker-prd.md)
- [Solution Diagrams](./offer-blocker-solution-diagrams.md)
- [Assumptions Log](./assumptions-decisions-log.md)

---

*Document Version: 1.0*
*Author: Gabriela Souza*
