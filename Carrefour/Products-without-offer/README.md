# Carrefour - Products Without Offer Blocker

## Project Overview

**Client:** Carrefour Brasil
**Project:** Products Without Offer Blocker
**Engagement Type:** Production
**Status:** Discovery

## Project Summary

A cost optimization solution that prevents products without valid offers (price and stock) from entering the catalog enrichment pipeline. By blocking incomplete product registrations early, Carrefour avoids unnecessary costs from third-party services like Omnilogic, VTEX registration, and EAN lookups for products that cannot be sold.

## Team

| Role | Name | Contact |
|------|------|---------|
| Product Manager | Gabriela Souza | |
| Tech Lead | TBD | |
| Client Contact | TBD | |

## Key Documents

| Document | Status | Location |
|----------|--------|----------|
| Blueprint | Complete | `discovery-docs/offer-blocker-blueprint.md` |
| PRD | Complete | `project-docs/offer-blocker-prd.md` |
| Solution Diagrams | Complete | `project-docs/offer-blocker-solution-diagrams.md` |
| SOW | Complete | `project-docs/offer-blocker-sow.md` |
| Assumptions Log | Active | `project-docs/assumptions-decisions-log.md` |
| Client Docs | Reference | `client -docs/` |

## Milestones

1. **Intercept Product Registration** - Capture product data before Mirakl processing
2. **Offer Validation Logic** - Validate price and stock are present and valid
3. **Block Without Offer** - Prevent incomplete products from entering pipeline

## Business Value

| Metric | Impact |
|--------|--------|
| Cost Reduction | Eliminate enrichment costs for unsellable products |
| Pipeline Efficiency | Only process products that can generate revenue |
| Seller Experience | Clear feedback on registration requirements |

## Quick Links

- [Blueprint](./discovery-docs/offer-blocker-blueprint.md)
- [PRD](./project-docs/offer-blocker-prd.md)
- [Solution Diagrams](./project-docs/offer-blocker-solution-diagrams.md)
- [Statement of Work](./project-docs/offer-blocker-sow.md)
- [Assumptions & Decisions Log](./project-docs/assumptions-decisions-log.md)
