# CreativeBooks Platform - Personalized Children's ABC Books

**Project Status**: Pre-Launch (Collecting Waitlist) | Working Implementation Available
**Live Website**: https://creativebooks.app | **Version**: 2.0 (Updated September 23, 2025)

## Executive Overview

**"Boost early reading with personalized ABC coloring books starring your child"**

CreativeBooks creates personalized 85+ page ABC activity books featuring children as main characters, combining AI image generation with educational content for print-at-home books.

**Current Status**: the client has a working implementation with image generation, PDF creation, and brand presence. First personalized book produced for "the client" using the insects theme: "I have now completed my first full book (manually) so I'm even better prepared for this project."

**Current Implementation Status:**

- **AI Pipeline**: Batch processing using nano-banana model with 26 personalized images per child (A-Z coverage) and QA face validation
- **Educational Content**: A-Z insects theme with background images, typography (Chewy + KG Primary Dots), and learning structure
- **CSV-Driven System**: CSV files for theme development and personalization
- **Book Output**: 85+ page books with alphabet tracing, word practice, and personalized coloring pages
- **Website**: Live at creativebooks.app targeting TK/Kindergarten/1st grade preparation
- **the client's Development Requests**: Frontend interface, production environment, and security hardening (for public launch)

---

## Current Architecture and Implementation

### the client's Implementation Approach

**CSV-Driven Content Management**: CSV files drive the workflow. The insects_archer.csv file contains 26 rows with A-Z theme specifications.

**Batch Processing**: System processes multiple background templates. MVP requires 26 personalized images with QA face validation.

**Educational Structure**: Typography (Chewy for display, KG Primary Dots for tracing), SVG templates with named zones for content placement, A-Z learning progression.

**Quality Control**: the client requested a "check step" for face integration. Current file organization includes batch folders (development artifacts, not relevant to actual QA validation process).

### Current Implementation Architecture

**File Organization** (from the client's creativebooks-assets folder):

- CSV metadata files (insects_archer.csv with A-Z theme definitions)
- Python scripts (generate_composites_parallel_insects_nano_final.py, generate_worksheet_from_csv_row.py)
- Child photos and line art (face_photo.png, face_lineart.png)
- Background templates (58 insect scenes in subject_child_backgrounds/insects/)
- Composite images (26 per child with QA validation in subject_child_composites/)
- SVG templates with named zones (worksheet_templates/): worksheet template + new cover template
- Final PDFs output (worksheet_outputs/insects/)

**User Journey** (from creativebooks.app):
5-step process: Pick subject → Upload photo → Approve illustration → Get pages → Print at home

---

## Current Implementation Status (Per the client's Communications)

### What the client Has Built and Working

**Insects Theme**: 58 background templates, CSV metadata with file naming, batch AI generation of 26 composites per child, PDF generation with typography, SVG templates with named content zones (see Architecture section above for details).

**the client Child Profile**: Profile with photos and generated line art, insects theme personalization across all 26 letters, composite images, and PDF outputs.

**Website**: Live at creativebooks.app with product information, 5-step UX, pre-launch waitlist collection, and brand positioning.

### What the client Has Requested for The Contractor Development

**Frontend Application** (the client's Specific Request):

the client stated: "where I'll really want your help to focus is on building the front end app / UI"

- User interface implementing the 5-step process
- Photo upload and processing interface
- Theme selection and customization screens
- Preview and approval workflow with regeneration options

**Production Infrastructure** (the client's Priority Request):

the client stated: "setting up scaleable environments (dev, staging, prod in GIT, etc), ensuring the pipelines are hardened against SQL injection, brute force, etc"

- Development/staging/production environments with GIT integration
- Security hardening against SQL injection and brute force attacks (required for public launch, not MVP)
- Deployment architecture
- DevOps practices

**System Integration**:

- User account and authentication
- Payment processing for book orders
- Print fulfillment integration (home printing for MVP + professional printing for public launch)
- Customer support and order management

---

## the client's Detailed MVP Requirements (From CreativeBooks MVP.md)

### User MVP Specifications (the client's Requirements)

**New User CRUD**:

- Signup authentication handled by Supabase (already working)
- Billing integration
- Support for multiple children per user account

**New Child CRUD** (child ID tied to user ID):

- Child name creation
- Child portrait upload → sends to Replicate x4 for line-art creation
- Child line art portrait regeneration (using nano-banana: https://replicate.com/google/nano-banana)
- Child line art portrait selection and saving
- **Post-MVP Feature**: Multiple line art versions per child — "users will be able to have multiple line art images for the same child and be able to apply that to the same theme for different results" (schema/scaffolding considerations required for MVP planning)

**Theme Selection & Book Creation Workflow**:

- Theme selection (insects, dinosaurs, etc.) from pre-built image libraries
- Selecting child portrait + theme triggers full build process
- Confirm build with "create" button (triggers Stripe payment workflow in production)

**Personalized Image Generation Workflow** (the client's Current Process):

1. Pulls pre-built images from Supabase or AWS storage
2. Sends child line art + child photo + pre-built images + single prompt to nano-banana model
3. **Critical Quality Check Step**: "a 'check step' that looks for a completed face"
   - Face exists → pass to PDF page assembly
   - No face or deformed → automatically resend API call
   - Failure rate: ~1/6 of the time
4. PDF page assembly using child name + pre-built SVG template + Python script
5. PDF book collation assembling individual pages in order

**Book Review & Management Interface**:

- **Progressive Page Display**: Pages appear in carousel/grid as individual jobs complete
- **Individual Page Jobs**: Each page maintained as separate entity for optimal regeneration
- the client's requirement: "need a way to view each page inside the app (a carousel could work) and include a button on the personalized pages to regenerate the image if desired"
- **Seamless Regeneration**: Click regenerate → queue individual page job → update UI when complete (no impact on other pages)
- **Smart Regeneration** (Post-MVP): System tries different "magic prompts" on regeneration
- **On-Demand PDF Assembly**: "Print PDF book" triggers real-time collation of all completed page jobs
- **Flexible Book Management**: Save, share, delete operations on complete book collections
- **Individual Page Management**: Save, share, or replace individual pages without affecting book integrity
- Order PDF (production feature) — Submit support request (triggers email to info@creativebooks.app)

### Admin MVP Specifications (the client's Requirements)

**User Management**:

- User CRUD with related child CRUD capabilities
- Related Book(s) CRUD — Ability to log in as user for support purposes

**Content Management**:

- Theme/category and background images CRUD
- Add/delete category to dropdown UI connecting to backend templates
- Background image system
- **Magic Prompt Management** (Post-MVP):
  - CRUD interface for managing 4 "magic prompts" (expandable)
  - Prompt performance analytics integration
  - A/B testing controls for prompt distribution
  - Schema designed for scalability beyond 4 prompts

**Admin Analytics Dashboard**:

- Most popular subjects tracking
- **Magic Prompt Performance Analysis** (Post-MVP):
  - Track performance of 4 "magic prompts" (scalable schema)
  - Prompt usage distribution across generated pages
  - Regeneration rates per prompt variant (quality indicator)
  - Parent feedback/approval rates by prompt
  - Conversion optimization data for prompt selection
- Error/regeneration rate by page (to optimize underlying images)
- Cost of generations (Replicate account integration)
- User and content analysis tools

**Post-MVP Admin Features for A/B Testing**:

- **Flow Variant Management**: Enable/disable theme-first vs child-first flows
- **Conversion Funnel Analytics**: Track completion rates per flow variant
- **Feature Flag Controls**: Real-time A/B test configuration without deployments
- **Statistical Significance Monitoring**: Automated alerts when tests reach significance
- **User Cohort Analysis**: Performance comparison across flow variants

### Technical Infrastructure (the client's Current Setup)

**Supabase Configuration**:

- **Project Name**: ABEme_front-end
- the client provided Supabase project access and configuration details

**AWS Status Clarification**:
the client stated: "I'm not sure we need AWS anymore" and "Honestly, I'll need your help here as I get lost in the AWS backend"

- **AWS Rekognition**: Eliminated — confirmed "don't need this anymore"
- **S3 Storage**: Can be handled via Supabase if more convenient
- **IAM Access**: the client requested guidance if AWS is used

**Current Tech Stack** (Per CreativeBooks MVP.md):

- **Frontend**: React/Next.js with Tailwind (i18n-ready framework structure required)
- **Backend**: Python (internationalization library integration planned)
- **Storage**: AWS S3 (working) & Supabase (working)
- **Auth & DB**: Supabase (working) — schema must support i18n from MVP
- **Image Generation**: Replicate nano-banana model
- **PDF Builder**: SVG template processing with Base64 image embedding, converted via Inkscape subprocess (Python) — multi-language font support required
- **Delivery**: Signed S3 URLs, Email (SendGrid)

**Recommended Post-MVP Additions for A/B Testing**:

- **Feature Flags**: LaunchDarkly, Split.io, or custom implementation
- **Analytics**: Mixpanel, Amplitude, or Google Analytics 4 for funnel tracking
- **A/B Testing Framework**: Statistical significance testing and variant management
- **Remote Configuration**: Real-time flow control without deployments

**MVP Schema Requirements for Future Internationalization**:

- **Content Tables**: locale/language_code columns for themes, prompts, and text content
- **User Preferences**: language_preference, region, timezone fields
- **Localized Content**: Separate tables for theme names, descriptions, and UI text by language
- **Cultural Adaptations**: Region-specific image variants and cultural preferences
- **Character Set Support**: UTF-8/Unicode for all text fields from day one
- **Font Management**: Multi-language font library support in PDF generation

**Planned Production Integrations**:

- **Print API**: Lulu.com (public launch, not MVP)
- **Payments**: Stripe
- **Marketing Website**: Lovable (https://creativebooks.app/)

### the client's Production Features Vision

**Infrastructure Hardening** (For Public Launch):

- Brute force and SQL injection prevention
- Production, staging, and dev environments with GIT integration

**Production Application Features**:

- User-facing app with CRUD for account/profile, child/children line images, theme worksheets & books
- Marketing website (the client has background in this area)
- Payment integration (Stripe)
- Custom book printing integration (Lulu.com API) — public launch feature
- Social integration for sharing outputs/images/links
- Affiliate code integration (ClickBank)
- Customer support handling (email to info@creativebooks.app)

**Future Features** (Schema & Scaffolding Required from MVP):

- **Internationalization**: Schema and scaffolding must account for i18n from MVP — affects database architecture from launch

### Major Pipeline Changes (the client's Evolution)

**Removals**:

1. **Parallel Image Pipeline**: No longer used (Replicate only now)
2. **Dynamic Prompt Creation**: the client found "one prompt to rule them all!" (post-MVP expansion to 4 "magic prompts" for optimization)
3. **Individual Page Creation**: Now full books only (individual page regeneration after creation included)
4. **Batch Background Creation**: the client now makes background images personally for each theme

**Additions**:

1. **AI-Driven Quality Check**: Automatic face detection and retry before showing to user (~1/6 failure rate)
2. **Individual Page Regeneration**: Parents can click "regenerate" on personalized pages

**Architecture Simplification**:

- "The new image pipeline is more elegant and requires less steps"
- "This simplifies the initial API calls considerably"
- Nano-banana has "DRAMATICALLY simplified the image pipeline"
- AWS may no longer be needed

### MMVP Consideration (the client's Note)

the client considered a more minimal MVP: "is there an MMVP where I just have them set up the supabase -- replaces so I can make these books on demand easily before even opening this to the public???"

---

## User Experience (From the client's Website)

### User Experience (From the client's creativebooks.app Website)

The 5-step process from creativebooks.app:

**Step 1: Pick a Subject** — Select from available themes (insects, dinosaurs, vehicles, sports)
**Step 2: Upload a Photo** — Simple photo upload for integration into ABC scenes
**Step 3: Approve Your Illustration** — Preview and select preferred line art
**Step 4: Get Your Pages** — 85+ page book with alphabet tracing and personalized images
**Step 5: Print at Home** — Flexible printing with focus on specific letters

### User Flow Optimization Strategy (Post-MVP A/B Testing)

**Conversion Optimization Question**: Which flow sequence maximizes completion rates?

**Current MVP Flow (Theme-First)**:

1. Pick Subject → 2. Upload Photo → 3. Approve Line Art → 4. Generate Pages → 5. Print

**Alternative Flow (Child-First)**:

1. Upload Photo → 2. Approve Line Art → 3. Pick Subject → 4. Generate Pages → 5. Print

**A/B Testing Hypothesis**:

- **Theme-First**: May increase engagement through immediate theme connection
- **Child-First**: May increase commitment through early personalization investment

**Technical Requirements for A/B Testing** (Post-MVP):

- Feature flag system for flow control
- Remote configuration management
- Conversion funnel analytics per flow variant
- User session tracking across flow variations
- Statistical significance testing framework

**Key Design Principles**:

- No complex account setup
- Parent approval at every quality-sensitive step
- Book delivery (85+ pages) rather than individual pages
- Print-at-home primary (MVP), physical binding secondary (public launch)

**Actual Implementation Requirements:**

1. **Frontend Development**: Interface for the 5-step user journey
2. **Photo Processing Integration**: Connect upload to nano-banana pipeline
3. **Preview System**: Parent approval of generated line art and composites
4. **Delivery System**: Package 85+ page books for download/printing
5. **Account Management**: User accounts for order history and multiple children

### Working Image Processing Pipeline

**Current Implementation**:
Photos processed through nano-banana to generate line art. Batch processing handles background templates with 26 composites per child validated through QA face detection.

**Production Requirements**:

- Web interface for photo upload and processing
- Progress indicators for batch generation
- Quality validation with automatic retry for failures
- Parent approval interface for line art selection

**the client's Described Workflow**:

1. **Photo Processing**: Parent uploads photo → nano-banana generates line art
2. **CSV Processing**: Load theme CSV (insects_archer.csv) with A-Z specifications
3. **Parallel Page Generation**: Each page as independent job:
   - **Cover Job**: Independent generation using cover template
   - **A-Z Worksheet Jobs**: 26 independent jobs using worksheet templates
   - **Additional Content Jobs**: Tracing pages, word practice, etc.
4. **Quality Check**: Face detection per job (~1/6 failure rate, automatic retry)
5. **Progressive UI Updates**: Pages appear as jobs complete (parallel processing)
6. **Individual Page Regeneration**: Any page regenerated without affecting others
7. **Book Assembly**: On-demand PDF collation at "print" workflow
8. **Book Delivery**: Complete 85+ page book from individual completed jobs

the client noted: "these two scripts actually hold 90% of the production workflow to make the books"

---

## CSV-Driven Content System (the client's Implementation)

### CSV-Driven Content Management System

**Current Implementation (Insects Theme)**:

- **CSV Metadata**: `insects_archer.csv` containing 26 rows (A-Z)
- **Background Templates**: 58 illustrations in `subject_child_backgrounds/insects/`
- **File Naming Conventions**: Systematic approach linking CSV data to file assets
- **Educational Content**: Each letter paired with insect and varied content (action verbs, relational phrases) — CSV input handles all variations

**Validated Content Structure** (Examples):

- **A**: Ant + "picks apples" → "the client picks apples with an ant" (action verb)
- **D**: Dragonfly + "dances" → "the client dances with a dragonfly" (action verb)
- **P**: Praying Mantis + "paints" → "the client paints with a praying mantis" (action verb)
- Content variations include relational phrases like "on a [thing]" — all handled by CSV input

**CSV Schema Architecture**

The metadata system uses 10 columns driving all content generation:

| Column                     | Purpose          | Example                                     |
| -------------------------- | ---------------- | ------------------------------------------- |
| `letter`                   | Alphabet focus   | A                                           |
| `image_subject`            | Subject type     | ant                                         |
| `child_name`               | Personalization  | the client                                      |
| `related_element`          | Activity         | picks apples                                |
| `trace_text_upper`         | Tracing practice | the client picks apples                         |
| `trace_text_lower`         | Context text     | with an ant                                 |
| `composit_output_filename` | Generated file   | a_insects_ant_archer_picks apples_en_01.png |

**Scalability**: Same CSV structure supports any theme (dinosaurs, vehicles, sports) by changing background templates and subject data.

**Internationalization Considerations** (Schema Planning):

- CSV structure must accommodate locale/language columns
- Text fields (trace_text_upper, trace_text_lower, related_element) need localization support
- File naming conventions should include language codes
- Database migration from CSV must preserve i18n schema requirements

### Batch Generation Workflow

**Current Implementation**:
System generates 26 personalized images per child. Script processes CSV files with QA validation.

**Working Process**:

1. CSV specifies all 26 letters with background templates and text content
2. `generate_composites_parallel_insects_nano_final.py` processes backgrounds in parallel
3. Nano-banana API handles face swapping; child line art + background → personalized composite with QA validation
4. Results organized (batch folders are development artifacts only)
5. `generate_worksheet_from_csv_row.py` creates final worksheets with CSV-driven text content

the client: "The problem I've been focused on is making sure I can make the custom pages in parallel (instead of in serial)"

**MVP Library Reduction Strategy**: QA validation eliminates the need for extensive image libraries. the client's large collection exists only for testing which backgrounds produce blank faces more frequently. With QA validation, MVP needs just 26 images (A-Z) with automatic retry for failures.

**the client's Quality Check Request**

Full request: "Creating a 'verification' step for face-swap generated images to ensure that a face was added before showing to the user. Right now the failure rate on generating faces in https://replicate.com/google/nano-banana is about 1/6 and what Id like to do is have. A'check step' that looks for a face-swap and, if not, re-runs the API call."

### the client's User Experience Request

From CreativeBooks MVP.md: "need a way to view each page inside the app (a carousel could work) and include a button on the personalized pages to regenerate the image if desired"

---

## PDF Generation System (the client's Implementation)

### Proven Worksheet Creation Implementation

**Working System**:

- **SVG Templates**: `subject_child_composit.svg` for worksheets + new cover template with named zones
- **Typography System**: Embedded fonts (Chewy for display, KG Primary Dots for tracing)
- **CSV Integration**: Metadata drives text content and image placement
- **Output Format**: Print-ready PDFs for home printing (MVP) and physical binding (public launch)

**Template Architecture**:

**Worksheet Template** (`subject_child_composit.svg`):

- `image_subject`: Zone for personalized composite images
- `trace_text_upper` / `trace_text_lower`: Zones for educational text
- `subject_upper` / `related_element`: Zones for theme and activity text
- Named zones enable precise, consistent layout across all worksheets

**Cover Template** (New):

- `subject_image`: Zone for cover image
- `child_name`: Zone for child's name
- Simplified template requiring new script for cover generation

**Working PDF Creation Process:**

```python
# Actual implementation from the client's scripts
def generate_pdf_from_row(row):
    # Load SVG template with named zones
    tree = ET.parse(TEMPLATE_SVG)
    root = tree.getroot()

    # Inject text with proper fonts
    inject_text(root, "subject_upper", row["subject"].upper(), FONT_BUBBLE, 48, outline=True)
    inject_text(root, "trace_text_upper", row["trace_text_upper"], FONT_TRACE, 36)

    # Embed personalized composite image
    embed_image(root, "image_subject", image_path)

    # Convert to PDF via Inkscape
    subprocess.run(["inkscape", temp_svg, "--export-type=pdf", f"--export-filename={output_pdf}"])
```

### Production-Ready PDF Assembly

**Current Capabilities**: Automated CSV processing with column normalization, Base64 image embedding, font embedding for consistent typography, Inkscape PDF output, and error handling/validation.

**PDF Generation Workflow** (from generate_worksheet_from_csv_row.py):

1. **CSV Processing**: Load theme metadata (insects_archer.csv) with normalized columns
2. **Cover Creation** (Separate from worksheets): Parse cover SVG template (`subject_image` and `child_name` zones), inject cover image and child name, apply cover-specific styling, generate PDF via Inkscape
3. **Worksheet Creation** (per row A-Z): Load SVG template → extract zone boundaries via get_bounds_by_id → inject text with font styling (Chewy + KG Primary Dots) → embed composite image as base64 → write temp SVG (temp_output.svg) → convert via Inkscape subprocess
4. **Book Assembly**: Combine cover + worksheets in correct order
5. **Output Organization**: Save to worksheet_outputs/insects/

### Current Book Assembly Status

**Current Status**: Individual PDF worksheets (A-Z) generated. Complete 85+ page assembly requires:

- **Cover Page** (not yet implemented): Uses cover template (`subject_image` + `child_name` zones), different layout than worksheets — requires new generation script
- **Worksheet Pages** (working): A-Z coverage (26 pages) via `generate_worksheet_from_csv_row.py` + additional educational content (tracing, coloring, word practice)
- **Final Assembly**: Cover + worksheets in correct A-Z sequence, consistent formatting, print-ready

**the client's Production Requests**: Cover generation script, automated book assembly with page ordering, delivery system integration for download/printing.

---

## Individual Page Job Architecture (Optimal UX Solution)

### Architectural Decision: Individual Page Jobs vs Full PDF Generation

**Problem**: Complete 85+ page book delivery while maintaining individual page regeneration without affecting other pages.

**Solution**: Each page as an independent job with parallel processing and on-demand assembly.

### Individual Job Processing Workflow

**Book Generation Trigger**:

1. User selects child + theme → triggers book generation
2. System queues individual jobs:
   - 1 Cover job (cover template)
   - 26 A-Z worksheet jobs (worksheet template)
   - Additional content jobs (tracing, word practice, etc.)
3. All jobs process in parallel via nano-banana API (MVP uses single prompt)
4. Pages appear in UI progressively as jobs complete

**Post-MVP Enhancement - Magic Prompt Selection**:

- Each job randomly assigned one of 4 "magic prompts" for data collection
- Prompt assignment tracked for performance analysis (regeneration rates, parent feedback)
- Scalable schema supports expansion beyond 4 prompts

**User Experience Benefits**:

- **Immediate Feedback**: First pages within 30-60 seconds; progressive loading
- **Seamless Regeneration**: Click "regenerate" → queue job → update when complete; no impact on other pages
- **Fast Print Assembly**: PDF collation <10 seconds from completed jobs

**Technical Benefits**:

- **Parallel Processing**: Maximum speed through concurrent API calls; scalable across workers
- **Error Isolation**: Failed jobs don't block other pages; face check per job with auto-retry
- **Flexible Storage**: Each page stored independently for optimal regeneration
- **Magic Prompt Analytics** (Post-MVP): Track which prompts produce fewer regenerations and higher satisfaction

**Implementation Approach**:

- **Job Queue System**: Individual page jobs with status tracking (MVP: single prompt)
- **Progressive UI**: Carousel/grid updates as jobs complete
- **On-Demand Assembly**: PDF collation only at "print"
- **Individual Page Management**: Save, share, regenerate any page independently
- **Magic Prompt System** (Post-MVP): Schema supports 4+ prompts, each job linked to variant for tracking, assignment via random or weighted algorithm

This architecture delivers both requirements: complete book experience + seamless individual page regeneration.

---

## the client's Development Requests

### Frontend Development Requirements

**From creativebooks.app**:

1. **Subject Selection Interface**: Theme picker with visual examples (feature flag support for flow reordering)
2. **Photo Upload System**: Drag-and-drop with quality guidelines (flexible flow positioning)
3. **Illustration Approval**: Preview interface for line art selection (adaptable to flow sequences)
4. **Book Preview**: Progressive page-by-page display with individual regeneration
5. **On-Demand Assembly**: Real-time PDF collation at "print" (85+ pages from completed jobs)
6. **Delivery Options**: Print-at-home primary (MVP), physical binding secondary (public launch)

**Flow Flexibility Requirements** (MVP Design Consideration):

- Modular interface components for easy reordering
- Feature flag integration points for A/B testing
- Analytics event tracking at each step (Post-MVP)

**Critical Features Needed**:

- Parallel job processing with progressive UI updates
- Real-time per-page status with overall completion progress
- Seamless page regeneration without affecting other pages
- On-demand PDF assembly and flexible page selection for targeted printing
- Quality validation with automatic retry per job
- Account management for multiple children/orders with job history

**Development Priorities** (see "What the client Has Requested" for full quotes):

- **High**: Frontend development, dev/staging/prod environments, security hardening (public launch, not MVP), production workflow optimization
- **Medium**: Database migration from CSV (with i18n schema), payment processing, print fulfillment (public launch), customer support
- **Public Launch** (Post-MVP): Security hardening, monitoring, scalable infrastructure, performance optimization, A/B testing infrastructure, analytics & conversion tracking

### Quality Standards

**the client's Quality Results**:

- Illustration quality across 58 background templates
- Face integration across 26 composites per child (QA validation eliminates need for large image libraries)
- Typography using Chewy and KG Primary Dots
- Print-ready PDF output for home and commercial printing
- A-Z educational coverage with content structure

**the client's Quality Requests**:

- Face check for blank faces (~1/6 failure rate)
- Parent approval workflow (preview and select)
- Page regeneration for personalized pages
- Support request via email to info@creativebooks.app (MVP)

---

## Current Performance Status

### Performance Data

**Technical Performance Data**

- **Image Generation**: 26 composites per child with QA face validation
- **Content Coverage**: A-Z theme (26 letters) with single validated image per letter
- **PDF Generation**: Working pipeline from CSV to print-ready PDFs
- **Output Quality**: Print-ready for home and commercial printing

**Current Limitations** (Development Focus Areas)

- **Manual Processing**: Scripts require manual execution
- **Local Environment**: Hardcoded paths tied to the client's desktop
- **No User Interface**: Command-line only
- **Single Child Focus**: Optimized for the client profile only

**Production Readiness Metrics** (To Be Implemented)

- **User Onboarding Time**: Target <3 minutes total — signup via Supabase, photo upload + nano-banana <15 seconds (typically <9s), first pages within 30-60 seconds (parallel), all 85+ pages within 2-3 minutes
- **Regeneration**: Individual page <30 seconds; PDF collation <10 seconds
- **Multi-Child Support**: Multiple children per family with independent job queues
- **Theme Scalability**: Add themes using same CSV approach and job architecture

**Business Metrics** (From creativebooks.app)

- **Market Demand**: Pre-launch waitlist demonstrating interest
- **Value Proposition**: 85+ page books at print-at-home price point
- **Target Market**: TK/Kindergarten/1st grade preparation
- **Revenue Model**: Digital delivery (MVP) + physical binding (public launch)

### the client's Development Priorities

Priority 1 and 2 detailed in "What the client Has Requested" section above.

**Phase 1 Production Features**: Stripe payments, Lulu.com print API (public launch), social sharing, ClickBank affiliate codes, customer support (info@creativebooks.app).

**Development Timeline**:

- **MVP**: Core functionality, single prompt, English only
- **Production/Public Launch**: Security hardening, scaling, payment integration
- **Post-MVP**: A/B testing, magic prompts, advanced analytics
- **Future**: Multi-language support (schema prepared from MVP)

**Future Features**: Additional themes (dinosaurs, vehicles, sports), multiple line art styles per child, A/B testing infrastructure, conversion analytics, magic prompt optimization (single → 4 → larger library), internationalization (schema from MVP), international payments (multi-currency), localized themes (culturally appropriate per region), regional printing partners, intelligent prompt selection (AI-driven based on photo/theme compatibility).

---

## Summary

**the client's Current System**:

- 26 personalized images per child via nano-banana with QA validation
- A-Z insects theme with 58 background templates
- Working PDF generation pipeline with CSV-driven content
- Live website (creativebooks.app) with 85+ page book specifications
- Python scripts for batch processing and PDF creation

**the client's Development Requests for The Contractor**:

- Frontend application development (i18n-ready architecture)
- Production infrastructure (dev/staging/prod environments)
- Security hardening (SQL injection, brute force) — required for public launch, not MVP
- Project scaffolding with i18n schema planning
- Database architecture supporting future multi-language expansion
