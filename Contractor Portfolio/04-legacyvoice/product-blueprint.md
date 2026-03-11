# LegacyVoice - Blueprint

## Cover Page

| Field               | Value                               |
| ------------------- | ----------------------------------- |
| **Project Name**    | LegacyVoice                          |
| **Client**          | The Client                      |
| **Document Author** | The Contractor     |
| **Date / Version**  | January 2026, v1.1                  |
| **Document Status** | DRAFT - Pending client confirmation |

---

## Project Overview

| Attribute            | Details                                                               |
| -------------------- | --------------------------------------------------------------------- |
| **Engagement Type**  | MVP                                                                   |
| **Client Readiness** | Vision doc provided; high-level features and flow references included |
| **Primary Contact**  | The Client                                                        |
| **Source Materials** | LegacyVoice Brief, Legends App (buildlegends.com), Figma Links         |

## Document Objective

**What is this document?**

This Blueprint captures The Contractor's understanding of LegacyVoice based on your provided materials. It reflects what we heard, not what we recommend.

**Purpose:** Alignment confirmation. We want to ensure:

1. We correctly understand the problem you're solving
2. We accurately captured your vision for LegacyVoice
3. We identified the right gaps and questions before proceeding

**What we need from you:**

Please review this document and confirm:

- Our understanding matches your intent
- Any corrections or clarifications needed
- Answers to the open questions at the end

Once aligned, we proceed to the detailed Product Requirements Document (PRD).

**Accompanying documents:**

- **Glossary** — Definitions of terms used in this Blueprint
- **Client Questions** — Full list of questions with detailed response options

## Client Narrative

### What the client says:

> "We believe storytelling is the world's most important skill."
>
> "Yet for far too long, we've assumed some people 'are just good storytellers' - as if it's a trait you're born with."
>
> "As a society, we don't take this skill seriously. In fact, there are no rigorous programs that train storytelling at all."
>
> "Your story is too important to let someone else tell. (not lack of will, lack of skill)"

### Our understanding:

The client wants to build the first program that trains storytelling as a learnable skill through daily, bite-sized interactive sessions over 10 weeks (70 days).

### Key problem elements identified (from your brief):

- "We've assumed some people 'are just good storytellers' - as if it's a trait you're born with" (storytelling treated as innate, not learnable)
- "There are no rigorous programs that train storytelling at all" (no structured training exists)
- "Learn to control your narrative - for you, your family, and your business" (people lack tools to own their story)

## Client's Stated Vision

### What the client wants to build:

> "LegacyVoice is the first program that trains storytelling as a skill through fun, bite-sized interactive daily sessions. Think of it as 'micro-dosing the art of storytelling'."
>
> "Each day you get a short, five-minute lesson and challenge from a digital coach, designed to gradually level up your ability to craft compelling stories."
>
> "Over the course of 10 weeks, you'll quantifiably improve your storytelling skills."

### Expected outcomes (client's words):

> "By the end, we guarantee you'll become a great storyteller."
>
> "Learn to control your narrative - for you, your family, and your business."
>
> "Your story is your strategy. Start with your story. Put your story first."

### Key product elements mentioned:

1. **Daily Structure**: Short daily lessons (~5 min) + challenges over 70 days (10 weeks)
2. **Digital Coach**: AI coach named "Devon" — high-energy, DJ-style instructor
3. **Social Elements**: Story Circles (peer groups) and Story Elders (external storytelling professionals who provide feedback)
4. **Gamification**: Streaks, XP, leaderboards, XP-based status levels (0-3), badges
5. **Two Daily Sessions**: Morning "Lesson" + End-of-day "Review"

### Existing products referenced as inspiration:

> "Wordle, Duolingo, Streaks, Strava, Oura Ring - These habit-building products inspire the blend of daily engagement, social fun, and gamification."

### Existing product to model:

> "NOTE: I'd STRONGLY recommend using Legends to understand the flow as well. You can visit 'buildlegends.com' to see the experience."

## Source Material Summary

### LegacyVoice Brief

Key facts treated as true per materials provided. _(Our interpretation, not commitments—please confirm. Commitments formalized in PRD.)_

1. **Program structure**: 10-week (70-day) program with two daily sessions (Morning Lesson + End-of-day Review)
2. **Digital coach**: AI coach "Devon" delivers high-energy, DJ-style instruction
3. **Social elements**: Story Circles (peer groups) and Story Elders (external storytelling professionals) as core engagement mechanics
4. **Gamification**: Streaks, XP, leaderboards, XP-based status levels (0-3), badges
5. **Reference model**: Legends app (buildlegends.com) as primary UX/architecture reference

**Material coverage and gaps:**

- High-level vision is clear; specific details (XP values, triggers) need clarification
- 12 open questions requiring client input

### Legends App (Referenced Model)

| Aspect       | What Client Said                                                                              |
| ------------ | --------------------------------------------------------------------------------------------- |
| UX Flow      | "THIS IS ALREADY SET UP IN LEGENDS SO YOU CAN SEE THIS IN THE LEGENDS USER FLOW"              |
| Onboarding   | "We should mimic the Legends onboarding as much as possible"                                  |
| Architecture | "Here's a Figma representation of the Legends Architecture. This is a helpful place to start" |

## Assumptions

Please flag any assumptions that don't match your expectations.

**Status key:**

- **Confirmed** — Validated by client
- **Pending client confirmation** — Awaiting confirmation
- **Pending Q#.#** — Depends on answer to a question
- **Internal assumption (ok to proceed)** — Safe to proceed unless flagged

| ID  | Assumption                                                                                     | Source                                                                          | Impact if Wrong                           | Status                              |
| --- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------- |
| A01 | Mobile-first responsive web app, not native iOS/Android                                        | Brief → Architecture section: "Legends architecture"                            | Architecture change required              | Confirmed                           |
| A02 | Client team provides Devon video content on schedule                                           | Brief → Team section: "AI Coach & Content: Content Team Lead"                      | Timeline delay                            | Confirmed                           |
| A03 | Payment/Stripe integration is Phase 2, not MVP                                                 | Brief → Development Phases section: "Stripe integration is a phase 2"           | Scope change if needed earlier            | Confirmed                           |
| A04 | Legends app architecture can be referenced/reused                                              | Brief → Architecture section: "helpful place to start"                          | More design work needed                   | Confirmed                           |
| A05 | 7-10 days of content available for Phase 1 MVP                                                 | Brief → Development Phases section: "7-10 days of testable content"             | Content delivery dependency               | Confirmed                           |
| A06 | MVP notifications will use SMS (client confirmed as ideal); email fallback if SMS fails       | Brief → User Experience section: SMS triggers described throughout              | May need alternative if costs prohibitive | Confirmed                           |
| A07 | User responses (text/audio) require storage and AI analysis                                    | Brief → User Experience section: "sent to another system for AI/human analysis" | Infrastructure complexity                 | Confirmed                           |
| A08 | Story Circles and Story Elders are manual processes in MVP                                     | Brief → Social Elements section: "In the MVP: we will manually organize them"   | Operational overhead for client           | Confirmed                           |
| A09 | English only for MVP                                                                           | Brief/Figma: no localization requirements provided                              | Internationalization scope                | Confirmed                           |
| A10 | Web-based access via magic link (client confirmed); delivery method TBD (SMS vs email)         | Brief → User Experience section: Legends model reference                        | UX change if different                    | Confirmed                           |

## Questions Requiring Your Input

Your input on **12 questions** in the accompanying **Client Questions** document is needed before proceeding to detailed requirements.

### How to Respond

In the **Client Questions** document, comment on preferred options. Each question includes:

- Clear options to choose from
- Context on why the question matters
- Space for additional notes

### Note on Contradictions

Conflicting statements in your brief require clarification. _(Section names may vary.)_

| Contradiction      | Statement A                                                                                                                    | Statement B                                                                                                | Resolution       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------- |
| **Circle access**  | "You can join on your own, or set up your own private storytelling circles" _(Story Circles section)_                          | "STATUS 2: Based on XP, you unlock the ability to be placed into a Story Circle" _(Status Levels section)_ | See Question 3.3 |
| **Feedback model** | "Get feedback from an AI grader... automatically graded by a pre-defined AI rubric" _(End-of-Day Check-In + Status 1 section)_ | "Unlock grading & feedback from LegacyVoice Elders" _(Status 1 section)_                                    | See Question 2.2 |

Your answers to the referenced questions will resolve these.

## Next Steps

### What We Need From You:

1. **Complete the Client Questions document** — We can begin drafting requirements, but cannot finalize the PRD until questions are answered.

### What Happens Next:

Once we receive your responses:

1. We will update this Blueprint with your answers
2. Create Lo-Fi UX wireframes for the user experience
3. Proceed to detailed Product Requirements Document (PRD)

## Related Documents

| Document                | Description                                                            |
| ----------------------- | ---------------------------------------------------------------------- |
| **LegacyVoice Glossary** | Definitions of terms used in this Blueprint                            |
| **Client Questions**    | 12 questions with response options — **please complete this document** |

---

## Document History

| Version | Date         | Author    | Changes                                                                                                                                    |
| ------- | ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.1     | January 2026 | The Contractor | Updated after v1.0. Changes: Clarified Story Elders description from "expert mentors" to "external storytelling professionals who provide feedback"; Added "XP-based" qualifier to status levels description; Updated assumptions table (A01-A10) from "Pending client confirmation" or "Internal assumption (ok to proceed)" to "Confirmed" status |
| 1.0     | January 2026 | The Contractor | Initial blueprint                                                                                          |

_The Contractor_
