# Blueprint - ANATEL Homologation Validation System

---

## Cover Page

| Field | Description |
|-------|-------------|
| Project Name | ANATEL Homologation Validation System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Document Status | Complete |

---

## Project Overview

| Attribute | Value |
|-----------|-------|
| Project Name | ANATEL Homologation Validation System |
| Client | Carrefour Brasil |
| Engagement Type | Production |
| Client Readiness Level | Level 2 (Requirements defined with acceptance criteria) |
| Primary Contact | TBD |
| Source Materials | Context document, Proposed Solution, ANATEL regulations |

**Source Materials Received:**

| Material | Type | Notes |
|----------|------|-------|
| Context Document | Text | Problem context and regulatory requirements (Portuguese) |
| Proposed Solution | Text | Technical solution proposal and MVP definition |
| ANATEL Regulations | External Links | Official certification requirements |
| ANATEL Homologation Database | External API | Product certification lookup |

---

## Problem Statement (As Understood)

### What the client says:

> "A agência nacional de telecomunicações ANATEL irá colocar em vigor o bloqueio de anúncios de produtos de telecomunicações homologados sem licença associada, de forma a derrubar a venda de produtos piratas comercializados no marketplace."

> "O Órgão compartilha o recente posicionamento da Procuradoria Federal Especializada que versa sobre a responsabilidade das plataformas de Marketplace na comercialização de produtos irregulares, não homologados ou em condições diversas."

### Our understanding:

ANATEL (Brazilian National Telecommunications Agency) is enforcing new regulations requiring marketplaces to:

1. **Block Unlicensed Products:** Prevent listing of telecommunications products without valid homologation licenses
2. **Validate Licenses:** Verify that license codes correspond to correct products in ANATEL's database
3. **Display Compliance:** Show homologation codes in product listings
4. **Report Violations:** Provide lists of sellers who attempt to circumvent the rules

**Regulatory Context:**
- Marketplaces are now legally responsible for unauthorized product sales
- Non-compliance exposes Carrefour to regulatory penalties
- This is a mandatory compliance requirement, not optional

### Primary Objective:

> "Garantir que no e-commerce e no marketplace todos os produtos cadastrados e os anúncios exibidos tenham as licenças corretas caso o produto esteja homologado pela Anatel."

**Translation:** Ensure that all registered products and displayed listings in the e-commerce and marketplace have correct licenses if the product is homologated by ANATEL.

---

## Client's Stated Vision

### Compliance Requirements

| Milestone | Description | Regulatory Requirement |
|-----------|-------------|------------------------|
| 1 | Remove all non-homologated telecom product listings | Mandatory |
| 2 | Implement mandatory homologation code field in registration | Mandatory |
| 3 | Validate homologation codes against ANATEL database | Mandatory |
| 4 | Report non-compliant sellers to ANATEL | Mandatory |

### Solution Components

**Component 1: License Validation in Product Registration**
- Build validation mechanism during product catalog registration
- Identify if product requires ANATEL license
- Validate license if required
- Block registration if license is invalid/missing

**Component 2: Existing Product Audit**
- Update e-commerce to display all product licenses
- Identify products without registered licenses and deactivate listings
- Validate existing licenses against ANATEL database
- Deactivate listings for products with expired/invalid licenses

### Acceptance Criteria (From Client)

1. Tool must identify ANATEL-homologable products (distinguish if product needs license)
2. Only products in specific configurable categories go through validation
3. Tool must offer multiple validation layers:
   - **Validation 1:** Verify license exists in internal ANATEL database
   - **Validation 2:** Verify license is active (status = "vigente")
   - **Validation 3:** Verify license belongs to correct product
4. Use ANATEL's official homologation database (products + 5G phones)
5. Use brand/manufacturer and model data for product identification

### Technical Approach

**Integration Points:**
- Omnilogic (categorization and enrichment service)
- Mirakl (marketplace platform)
- ANATEL homologation database (via BigQuery crawler)

**Product Flow:**
```
[Seller Submits Product] → [Omnilogic Categorization] → [ANATEL Validation] → [Mirakl Status Update]
                                                              ↓
                                                    [Valid License] → [Published]
                                                              ↓
                                                    [Invalid/Missing] → [Pending/Rejected]
```

**APIs Involved:**
- CM21: POST products/synchronization
- CM22: GET products/synchronization/{ID}
- CM23: GET products/synchronization/{ID}/report
- CM51: POST products/export

---

## Source Material Summary

| Material | Type | Summary | Key Information |
|----------|------|---------|-----------------|
| Context Document | Discovery Input | Regulatory compliance requirements | ANATEL mandates, milestones, timeline |
| Proposed Solution | Technical Spec | MVP definition and acceptance criteria | Validation layers, integration points |
| ANATEL Legislation | External | Resolution 715, Act 7280 | Legal requirements for homologation |
| ANATEL Database | External | Homologated products lookup | Product verification source |

### Information Quality Assessment

| Area | Quality | Notes |
|------|---------|-------|
| Problem Statement | Excellent | Regulatory requirement clearly defined |
| Compliance Requirements | Excellent | Specific milestones with clear outcomes |
| Technical Solution | Good | MVP well defined, integration points identified |
| Acceptance Criteria | Good | Validation layers specified |
| User Stories | Moderate | High-level stories provided |
| Architecture | Moderate | Integration flow outlined, needs detail |

---

## Assumptions

| ID | Assumption | Source | Risk if Wrong |
|----|------------|--------|---------------|
| A01 | ANATEL database is accessible and reliable | Solution doc | Cannot validate licenses |
| A02 | Omnilogic provides category and enrichment data before validation | Solution doc | Validation cannot run |
| A03 | Mirakl rejection flow works as expected | Solution doc | Products cannot be blocked |
| A04 | BigQuery crawler updates ANATEL data regularly | Solution doc | Stale validation data |
| A05 | Category list of homologable products is maintained | Solution doc | Incorrect filtering |
| A06 | Sellers can resubmit products after fixing license | Solution doc | Poor seller experience |
| A07 | Brand/model matching is sufficient for product identification | Solution doc | False positives/negatives |
| A08 | Project language is Portuguese (Brazilian) | Source material | Documentation/communication |

---

## Open Questions

### Tier 1: Critical (Resolved in Documentation)

| ID | Category | Question | Status |
|----|----------|----------|--------|
| Q1 | Technical | How does Omni recognize new product submissions? | Resolved: Async via trackingId |
| Q2 | Data | Who creates/maintains ANATEL database? | Resolved: Tiago (Portal Seller), crawler updates every 2 days |
| Q3 | Process | Deadline for sellers to fix products? | Deferred: Not defined for MVP, will monitor volume first |

### Tier 2: Important (For Implementation)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q4 | Operations | How to update/edit homologable category list? | Category management |
| Q5 | Technical | How to check expiration of existing product licenses? | Ongoing compliance |
| Q6 | Metrics | How to measure validation tool effectiveness? | Success measurement |

### Tier 3: Nice to Have

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q7 | Process | Periodic purge of pending items? | Catalog cleanliness |

---

## Gap Analysis

```
Area                        Known    Gaps     Status
------------------------------------------------------------
Regulatory Requirements    100%       0%      Complete
Validation Logic            90%      10%      Minor edge cases
Integration Architecture    80%      20%      API details needed
Seller Experience           70%      30%      Resubmission flow
Monitoring/Reporting        50%      50%      Metrics undefined
Category Management         60%      40%      Update process unclear
```

### Visual Summary

| Area | Status |
|------|--------|
| Compliance Requirements | Fully defined |
| Validation Rules | Well specified |
| Integration Points | Identified, need detail |
| Seller Flow | Outlined, needs UX detail |
| Reporting | Pending definition |

---

## Use Cases (From Client)

| Use Case | Description | Expected Outcome |
|----------|-------------|------------------|
| UC-01 | Product rejected by Omnilogic / no category identified | Product not validated |
| UC-02 | Product not in homologable category | Pass through, no validation |
| UC-03 | Product is not homologable | Pass through, no validation |
| UC-04 | Homologable product with valid license | Product published |
| UC-05 | Homologable product with invalid license | Product rejected/pending |
| UC-06 | Homologable product rejected by Omni with invalid license | Product rejected |

---

## External References

| Reference | URL | Purpose |
|-----------|-----|---------|
| ANATEL Product List | https://informacoes.anatel.gov.br/legislacao/atos-de-certificacao-de-produtos/2020/1493-ato-7280 | Telecom product reference |
| Resolution 715 | https://informacoes.anatel.gov.br/legislacao/resolucoes/2019/1350-resolucao-715 | Homologation regulations |
| MOSAICO System | https://antigo.mctic.gov.br/mctic/opencms/comunicacao/SERAD/radiofusao/Sistemas/radiodifusao_sistemaMosaico.html | Spectrum management |
| Homologation Lookup | https://sistemas.anatel.gov.br/mosaico/sch/publicView/listarProdutosHomologados.xhtml | Product verification |
| Product Query | https://informacoes.anatel.gov.br/paineis/certificacao-de-produtos/consulta-de-produtos | Data downloads |
| BigQuery Database | https://console.cloud.google.com/bigquery?project=br-digitalcomm-prod | Internal ANATEL data |

---

## Next Steps

### Immediate Actions

1. Finalize category list for homologable products
2. Confirm Omnilogic integration specifications
3. Define Mirakl rejection payload structure
4. Create test scenarios for validation layers

### After Blueprint Approval

1. Proceed to PRD development
2. Define technical architecture (TRD)
3. Create development backlog
4. Plan QA test cases

---

## Related Documents

- [PRD](../project-docs/anatel-prd.md) - Product Requirements Document
- [Context](../client-docs/Context) - Original problem context
- [Proposed Solution](../client-docs/proposed%20solution) - Technical solution proposal

---

*Document Version: 1.0*
*Author: Gabriela Souza*
