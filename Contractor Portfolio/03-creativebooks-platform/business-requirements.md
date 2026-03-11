# CreativeBooks Platform - Business Requirements Document

## 1. Cover Page

**Project Name:** CreativeBooks - Personalized Children's ABC Books Platform  
**Client:** CreativeBooks (creativebooks.app)  
**Document Author:** The Contractor  
**Date:** November 10, 2025  
**Version:** 2.3  
**Status:** FINAL - SOW Attachment

---

## 2. Introduction

### Document Purpose

This BRD defines the business needs, functional requirements, and scope for the CreativeBooks MVP web application. It serves as the foundation for technical design and development planning.

### Project Scope

**In Scope for MVP Phase 1:**

- Self-service web platform for parents to create personalized ABC coloring books
- User authentication and account management
- Photo upload and AI-powered line art conversion
- Theme selection and book customization
- Automated page generation with quality validation
- Individual page review and regeneration capability
- Payment processing integration
- Digital PDF book delivery
- Admin panel for theme and asset management
- Privacy compliance features (consent tracking, data deletion)

**Out of Scope for MVP Phase 1:**

- Child profile management (future enhancement)
- Professional print fulfillment (Lulu.com integration - future feature)
- Social sharing features
- Affiliate program integration
- Advanced security hardening (planned for public launch)
- Multi-language support (schema prepared, implementation post-MVP)
- Advanced analytics dashboard
- Multiple line art versions per child
- Incremental billing for additional regenerations beyond 25 total regeneration allowance

### Audience

- Client stakeholders (the client - Business Owner)
- The Contractor project management and development team
- Quality assurance and testing teams
- Future technical and business stakeholders

---

## 3. Business Context

### Background

The client has a working proof-of-concept that creates personalized 87-page ABC activity books where children become the main characters. The current implementation uses Python scripts, CSV files, and manual processes to generate books with AI-generated illustrations integrating children's photos into educational content.

Key accomplishments to date:

- Live marketing website (creativebooks.app) collecting waitlist signups
- Complete insects theme with 78 alphabet pages plus educational content
- Working AI image generation pipeline using Replicate nano-banana model
- SVG-based PDF generation system with custom typography
- First complete book produced manually for validation

**Note:** The MVP implements an updated 61-page book structure (2 pages per letter) based on client feedback (November 6, 2025), consolidating pages for improved production efficiency while maintaining educational value.

### Problem to Solve

**Primary Business Challenges:**

1. **Manual Process Limitations**: Requires manual script execution and technical knowledge, preventing scalability and self-service

2. **No User Interface**: Parents cannot independently create books; the client must manually process each order

3. **Quality Control Bottleneck**: Manual face validation creates delays and limits capacity

4. **Limited Market Testing**: No mechanism to validate product-market fit with real paying customers

5. **Revenue Generation Gap**: Cannot monetize the concept without payment processing and delivery automation

### Business Objectives

**Phase 1 MVP Objectives:**

1. **Enable Self-Service Book Creation**: Parents independently create books from photo upload through payment and download

2. **Validate Product-Market Fit**: Launch to initial customers to test demand and gather feedback

3. **Establish Revenue Stream**: Process payments and deliver digital products automatically

4. **Prove Scalability**: Demonstrate handling of multiple concurrent book generations

5. **Build Foundation for Growth**: Architecture supports future themes, features, and scale

### MVP Pricing Strategy

Preview-before-payment approach balancing cost management with user experience:

**Pricing:** $5.99 per book (fixed for MVP Phase 1)

**Cost Structure per completed book:**

- Line art generation: $0.16 (4 AI generation attempts) - **per child profile, one-time cost**
- Preview generation: $0.12 (3 AI personalized pages: cover + Letter A + Letter B)
- Full book generation: $0.94 (24 AI personalized pages: Letters C-Z)
- Regeneration allowance (up to 25 total regenerations included): $0.98
- Base cost per book (first book for a child): ~$1.22 (line art + preview + full book)
- Base cost per book (additional books, same child): ~$1.06 (line art reused)
- Maximum cost (with 25 regenerations): ~$2.20 per book
- Target profit margin: ~$4.77 (first book, no regenerations) to ~$3.79 (max regenerations)

**Note:** Costs rounded for business clarity. Line art is a one-time cost per child profile, reused across all books for that child. See TRD for precise technical calculations.

**Preview Strategy:** Account required first, then limited preview (cover + letters A & B, 5 pages) before payment. Minimizes abandoned preview costs (~$0.28 for first child profile, ~$0.12 for additional children) while enabling informed purchase decisions, versus $1+ for full books without payment commitment.

**Success Metrics:**

- Users create and purchase books without assistance
- Acceptable generation quality (minimal regeneration needed)
- Reliable payment processing (< 1% failure rate)
- Positive customer feedback on book quality and UX
- 100+ concurrent users with < 2 second page load times
- Photo deletion compliance: > 99.5% success rate within 60 seconds
- Average book completion: < 10 minutes from registration to download

---

## 4. Business Requirements

### BR-01: User Registration and Authentication

**Priority:** Critical  
**Description:** Parents create accounts and authenticate securely BEFORE accessing any book generation features. Required before preview generation to prevent bot abuse and manage costs.  
**Business Value:** Enables user identification, prevents anonymous cost generation, enables order tracking and library access.  
**Acceptance Criteria:**

- Users register with email and password
- Secure login with session management
- Password reset capability
- **Account creation required before any preview or book generation**
- Unauthenticated users blocked from generation features

### BR-02: Photo Upload and Line Art Conversion

**Priority:** High  
**Description:** Parents upload a child's photo and receive AI-generated line art options for selection.  
**Business Value:** Creates the core personalized element differentiating the product.  
**Acceptance Criteria:**

- Upload child photo (standard image formats)
- **Upload UI includes crop/resize tool with square aspect ratio guides** (square reduces AI errors by 50% per client alpha testing)
- **Cropping guidance prevents full-body submissions** that negatively impact line art quality
- System generates 4 line art variations with **differentiated prompt styles** (e.g., anime, Disney, Saturday morning cartoon) to create distinct visual options
- **Prompt variations tracked** to identify which styles produce most desirable outcomes
- Users select preferred line art from 4 style options
- **Original photo retained through book generation, deleted after completion and payment** (child safety, per BR-RULE-04)
- Selected line art stored for book generation

### BR-03: Theme Selection

**Priority:** High  
**Description:** Parents select from available book themes (insects, future themes).  
**Business Value:** Provides product variety and personalization options.  
**Acceptance Criteria:**

- Users browse available themes
- One theme selected per book
- Theme selection displays preview information
- System validates theme availability

### BR-04: Preview Book Generation (Pre-Payment)

**Priority:** Critical  
**Description:** Generate limited preview before payment for informed purchase decisions while managing generation costs.  
**Business Value:** Users see personalized results before payment (~$0.28 abandoned cost for first child vs $1+ for full book).  
**Acceptance Criteria:**

- Preview generated after account creation, photo selection, and theme selection
- Preview includes exactly 5 pages:
  - 1 cover page (personalized with child)
  - 2 Letter A pages (letter+subject combined, personalized scene)
  - 2 Letter B pages (letter+subject combined, personalized scene)
- **Personalized page AI model input order** (client-validated through extensive alpha testing):
  1. **Background theme image** (scene context) - square format
  2. **Child photo** (facial reference) - cropped to square
  3. **Child line art** (outline overlay) - square format
  - **On retry** (if face validation fails): Photo → Line Art → Background (different order minimizes blank faces)
  - All inputs square (~1024x1024) for 50% error reduction
  - AI outputs square composite images, placed into standard portrait PDF page templates
- Pages display progressively as generation completes
- Automated face detection validates personalized pages
- Failed pages automatically regenerate (up to maximum retries)
- Each preview page maintained as independent entity for regeneration
- Preview must complete before payment option is presented

### BR-05: Full Book Page Generation (Post-Payment)

**Priority:** High  
**Description:** Automatically generate remaining 56 pages after payment to complete the 61-page book.  
**Business Value:** Completes delivery after payment, eliminating manual production.  
**Acceptance Criteria:**

- Remaining pages generated automatically after payment:
  - 1 "This book belongs to" page (static template with blank space)
  - 48 alphabet pages (2 pages × 24 letters: C through Z)
  - 5-6 handwriting practice pages (static)
  - 1 back cover
- **Same AI model input order as BR-04** (Background → Photo → Line Art; reversed on retry)
- Pages display progressively as generation completes
- Automated face detection validates personalized pages
- Failed pages automatically regenerate
- Each page maintained as independent entity
- Total book: 61 pages (5 preview + 56 post-payment)

### BR-06: Page Review and Regeneration

**Priority:** High  
**Description:** Parents review generated pages and can regenerate any they don't like (with limits).  
**Business Value:** Ensures satisfaction while managing costs, reduces refund requests.  
**Acceptance Criteria:**

- Users view all pages in organized interface in correct book order
- Users can regenerate individual AI-generated personalized pages
- **Maximum 25 total USER regenerations per book** (global limit across preview AND post-payment)
- **Free "System Retry"**: If page fails after automatic retries (2 attempts), user gets FREE retry that doesn't count toward quota
- System failures logged for admin monitoring
- User-requested regeneration available for ANY AI-generated page at any time
- Regeneration doesn't affect other pages
- System tracks both user regenerations (25 limit) and system failures (free, max 10 per book)

### BR-07: Payment Processing

**Priority:** High  
**Description:** Securely process payments after preview review and before full book generation.  
**Business Value:** Enables revenue, validates purchase commitment before full generation costs.  
**Acceptance Criteria:**

- Payment required after preview review, before full book generation
- Stripe integration for secure processing
- **Fixed price: $5.99 per book** (MVP Phase 1)
- Payment confirmation triggers full book generation (remaining 56 pages)
- Failed payments handled gracefully with clear messaging
- No full book generation without successful payment

### BR-08: Digital Book Delivery

**Priority:** High  
**Description:** Downloadable PDF after payment and full generation completion.  
**Business Value:** Delivers product value, completes transaction, creates engagement loop requiring platform return.  
**Acceptance Criteria:**

- System assembles complete 61-page PDF on-demand after all pages generated
- Download through platform interface (no email delivery)
- Unlimited download access after purchase
- PDF includes all preview and generated pages
- Books stored in user's library for future download
- Download requires login

### BR-09: Book Library Management

**Priority:** Medium  
**Description:** Access previously purchased books for re-download.  
**Business Value:** Provides ongoing value and reduces support burden.  
**Acceptance Criteria:**

- Users view list of purchased books
- Download any previously purchased book
- Books remain accessible indefinitely
- Unlimited downloads per book

### BR-10: Multiple Book Creation

**Priority:** High  
**Description:** Create and purchase unlimited books for same child (different themes) or different children (siblings).  
**Business Value:** Increases customer lifetime value and revenue per user.  
**Acceptance Criteria:**

- New book creation available at any time
- User selects which child profile to use (existing or new)
- Each book requires separate payment
- Same child can have different themes (line art reused)
- Different children each have own line art
- No limits on books per account or children per account

### BR-11: Admin Theme Management

**Priority:** High  
**Description:** The client manages all theme content and assets through admin interface.  
**Business Value:** Eliminates CSV/script dependency and enables theme expansion.  
**Acceptance Criteria:**

- Admin creates/edits/deletes themes
- Per letter (26 per theme), admin uploads and manages:
  - Letter + Subject combined static image (pre-set, non-personalized)
  - Background scene image (for AI-generated personalization)
  - Subject name and metadata
  - Related element text
  - Trace text templates
- Admin uploads/replaces static handwriting practice pages
- Admin uploads SVG templates (cover, worksheets)
- All assets stored in Supabase storage
- Changes reflect immediately in user book generation

### BR-12: Admin Asset Library

**Priority:** Medium  
**Description:** View and manage all uploaded assets.  
**Business Value:** Enables content organization and storage management.  
**Acceptance Criteria:**

- Admin views all uploaded images by theme
- Admin deletes unused assets
- Admin sees storage usage metrics
- Assets organized by theme and type
- **Admin views line art prompt variation performance metrics** (which styles users select most frequently)
- **System tracks prompt variation selection data for optimization**

### BR-13: Beta Access Control

**Priority:** ~~High~~ **REMOVED PER CLIENT DECISION (Oct 30, 2025)**  
**Status:** **REMOVED** - Client decided to allow public registration without beta approval. Product quality validated through alpha testing; controlled launch via selective marketing instead.  
**Acceptance Criteria:** ~~Removed~~ - Open registration enabled

**Client Quote (Oct 30, 2025):** _"I feel very confident that I've solved enough of the technical issues that we don't need the beta check anymore."_

### BR-14: Automated Quality Validation

**Priority:** High  
**Description:** Automatically detect and retry failed image generations.  
**Business Value:** Ensures quality without manual review bottleneck.  
**Acceptance Criteria:**

- AI-driven face detection validates personalized pages
- Blank or deformed faces automatically trigger regeneration
- Maximum retry attempts defined (prevent infinite loops)
- Failed pages flagged for admin review after max retries
- Detection occurs before showing pages to users

### BR-15: Child Profile Management

**Priority:** High  
**Description:** Parents create profiles for multiple children (siblings) with one line art per child, enabling reuse across books.  
**Business Value:** Increases lifetime value, simplifies repeat purchases, reduces friction for multi-child families.  
**Acceptance Criteria:**

- Multiple child profiles per account
- Each profile stores: first name only, line art reference
- During book creation, parent selects child from profile list
- One line art per child (reusable across books)
- Original photo deleted immediately after line art generation and selection (per BR-RULE-04)
- Line art persists in profile for future books
- No limit on children per account
- Parents can delete child profiles (with confirmation)

### BR-16: Marketing Data Integration

**Priority:** Medium  
**Description:** Send user activity data to HubSpot via webhooks for marketing campaign management.  
**Business Value:** Enables targeted campaigns based on theme preferences and purchase behavior.  
**Acceptance Criteria:**

- Webhook on registration (parent ID, email, date)
- Webhook on book completion (parent ID, child ID, theme, date)
- Webhook on payment (parent ID, book ID, amount, theme)
- Data mappable to HubSpot contact properties for segmentation
- Webhook failures logged but don't block user workflows (non-blocking)
- Webhook endpoint configurable via environment variables

### BR-17: Privacy & Compliance Framework

> **LEGAL DISCLAIMER - NOT LEGAL ADVICE**
>
> The Contractor provides **technical recommendations** only, not legal advice. **Client must retain qualified legal counsel** to review privacy policies, Terms of Service, verify COPPA/GDPR/CCPA compliance, validate data handling, and approve all user-facing legal language. These recommendations are starting points only.

**Priority:** Critical  
**Description:** Technical features to support privacy compliance, subject to client's legal counsel review.  
**Business Value:** Protects user privacy, reduces legal risk, builds trust with parents.

**Technical Compliance Features (Not Legal Advice):**

**User-Facing Legal Pages:**

- Privacy Policy and Terms of Service pages (client must provide/approve content with legal counsel)
- Both accessible before registration and linked in footer
- The Contractor can provide AI-generated drafts as starting points, but must be reviewed by client's counsel

**Data Collection & Consent:**

- Registration requires: age 18+ confirmation, parent/guardian confirmation, ToS acceptance, Privacy Policy link visible
- Child profile creation requires: parental authority attestation (exact wording finalized by attorney) and clear statement of what data is collected and why

**Data Minimization:**

- Collect only: child first name + line art (non-identifiable)
- Do NOT collect: last name, date of birth, or other identifying information
- Original photos deleted immediately after line art selection (per BR-RULE-04)
- Line art: non-PII, safe to retain

**PII Handling:**

| Category | Data | Handling |
|----------|------|----------|
| **Parent PII** | Email, password (hashed) | Authentication and communication |
| **Child Minimal PII** | First name only | No last name, DOB, or other identifiers |
| **Temporary Data** | Child photo | Deleted within 60 seconds per BR-RULE-04 |
| **Non-PII** | Line art | Anonymized, non-identifiable |
| **Not Collected** | Child last names, DOBs, SSNs, addresses, phone numbers, payment cards (Stripe PCI DSS Level 1), behavioral tracking beyond basic analytics | N/A |

**PII Protection:**

- Row-Level Security prevents unauthorized access
- Encryption at rest (Supabase AES-256) and in transit (HTTPS/TLS 1.3)
- Minimal data retention (child first name + line art only)
- No public access to child data
- Activity logging for compliance audits

**Data Access & Deletion:**

- Parents view all data associated with their account
- Parents delete child profiles at any time (removes name, line art, references)
- Parent account deletion cascades to all child profiles and data
- Soft delete with 30-day recovery, then hard delete
- Deletion operations logged

**Acceptance Criteria:**

- Legal pages exist and are accessible
- Consent checkboxes function correctly
- Data deletion workflows work as specified
- Photo deletion within 60 seconds (logged)
- Security controls prevent unauthorized access
- Legal content review and compliance certification are client responsibility

**Out of Scope for The Contractor:** Privacy policy language, Terms of Service language, legal compliance verification, regulatory filings (all client + attorney).

---

## 5. Use Cases / Business Scenarios

### Use Case 1: Parent Creates First Personalized Book

**Actor:** Parent (First-time User)

**Flow:**

1. Parent discovers CreativeBooks and visits app URL
2. Parent creates account with email and password (open registration)
3. Parent logs in to dashboard
4. Parent selects "Create Child Profile" and enters child's first name
5. Parent uploads child's photo
6. **System presents square crop tool** (square reduces errors by 50%)
7. Parent adjusts photo to focus on face/upper body in square frame
8. System generates 4 line art style variations (cost: $0.16)
9. Parent selects preferred line art
10. **Original photo deleted immediately** (within 60 seconds, logged)
11. Child profile saved with first name and line art
12. Parent selects "Create New Book", chooses child, browses themes, selects "Insects"
13. **System generates 5-page preview** (cover + Letter A + Letter B, cost: $0.12)
14. Preview pages appear progressively; parent reviews
15. Parent proceeds to payment: $5.99 via Stripe
16. **Payment triggers full generation**: remaining 56 pages (cost: $0.94)
17. Pages appear progressively; parent can regenerate any AI-generated pages (up to 25 total)
18. System assembles 61-page PDF
19. Parent downloads book; can re-download anytime from library

**Success Outcome:** Parent receives 61-page personalized book after preview-informed purchase, no developer intervention. Profile stored for future books. Cost: ~$1.22 to ~$2.20; Revenue: $5.99; Profit: ~$3.79 to ~$4.77.

### Use Case 2: Parent Creates Additional Book (Same Child, Different Theme)

**Actor:** Parent (Returning User)

**Flow:**

1. Parent logs in, selects "Create New Book"
2. Selects existing child from profile list (no new photo needed, line art reused)
3. Selects different theme (e.g., "Dinosaurs")
4. System generates 5-page preview using stored line art
5. Parent reviews and confirms preview
6. Payment: $5.99 → system generates remaining 56 pages
7. Parent reviews, regenerates if needed (within 25 limit), downloads
8. Both books accessible in library

**Success Outcome:** Line art reused for faster creation. Cost: ~$1.06 to ~$2.04; Revenue: $5.99; Profit: ~$3.95 to ~$4.93.

### Use Case 3: the client Adds New Theme

**Actor:** the client (Admin)

**Flow:**

1. The client logs into admin panel and creates new theme "Dinosaurs"
2. For each letter (A-Z), uploads: letter+subject combined static image, background scene image
3. Enters metadata per letter: subject name, related element, trace text templates
4. Uploads cover and worksheet SVG templates
5. Activates theme → immediately available for users

**Success Outcome:** New theme available without code deployment.

### Use Case 4: ~~Beta Invitation Management~~ **REMOVED**

**Status:** **REMOVED PER CLIENT DECISION (Oct 30, 2025)** - Public registration enabled; controlled launch via selective marketing.

### Use Case 5: ~~Non-Approved User Registration~~ **REMOVED**

**Status:** **REMOVED PER CLIENT DECISION (Oct 30, 2025)** - All users can register freely.

### Use Case 6: Parent Creates Book for Second Child (Sibling)

**Actor:** Parent (Returning User with Multiple Children)

**Flow:**

1. Parent logs in, creates new child profile for sibling
2. Enters second child's first name, uploads photo
3. System presents square crop tool; parent adjusts composition
4. System generates 4 line art variations (cost: $0.16)
5. Parent selects preferred line art; photo deleted immediately (within 60 seconds, logged)
6. Second child profile saved
7. Parent selects "Create New Book", chooses second child, selects theme
8. System generates 5-page preview; parent reviews and pays $5.99
9. System generates remaining 56 pages; parent reviews and downloads
10. Library shows books for both children

**Success Outcome:** Multiple children managed within one account, each with own reusable line art. Cost for second child's first book: ~$1.22; subsequent books: ~$1.06.

---

## 6. Business Rules

### BR-RULE-01: One Line Art Per Child (Reusable Across Books)

Each child profile has one line art reusable across multiple books. To use different line art, create a new child profile or update existing (generates new options).

**MVP Limitation:** One reusable line art per child. Future enhancement: test different line art on different backgrounds without new profiles. Schema should accommodate this.

### BR-RULE-02: Payment Required Before Download

No book PDF downloadable without completed payment. All users must pay before full book access.

### BR-RULE-03: Single Theme Per Book

Each book uses exactly one theme. No mixing themes within a book.

### BR-RULE-04: Photo Privacy and Immediate Deletion

Original photos deleted IMMEDIATELY after line art generation and selection (within 60 seconds). Photos NOT retained for book generation — only line art is used. Deletion logged for compliance audit trail. Line art persists indefinitely in child profile (non-identifiable, safe to retain).

### BR-RULE-06: Regeneration Limits

Maximum 25 total regenerations per book (global limit across preview AND post-payment, ~$1.00 additional cost included in $5.99 price). Users can regenerate ANY AI-generated page until limit reached.

**Error Message (client-approved):** _"You have reached the maximum number of re-generations for this book. Please re-purchase a book to reset the regeneration limit."_

**Note:** Incremental billing planned post-MVP for unlimited pay-per-regeneration.

### BR-RULE-07: Two Page Types Per Letter

Each letter requires exactly two pages:

1. **Letter + Subject Combined Page** (pre-set, non-personalized): static image combining decorative letter and subject
2. **Personalized Scene Page**: AI-generated scene with child, letter, and subject

Changed from 3 to 2 pages per letter per client feedback (November 6, 2025).

### BR-RULE-08: Automated Quality Control

Personalized pages with blank or deformed faces automatically regenerated before being shown to users. Manual face checking not acceptable for MVP.

### BR-RULE-09: Beta Access Restriction

**REMOVED PER CLIENT DECISION (Oct 30, 2025)** — Public registration enabled. Controlled launch via selective marketing.

### BR-RULE-10: Fixed Pricing

All books $5.99 during MVP Phase 1. Base cost: ~$1.22 first book, ~$1.06 additional (line art reused), up to ~$2.20 max (25 regenerations). Theme-specific or variable pricing not supported.

### BR-RULE-11: Registration Required Before Generation

Account creation and authentication required BEFORE any generation features (including preview). Prevents bot abuse and manages costs through user accountability.

---

## 7. Assumptions and Dependencies

### Assumptions

1. **User Access**: Reliable internet and devices for photo upload and PDF download
2. **Photo Quality**: Parents upload clear, front-facing photos suitable for line art conversion
3. **Payment Method**: Valid Stripe-supported payment methods
4. **Browser Compatibility**: Modern web browsers (Chrome, Safari, Firefox, Edge)
5. **Printing Capability**: Access to home printers for PDF printing
6. **Content Readiness**: 6 themes configured before launch: insects, dinosaurs, birthday, fantasy kingdom, animals, sports & activities
7. **API Reliability**: Google Gemini API (gemini-2.5-flash-image model) maintains current quality and performance
8. **User Behavior**: Early adopter customers willing to provide feedback

### Dependencies

1. **Supabase**: Authentication, database storage (themes, letters, metadata), file storage (images, PDFs, assets)

2. **Google Gemini API**: gemini-2.5-flash-image model availability and 99.9% SLA uptime; current ~1/6 failure rate acceptable with auto-retry; structured output for face validation

3. **Stripe**: Account setup/approval, API integration, payment gateway availability

4. **HubSpot** (optional, can be Phase 1.5): Webhook endpoint for user activity events, contact property mapping for segmentation; not required for core functionality

5. **Third-Party Services**: PDF generation libraries, image processing capabilities

6. **Client Assets**: Complete theme assets/metadata, properly formatted SVG templates, brand assets, Privacy Policy and Terms of Service content (with legal counsel approval)

7. **Technical Infrastructure**: Hosting, domain/SSL, dev/staging/production environments

---

## 8. Exclusions (Out of Scope)

### Explicitly Excluded from MVP Phase 1

1. **Professional Print Fulfillment** - No Lulu.com integration; digital PDF delivery only

2. **Social Features** - No social sharing, public galleries, or user-to-user interactions

3. **Marketing Integrations Beyond Webhooks** - No affiliate program (ClickBank); no advanced analytics beyond basic webhook events

4. **Security Hardening** - Basic SQL injection and rate limiting protection; full security audit planned for public launch

5. **Admin Advanced Features** - No user/order management, refund processing, or analytics dashboard; asset management only

6. **Advanced Book Features** - No custom text editing, page reordering, or content customization

7. **Multi-language Support** - English only; schema supports future languages

8. **Saved Drafts** - Incomplete books not saved; single-session completion required

9. **Post-Purchase Modifications** - No editing or regeneration after purchase; books final upon download

10. **Multiple Subject Options Per Letter** - Single predetermined subject per letter; no user choice between alternatives

11. **Incremental Billing for Regenerations** - No pay-per-regeneration beyond 25 limit; future feature would allow unlimited for incremental fees

---

## 9. High-Level Risks

### Risk 1: AI Image Generation Failure Rate

**Description:** Current 1/6 failure rate could impact UX if auto-retry doesn't sufficiently mask failures.  
**Mitigation:** Robust automated retry with max attempt limits; monitor rates at launch; adjust strategy as needed.  
**Impact:** High - core product quality  
**Priority:** Address in MVP

### Risk 2: Regeneration Costs (MITIGATED)

**Description:** Regenerations cost ~$0.04 each and could accumulate.  
**Mitigation:** **Maximum 25 regenerations per book** limits exposure to ~$1.00/book worst case, absorbed in $5.99 price. Incremental billing planned post-MVP.  
**Impact:** Medium - controlled through hard limits  
**Priority:** Addressed in MVP design

### Risk 3: Preview Abandonment Costs

**Description:** Users may generate previews (~$0.28 first child, ~$0.12 additional) without completing payment.  
**Mitigation:** Account required before generation; preview value encourages conversion; monitor abandonment rates; line art reuse reduces per-book abandonment cost for returning users.  
**Impact:** Medium - unit economics and conversion  
**Priority:** Monitor during MVP; acceptable loss-leader for qualified leads

### Risk 4: Payment Processing Reliability

**Description:** Payment failures or disputes could impact revenue and satisfaction.  
**Mitigation:** Comprehensive error handling, clear messaging, transaction logging; thorough pre-launch testing.  
**Impact:** High - revenue generation  
**Priority:** Address in MVP

### Risk 5: PDF Generation Performance

**Description:** On-demand 61-page PDF assembly could cause download delays.  
**Mitigation:** Optimize generation, implement progress indicators, consider pre-assembly after generation completes.  
**Impact:** Medium - user experience  
**Priority:** Monitor during MVP

### Risk 6: Session Timeout and Lost Progress

**Description:** Session timeout could cause frustration and abandonment.  
**Mitigation:** Clear timeout warnings, reasonable timeout duration; documented as known limitation.  
**Impact:** Medium - UX and conversion  
**Priority:** Post-MVP (saved drafts)

### Risk 7: Theme Asset Complexity

**Description:** Managing 52+ images per theme through admin could be cumbersome.  
**Mitigation:** Intuitive admin interface with bulk upload, validation checks, and preview.  
**Impact:** Medium - content management efficiency  
**Priority:** Address in MVP through good UX

### Risk 8: Initial Launch Volume Management

**Description:** Concurrent users at launch could overwhelm system; insufficient monitoring could miss issues.  
**Mitigation:** Rate limiting, performance monitoring, proactive scaling based on traffic.  
**Impact:** Medium - launch success and stability  
**Priority:** Active monitoring during launch

### Risk 9: Line Art Quality Variation

**Description:** All 4 line art options might be poor quality for some photos.  
**Mitigation:** Photo upload guidance; allow different photo if all options unsatisfactory.  
**Impact:** Medium - product quality perception  
**Priority:** Monitor at launch, improve guidance as needed

---

## 10. High-Level Roadmap / Timeline

**Contract Period:** November 10, 2025 - January 10, 2026 (8 weeks)  
**Development Approach:** Linear Method with 2-week cycles and client demos at each milestone

---

### Cycle 1: Foundation & Admin Portal (Nov 10-24, 2025)

**Duration:** 2 weeks  
**Client Demo:** November 24, 2025

**Deliverables:**

- Development environment and deployment pipeline (Vercel + Supabase)
- Database schema and migrations (11 tables with Row-Level Security)
- Type-safe API foundation (tRPC) with authentication middleware
- Google Gemini AI integration for image generation
- Trigger.dev background job queue configuration
- Admin portal: dashboard, navigation, theme creation/management
- Letter asset upload system (52 images per theme: 26 letters × 2)
- Static template management (cover, practice pages, back cover)
- Asset library with storage metrics

**Milestone:** Admin portal operational; the client can upload theme content

---

### Cycle 2: User Experience & Preview Generation (Nov 24 - Dec 8, 2025)

**Duration:** 2 weeks  
**Client Demo:** December 8, 2025

**Deliverables:**

- User registration/authentication with email verification
- Privacy compliance: legal pages and consent tracking
- Child profile management: create, view, delete for multiple children
- Photo upload with square crop tool and 4-style AI line art generation
- Immediate photo deletion (within 60 seconds, logged)
- Book creation workflow: select child, choose theme
- Preview generation: 5-page preview (cover + A + B) before payment
- Real-time progress tracking with Supabase Realtime
- Regeneration system: user regenerations (25 limit) + free system-failure retries
- Client-approved error messaging at regeneration limit

**Milestone:** Complete user journey from registration through preview

---

### Cycle 3: Payment, Full Book Generation & Core Delivery (Dec 8-22, 2025)

**Duration:** 2 weeks  
**Client Demo:** December 22, 2025

**Deliverables:**

- Stripe payment integration ($5.99/book) with secure checkout and webhooks
- Full book generation: 56 pages post-payment (61 total)
- Post-payment regeneration (continuing global 25-regeneration quota)
- PDF assembly with caching and signed URL generation
- Book library dashboard with detail view, regeneration, and download
- Privacy: automated cleanup jobs for expired profiles (30-day soft delete)
- Initial end-to-end testing and bug fixes

**Milestone:** Complete MVP with full book creation workflow

---

### Cycle 4: Testing, Polish & Launch Preparation (Dec 22, 2025 - Jan 5, 2026)

**Duration:** 2 weeks  
**Client Demo:** January 5, 2026 (Final Launch Review)

**Deliverables:**

- Comprehensive end-to-end testing across all flows
- Security audit (RLS, rate limiting, SQL injection prevention)
- Performance optimization (indexing, image loading, connection pooling)
- Cross-browser testing (Chrome, Safari, Firefox, Edge)
- UI/UX polish and responsive design
- Admin monitoring for system failures and compliance metrics
- Load testing with concurrent users
- Bug fixes and edge case handling
- Documentation: user guides, admin docs, API docs
- Optional (if time): HubSpot marketing webhook integration
- Production deployment and launch verification

**Milestone:** Production-ready platform

---

### Project Milestones & Client Touchpoints

| Date             | Milestone      | Deliverable                                         |
| ---------------- | -------------- | --------------------------------------------------- |
| **Nov 24, 2025** | Cycle 1 Review | Admin portal demo with 1+ themes configured         |
| **Dec 8, 2025**  | Cycle 2 Review | Complete user flow through preview generation       |
| **Dec 22, 2025** | Cycle 3 Review | Full book generation, payment, and download working |
| **Jan 5, 2026**  | Final Review   | Production-ready platform ready for launch          |

---

### Post-MVP Enhancements (Future Phases)

- Saved draft functionality for incomplete books
- Multiple line art versions per child
- Professional print fulfillment (Lulu.com)
- Social sharing features
- Affiliate program integration
- Multi-language support (schema prepared)
- Additional educational content options
- Advanced analytics dashboard
- Mobile app (React Native)

---

## 11. Approvals

### Stakeholder Sign-Off

| Name                | Role                         | Signature | Date |
| :------------------ | :--------------------------- | :-------- | :--- |
| Client Stakeholder   | Business Owner/Product Owner |           |      |
| The Contractor PM        | Project Manager              |           |      |
| The Contractor Tech Lead | Technical Authority          |           |      |

---

## Appendix A: Book Structure Details

### Complete 61-Page Book Composition

1. **Cover Page** (1 page) - Personalized with child's illustration + theme name; uses cover template SVG

2. **"This Book Belongs To" Page** (1 page) - Decorative with space for child's name; theme-specific decorations

3. **Alphabet Pages** (52 pages = 26 letters × 2 pages)
   - **Letter + Subject Combined Page** (26): Pre-set static image (e.g., "Aa" with ant illustration)
   - **Personalized Scene Page** (26): AI-generated composite with child in themed scene

4. **Handwriting Practice Pages** (5-6 pages) - Stroke practice, uppercase/lowercase tracing, blank practice lines

5. **Back Cover** (1 page) - Thank you message and branding

### Theme Asset Requirements Per Letter

For each of 26 letters, admin configures:

**Images (2 per letter):**
- Letter + Subject combined static image
- Background scene image (for AI personalization)

**Metadata:**
- Subject name (e.g., "ant", "bee")
- Related element (e.g., "picks apples")
- Trace text upper template (e.g., "{child_name} picks apples")
- Trace text lower (e.g., "with an ant")

**Total per theme:** 52 images + metadata for 26 letters

---

## Appendix B: Technical Terminology Reference

**Business-focused language used in BRD. Technical implementation in TRD.**

### Key Business Terms

- **Child Profile**: Parent-created profile (first name + line art), reusable across books. Multiple profiles per account.
- **Line Art**: B&W outline illustration generated from photo, stored in profile for reuse. Non-identifiable.
- **Theme**: Complete educational content set for one subject area (e.g., Insects, Dinosaurs)
- **Page Generation**: Automated creation of personalized book pages with child's illustration
- **Quality Validation**: Automated detection of blank/deformed faces requiring regeneration
- **Individual Page Job**: Single page as independent entity for selective regeneration
- **Book Assembly**: Combining all pages into single downloadable PDF
- **Photo Deletion**: Original photos deleted immediately after line art selection (within 60 seconds), logged per BR-RULE-04
- **Early Adopter**: Initial customer during launch providing product feedback
- **Marketing List**: Email list from creativebooks.app signup

---

## Appendix C: Change Log

### Version 2.3 - November 10, 2025

**Production Launch Preparation & PII Clarification** (The Contractor)

- Replaced beta testing references with production launch language throughout
- Added comprehensive PII handling section to BR-17 (what we collect vs don't collect, protection measures)
- Enhanced success metrics with quantifiable targets (< 1% payment failures, 100+ concurrent users, < 2s loads, > 99.5% photo deletion, < 10 min completion)

---

### Version 2.2 - November 10, 2025

**Timeline Update & Final Review** (The Contractor)

- Added specific contract period: Nov 10, 2025 - Jan 10, 2026 (8 weeks)
- Replaced generic phases with 4 dated cycles and client demo dates
- Clarified line art as per-child-profile one-time cost; distinguished first vs additional book costs
- Status changed to "Final - SOW Attachment"

---

### Version 2.1 - November 6, 2025

**Book Structure Consolidation** (The Contractor)

- Book: 87 → 61 pages (3 → 2 pages per letter)
- Preview: 7 → 5 pages; Post-payment: 80 → 56 pages
- Decorative letter + subject focus pages merged into single combined image
- Admin assets: 78 → 52 images per theme
- Updated BR-04, BR-05, BR-11, BR-RULE-07, Appendix A

---

### Version 2.0 - November 4, 2025

**Multi-Child Support, Marketing Integration & Privacy** (The Contractor)

- Added BR-15 (Child Profile Management): multiple children per parent, one reusable line art per child
- Added BR-16 (Marketing Data Integration): HubSpot webhooks for registration, completion, payment events
- Added BR-17 (Privacy & Compliance): COPPA/GDPR/CCPA technical features, legal disclaimer, consent tracking, data deletion
- Updated BR-02: photo deletion immediate after line art selection (was: after book completion)
- Updated BR-10: supports same child (different themes) + siblings
- Updated BR-RULE-01: "One Line Art Per Child" (was: per book); BR-RULE-04: immediate photo deletion (was: retained until completion)
- Added Use Case 6 (sibling workflow); updated Use Cases 1 & 2 for child profiles
- HubSpot dependency updated to optional marketing webhooks

---

### Version 1.0 - October 31, 2025

**Initial Release** (The Contractor)

Original MVP requirements: BR-01 through BR-14, use cases, business rules, project scope. Core features: registration, photo/line art, themes, preview (5 pages), full generation (56 pages), regeneration (25 limit), payment ($5.99), PDF delivery, library, admin management, quality validation. Open registration per client decision Oct 30, 2025.

---

## Important Note: Accessibility in MVP

**Accessibility features are OPTIONAL for MVP Phase 1 and not in core scope.** This includes WCAG 2.1 AA compliance, screen reader support, keyboard navigation, high contrast modes, and ARIA labels. MVP focuses on core functionality with basic usability. Full accessibility can be implemented post-MVP based on feedback and priorities.

---

**Document Status**:  **Version 2.3 - FINAL** - SOW Attachment Ready for Client Signature

---

**Document End**

_Technical specifications, architecture decisions, and implementation details are defined in the companion Technical Requirements Document (TRD)._
