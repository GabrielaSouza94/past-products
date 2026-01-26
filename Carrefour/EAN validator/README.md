# Carrefour - EAN Validator System

## Project Overview

**Client:** Carrefour Brasil
**Project:** EAN Validator System
**Engagement Type:** Production
**Status:** Discovery

## Project Summary

A product catalog validation system to ensure all products in the Carrefour marketplace have valid, tested, and verified EAN (European Article Number) codes that correctly correspond to the products being offered. The system prevents invalid product registrations and cleanses the existing catalog of products with missing or incorrect EANs.

## Team

| Role | Name | Contact |
|------|------|---------|
| Product Manager | Gabriela Souza | |
| Tech Lead | TBD | |
| Client Contact | TBD | |

## Key Documents

| Document | Status | Location |
|----------|--------|----------|
| Blueprint | DRAFT | `discovery-docs/ean-validator-blueprint.md` |
| PRD (Phase 1) | DRAFT | `project-docs/ean-validator-prd.md` |
| Solution Diagrams | Complete | `project-docs/ean-validator-solution-diagrams.md` |
| SOW | DRAFT | `project-docs/ean-validator-sow.md` |
| Assumptions Log | Active | `project-docs/assumptions-decisions-log.md` |
| Client Docs | Reference | `client-docs/` |

## Milestones

1. **Block Products Without EAN** - Prevent registration of products without EAN code
2. **EAN Testing (New Products)** - Validate EAN legitimacy on new product registration
3. **EAN Testing (Catalog)** - Test EAN legitimacy for entire existing catalog
4. **EAN/Product Match (New Products)** - Validate EAN corresponds to correct product
5. **EAN/Product Match (Catalog)** - Validate correspondence for entire catalog

## Quick Links

- [Blueprint](./discovery-docs/ean-validator-blueprint.md)
- [PRD - Phase 1](./project-docs/ean-validator-prd.md)
- [Solution Diagrams](./project-docs/ean-validator-solution-diagrams.md)
- [Statement of Work](./project-docs/ean-validator-sow.md)
- [Assumptions & Decisions Log](./project-docs/assumptions-decisions-log.md)
- [GS1 EAN Information](https://gs1br.org/codigos-e-padroes/padroes-de-identificacao/Paginas/GTIN.aspx)
- [EAN Check Digit Calculation](https://www.gs1.org/services/how-calculate-check-digit-manually)
