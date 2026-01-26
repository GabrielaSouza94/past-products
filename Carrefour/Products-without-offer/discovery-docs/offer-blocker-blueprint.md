# Blueprint - Products Without Offer Blocker

---

## Cover Page

| Field | Description |
|-------|-------------|
| Project Name | Products Without Offer Blocker |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Document Status | Complete |

---

## Project Overview

| Attribute | Value |
|-----------|-------|
| Project Name | Products Without Offer Blocker |
| Client | Carrefour Brasil |
| Engagement Type | Production |
| Client Readiness Level | Level 2 (Requirements defined with use cases) |
| Primary Contact | TBD |
| Source Materials | Context document with problem description and use cases |

**Source Materials Received:**

| Material | Type | Notes |
|----------|------|-------|
| Context Document | Text | Problem context, objective, milestones, use cases (Portuguese) |

---

## Problem Statement (As Understood)

### What the client says:

> "Durante o cadastro de produtos a esteira do processo passa por etapas que exigem a utilização de serviços terceiros, e que acarretam gastos para o Carrefour para construção do nosso catálogo. Ou seja, todos os produtos cadastrados geram um custo."

> "Para realizar o cadastro de produtos em catálogo é permitido que os sellers enviem as informações do produto a ser cadastrado contendo ou não os detalhes da oferta de produto (preço e estoque disponível para venda)."

> "Um produto pode ser cadastrado mesmo sem ter oferta disponível e consequentemente o produto não aparece no e-commerce, pois apenas produtos com oferta cadastrada são publicados. E portanto por não estarem sendo comercializados, não trazem nenhum lucro."

### Our understanding:

Carrefour's product registration pipeline incurs costs at multiple stages regardless of whether the product can actually be sold:

**Current Flow:**
```
[Seller Submits] → [Mirakl] → [Omnilogic] → [EAN Lookup] → [VTEX] → [Published?]
                                  💰            💰           💰
                              (Cost)       (Cost)       (Cost)
```

**Problem:**
1. **Unnecessary Costs:** Products without offers (price/stock) go through the entire enrichment pipeline
2. **No Revenue:** Products without offers are never published and generate zero revenue
3. **Wasted Resources:** Third-party services (Omnilogic, EAN lookups, VTEX) are consumed for unsellable products
4. **No Early Gate:** Current system allows incomplete registrations to proceed

**Cost Centers Affected:**
- Omnilogic categorization and enrichment
- VTEX catalog registration
- EAN validation via external bases (GS1, etc.)
- Storage and processing resources

### Gaps:

- [ ] Volume of products currently registered without offers (Q1)
- [ ] Current cost per product registration through pipeline (Q2)
- [ ] Estimated monthly savings from blocking incomplete registrations (Q3)

---

## Client's Stated Vision

### Primary Objective

> "Modificar o fluxo de cadastro de produtos, bloqueando o cadastro de produtos enviados sem oferta (preço e estoque) para que não gerem custos de enriquecimento com a Omnilogic, cadastro na VTEX, pesquisas de EAN em bases externas, etc."

**Translation:** Modify the product registration flow to block products sent without offers (price and stock) so they don't generate enrichment costs with Omnilogic, VTEX registration, EAN lookups in external bases, etc.

### Expected Milestones

| # | Milestone | Description |
|---|-----------|-------------|
| 1 | Intercept Registration | Intercept new product information before Mirakl |
| 2 | Offer Validation | Create mechanism to validate offer presence |
| 3 | Block & Communicate | Block products without offers with clear seller notification |

### Offer Requirements

For a product to be considered "with offer":

| Field | Requirement |
|-------|-------------|
| Price | Must be present, non-null, non-zero, valid numeric |
| Stock | Must be present, non-null, non-zero, valid numeric |

---

## Use Cases (From Client)

### Complete Set of Use Cases

| UC | Scenario | Has Price | Has Stock | Result |
|----|----------|-----------|-----------|--------|
| UC-01 | Complete offer | Yes (valid) | Yes (valid) | ✅ Registration proceeds |
| UC-02 | Price only, no stock | Yes | No/Zero/Null | ❌ Blocked |
| UC-03 | Stock only, no price | No/Zero/Null | Yes | ❌ Blocked |
| UC-04 | No offer data | No/Zero/Null | No/Zero/Null | ❌ Blocked |
| UC-05 | Invalid characters | Invalid | Invalid | ❌ Blocked |
| UC-06 | Stock update (existing) | N/A | Yes | ✅ Update proceeds |

### Use Case Details

**UC-01: Product with Valid Offer**
- Seller submits product with price > 0 and stock > 0
- Product proceeds through normal pipeline
- Expected behavior: Registration completed

**UC-02: Product with Price but No Stock**
- Seller submits product with valid price but stock is null/zero
- Product cannot be sold (no inventory)
- Expected behavior: Registration blocked

**UC-03: Product with Stock but No Price**
- Seller submits product with valid stock but price is null/zero
- Product cannot be sold (no price)
- Expected behavior: Registration blocked

**UC-04: Product with No Offer Data**
- Seller submits product without price and stock
- Product cannot be sold
- Expected behavior: Registration blocked

**UC-05: Product with Invalid Characters**
- Seller submits product with non-numeric values in price/stock
- Cannot process invalid data
- Expected behavior: Registration blocked

**UC-06: Stock Update for Existing Product**
- Seller updates stock for already-registered product
- This is an update, not new registration
- Expected behavior: Update proceeds normally

---

## Technical Approach (As Understood)

### Proposed Solution

**Intercept Before Pipeline:**
```
[Seller Submits] → [Offer Validator] → [Has Valid Offer?]
                         ↓                    ↓
                    [Blocked]            [Mirakl] → [Pipeline continues...]
```

### Integration Point

The validator must intercept product registration BEFORE:
- Mirakl catalog ingestion
- Omnilogic enrichment
- EAN validation
- VTEX registration

### Validation Logic

```
IF price IS NULL OR price <= 0 OR price IS NOT NUMERIC:
    BLOCK with reason "Price required"
ELSE IF stock IS NULL OR stock <= 0 OR stock IS NOT NUMERIC:
    BLOCK with reason "Stock required"  
ELSE:
    PROCEED to Mirakl
```

---

## Referenced Systems

| System | Role | Impact |
|--------|------|--------|
| **Mirakl** | Marketplace platform | Integration point for blocking |
| **Omnilogic** | Categorization service | Cost to avoid |
| **VTEX** | E-commerce platform | Cost to avoid |
| **EAN Services** | External validation | Cost to avoid |

---

## Source Material Summary

| Material | Type | Summary | Key Information |
|----------|------|---------|-----------------|
| Context Document | Discovery Input | Problem context and use cases | 3 milestones, 6 use cases |

### Information Quality Assessment

| Area | Quality | Notes |
|------|---------|-------|
| Problem Statement | Excellent | Clear cost optimization objective |
| Use Cases | Excellent | 6 comprehensive use cases |
| Milestones | Good | 3 clear milestones |
| Technical Approach | Moderate | Concept clear, integration point TBD |
| Business Value | Good | Cost savings clearly articulated |
| Metrics | Low | No baseline costs provided |

---

## Assumptions

| ID | Assumption | Source | Risk if Wrong |
|----|------------|--------|---------------|
| A01 | Seller API calls can be intercepted before Mirakl | Implied | Need different integration point |
| A02 | Mirakl supports pre-registration hooks/webhooks | Implied | Cannot block before Mirakl |
| A03 | Offer data (price/stock) is sent with product registration | Context | Different payload structure |
| A04 | Sellers can resubmit after adding offer data | Implied | Poor seller experience |
| A05 | Stock updates for existing products should proceed | UC-06 | May block valid updates |
| A06 | Zero price/stock means no offer (not free items) | Implied | May block valid scenarios |

---

## Open Questions

### Tier 1: Critical (Blocks PRD)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q1 | Data | What volume of products are registered without offers? | Business case |
| Q2 | Business | What is the cost per product through the enrichment pipeline? | ROI calculation |
| Q3 | Technical | Where exactly can we intercept before Mirakl? | Architecture |
| Q4 | Business | Are there valid scenarios for zero-price products (promotions)? | Validation logic |
| Q5 | Technical | How does seller API/portal submission work? | Integration point |

### Tier 2: Important (Needed for TRD)

| ID | Category | Question | Impact |
|----|----------|----------|--------|
| Q6 | UX | What error message should sellers receive? | Communication |
| Q7 | Technical | Can we distinguish new registration vs. update? | UC-06 handling |
| Q8 | Operations | Should blocked products be logged for analysis? | Reporting |

---

## Gap Analysis

```
Area                        Known    Gaps     Status
------------------------------------------------------------
Problem Statement          100%       0%      Complete
Use Cases                  100%       0%      Complete  
Validation Logic            90%      10%      Minor: Edge cases
Integration Point           40%      60%      Critical: Where to intercept
Cost Metrics                20%      80%      Warning: Need baseline
Timeline/Budget              0%     100%      Critical: Not provided
```

### Visual Summary

| Area | Status |
|------|--------|
| Problem Understanding | Complete |
| Use Cases | Complete |
| Validation Rules | Well defined |
| Integration Architecture | Needs clarification |
| Business Metrics | Need baseline data |

---

## Next Steps

### Immediate Actions

1. **Confirm Integration Point**
   - Where can we intercept seller submissions?
   - Before Mirakl or within Mirakl?

2. **Gather Baseline Metrics**
   - Products registered without offers (volume)
   - Cost per product registration

3. **Proceed to PRD**
   - Use cases are clear
   - Validation logic is defined

### After Blueprint Approval

1. Create PRD with requirements
2. Define technical architecture (TRD)
3. Calculate ROI with cost data

---

## Related Documents

- PRD (Pending) - To be created
- TRD (Pending) - After PRD approval

---

*Document Version: 1.0*
*Author: Gabriela Souza*
