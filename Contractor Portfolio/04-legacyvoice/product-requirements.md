# LegacyVoice - Product Requirements Document (PRD)

---

## Cover Page

| Field | Value |
|-------|-------|
| **Project Name** | LegacyVoice |
| **Client** | The Client |
| **Document Author** | The Contractor |
| **Date** | February 3, 2026 |
| **Version** | 1.5.1 |
| **Status** | Draft - Pending Client Approval |

---

## Introduction

### Document Purpose

This PRD defines business needs, functional requirements, and scope for LegacyVoice MVP. It is the foundation for TRD and development planning.

The The Contractor PRD is a **hybrid BRD/PRD**:

- **BRD:** Why are we doing this? For whom? What business outcome? What constraints?
- **PRD:** What exactly are we building? How will it behave? How will we validate it?

**Objectives:**
1. Stakeholders understand what LegacyVoice MVP will deliver
2. Development team has clear requirements to build from
3. Success criteria and validation methods defined
4. Scope boundaries (MVP vs future phases) clearly established

**Review requested:** Confirm requirements reflect your vision, scope aligns with expectations, and note any corrections or clarifications before development. Once approved, this PRD guides technical design and execution.

### Project Scope

**In Scope for MVP (Phase 1):**

**Content Delivery Model:**
LegacyVoice uses a "rolling delivery" model: Content is uploaded incrementally via Admin Panel as it becomes available, rather than requiring all 70 days complete before launch. MVP launches with 7-10 days of content, with additional days added as client team produces them.

| Category | Features |
|----------|----------|
| **Core Experience** | 7-10 days content at launch (rolling delivery), Daily Lesson flow (Pre-Lesson intro with Gen AI personalization, Direct Instruction with karaoke captions, Q&A, Challenge, Post-Lesson wrap-up with Gen AI), Block-based CMS for lesson creation |
| **Marketing** | Single-page landing page (static HTML/CSS, no logic). Register for Waitlist button redirects to app. Waitlist registration (initial questions) lives in app. Bot prevention via "how you heard about it" field |
| **Engagement** | SMS trigger/notification system with dynamic message variants, Streak tracking, XP accumulation, Global leaderboards, Pause Tokens, Celebration Moments (animations + triggers) |
| **Progression** | Status level system (0-3) with XP thresholds |
| **Feedback** | AI Feedback Approval: AI-generated feedback on Q&A and Challenges with Admin Portal approval workflow (MVP) / Elder Portal approval workflow (Phase 2) - weekly batch delivery |
| **Social** | Story Circles (admin-controlled), "Join with Friends" option, Circle leaderboards, WhatsApp integration |
| **Admin** | Content upload/management (CMS with block-based lesson builder), User management, Signup approval queue (waitlist prioritization), Circle management (manual assignment), Circle bulk communication, Celebration dashboard, XP configuration, Sequential unlock override, Basic data export |
| **Navigation** | Two-tab interface (Learn/Feed), Basic user profile |
| **Testing** | Alpha/Beta feedback tool with Linear integration |

**Out of Scope for MVP:**

| Category | Feature | Rationale | Future Phase |
|----------|---------|-----------|--------------|
| **Authentication** | Stripe Payment Integration | MVP uses manual admin approval | Phase 2 |
| **Onboarding** | Mailing Address Collection | Physical totems not in MVP | Phase 2 |
| **Onboarding** | Avatar Selection | Display name used instead | Phase 2 |
| **Lessons** | Daily Review Session (A4-A5-A3) | Focus on core lesson flow first | Phase 2 |
| **Notifications** | Two-Way SMS | One-way SMS sufficient for MVP | Phase 2 |
| **Gamification** | Streak Milestone Badges | Visual badges deferred | Phase 2 |
| **Feedback** | Story Elder Feedback System | Elder Feedback (direct evaluation) | Phase 2 |
| **Feedback** | Elder Portal AI Approval | AI Feedback Approval migration (from Admin Portal to Elder Portal) | Phase 2 |
| **Profile** | Memories Playback | Recordings stored but playback deferred | Phase 2 |
| **Profile** | Download Recordings (MP4) | Export functionality deferred | Phase 2 |
| **Marketing** | Marketing Landing Page | Single-page signup form with bot prevention | MVP |
| **Admin** | Goal-Specific Feed Curation | Basic Feed without goal filtering | Phase 2 |
| **Feed** | Feed Content Ordering/Scheduling | Reorder posts or schedule publish dates; content calendar | Phase 2 |
| **Feed** | UGC Consent Flow | Opt-in/consent before admin publishes user content | Phase 2 |
| **Gamification** | XP for Liking Feed Posts | Admin-configurable; disabled in MVP | Phase 2 |
| **Gamification** | XP for UGC Likes (when others like user's content) | Admin-configurable; disabled in MVP | Phase 2 |
| **Admin** | Elder Management | Depends on Elder feature | Phase 2 |
| **Platform** | Native Mobile Apps | Web-first approach | Phase 3+ |
| **Social** | In-App Circle Communication | Real-time chat deferred | Phase 3 |
| **Content** | Level 2 Advanced Content | Post-70 day feature | Phase 3 |
| **Content** | Refresher Challenges | Post-completion feature | Phase 3 |
| **Rewards** | Physical Totems | Logistics complexity | Phase 3 |
| **Content** | Full 70 days at launch | Rolling delivery model | Ongoing |
| **Platform** | Multi-language Support | English only MVP | Phase 2+ |

**Future-Ready Architecture:** User model stores goal fields (not used for personalization in MVP). Response recordings stored for future Memories/Elder. XP admin-configurable (no code changes). Feed supports goal-based filtering (disabled in MVP). Status 2 auto-granted for "Join with Friends." Block-based lesson architecture supports extensible content types.

### Document Structure (Compartmentalized PRDs)

This PRD is the **master document** containing all LegacyVoice requirements. Specialized PRDs copy area-specific requirements for compartmentalized verification:

| Document | Location | Covers | Use when |
|----------|----------|--------|----------|
| **Main PRD** (this document) | `discovery-docs/prd.md` | Full scope, all BRs, NFRs, rules, glossary | Authoritative reference; cross-area context |
| **Main App PRD** | `discovery-docs/prd-main-app.md` | Learner app: onboarding, lessons, Feed, profile, XP/streak, circles (user-facing), celebrations, alpha/beta feedback | Verifying or updating main app behavior and BRs |
| **FamilyElder Portal PRD** | `discovery-docs/prd-familyelder-portal.md` | Elder portal (Phase 2): Elder feedback, AI approval workflow migration | Verifying or updating Elder portal behavior |
| **Admin Portal PRD** | `discovery-docs/prd-admin-portal.md` | Admin panel: CMS, users, signup queue, feedback review, circles, celebrations, exports | Verifying or updating admin workflows and BRs |
| **Marketing Page PRD** | `discovery-docs/prd-marketing-page.md` | Marketing landing page (static), redirect flow, handoff to app | Verifying or updating marketing/landing scope and BRs |

**Update rule:** When changing requirements, update the **main PRD** (`prd.md`) and the **relevant specialized PRD(s)** so both humans and AI can rely on either the master or the compartmentalized doc.

### Related Documents

| Document | Location | Relationship |
|----------|----------|--------------|
| Blueprint | `clients/sonny/legacyvoice/discovery-docs/blueprint.md` | Strategic foundation |
| Lo-Fi Wireframes | `clients/sonny/legacyvoice/discovery-docs/lofi-ux.md` | Screen specifications |
| Client Questions | `clients/sonny/legacyvoice/discovery-docs/client-questions.md` | Open questions for client |
| Glossary | `clients/sonny/legacyvoice/discovery-docs/glossary.md` | Term definitions |

---

## Business Context

### Background / Current State

Storytelling is treated as innate rather than learnable; no rigorous programs teach it as daily practice. The client developed a curriculum for daily micro-learning, inspired by Duolingo, Wordle, Strava.

**Reference Product:** Legends (buildlegends.com)—architectural and UX reference. LegacyVoice borrows Legends patterns, adds engagement features (XP, status, social).

### Problem Statement

> Adults who want to improve their storytelling skills need a way to practice consistently because storytelling is treated as an innate talent rather than a learnable skill. Currently, there are no rigorous programs that train storytelling systematically.

**Key Problem Elements (Client's Words):**
- "We've assumed some people 'are just good storytellers' - as if it's a trait you're born with"
- "There are no rigorous programs that train storytelling at all"
- "Your story is too important to let someone else tell. (not lack of will, lack of skill)"

### Business Objectives

| ID | Objective | Measurement |
|----|-----------|-------------|
| OBJ-01 | Validate 70-day storytelling program concept | Testable MVP with 7-10 days of content |
| OBJ-02 | Create habit-forming daily engagement | Streak completion rates, daily session participation |
| OBJ-03 | Build social accountability through circles | Circle participation, peer engagement |
| OBJ-04 | Test gamification as engagement driver | XP accumulation, status progression rates |

### Success Metrics

| Metric | Target | Measurement Method | Timeline | Owner |
|--------|--------|-------------------|----------|-------|
| Testable Content | 7-10 days complete | Content delivery | Phase 1 (Jan-Mar) | Client (the content team) |
| Daily Completion Rate | TBD% (baseline post-launch) | Analytics dashboard | Post-launch baseline | Client + The Contractor PM |
| Average Streak Length | TBD days (baseline post-launch) | Streak tracking | Post-launch baseline | Client + The Contractor PM |
| Status 1 Progression | TBD% of users (baseline post-launch) | Day/Status tracking | Post-launch baseline | Client + The Contractor PM |
| User Retention (Day 7) | TBD% (baseline post-launch) | Cohort analysis | Post-launch baseline | Client + The Contractor PM |

*Note: Specific numeric targets will be established post-launch based on baseline data. Pre-launch targets TBD by Client + The Contractor PM before TRD completion.*

---

## Users & Personas

| Persona | Description | Goals | Pain Points |
|---------|-------------|-------|-------------|
| **New User** | Adult who just signed up (Day 1-7) | Learn the system, build initial habit | Needs guidance, unfamiliar with format |
| **Active User** | User on Day 8-49, maintaining streak | Improve storytelling skills, stay consistent | May struggle with daily commitment |
| **Power User** | User on Day 50+, high XP, potential Elder | Master storytelling, help others | Wants advanced content, recognition |
| **Lapsed User** | User who broke streak, returning | Get back on track | Needs motivation, may feel discouraged |

### Key Actors

| Actor | Description |
|-------|-------------|
| **User** | Adult learner going through the 70-day storytelling program |
| **Coach Devon** | AI coach persona - high-energy, DJ-style digital instructor who guides lessons |
| **Story Elder** | External storytelling professional who provides goal-matched feedback (Phase 2) |
| **Admin** | Client team member managing content and users via admin panel |

---

## Product Requirements

### BR-01: User Onboarding

**Priority:** Critical
**Persona:** New User

**Description:** Multi-step onboarding flow collecting user info, preferences, and introducing Coach Devon. Onboarding initializes on the marketing page and continues in the app through a waitlist registration flow, followed by admin approval and magic link access.

**Onboarding Flow Overview:**

| Step | Location | User Action | System Action |
|------|----------|-------------|---------------|
| 1 | Marketing page | Sees "Register for Waitlist" (or equivalent) button | — |
| 2 | App (redirect) | Clicks button → lands on app at `app.legacyvoice.com/register` | Redirect from marketing page |
| 3 | App | Fills out initial registration questions (name, email, how you heard about it, etc.) | — |
| 4 | App | Submits form | Request sent to admin team; user sees "Thanks for joining the waitlist!" |
| 5 | Admin Portal | — | Admin reviews waitlist, approves request |
| 6 | App (via magic link) | Receives magic link via SMS, clicks to access | User gains access; completes full onboarding (phone verification, goals, schedule, Coach Devon); Day 0 + Day 1 |

**Business Value:** First impression, personalization data, trigger schedule setup.

**User Story:** As a new user, I want to sign up quickly and set preferences so I can start my storytelling journey at a time that works for me.

**Acceptance Criteria:**
- [ ] User can enter phone number and verify via SMS code
- [ ] User can enter name and email
- [ ] User can set display name ("How you want your name to appear") - optional, defaults to full name
- [ ] ~~User can select avatar from predefined options~~ [DEFERRED TO PHASE 2]
- [ ] User can select storytelling goals ("click all that apply" format)
- [ ] Optional details field available per selected goal
- [ ] Goal selection UI explains: "This will help us match you with like-minded people and experts!"
- [ ] User asked: "Do you have people you want to go on this journey with?" (Join with Friends)
  - If Yes (2-3 friends): User can invite friends/provide contacts for private circle
  - If Yes (team/company): Show "Contact Admin" instead of "Invite your people"; user indicates interest → email sent to Admin → Admin handles manually. Optionally: shareable link to info page for team signups
  - If No: User starts solo (assigned to goal-based circle by admin later)
- [ ] Users who join with friends receive auto-Status 2 ("Better with Friends" benefit)
- [ ] User can set SMS trigger schedule (days, time, timezone)
- [ ] Time selection uses 15-minute intervals (e.g., 9:00, 9:15, 9:30, 9:45) - aligns with Legends behavior and simplifies backend cron job implementation
- [ ] User timezone editable in settings; changes apply to future triggers only (not retroactive)
- [ ] Streak window calculated in user's current timezone setting
- [ ] **Timezone verification for notifications:** When user selects a time (lesson reminder or snooze), the system MUST resolve the user's timezone to schedule delivery correctly. Users are globally located; all notifications MUST be delivered in the user's local time. System uses stored timezone preference; device/browser timezone as fallback if needed.
- [ ] User sees welcome video from Coach Devon
- [ ] Marketing landing page created (single page, purposely vague - no team/founder info); **static only (HTML/CSS, no logic, no forms)**
- [ ] Landing page structure: Hero ("Tell better stories"), three core features block, "Better with friends" section
- [ ] **Register for Waitlist button (marketing page):** Primary CTA; redirects to `app.legacyvoice.com/register`
- [ ] **Waitlist registration (in app):** User arrives via redirect from marketing page, fills initial registration questions: name, email, **"how you heard about it"** (mandatory, anti-bot), goals (optional), reminder time (optional)
- [ ] After form submit, user sees: "Thanks for joining the waitlist! We'll get back to you shortly"
- [ ] **Request sent to admin:** Form submission creates waitlist entry; admin team receives dashboard notification AND Slack message (Slack is notification only; approval happens in Admin Portal or Airtable if configured)
- [ ] Admin Panel shows pending approvals count badge on signup queue
- [ ] Admin reviews waitlist and moves users up/down priority (not binary approve/reject)
- [ ] Admin can add notes to waitlist entries
- [ ] Admin dashboard flags users who reach point thresholds but haven't been assigned to circles
- [ ] Target approval turnaround: within 1 business day
- [ ] Upon approval: User receives magic link via SMS
- [ ] Upon approval: User sees Day 0 content (orientation delivered by Coach Devon - how app works, layout)
- [ ] Day 0 may or may not include name personalization (TBD)
- [ ] Day 1 immediately follows Day 0 (no gap)
- [ ] "Tips and tricks" email triggered simultaneously upon approval
- [ ] User can start first lesson immediately or snooze to scheduled time

**Business Rules:**
- Phone verification required before proceeding
- Email collected but not verified in MVP
- Goals CANNOT be edited after onboarding
- All other settings (time, name, display name) can be edited later
- Avatar selection deferred to Phase 2
- ONB-R01: No Stripe payment in MVP - manual approval gate instead
- ONB-R02: User cannot access lessons until admin approves

**Phase 2 Preparation:** Goal data stored for future personalization (Circles, Elders, Feed). Mailing address added when physical totems introduced.

**Goal Options:**
| Goal | Target Audience |
|------|-----------------|
| Application Storytelling | Job applicants |
| Personal Storytelling (Relationships) | Relationships & dating |
| Marketing Storytelling | Marketers |
| Vision Storytelling | Startup Founders |
| Leadership Storytelling | CEOs or Partners |
| Student Storytelling | School applications |
| Personal Storytelling (Confidence) | Personal confidence |
| Other | Free text input for custom goals |

**Goal Selection Requirements:**
- Goals must be selected in **ranked order** (user prioritizes their goals)
- **Maximum 3 goals** can be selected
- "Other" option available with free text input field
- Multiple goals can be selected ("click all that apply")
- **Primary goal** (first ranked) used for circle assignment and personalization
- Secondary/tertiary goals stored for analytics/marketing but not actively used in MVP

**Goal Usage (MVP):**
- Pre-recorded content: Same for all users (linear curriculum)
- Analytics: Goals stored for marketing/acquisition reports
- *Phase 2: Feed personalization, Circle/Elder matching based on goals*

**Access Control:** No Stripe in MVP. Marketing page: static only (HTML/CSS); Register for Waitlist button redirects to app. Waitlist registration at `app.legacyvoice.com/register` requires "how you heard about it" (anti-bot). Admin Portal waitlist (move up/down; Airtable alternative if client prefers). Slack: notification only; approval in Admin Portal. Flow: Marketing page (waitlist CTA) → Redirect to app → User fills initial registration questions → Request sent to admin → Admin approves in Portal → User receives magic link → Day 0 + Day 1 access. Stripe replaces manual gate in Phase 2.

**Day 0 Content:** Coach Devon orientation (how app works, layout, navigation). Day 1 follows immediately. "Tips and tricks" email sent upon approval.

**Open Questions:**
- FEED-01: Clarify how Feed operates and what information is exhibited (Owner: Client)

**Dependencies:**
- Depends on: None (entry point)
- Blocking: BR-02, BR-04

---

### BR-02: Daily Lesson Delivery

**Priority:** Critical
**Persona:** All Users

**Description:** Daily lesson: Pre-Lesson (Gen AI via Eleven Labs), Direct Instruction (karaoke captions), Q&A, Challenge, Post-Lesson (Gen AI via Eleven Labs). Direct Instruction and Challenge from client via Admin Panel; Pre/Post personalization system-generated.

**Business Value:** Core learning experience; delivers curriculum, captures practice responses.

**User Story:** As a user, I want to receive my daily lesson at my scheduled time so I can build a consistent storytelling practice habit.

**Acceptance Criteria:**
- [ ] User receives magic link at scheduled time (SMS)
- [ ] Magic link is single-use, expires after 24 hours if not clicked
- [ ] Clicking link opens web app with authenticated session
- [ ] Authenticated session persists (duration TBD in TRD); user can return to app without new link if session valid
- [ ] If session expired, user must request new magic link via SMS
- [ ] Pre-Lesson plays Gen AI personalized intro (via Eleven Labs) with user name, day, streak
- [ ] Optional personalization block may appear between Direct Instruction and Q&A (small transition: "Hey [Name], now we're going to talk about this thing")
- [ ] Direct Instruction plays main lesson video (~5 minutes) with karaoke-style captions
- [ ] Q&A presents interactive questions requiring user response (text, audio, or closed answers)
- [ ] Privacy notice shown before FIRST recording only
- [ ] User can retry recording before submitting
- [ ] Challenge presents exercise that can be completed or snoozed
- [ ] When user snoozes Challenge, UI shows: "Remind me later" → If yes, then "When?" (time selection)
- [ ] Snooze reminder sent at user-selected time (admin-configured default: 24 hours later)
- [ ] Snooze reminder delivered via SMS magic link (same format as daily lesson trigger)
- [ ] Snooze time interpreted in user's timezone: when user selects a time for snooze, system MUST use user's timezone to set the delivery timer (users are globally located)
- [ ] Snoozed challenges accessible from: Snooze SMS link, user inbox, or user admin panel
- [ ] Users can complete multiple snoozed challenges later (e.g., "do five challenges over the weekend")
- [ ] Post-Lesson plays Gen AI personalized wrap-up (via Eleven Labs) with progress, streak, feedback info
- [ ] Completing Q&A awards base XP (1 XP) and credits streak (all users)
- [ ] Completing Challenge awards bonus XP (2 additional XP) (all users)
- [ ] Total lesson XP = Base XP (1) + Bonus XP (2) = 3 XP per day (or potentially 4 XP - TBD)
- [ ] Status 0 users see: "Great job! Your response has been saved. Complete more lessons to unlock AI feedback!" (XP and streak update visibly)
- [ ] Status 1+ users receive AI feedback weekly via in-app inbox (not immediately; see BR-07B)
- [ ] User navigates to Feed upon completion

**Business Rules:**
- LES-R01: Next day's session unlocks after current day's Q&A completion
- LES-R01A: One lesson per day (default behavior)
- LES-R01B: Lesson unlocks at 12:01am user timezone on next day after completion
- LES-R01C: Admin can enable sequential unlock mode for specific users, bypassing daily restrictions. When enabled, users can complete multiple lessons per day and next lesson unlocks immediately after Q&A completion
- LES-R02: Completing Q&A = base XP (1 XP) - minimum to maintain streak
- LES-R03: Completing Challenge = bonus XP (2 additional XP)
- LES-R03A: Total lesson XP = Base XP (1) + Bonus XP (2) = 3 XP per day (or potentially 4 XP - TBD)
- LES-R03B: XP terminology simplified - just "points", no "partial/full XP" distinction
- LES-R04: Streak credited upon Q&A completion (base XP earned)
- LES-R05: Snoozed challenge triggers reminder at user-selected time (default: 24 hours later, customizable during snooze action)
- LES-R05A: Snooze reminder delivered via SMS magic link (same format as daily lesson trigger)
- LES-R05B: All notifications (lesson triggers, snooze reminders) MUST be scheduled and delivered in the user's local time. System MUST resolve user timezone (from stored preference, or device/browser as fallback) when scheduling any notification, since users are globally located.
- LES-R06: Users cannot complete multiple lessons in one day
- LES-R07: Dynamic trigger message variants based on streak, status, missed days
- LES-R08: Maximum 1 follow-up message (4 hours after initial)
- LES-R09: Response limits per question: Text 2000 characters, Audio 120 seconds. Each question has independent limits.
- LES-R10: Response input types: Text, Audio, Multiple Choice, Image Upload, Video Upload, Audio Upload
- LES-R10A: Number of questions per lesson is flexible (configurable by admin per lesson)
- LES-R10B: MCQ fully configurable: admin sets number of options and single/multiple correct answers
- LES-R10C: Text response length configurable with presets (short/medium/long)
- LES-R10D: Q&A questions appear AFTER Direct Instruction video (not during)
- LES-R10E: Audio prompt signals start of Q&A section
- LES-R11: Magic link delivered via SMS (primary); email fallback if SMS delivery fails
- LES-R12: Users can access lesson at any time after it unlocks (scheduled time or earlier). Magic link works immediately upon unlock. No restriction on accessing lesson before scheduled time.
- LES-R13: SMS trigger time selection uses 15-minute intervals (e.g., 9:00, 9:15, 9:30, 9:45) - consistent with Legends app behavior

**Lesson Structure (MVP) - Block-Based Architecture:**
Lessons are built from **blocks** arranged in a timeline/sequence via CMS:

| Block Type | Content Source | Required? | Notes |
|------------|----------------|-----------|-------|
| Pre-Lesson Personalization | GEN AI (Eleven Labs) | Yes | Always at introduction - personalized greeting with user name, day, streak |
| Direct Instruction | CLIENT-PROVIDED (video) | Yes | Main lesson content with karaoke-style captions |
| Optional Personalization | GEN AI (Eleven Labs) | No | Small transition block between Direct Instruction and Q&A ("Hey [Name], now we're going to talk about this") |
| Q&A | CLIENT-PROVIDED (question prompts) | Yes | Text/audio/MCQ responses; questions shown after video |
| Challenge | CLIENT-PROVIDED (prompt) | Yes | Extended exercise, same for all users |
| Post-Lesson Wrap-up | GEN AI (Eleven Labs) | Yes | Personalized wrap-up with progress, streak, feedback info |

**CMS Block Builder:** Admin creates day → configures settings → adds blocks via plus → configures each (duration, background, content) → reorders drag-and-drop → previews sequence → saves draft → publishes. Blocks extensible for future content types.

**Personalization Block (Pre-Lesson, Optional, Post-Lesson):**
- **Background:** Personalization block MUST support background configuration (upload looping video). Background SHOULD match the main Direct Instruction video for visual consistency. Admin can upload a looping video as background.
- **Dynamic visual layer (optional):** Personalization block MAY include a dynamic visual layer (blob or waveform). When present, the visual MUST be synced with the 11 Labs voice playback. Implementation options: (a) video layer with waveform baked in, or (b) CSS-animated blob + audio-driven waveform (POC recommended). Optional configuration: select blob/waveform style per block.
- **Karaoke-style captions:** Active word highlighted (e.g., white); upcoming words darker or ~50% opacity. Applies to Personalization block (auto-generated from 11 Labs) and Direct Instruction (baked into uploaded video). Reference: Client to provide sample video for caption style.

**Content Sources (MVP):** Client-Provided (the client/Client via Admin): all video, Q&A prompts, Challenge prompts, Feed content.

**MVP Features (Client Confirmed):** Pre/Post Gen AI via Eleven Labs (name, day, streak); karaoke captions; dynamic message variants (streak, status, missed days) for SMS and email.

**Open Questions:** 7.1: XP values per action—deferred to TRD (admin configurable).

**Re-engagement Message Schedule:**
| Days Inactive | Message Type |
|---------------|--------------|
| Day 1 | First reminder |
| Day 2 | Second reminder |
| Day 3 | Third reminder |
| Day 4 | Fourth reminder |
| Day 7 | Week reminder |
| Day 10 | Ten-day reminder |
| Day 15 | Final reminder |

*Note: Day spacing and message content are variable and configurable by admin.*

**Lesson Unlock Logic:** One lesson per day (default). Unlock at 12:01am user timezone day after Q&A (e.g., Day 2 Q&A 10:15am 5/1 → Day 3 unlocks 12:01am 5/2). SMS magic link at user's reminder time. Incomplete Q&A = next day locked. **Sequential Unlock Override:** Admin can enable per user; bypasses daily restriction—users complete multiple lessons per day, next unlocks immediately after Q&A (see LES-R01C).

**Dependencies:**
- Depends on: BR-01 (user must be registered)
- Blocking: BR-04, BR-05, BR-06

---

### BR-03: Daily Review Session [DEFERRED TO PHASE 2]

**Status:** Deferred to Phase 2

**Summary:**
Evening reinforcement session with spaced repetition Q&A. Includes welcome back video (A4), day recap (A5), and retention questions. Awards bonus XP but does not affect streak.

**Rationale for Deferral:**
- Focus on validating core lesson flow first
- Reduces MVP complexity (single daily touchpoint)
- Review content requires additional production from client team

**Phase 2 Implementation Notes:**
- Review trigger sent 8 hours after Lesson completion
- Optional for streak (only Lesson Q&A required)
- Snoozed challenges can be completed during Review
- Gen AI personalization for A4 welcome back video


---

### BR-04: XP and Status System

**Priority:** High
**Persona:** All Users

**Description:** Users progress through status levels (0–3) based on XP earned. Actions earn XP; reaching thresholds unlocks status levels.

**Business Value:** Gamification drives engagement; XP-based status rewards participation and unlocks features.

**User Story:** As a user, I want to earn XP and unlock higher status levels so I feel rewarded and gain access to premium features.

**Acceptance Criteria:**
- [ ] XP awarded for: Lesson Q&A completion (base XP: 1), Challenge completion (bonus XP: 2)
- [ ] XP values admin-configurable in Admin Panel (not hardcoded)
- [ ] XP terminology: Just "points" - no "partial XP" or "full XP" distinction
- [ ] Status levels based on XP THRESHOLDS (admin-configurable):
  - Status 0: Starting level (0 XP)
  - Status 1: XP threshold TBD (Owner: Client + The Contractor PM, Timeline: Before TRD) - unlocks AI Feedback
  - Status 2: XP threshold TBD (Owner: Client + The Contractor PM, Timeline: Before TRD) - unlocks Story Circles (also auto-granted to users who "Join with Friends")
  - Status 3: XP threshold TBD (Owner: Client + The Contractor PM, Timeline: Before TRD) - *MVP: Pause Tokens (+3 tokens)* | *Phase 2: Priority Elder Feedback*
- [ ] Status is PERMANENT once earned (cannot be lost)
- [ ] Admin can override status for any user
- [ ] Status displayed in user profile and leaderboard

**Business Rules:**
- XP-R01: XP can be earned but not lost
- XP-R02: Status is PERMANENT once earned
- XP-R03: Admin can manually assign any status
- XP-R04: Status is XP-BASED (user actions earn XP toward thresholds)
- XP-R05: XP used for BOTH status progression AND leaderboard ranking

**Phase 2 Preparation:** Status unlocks future features (Circles at Status 2, Elder priority at Status 3). XP admin-configurable (no code changes). "Join with Friends" auto-Status 2 (critical for acquisition).

**Open Questions:**
- 7.1: What are the initial XP values and thresholds for each action/status? (Owner: Client + The Contractor PM, Timeline: Before TRD - admin-configurable in MVP)

---

### BR-05: Streak Tracking

**Priority:** High
**Persona:** All Users

**Description:** Track consecutive days of lesson completion. Streak resets to 0 if user misses a day.

**Business Value:** Proven engagement mechanic; daily habit loop and loss aversion.

**User Story:** As a user, I want to see my streak count so I'm motivated to maintain my daily practice.

**Acceptance Criteria:**
- [ ] Streak count displayed throughout experience (Feed, Profile, Learn tab)
- [ ] Streak increments when daily lesson Q&A is completed
- [ ] 24-hour window to complete lesson without breaking streak (midnight user timezone)
- [ ] Pause token system: All users start with 3 pause tokens
- [ ] If user misses a day and has pause tokens: Token automatically consumed, streak preserved, no XP awarded
- [ ] If user misses a day and has no pause tokens: Streak resets to 0
- [ ] Token earning: Status 1 (+1 token), Status 2 (+2 tokens), Status 3 (+3 tokens)
- [ ] Token count displayed in user profile alongside streak
- [ ] When streak resets (no tokens), user sees message on Feed: "Your streak has reset. Start a new one today!"
- [ ] Streak count visible on user profile and leaderboard

**Business Rules:**
- STR-R01: Streak credited upon partial completion (Q&A done)
- STR-R02: 24-hour window resets at midnight user's current timezone setting
- STR-R03: If user misses a day and has pause tokens: Token automatically consumed, streak preserved, no XP awarded
- STR-R03A: If user misses a day and has no pause tokens: Streak resets to 0
- STR-R04: When streak resets, user sees re-engagement message on Feed upon next app open
- STR-R05: User timezone editable in settings; timezone changes apply to future triggers and streak windows only (not retroactive)

**Phase 2 Features:**
- Streak milestone badges (7, 14, 30, 50, 70 days)
- Advanced token features (token purchase, expiration, gifting)

---

### BR-06: Leaderboards

**Priority:** Medium
**Persona:** Active Users, Power Users

**Description:** Display leaderboards by streak length and XP.

**Business Value:** Social competition drives engagement; visible progress motivates users.

**User Story:** As a user, I want to see how I rank so I'm motivated to improve.

**Acceptance Criteria:**
- [ ] Two leaderboard types: Global leaderboard (all users) and Circle leaderboard (if user is in a circle)
- [ ] Leaderboard metric: Streaks (for MVP simplicity; XP terminology may be confusing)
- [ ] Always show top 5 users on each leaderboard (default view)
- [ ] If user is in top 5: User's position is highlighted within the top 5 list
- [ ] If user is not in top 5: Show top 5 users + user's position displayed below (e.g., "You are #12")
- [ ] **Top 10 table view:** Option to view top 10 users (button or toggle to switch from avatar/card view to table view)
- [ ] Leaderboards appear on Feed screen
- [ ] Leaderboards update periodically (not real-time in MVP)
- [ ] Reference apps for UX: Nike Run Club, Oura Ring, Fitbit, Calm, Headspace, Duolingo

**Phase 2 Features:**
- Horizontal scroll/swipe for multiple circle leaderboards
- Real-time leaderboard updates

---

### BR-07: Story Elders Feedback System [DEFERRED TO PHASE 2]

**Status:** Deferred to Phase 2

**Summary:**
Human expert feedback from external storytelling professionals. Elders are matched to users by goal expertise and provide written feedback on Q&A and Challenge responses. Includes dedicated Elder Dashboard with goal-filtered submission pools.

**Rationale for Deferral:**
- Requires Elder portal development (separate from user app)
- Needs Elder onboarding and account management
- Goal matching and submission queue system adds complexity
- MVP focuses on AI feedback first; Elder feedback adds human touch in Phase 2

**Phase 2 Implementation Notes:**

**Elder Portal Features:**

1. **Elder Feedback (Direct Evaluation):**
   - Elders evaluate user responses directly (client-requested evaluations)
   - Submission queue filtered by Elder's goal expertise
   - Feedback submission interface for writing direct feedback
   - Written text feedback (1-2 sentences to paragraph)
   - Priority queue for Status 3 users
   - No SLA - feedback delivered whenever Elders have time

2. **AI Feedback Approval (Migration from Admin Portal):**
   - Elders approve AI-generated feedbacks before sending to users (replaces Admin approval workflow)
   - Review interface shows AI draft feedback with approve/edit/reject options
   - Admin Portal feedback review queue transitions to Elder Portal
   - Same approval workflow as MVP Admin Portal, but executed by Elders

**Elder Portal Infrastructure:**
- **Dedicated Elder Portal** — separate from user app with:
  - Submission queue filtered by Elder's goal expertise
  - Feedback submission interface (for direct Elder feedback)
  - AI feedback approval interface (for AI approval workflow)
  - Simple analytics dashboard
- **Elder Onboarding** — Admin creates Elder accounts, assigns goal expertise, sends magic link
- **Submission Assignment** — Hybrid model:
  - Primary: Elders see goal-filtered queue and self-select submissions
  - Secondary: Admin can manually assign specific submissions
- Unified inbox with AI feedback (users see both Elder feedback and approved AI feedback)

**MVP Preparation:**
- User responses are stored and available for future Elder review
- Goal data captured during onboarding for future matching
- Inbox infrastructure built for AI feedback can be extended to Elder feedback


---

### BR-07B: AI Feedback Approval

**Priority:** High
**Persona:** Status 1+ Users, Admin

**Description:** Status 1+ users receive AI-generated grading on Q&A and Challenge responses. AI generates draft feedback asynchronously after submission. **MVP:** Admin approves all AI feedback via Admin Panel before delivery. **Phase 2:** Workflow migrates to Elder Portal (Elders approve). Approved feedback delivered weekly (batched), not immediately.

**Business Value:** Scalable AI feedback with human oversight for quality. MVP: Admin Portal; Phase 2: Elder Portal.

**User Story:**
As a user who completed lessons, I want to receive curated AI feedback weekly so that I can reflect on my progress in a dedicated feedback moment.

**Admin User Story:**
As an admin, I want to review and approve AI-generated feedback so that I can ensure quality before users receive it.

**Acceptance Criteria:**

**AI Feedback Generation:**
- [ ] AI feedback available for Status 1+ users only
- [ ] Status 0 users see: "Great job! Your response has been saved. Complete more lessons to unlock AI feedback!" (XP and streak update visibly, but no AI evaluation)
- [ ] Status 0 user responses are stored and available for AI feedback when they reach Status 1
- [ ] System transcribes audio responses to text (speech-to-text) for AI processing
- [ ] AI evaluates Q&A responses for correctness (pass/fail or comprehension score 0-100%)
- [ ] AI evaluates Challenge responses with structured scores (structure, emotion, clarity, relevance, each 1-5) + written explanation paragraph
- [ ] AI feedback generated asynchronously after user submission (background processing)
- [ ] If AI generation fails, submission still appears in admin queue (marked as "AI unavailable")
- [ ] System retries AI generation up to 3 times on failure; admin notified if all retries fail

**Admin Feedback Review Queue:**
- [ ] New section in Admin Panel: "Feedback Review"
- [ ] Queue displays all submissions with AI-generated feedback pending approval
- [ ] Queue sortable by: submission date, user status, lesson day
- [ ] Queue filterable by: submission type (Q&A/Challenge), status (pending/approved)
- [ ] Admin can click to review a submission
- [ ] No locking mechanism (multiple admins can work simultaneously)
- [ ] Admin dashboard shows pending feedback count
- [ ] Alert if pending queue exceeds threshold (e.g., >50 pending)

**Admin Review Interface:**
- [ ] Admin sees user info: name, email, current day, goal
- [ ] Admin sees original question/challenge prompt
- [ ] Admin sees user response (text or transcribed audio)
- [ ] For audio: Admin can play original recording
- [ ] Admin sees AI-generated feedback (scores + written feedback)
- [ ] For Q&A: Admin sees AI correctness evaluation (pass/fail or score)
- [ ] For Challenges: Admin sees AI scores (structure, emotion, clarity, relevance) and written explanation
- [ ] Admin can approve AI feedback as-is
- [ ] Admin can edit AI feedback before approving
- [ ] Admin can reject AI feedback and write entirely new feedback
- [ ] **"Reject & Regenerate" button:** Trigger AI to generate new feedback (no manual write required)
- [ ] Upon approval, feedback is sent to user
- [ ] System tracks: original AI feedback, admin edits, final approved version, regeneration attempts (align with TRD max 3 retries)

**User App - Feedback Delivery:**
- [ ] Approved feedback delivered WEEKLY (batched) via in-app inbox and/or email
- [ ] Delivery frequency configurable by admin at system/circle/user level (default: weekly)
- [ ] For Q&A: Display correctness result (pass/fail or score)
- [ ] For Challenges: Display structured scores (structure, emotion, clarity, relevance)
- [ ] For Challenges: Display written feedback paragraph
- [ ] All feedback stored persistently in user account
- [ ] User can view historical feedback in Profile > Feedback History
- [ ] Each feedback entry shows: date received, associated lesson day, feedback content
- [ ] Visual notification indicator when new feedback is available

**AI Evaluation Criteria:**

**Q&A Responses:**
```
Input: Question prompt + correct answer (from admin) + user response
Output:
- Correctness: Pass/Fail OR score (0-100%)
- Brief explanation (optional): Why correct/incorrect
```

**Challenge Responses:**
```
Input: Challenge prompt + grading rubric (from admin) + user response
Output:
- Structure score (1-5): How well organized is the story?
- Emotion score (1-5): How emotionally engaging is it?
- Clarity score (1-5): How clear and understandable?
- Relevance score (1-5): How relevant to the challenge prompt?
- Written feedback (1-3 paragraphs): Holistic feedback with specific suggestions
```

**Technical Components:**
- Speech-to-Text Service: Transcribe audio responses (Whisper API or similar)
- Q&A Evaluation Prompt: GPT-4 prompt for correctness evaluation
- Challenge Evaluation Prompt: GPT-4 prompt for structured scoring + explanation
- Async Processing Queue: Background job for AI evaluation
- AI Feedback Storage: Store AI drafts separately from final feedback

**Business Rules:**
- AI-R01: Status 0 users see completion message with XP/streak updates visible, but no AI evaluation - responses stored for future feedback
- AI-R02: AI feedback requires admin approval before being shown to users
- AI-R03: Approved feedback delivered weekly (batched), not immediately
- AI-R04: All feedback stored persistently for user reference
- AI-R05: Audio responses transcribed to text for evaluation (speech-to-text)
- AI-R06: If AI feedback generation fails, system retries up to 3 times; admin notified if all fail
- AI-R07: Feedback delivery frequency configurable at system/circle/user level (default: weekly)
- AI-R08: Admin can approve, edit, or reject AI feedback
- AI-R09: System tracks AI draft, admin edits, and final approved version
- AI-R10: Multiple admins can review simultaneously (no locking mechanism)

**UX Design Rationale:** Feedback intentionally batched to keep user flow quick ("in and out"—few minutes/day). Batching creates anticipation and dedicated "feedback moment." Applies to ALL response types (no MCQ exceptions). Admin approval ensures quality; AI handles evaluation.

**Dependencies:**
- AI provider selection (OpenAI GPT-4, Claude, etc.) - Owner: The Contractor
- Speech-to-text provider (Whisper, etc.) - Owner: The Contractor
- Grading rubric per Challenge - Owner: Client
- Q&A correct answers - Owner: Client
- Admin team bandwidth for review - Owner: Client

**Effort Estimation:**
- Speech-to-Text Integration: 1 day
- AI Evaluation Prompts: 1.5-2 days
- Async Processing Queue: 1 day
- Admin Feedback Queue (2 screens): 1.5-2 days
- User Feedback Delivery: 0.5-1 day
- AI Feedback Storage: 0.5 day
- Testing & QA: 1.5-2 days
- **Total: 7-9 days (~1-1.5 weeks)**

**Phase 2 Enhancement:**
- **AI Feedback Approval Migration:** Approval workflow migrates from Admin Portal to Elder Portal - Elders approve AI-generated feedbacks before sending to users (replaces Admin approval)
- Unified inbox with Elder feedback (see BR-07)
- In-app toast/badge notifications

---

### BR-08: Story Circles

**Priority:** High
**Persona:** All Users

**Description:** Social cohort groups where users learn alongside peers with similar goals. Admin-controlled in MVP (no automatic matching). Critical for product-led growth via invitations.

**Business Value:** Social accountability drives engagement; invitations enable product-led growth.

**User Story:** As a user, I want to be part of a Story Circle so I can learn alongside others and stay accountable.

**Acceptance Criteria:**
- [ ] Users asked at signup: "Do you have people you want to go on this journey with?"
- [ ] Private circles: Available from Day 1 for users who invite friends
- [ ] Users who join with friends receive auto-Status 2 ("Better with Friends" benefit)
- [ ] Goal-based circles: Admins manually assign users to circles based on primary goal
- [ ] Circle assignment is 100% manual in MVP (no automatic algorithm)
- [ ] Admin assigns users based on: Primary goal, Number of points/status reached, Group requests (team signups)
- [ ] Seven default circles exist (one per goal type) + ability to create custom circles (e.g., The Contractor team circle)
- [ ] Group signup flow: When user wants team/company experience, show "Contact Admin" — user indicates interest → email sent to Admin → Admin handles manually. Optionally: shareable link to info page for team signups
- [ ] Circle assignment timing: Configurable by admin (considering Day 3-5)
- [ ] No limit on number of circles a user can belong to (admin-controlled)
- [ ] Circle leaderboards show member rankings (streak - for MVP simplicity)
- [ ] WhatsApp used for circle communication (in-app chat is Phase 3)

**Circle Types:**
| Type | Access | Assignment |
|------|--------|------------|
| Private/Friend Circles | Day 1 | User invites friends at signup |
| Goal-Based Circles | Admin assigns | Admin manually groups users by goal |

**Business Rules:**
- CIR-R01: Users who join via private circle invitation are NOT auto-assigned to goal-based circles
- CIR-R02: Users CAN belong to multiple circles (admin-controlled only)
- CIR-R03: No limit on circle membership count
- CIR-R04: Circle assignment is 100% manual in MVP (no automatic algorithm)
- CIR-R05: Circle size has no minimum or maximum limit
- CIR-R06: Admin dashboard flags users who reach point thresholds but haven't been assigned to circles (visual indicator like red highlight)

**Phase 2 Features:**
- Automatic goal-based matching algorithm
- In-app circle communication (Phase 3)

---

### BR-09: Feed and Navigation

**Priority:** High
**Persona:** All Users

**Description:** Two tabs: "Learn" (lesson pathway) and "Feed" (engagement content).

**Business Value:** Central engagement hub; shows progress, motivates between sessions.

**User Story:** As a user, I want to see my progress and engaging content so I stay motivated between lessons.

**Acceptance Criteria:**
- [ ] Two tabs: "Learn" and "Feed"
- [ ] **Default landing:** Feed tab is default homepage after lesson completion
- [ ] **Entry points:**
  - SMS magic link → Drops directly into day's lesson
  - Web app direct access → Lands on Learn tab (roadmap view)
  - After lesson completion → Lands on Feed tab
- [ ] Learn tab: 70-day roadmap/journey view (like Legends) - completed days, current day, locked days. Lessons grouped by pillar/theme (NOT by "week"); 10 groups of 7 lessons each. Labels: "Circle 1, 2, 3..." or "Story Journey 1, 2..." (avoid "Week")
- [ ] Completed days show checkmark, current day highlighted, future days locked
- [ ] Clicking locked day shows "Unlocks on Day X" message
- [ ] Clicking completed day shows completion status (playback deferred to Phase 2)
- [ ] Feed tab: Organized content feed with multiple sections
- [ ] Feed Section 1: Progress Widget (streak counter, current day, XP total, status level)
- [ ] Feed Section 2: Leaderboard Preview (top 5 users from global leaderboard + circle leaderboard if user is in circle, see BR-06)
- [ ] Feed Section 3: Content Tiles (curated content uploaded by admin)
- [ ] **Feed card layout types (admin-configurable per post):** Media + title + text; Media only; Text only; other formats as needed
- [ ] **Feed content types (MVP):**
  1. Quotes — inspirational quotes around storytelling
  2. Statistics — interesting stats about storytelling
  3. Tips and tricks — storytelling tips
  4. Announcements — admin-created functional announcements
  5. User content — manually curated user challenge responses (admin handpicks; NEVER auto-publish; user consent required before publishing—Phase 2 consent flow)
- [ ] Content displayed as tiles (Figma template style)
- [ ] Content tiles displayed in chronological order (newest first)
- [ ] **Pin option:** Admin can pin posts so they always appear at top of feed. Pinned posts override chronological order for all users. MVP: simple pin toggle per post in Admin Panel
- [ ] **Share option:** Users can share Feed content to social or by email. MVP: share globally (same content for all users; small community). Mimics Legends share behavior (social, email)
- [ ] Feed supports manual pull-to-refresh and auto-refresh on app open
- [ ] All Feed content uploaded by admin team via Admin Panel
- [ ] **Like functionality:** Users can heart/like content
- [ ] **Like visibility:** Users see if THEY liked it (not total count visible to users)
- [ ] **Admin visibility:** Admin can see total like counts per content piece
- [ ] Content shown to all users (no goal filtering in MVP — Phase 2)

**Business Rules:**
- NAV-R01: User lands on Feed after completing lesson (default landing)
- NAV-R02: Learn tab shows roadmap/journey view (like Legends) with next available lesson highlighted
- NAV-R03: All 70 days visible from Day 1 (organized by pillar/theme; 10 groups of 7 lessons; labels "Circle 1, 2, 3..." or "Story Journey 1, 2..." (avoid "Week"))
- NAV-R04: System only displays days with complete uploaded content
- NAV-R05: App URL structure: Marketing page at `legacyvoice.com`, app at `app.legacyvoice.com`

**Content Boundary Scenario:**
When user completes all available content (e.g., Day 10 done, Day 11 not yet uploaded):
- [ ] Learn tab shows completed days with checkmarks
- [ ] Day 11+ shows "Coming Soon" state (not locked icon)
- [ ] User sees message: "You're all caught up! New content is on its way."
- [ ] User can complete any snoozed challenges
- [ ] Feed remains fully accessible
- [ ] Admin notified when users reach content boundary (for prioritization)

**Phase 2 Features:**
- Memories view: playback completed challenge recordings
- Goal-specific Feed content (personalized based on user goals)
- Elder profiles in Feed

---

### BR-10: User Profile & Settings

**Priority:** Medium
**Persona:** All Users

**Description:** Profile with settings, progress display, and feedback history.

**Business Value:** Self-service, progress tracking; reduces support requests.

**User Story:** As a user, I want to view my progress and manage settings so I can track my storytelling journey.

**Acceptance Criteria:**
- [ ] Profile shows: display name (or full name if not set), streak, XP, status level, progress bar, pause token count
- [ ] Settings editable: trigger time, timezone, phone, email, name, display name
- [ ] Avatar selection available in Phase 2
- [ ] Timezone changes apply to future triggers and streak windows only (not retroactive)
- [ ] Goals NOT editable after onboarding
- [ ] Pause token count displayed prominently in profile
- [ ] Token usage history displayed in profile (when tokens were consumed)
- [ ] Feedback History section shows all AI feedback received
- [ ] Each feedback entry shows: date received, associated lesson day
- [ ] User can view historical AI feedback

**Phase 2 Features:**
- Memories section: playback completed challenge recordings
- Download recordings as MP4
- Advanced token features (token purchase, expiration, gifting)
- Unified inbox with Elder + AI feedback
- Feedback filtering and read/unread status

---

### BR-11: Admin Panel (Content Management System)

**Priority:** High
**Persona:** Admin

**Description:** Admin interface for content, users, and signup approvals. Critical for MVP rolling content delivery.

**Business Value:** Client team operates product without engineering support; supports rolling content model.

**User Story:** As an admin, I want to manage content and users so I can operate LegacyVoice and upload new days as they become available.

**Content Upload (CMS) - Block-Based Lesson Builder:**
- [ ] Day creation workflow: Admin creates new day → Configures day-level settings (name, completion requirements) → Builds lesson blocks
- [ ] Visual timeline interface with plus sign (+) to add blocks
- [ ] Block type selection menu: Intro block, Customized message block, Audio block, Video block, Content piece block, Personalization block, Direct Instruction block, Q&A block, Challenge block, Wrap-up block
- [ ] Block configuration per type:
  - [ ] Duration setting (e.g., 5 seconds for text blocks)
  - [ ] Background configuration (transparent, color, image, looping video for Personalization blocks)
  - [ ] Personalization block: Background upload (looping video); optional blob/waveform layer; background SHOULD match Direct Instruction video
  - [ ] Media selection for video/audio blocks
  - [ ] Template handlers for personalized blocks (e.g., `{username}`, `{day}`, `{streak}`)
  - [ ] Content/text input per block type
  - [ ] **Karaoke caption typeface:** Configurable per lesson (default) or globally. Personalization block captions MUST use same typeface as Direct Instruction. Default from brand guidelines; Admin can change without code changes.
- [ ] Drag-and-drop block reordering in timeline
- [ ] Block thumbnails/previews visible in timeline
- [ ] Video preview player at top of timeline showing how lesson will play sequentially
- [ ] Preview regenerates automatically when blocks are reordered
- [ ] Side panel showing block configurations and day parameters
- [ ] Save workflow: Admin saves draft → Reviews → Publishes when ready
- [ ] Set content as "ready" / "draft" status
- [ ] View all uploaded content by day number
- [ ] Edit/replace existing content
- [ ] Upload Feed content tiles (quotes, tips, stats, announcements, user content); select card layout type per post (media+title+text, media only, text only)
- [ ] Video format validation: MP4 format required, max file size TBD in TRD
- [ ] Required fields validation: All lesson components must be uploaded before day can be marked "ready"
- [ ] System only shows days with complete content to users
- [ ] Reference: Client will provide Loom video walking through current admin panel functionality

**System Configuration:**
- [ ] Configure snooze reminder time (system-wide default setting, user can override when snoozing)
- [ ] Set default reminder time (e.g., 24 hours after snooze)
- [ ] **XP Configuration:** Set XP values for actions (Q&A completion, Challenge completion)
- [ ] **XP Configuration:** Set XP thresholds for status levels (Status 1, Status 2, Status 3)
- [ ] XP configuration allows experimentation without code changes

**User Management:**
- [ ] View/search users and their status
- [ ] **Editable user info:** Admin can edit user contact info (name, email, phone, display name) from User Detail page without dev involvement
- [ ] Override user status manually
- [ ] **Sequential Unlock Override:** Admin can enable sequential unlock mode for specific users
  - [ ] Toggle sequential unlock on/off per user via User Detail page (ADM-04)
  - [ ] When enabled: User can access lessons sequentially without daily unlock restrictions
  - [ ] When enabled: User can complete multiple lessons per day
  - [ ] When enabled: Next lesson unlocks immediately after Q&A completion (no 12:01am timezone wait)
  - [ ] Visual indicator in User Detail page showing sequential unlock status
  - [ ] Use cases: Content reviewers, Story Elders/graders, testing, admin team members
- [ ] View user responses (Q&A, Challenges)
- [ ] **Circle Assignment Flags:** Visual indicator (e.g., red highlight) for users who reach point thresholds but haven't been assigned to circles
- [ ] **Pause Token Management:**
  - [ ] View user's pause token count in user management
  - [ ] View token usage history (when tokens were consumed)
  - [ ] Manually adjust token count (override)
  - [ ] Configure starting token count (default: 3)
  - [ ] Configure token earnings per status level (Status 1: +1, Status 2: +2, Status 3: +3)
- [ ] Export user data (CSV) including: Anonymized user data (user ID, goals, status, XP, streak, pause token count), lesson completion dates, response metadata (response type, completion status, timestamps). **Note:** PII (name, email, phone) excluded from standard export. User data requests (GDPR compliance) handled separately via individual user export feature. Full response text/audio export available in Phase 2.

**Signup Approval Queue:**
- [ ] Admin receives email notification of new signups
- [ ] Admin Panel shows pending approvals count badge on signup queue section
- [ ] View pending signup approvals with user details (name, email, phone, goals, signup date)
- [ ] Approve or reject signups with optional message
- [ ] Upon approval: System sends SMS magic link to user to start Day 1

**Content Availability Dashboard:**
- [ ] View content status by day (complete/incomplete/draft)
- [ ] See which days are published vs pending
- [ ] Alert when users are approaching content boundary

**AI Feedback Review Queue (MVP):**
- [ ] New section in Admin Panel: "Feedback Review"
- [ ] Queue displays all submissions with AI-generated feedback pending approval
- [ ] Queue sortable by: submission date, user status, lesson day
- [ ] Queue filterable by: submission type (Q&A/Challenge), status (pending/approved)
- [ ] Admin can click to review a submission
- [ ] No locking mechanism (multiple admins can work simultaneously)
- [ ] Admin dashboard shows pending feedback count badge
- [ ] Alert if pending queue exceeds threshold (e.g., >50 pending)

**AI Feedback Review Interface (MVP):**
- [ ] Admin sees user info: name, email, current day, goal
- [ ] Admin sees original question/challenge prompt
- [ ] Admin sees user response (text or transcribed audio)
- [ ] For audio: Admin can play original recording
- [ ] Admin sees AI-generated feedback (scores + written feedback)
- [ ] For Q&A: Admin sees AI correctness evaluation (pass/fail or score)
- [ ] For Challenges: Admin sees AI scores (structure, emotion, clarity, relevance) and written explanation
- [ ] Admin can approve AI feedback as-is
- [ ] Admin can edit AI feedback before approving
- [ ] Admin can reject AI feedback and write entirely new feedback
- [ ] **"Reject & Regenerate" button:** Trigger AI to generate new feedback (no manual write required)
- [ ] Upon approval, feedback is sent to user (batched weekly delivery)
- [ ] System tracks: original AI feedback, admin edits, final approved version, regeneration attempts (align with TRD max 3 retries)
- [ ] Bulk approve/reject functionality available

**AI Grading Configuration (Admin Panel):**
- [ ] **Rubric editing:** Admin can edit grading rubric (structure, emotion, clarity, relevance, etc.) from Admin Panel. Edit applies to future evaluations (or per-Challenge if supported). Separate from per-feedback review screen (e.g., system/config section).
- [ ] **Prompt editing:** Admin can edit prompts for AI grading (tone, structure, instructions) in Admin Panel. No code changes required.
- [ ] **Prompt versioning:** Prefer prompt versioning and editing inside Admin Panel over external Langsmith. If Admin Panel versioning is not feasible, document Langsmith as fallback and how Admins access it.

**Circle Management (MVP):**
- [ ] Create circles (admin-created groups: marketing, school, beginners, advanced, etc.)
- [ ] Create custom circles (e.g., The Contractor team circle, company-specific circles)
- [ ] Seven default circles exist (one per goal type)
- [ ] Edit circle details (name, description)
- [ ] Assign users to circles based on primary goal (100% manual assignment)
- [ ] Assign users to circles based on: Primary goal, Number of points/status reached, Group requests
- [ ] View circle membership
- [ ] Remove users from circles
- [ ] Visual flags for users who need circle assignment (reached thresholds but not assigned)

**Circle Bulk Communication (MVP):**
- [ ] Send SMS to all members of a circle
- [ ] Send email to all members of a circle
- [ ] Message templates for common communications

**Celebration Dashboard (MVP):**
- [ ] View users hitting milestones (status changes, streak milestones, 70-day completion)
- [ ] Filter by milestone type
- [ ] Export list for "surprise and delight" outreach
- [ ] Automatic flags/notifications for admin team
- [ ] View like counts per Feed content piece (engagement metrics)
- [ ] Configure celebration settings: Enable/disable celebrations per milestone type
- [ ] Configure webhook URLs for milestone notifications
- [ ] Configure email templates for milestone emails
- [ ] Preview celebration animations

**Admin Notifications (MVP):**
- [ ] Dashboard notification for new signups
- [ ] Slack integration for signup notifications

**Phase 2 Admin Features:**
- Goal-specific Feed curation (content tagged by goal)
- Elder management (accounts, goal assignment, coverage monitoring)
- Advanced analytics and reporting
- Advanced token features (token purchase system, expiration, gifting)
- **AI model selection (optional):** Admin can select different AI model for regeneration (e.g., GPT-5.3 vs GPT-4.6). Lower priority than direct edit and rubric/prompt editing.

---

### BR-12: Post-Completion Experience [DEFERRED TO PHASE 3]

**Status:** Deferred to Phase 3

**Summary:**
Features for users who complete all 70 days: Level 2 advanced content, refresher challenges, alumni community features.

**Rationale for Deferral:**
- MVP only has 7-10 days of content
- Post-completion is a Phase 3 concern once full 70 days are available

**MVP Behavior:**
- When user completes all available content, they see "You're all caught up!" message
- All completed lessons remain accessible
- Status and XP persist


---

### BR-13: Celebration Moments

**Priority:** High
**Persona:** All Users

**Description:** In-app animations and multi-channel notifications at key milestones (status, streak, completion) for emotional engagement and "surprise and delight."

**Business Value:** Emotional engagement, retention; reinforces progress, motivates continued participation.

**User Story:** As a user, I want to see celebrations when I achieve milestones so I feel rewarded and motivated to continue.

**Acceptance Criteria:**

**In-App Celebration Animations:**
- [ ] Display celebration animation when user achieves Status 1, 2, or 3
- [ ] Display celebration animation at streak milestones (7, 14, 30, 50, 70 days)
- [ ] Display celebration animation upon Day 70 completion
- [ ] Animations are non-blocking (user can dismiss or they auto-dismiss after 3-5 seconds)
- [ ] Animation includes congratulatory message customized to milestone type
- [ ] Confetti/particle effects for major milestones (status changes, Day 70)
- [ ] Subtle animations for minor milestones (streak days)

**Automated Email Triggers:**
- [ ] Send congratulatory email when user achieves Status 1, 2, or 3
- [ ] Send congratulatory email at streak milestones (7, 14, 30, 50, 70 days)
- [ ] Send completion email when user finishes Day 70
- [ ] Email templates customizable by admin
- [ ] Emails include user's name, milestone achieved, and encouragement
- [ ] Emails can be disabled per milestone type (admin setting)

**Webhook/Zapier Integration:**
- [ ] Fire webhook when any milestone is achieved
- [ ] Webhook payload includes: user ID, user name, user email, milestone type, timestamp
- [ ] Admin can configure webhook URL
- [ ] Support for Zapier integration (standard webhook format)
- [ ] Admin can enable/disable webhooks per milestone type

**Admin Configuration:**
- [ ] Admin can define streak milestone thresholds (default: 7, 14, 30, 50, 70)
- [ ] Admin can enable/disable celebrations per milestone type
- [ ] Admin can preview celebration animations

**Milestone Trigger Points:**
- Status level changes (0→1, 1→2, 2→3)
- Streak milestones (7, 14, 30, 50, 70 days)
- Program completion (Day 70)
- First lesson completion
- First challenge completion

**Lesson Completion Celebrations (Daily Lesson):**
- [ ] Only ONE celebration per lesson completion
- [ ] Celebration shown ONLY when returning to Feed (never mid-lesson)
- [ ] Two variants: **Basic** (Q&A only, user snoozed challenge) → "You completed Day X" + XP for Q&A | **Full** (Q&A + challenge) → "You completed Day X and the challenge" + XP for Q&A + challenge
- [ ] If user snoozes challenge: celebration after snooze time selection, when returning to Feed
- [ ] No celebration after Q&A if user continues to challenge; celebration only after final step (challenge complete or snooze selected)

**Business Rules:**
- CEL-R01: Celebrations trigger automatically when milestones are achieved
- CEL-R02: Animations are non-blocking (don't interrupt user flow)
- CEL-R03: Email/webhook triggers can be disabled per milestone type by admin
- CEL-R04: Celebration Dashboard (admin view) shows all milestone achievements for manual outreach

**Dependencies:**
- Animation library (Lottie or CSS animations)
- Animation assets (design + export of celebration animations)
- Email provider (SendGrid, etc.)
- Webhook service

**Effort Estimation:**
- Animation Library Integration: 0.5 days
- Animation Assets (Design): 2-3 days (or use pre-built animations)
- Milestone Detection Service: 1 day
- In-App Animation Display: 1.5 days
- Email Template System: 1 day
- Webhook Service: 0.5 days
- Admin Configuration UI: 1 day
- Testing & QA: 1 day
- **Total: 8-10 days (~1.5-2 weeks)**


---

### BR-14: Alpha/Beta User Feedback Tool

**Priority:** High (for testing phase)
**Persona:** Alpha/Beta Test Users

**Description:** Persistent feedback mechanism for Alpha/Beta users to report bugs and submit ideas; automatic routing and Linear ticket creation.

**Business Value:** Rapid feedback during testing; bugs → dev team, ideas → client team.

**User Story:** As a test user, I want to easily submit feedback at any point so I can report issues or suggest improvements without disrupting my experience.

**Acceptance Criteria:**
- [ ] Persistent lightbulb button visible at all times during user session
- [ ] Button is easy to access and understand
- [ ] Clicking button opens feedback form with category selection
- [ ] User must select category: "Bug" or "Idea"
- [ ] Description field required
- [ ] Screenshot capture optional (auto-capture if possible)
- [ ] Page/context auto-captured with submission
- [ ] Form submission creates Linear ticket automatically

**Feedback Routing:**
| Category | Routed To | Action |
|----------|-----------|--------|
| Bug | Dev team | Auto-generated Linear ticket with client details |
| Idea | Client team (the client) | Auto-generated Linear ticket |

**Integration Requirements:**
- Linear API integration for ticket creation
- Sentry integration for bug tracking (client suggestion)

**Business Rules:**
- FEED-R01: Feedback tool always visible for Alpha/Beta users
- FEED-R02: All submissions create Linear tickets automatically
- FEED-R03: Bug reports include context (page, actions, browser)
- FEED-R04: Tool may be disabled or modified for production launch

---

## Use Cases

### UC-01: Complete Daily Lesson

**Actor:** User
**Preconditions:** User is registered and lesson is available

**Main Flow:**
1. User receives SMS with lesson link at scheduled time (dynamic message variant based on streak/status)
2. User clicks link and lands on Pre-Lesson screen
3. System plays Gen AI personalized intro (via Eleven Labs) with user name, day, streak
4. System auto-advances to Direct Instruction
5. User watches ~5 min lesson video with karaoke-style captions
6. System advances to Q&A
7. User answers each question via text, audio, or selection
8. Response saved; AI feedback generated and queued for approval (MVP: admin approval via Admin Portal; Phase 2: Elder approval via Elder Portal) - delivered weekly
9. System advances to Challenge
10. User completes challenge response
11. Response saved; AI feedback generated and queued for approval (MVP: admin approval via Admin Portal; Phase 2: Elder approval via Elder Portal) - delivered weekly
12. System plays Gen AI personalized Post-Lesson video (via Eleven Labs)
13. System awards XP and updates streak
14. User arrives at Feed

**Alternate Flows:**
- **A1 (First Recording):** Before step 7, if first recording, show Privacy Notice modal. User acknowledges to proceed.
- **A2 (Snooze Challenge):** At step 10, user clicks "Snooze". System schedules SMS reminder at admin-configured time, awards partial XP, navigates to Feed.
- **A3 (Retry Recording):** At step 7 or 10, user can retry recording before submitting.
- **A4 (Status 0):** At steps 8 and 11, user sees "Great job! Your response has been saved. Complete more lessons to unlock AI feedback!" XP and streak update visibly, but no AI evaluation displayed.

**Error Flows:**
- **E1 (Network Error):** Show retry button. User can retry submission. Auto-retry up to 3 times.
- **E2 (Link Expired):** Show "Link expired" message. Generate new link via SMS. User can request new link.
- **E3 (Video Playback Failure):** Show "Video failed to load" message with retry button. If retry fails, show "Please try again later" and allow user to skip to next section or contact support.
- **E4 (AI Feedback Generation Failure):** Show "Feedback processing, please check back in a few minutes" message. System retries up to 3 times. If all retries fail, admin notified. User can continue to Feed; feedback appears later when available.
- **E5 (SMS Delivery Failure):** Automatic email fallback (per NFR). If both fail, user can request new link via app (if session valid) or contact support.

**Postconditions:**
- Partial or full XP awarded
- Streak updated (if Q&A completed)
- AI feedback stored (if Status 1+)
- Next lesson unlocked (next day)

---

### UC-02: Complete Daily Review [DEFERRED TO PHASE 2]

*This use case is deferred to Phase 2. See BR-03 for summary.*

---

### UC-03: Elder Reviews Submission [DEFERRED TO PHASE 2]

*This use case is deferred to Phase 2. See BR-07 for summary.*

---

## Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|-------------|--------|-------------|
| **Performance** | Page load time | < 3 seconds | Lighthouse score |
| **Performance** | Video start time | < 2 seconds | Video analytics |
| **Availability** | Uptime | 99.5% | Monitoring dashboard |
| **Scalability** | Concurrent users | 500 (MVP) | Load testing |
| **Security** | Data encryption | TLS 1.2+ | Security audit |
| **Security** | Authentication | Magic link (SMS primary, email fallback) | - |
| **Platform** | Application type | Web-based (no native app) | - |
| **Mobile** | Mobile-first design | Experience optimized for mobile; acceptable on desktop | Device testing |
| **Mobile** | Responsive design | iOS Safari, Android Chrome | Device testing |
| **SMS** | Delivery rate | > 95% | SMS provider dashboard |
| **SMS** | US carrier coverage | All major carriers | Provider verification |
| **SMS** | Email fallback | Automatic on failure | System logs |
| **Accessibility** | WCAG compliance | Level AA (target) | Accessibility scan |

**SMS Provider Requirements (MVP):**

| Requirement | Detail |
|-------------|--------|
| US Carrier Coverage | Must work across ALL US carriers (Verizon, AT&T, T-Mobile, etc.) |
| One-Way SMS | Outbound notifications only (two-way is Phase 2) |
| Email Fallback | Automatic switchover to email if SMS delivery fails |
| Provider Options | Twilio, MessageBird, Vonage, Plivo, or similar |
| Selection | TRD will evaluate cost, deliverability, and API quality |

---

## Business Rules Summary (MVP)

| Rule ID | Category | Rule | Description |
|---------|----------|------|-------------|
| **Onboarding** |
| ONB-R01 | Onboarding | Payment | No Stripe payment in MVP - manual approval gate instead |
| ONB-R02 | Onboarding | Access control | User cannot access lessons until admin approves |
| **Lessons** |
| LES-R01 | Lesson | Session unlocking | Next day unlocks at 12:01am user timezone after Q&A completion |
| LES-R01A | Lesson | One per day | Users can only complete one lesson per day (default behavior) |
| LES-R01B | Lesson | Unlock timing | Lesson unlocks at 12:01am user timezone on next day after completion |
| LES-R01C | Lesson | Sequential unlock override | Admin can enable sequential unlock mode for specific users, bypassing daily restrictions. When enabled, users can complete multiple lessons per day and next lesson unlocks immediately after Q&A completion |
| LES-R02 | Lesson | Base XP | Q&A done = base XP (1 XP) - minimum to maintain streak |
| LES-R03 | Lesson | Bonus XP | Challenge done = bonus XP (2 additional XP) |
| LES-R03A | Lesson | XP calculation | Total lesson XP = Base XP (1) + Bonus XP (2) = 3 XP per day (or potentially 4 XP - TBD) |
| LES-R03B | Lesson | XP terminology | XP terminology simplified - just "points", no "partial/full XP" distinction |
| LES-R04 | Streak | Credit trigger | Streak credited on partial completion (Q&A done) |
| LES-R05 | Lesson | Snooze reminder | Snoozed challenge triggers reminder at admin-configured time (system-wide setting) |
| LES-R05A | Lesson | Snooze delivery | Snooze reminder delivered via SMS magic link |
| LES-R05B | Lesson | Notification timezone | All notifications (lesson, snooze) MUST be scheduled in user's local time; system MUST resolve user timezone (stored preference or device/browser fallback) since users are globally located |
| LES-R06 | Lesson | One per day | Cannot complete multiple lessons per day |
| LES-R07 | Lesson | Trigger message | Dynamic trigger message variants based on streak, status, missed days |
| LES-R08 | Lesson | Follow-up message | Maximum 1 follow-up message (4 hours after initial) |
| LES-R09 | Lesson | Response limits | Response limits per question: Text 2000 characters, Audio 120 seconds (independent per question) |
| LES-R10 | Lesson | Response types | Response input types: Text, Audio, Multiple Choice, Image Upload, Video Upload, Audio Upload |
| LES-R11 | Lesson | Magic link delivery | Magic link delivered via SMS (primary); email fallback if SMS delivery fails |
| LES-R12 | Lesson | Early access | Users can access lesson at any time after unlock (no restriction on accessing before scheduled time) |
| LES-R13 | Lesson | Schedule intervals | SMS trigger time selection uses 15-minute intervals (e.g., 9:00, 9:15, 9:30, 9:45) - consistent with Legends app |
| **Streaks** |
| STR-R01 | Streak | Credit trigger | Streak credited on partial completion (Q&A done) |
| STR-R02 | Streak | 24-hour window | Must complete within 24h of unlock (midnight user's current timezone setting) |
| STR-R03 | Streak | Token consumption | If user misses a day and has pause tokens: Token automatically consumed, streak preserved, no XP awarded |
| STR-R03A | Streak | Reset | If user misses a day and has no pause tokens: Streak resets to 0 |
| STR-R06 | Streak | Pause tokens | Starting tokens (3), Status 1 (+1), Status 2 (+2), Status 3 (+3) |
| STR-R07 | Streak | Token activation | Token consumption is automatic (user cannot manually activate) |
| STR-R04 | Streak | Reset messaging | User sees re-engagement message on Feed when streak resets |
| STR-R05 | Streak | Timezone changes | User timezone editable; changes apply to future triggers/windows only (not retroactive) |
| **XP & Status** |
| XP-R01 | XP | Accumulation | XP earned but never lost |
| XP-R02 | XP | Status permanence | Status is PERMANENT once earned |
| XP-R03 | XP | Admin override | Admin can manually assign any status |
| XP-R04 | Status | XP-based | Status based on XP thresholds |
| XP-R05 | XP | Dual use | XP used for BOTH status progression AND leaderboard ranking |
| **AI Feedback** |
| AI-R01 | Feedback | Status gating | Status 0 = completion message with XP/streak visible, no AI evaluation |
| AI-R02 | Feedback | Admin approval | AI feedback requires admin approval before being shown to users |
| AI-R03 | Feedback | Weekly delivery | Approved feedback delivered weekly (batched), not immediately |
| AI-R04 | Feedback | Storage | All feedback stored persistently for user reference |
| AI-R05 | Feedback | Audio transcription | Audio responses transcribed to text for evaluation (speech-to-text) |
| AI-R06 | Feedback | Failure handling | If AI feedback generation fails, system retries up to 3 times; admin notified if all fail |
| AI-R07 | Feedback | Configurable frequency | Feedback delivery frequency configurable at system/circle/user level (default: weekly) |
| **Celebration Moments** |
| CEL-R01 | Celebrations | Auto-trigger | Celebrations trigger automatically when milestones are achieved |
| CEL-R02 | Celebrations | Non-blocking | Animations are non-blocking (don't interrupt user flow) |
| CEL-R03 | Celebrations | Admin control | Email/webhook triggers can be disabled per milestone type by admin |
| CEL-R04 | Celebrations | Dashboard | Celebration Dashboard (admin view) shows all milestone achievements for manual outreach |
| **Story Circles** |
| CIR-R01 | Circles | Private vs Goal | Users who join via private circle are NOT auto-assigned to goal-based circles |
| CIR-R02 | Circles | Multiple membership | Users CAN belong to multiple circles (admin-controlled) |
| CIR-R03 | Circles | No limit | No limit on circle membership count |
| CIR-R04 | Circles | Admin control | Circle assignment is 100% manual in MVP (no automatic algorithm) |
| CIR-R05 | Circles | Size | Circle size has no minimum or maximum limit |
| CIR-R06 | Circles | Assignment flags | Admin dashboard flags users who reach point thresholds but haven't been assigned to circles |
| **Navigation** |
| NAV-R01 | Navigation | Post-completion | Land on Feed after lesson (default landing) |
| NAV-R02 | Navigation | Learn tab | Learn tab shows roadmap/journey view (like Legends) with next available lesson highlighted |
| NAV-R03 | Navigation | Day visibility | All 70 days visible from Day 1 (organized by pillar/theme; 10 groups of 7 lessons; avoid "Week" label) |
| NAV-R04 | Navigation | Content boundary | Only show days with uploaded content |
| NAV-R05 | Navigation | URL structure | Marketing page at `legacyvoice.com`, app at `app.legacyvoice.com` |
| **Alpha/Beta Feedback** |
| FEED-R01 | Feedback Tool | Visibility | Feedback tool always visible for Alpha/Beta users |
| FEED-R02 | Feedback Tool | Linear integration | All submissions create Linear tickets automatically |
| FEED-R03 | Feedback Tool | Bug context | Bug reports include context (page, actions, browser) |
| FEED-R04 | Feedback Tool | Production | Tool may be disabled or modified for production launch |

---

## Assumptions & Dependencies

### Assumptions

| ID | Assumption | Impact if Wrong |
|----|------------|-----------------|
| A01 | Mobile-first responsive web, not native apps | Architecture change |
| A02 | Client provides video content on schedule | Timeline delay |
| A03 | Payment is Phase 2, not MVP (manual approval for MVP) | Scope change |
| A04 | Legends architecture can be referenced | More design work |
| A05 | 7-10 days content for Phase 1 | Content dependency |
| A06 | SMS is primary notification channel (one-way for MVP) | Alternative needed |
| A07 | Story Circles are MVP (admin-controlled); Story Elders are Phase 2 | Scope validated |
| A08 | English only for MVP | Internationalization scope |
| A09 | User can only complete one lesson per day | UX change if different |
| A10 | Goals cannot be changed after onboarding | Feature change |
| A11 | AI feedback is weekly batched with admin approval (not immediate) | Scope validated |
| A12 | Gen AI personalization for pre/post lesson content via Eleven Labs (MVP) | Scope validated |

### Dependencies

| Dependency | Owner | Status | Risk if Unavailable |
|------------|-------|--------|---------------------|
| Video content (7-10 days) | Client (the content team) | In progress | Cannot test lessons |
| Legends architecture access | Client | Available | Reference unavailable |
| SMS provider account | The Contractor | TBD | Cannot send triggers |
| AI evaluation criteria | The Contractor | TBD | Cannot configure AI feedback |
| Brand assets (Figma) | Client | Available | - |

---

## Exclusions

| Exclusion | Rationale | Future Phase? |
|-----------|-----------|---------------|
| Native mobile apps | Web-first approach, faster MVP | Phase 3+ |
| Payment/Stripe | MVP is free testing | Phase 2 |
| Full 70-day content | Testing with 7-10 days | Phase 2 |
| In-app Circle chat | WhatsApp simpler for MVP | Phase 2 |
| Elder-Circle interactions | Elders focus on individual feedback | Phase 2+ |
| Cross-goal Elder feedback | Elders only review matching goals; queue if none | Consider Phase 2 |
| Phone call triggers | SMS sufficient for MVP | Phase 2 |
| Multi-language | English only MVP | Phase 2+ |
| Physical totems | Logistics complexity | Phase 2 |
| AI audio/gauge feature | Removed for MVP | Future |

---

## Risks (MVP)

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---------|------|------------|--------|------------|
| RSK-01 | Content not ready on time | Medium | High | Start with 7-10 days, add incrementally via Admin Panel |
| RSK-02 | SMS delivery issues | Low | Medium | Email fallback system, monitor delivery rates |
| RSK-03 | AI feedback quality | Medium | Medium | Iterate on evaluation criteria, gather user feedback |
| RSK-04 | User drop-off before Day 7 | High | High | Strong onboarding, AI feedback engagement |
| RSK-05 | Open questions delay development | Medium | High | Prioritize critical question resolution |
| RSK-06 | Admin content upload workflow issues | Medium | Medium | Thorough testing, clear documentation |

---

## Glossary

| Term | Definition |
|------|------------|
| **Day 0** | Orientation content delivered by Coach Devon upon approval (how the app works, layout) |
| **Pre-Lesson** | Gen AI personalized intro video with user name, day, streak overlay (via Eleven Labs) |
| **Direct Instruction** | Core lesson content with karaoke-style captions (client-provided video) |
| **Karaoke-Style Captions** | Caption display: active word highlighted (e.g., white); upcoming words darker or ~50% opacity. Applies to Personalization block (auto-generated from 11 Labs) and Direct Instruction (baked into uploaded video) |
| **Personalization Block** | Gen AI block (Pre-Lesson, Optional, Post-Lesson) with user variables. Background: looping video upload; SHOULD match Direct Instruction. Optional: blob/waveform layer synced with 11 Labs voice |
| **Blob/Waveform Layer** | Dynamic visual (blob or waveform) synced with 11 Labs voice in Personalization blocks. Implementation: video layer with waveform baked in, or CSS-animated blob + audio-driven waveform |
| **Q&A** | Questions to verify understanding (flexible: text, audio, MCQ, image/video/audio upload); appears after video |
| **Challenge** | Extended storytelling exercise with grading rubric; can be snoozed |
| **Post-Lesson** | Gen AI personalized wrap-up with progress, streak, feedback info (via Eleven Labs) |
| **Lesson** | Complete learning session: Pre-Lesson + Direct Instruction + Q&A + Challenge + Post-Lesson |
| **Feed** | Home screen with streaks, leaderboards, content tiles |
| **Coach Devon** | AI coach persona who guides lessons; video content provided by client team |
| **AI Feedback** | Automated evaluation of Q&A (correctness) and Challenges (structured scores + explanation); delivered weekly with admin approval |
| **Feedback History** | Account section where users view all historical AI feedback |
| **Streak** | Count of consecutive days completing lessons (Q&A) |
| **XP** | Experience points earned through actions, used for status progression and leaderboard ranking |
| **Status** | User level (0-3) based on XP earned; Status 1+ unlocks AI feedback |
| **Magic Link** | Passwordless authentication link (delivered via SMS primary, email fallback). Single-use, expires after 24 hours. Clicking creates authenticated session that persists (duration TBD in TRD) |
| **Notification Timezone** | All lesson and snooze notifications MUST be scheduled in user's local time. System resolves user timezone (stored preference or device/browser fallback) when scheduling any notification, since users are globally located. |
| **Rolling Delivery** | Content delivery model: Not all 70 days of content need to be delivered at MVP launch. Application must have up to 10 days of lessons ready/generated at launch. Content uploaded incrementally via Admin Panel as development continues after initial MVP delivery |
| **Base XP** | Experience points awarded for Q&A completion (1 XP) - minimum to maintain streak |
| **Bonus XP** | Additional experience points awarded for Challenge completion (2 additional XP) |
| **Total Lesson XP** | Base XP (1) + Bonus XP (2) = 3 XP per day (or potentially 4 XP - TBD) |
| **Content Boundary** | State when user completes all available content but more days not yet uploaded (shows "Coming Soon" for future days) |
| **Pause Token** | Token allowing user to skip a day without breaking streak (start with 3, earn more at each status level) - **MVP** |
| **Celebration Moments** | In-app animations and multi-channel notifications at key milestones (status changes, streak milestones, program completion) - **MVP** |

| **Story Circle** | Social cohort group for users with similar goals (MVP: admin-controlled assignment) |
| **Eleven Labs** | Gen AI service for personalized audio/video overlays in Pre/Post Lesson (MVP) |
| **Display Name** | User's preferred name for display (optional, defaults to full name; replaces avatar for MVP) |
| **WhatsApp Integration** | Circle communication via WhatsApp (MVP, in-app chat is Phase 3) |

**Phase 2 Terms (not in MVP):**
| Term | Definition |
|------|------------|
| **Review** | Evening reinforcement session with spaced repetition (Phase 2) |
| **Story Elder** | Storytelling professional who provides goal-matched feedback (Phase 2) |
| **Elder Dashboard** | Interface where Elders review submissions (Phase 2) |
| **Avatar Selection** | User profile picture selection (Phase 2, display name used for MVP) |
| **Memories** | Playback of user's completed challenge recordings (Phase 2) |
| **Speaking Quality Analysis** | Audio analyzed for delivery: intonation, pacing, pauses (Phase 2/3) |

---

## Appendices

### Appendix A: Complete Open Questions List

See `clients/sonny/legacyvoice/discovery-docs/client-questions.md` for the full list of open questions organized by priority tier.

### Appendix B: Screen Inventory (MVP)

| Area | Screens |
|------|---------|
| Onboarding | ONB-01 through ONB-06 (Landing, Phone, Profile, Goals, Schedule, Display Name, Welcome, Pending Approval) |
| Lesson | LES-01 through LES-05 (Pre-Lesson, Instruction, Q&A, Challenge, Post-Lesson, Completion) |
| Feed | FEED-01, LEARN-01 (two tabs) |
| Profile | PRO-01, PRO-02 (Profile, Settings, Feedback History) |
| Admin | ADM-01 through ADM-08 (Content Upload, Users, Signup Approvals, Content Dashboard, Feedback Review Queue, Feedback Review Detail) |

**Phase 2 Screens:**
| Area | Screens |
|------|---------|
| Review | REV-01 through REV-03 (Welcome Back, Recap, Q&A) |
| Memories | MEM-01 (Playback recordings) |
| Inbox | INBOX-01, INBOX-02 (Elder + AI unified inbox) |
| Elder Dashboard | ELD-01 through ELD-03 (Pool, Review, Submitted) |
| Circle | CIR-01, CIR-02 (Leaderboard, Members) |

*See Lo-Fi Wireframes document for detailed screen specifications.*

### Appendix C: Figma References

| Reference | URL | Purpose |
|-----------|-----|---------|
| Brand Work | [Figma Link]([Figma Design Link Removed]) | UI guidance, colors, typography |
| Legends UX | [Figma Link]([Figma Design Link Removed]) | UX patterns, onboarding |
| Legends Architecture | [Figma Link]([Figma Design Link Removed]) | Technical architecture reference |

### Appendix D: Inspirational Products

| Product | Relevance |
|---------|-----------|
| Duolingo | Daily streaks, gamification, micro-learning |
| Wordle | Daily habit, simple engagement |
| Strava | Social features, leaderboards |
| Calm | Daily sessions, habit formation |
| Oura Ring | Progress tracking, health habits |
| Legends | Direct reference platform (buildlegends.com) |

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.5.1 | February 12, 2026 | The Contractor | Timezone verification for notifications: All lesson and snooze notifications MUST be scheduled in user's local time; system MUST resolve user timezone (stored preference or device/browser fallback) since users are globally located. LES-R05B. |
| 1.5.0 | February 12, 2026 | The Contractor | Mockup review (Feb 12): Personalization block (background, blob/waveform, karaoke captions, caption font). AI Feedback (Reject & Regenerate, rubric/prompt editing, versioning). Admin-editable user info. Contact Admin for team setups. Single celebration at Feed return. Feed pin, share. Learn tab pillar/theme grouping. Phase 2: feed ordering, UGC consent, XP for likes. Glossary updates. |
| 1.4.2 | February 9, 2026 | The Contractor | Onboarding flow: Added flow overview table (marketing → app → waitlist registration → admin approval → magic link). Clarified "Register for Waitlist" CTA, "waitlist registration" (initial questions), "request sent to admin." Aligned terminology across PRDs. |
| 1.4.1 | February 6, 2026 | The Contractor | Refinement: tightened phrasing, removed redundancy, consolidated Access Control/Day 0, Lesson Unlock Logic, BR descriptions, Background, CMS Block Builder, UX Design Rationale. No information removed. |
| 1.4 | February 6, 2026 | The Contractor | Architecture: Landing page static only (no logic, no forms). Interest form moved to app. Admin Portal/Airtable for approval; Slack notification only. Feed card layout types. Leaderboard top 10 table view. Mobile-first NFR. |
| 1.3 | February 6, 2026 | The Contractor | Restructured PRD: added Document Structure section and compartmentalized PRDs (prd-main-app.md, prd-familyelder-portal.md, prd-admin-portal.md, prd-marketing-page.md). Main PRD remains master; specialized PRDs copy area-specific requirements for verification. Updated Related Documents (Lo-Fi reference). |
| 1.2 | February 3, 2026 | The Contractor | Added LES-R13: SMS trigger time selection uses 15-minute intervals (aligns with Legends app behavior, simplifies cron job implementation). |
| 1.1 | February 2, 2026 | The Contractor | Enhanced BR-11 Content Upload with detailed block-based lesson builder (timeline interface, drag-and-drop, video preview, block configuration). Added BR-11 Sequential Unlock Override feature for admins/elders (toggle per user, bypasses daily restrictions). |
| 1.0 | January 30, 2026 | The Contractor | Initial PRD |

---

*The Contractor*
