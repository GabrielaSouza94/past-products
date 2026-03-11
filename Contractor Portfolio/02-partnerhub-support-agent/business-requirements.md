# PartnerHub AI Support Agent - Business Requirements Document

## 1. Cover Page

| Field               | Details                         |
| ------------------- | ------------------------------- |
| **Project Name**    | PartnerHub AI Support Agent      |
| **Client**          | PartnerHub                       |
| **Document Author** | The Contractor - Applied Engineering |
| **Date**            | December 4, 2025                |
| **Version**         | 2.0                             |
| **Status**          | Draft - Pending Client Approval |

---

## 2. Introduction

### 2.1 Document Purpose

This BRD defines the business needs, functional requirements, and scope for the PartnerHub AI Support Agent. It serves as the foundation for technical design and development of an AI-powered system that automates customer support while maintaining service quality.

### 2.2 Project Scope

**In Scope for MVP:**

- AI-powered chat interface for customer support interactions
- Three primary support paths: Ask a Question, Request a Change, Report a Problem
- Email redirect system with automated responses directing users to AI chat
- Embrace API integration for AI-powered documentation search and answers
- Platform identification (PX vs Classic) via email lookup
- Multi-attempt Embrace conversations before live agent escalation
- Live agent handoff during business hours (all support paths)
- Outage detection with automatic PagerDuty alerts via Zendesk
- Classic platform ASPX page detection and Professional Services routing
- Module-based ticket routing (Tier 1, TCMA, NOD, SOD)
- Zendesk ticket creation with full chat transcript
- Feedback collection (thumbs up/down rating)
- Business hours configuration and management

**Out of Scope for MVP:**

- Professional services billing determination workflows
- Analytics dashboards (data stored and accessible, but no dashboards built)
- Mobile app version
- Multi-language support
- Offline use cases
- Integration with external CRM systems beyond Zendesk
- Custom AI model training or fine-tuning
- Real-time voice support (text chat only)
- Proactive outreach or notification systems
- Estimated wait times for live agent availability

### 2.3 Audience

- PartnerHub Support Management
- The Contractor Project Management and Engineering Teams
- Quality Assurance and Testing Teams
- Future Technical and Business Stakeholders

---

## 3. Business Context

### 3.1 Background

PartnerHub operates a multi-channel support system (email, webform, chat, CSM-initiated) with manual ticket processing. The support team handles requests for two platform types:

- **PX (Partner Experience)**: Modern SaaS platform
- **Classic**: Legacy platform with custom ASPX pages

Current challenges:

- High processing times due to manual information gathering
- Inconsistent response quality across channels
- Agent workload imbalance (80% routine tasks, 20% complex problem-solving)
- Variable customer experience depending on channel and agent
- Significant onboarding complexity for new team members

The company has invested in **Embrace**, an AI-powered documentation system that answers questions about PartnerHub's products and features.

### 3.2 Problem to Solve

**Primary Business Challenges:**

1. **Manual Process Limitations**: Agents manually gather information, categorize issues, and route tickets—limiting scalability and increasing costs

2. **Inconsistent Information Gathering**: Variable quality and completeness depending on agent and channel

3. **Underutilized Knowledge Base**: Embrace not leveraged in initial customer interactions

4. **Response Time Variability**: No standardized initial customer engagement approach

5. **Escalation Complexity**: Manual routing leads to delays and misrouted tickets

6. **Training Overhead**: Steep learning curve for new team members due to multiple channels and complex routing rules

### 3.3 Business Objectives

**MVP Objectives:**

1. **Centralize Support Entry**: Funnel all requests through a single AI-powered chat interface

2. **Automate Information Gathering**: AI collects required information through conversational prompts

3. **Leverage Embrace API**: Provide AI-powered answers before escalating to human agents

4. **Enable Self-Service**: Allow customers to resolve issues without human agent involvement

5. **Standardize Ticket Quality**: Ensure consistent, complete information on all tickets

6. **Reduce Agent Workload**: Decrease time on routine tasks, allowing focus on complex issues

7. **Improve Customer Experience**: Faster responses and 24/7 availability for initial support

---

## 4. Business Requirements

### BR-01: Unified AI Chat Interface

**Priority:** Critical  
**Description:** Provide a single AI-powered chat interface as the primary entry point for all support interactions.  
**Business Value:** Centralizes support, ensures consistent experience, and enables automation.  
**Acceptance Criteria:**

- Chat interface accessible via web widget embedded in PartnerHub portal
- Widget loads and initializes within 2 seconds
- Chat supports text input and file attachments
- Session maintains context throughout conversation
- Full chat transcript preserved for ticket creation
- AI disclosure at conversation start (required for legal compliance in multiple US states)

### BR-02: Email Redirect System

**Priority:** High  
**Description:** Automated responses redirect email support requests to the AI chat interface.  
**Business Value:** Funnels email users to the centralized AI system while maintaining communication.  
**Acceptance Criteria:**

- Automated email response sent within 60 seconds of receipt
- Email contains clear instructions and direct link to support assistant
- Link pre-populates any available context from original email
- Original email preserved in support queue for manual review if user doesn't engage
- No AI decision-making in email path (simple automated redirect)

**Client Responsibility:** PartnerHub IT configures the automated email reply. The Contractor provides the redirect URL and suggested email template content.

### BR-03: Initial Support Classification

**Priority:** Critical  
**Description:** Classify customer support needs into three categories via conversational interaction.  
**Business Value:** Enables appropriate workflow routing and information gathering.  
**Acceptance Criteria:**

- AI presents three options: Ask a Question, Request a Change, Report a Problem
- System classifies natural language responses to the appropriate category
- Maximum 3 clarification attempts before escalating to human agent
- Classification decision logged for analytics

### BR-04: Platform Identification

**Priority:** High  
**Description:** Identify whether the customer uses PX or Classic platform for appropriate support routing.  
**Business Value:** Enables platform-specific routing and documentation delivery.  
**Acceptance Criteria:**

- System queries platform mapping database using customer email
- If found, platform type captured automatically without customer interaction
- If not found, AI prompts customer to identify their platform type
- If customer is unsure, AI asks for their portal URL to help identify platform
- Platform type persisted throughout session and included in ticket

### BR-05: Embrace API Integration

**Priority:** Critical  
**Description:** Integrate with Embrace API to provide AI-powered answers and documentation for customer questions and change requests.  
**Business Value:** Enables self-service resolution and deflects routine inquiries from human agents.  
**Acceptance Criteria:**

- Embrace API called with user question, platform type, and user context
- AI-generated answer presented within 10 seconds
- Customer can provide feedback on answer quality
- Customer can ask follow-up questions (multi-turn conversation)
- Customer can request human agent if answer unsatisfactory

### BR-06: Multi-Attempt Embrace Conversations

**Priority:** High  
**Description:** Allow multiple follow-up questions or rephrased queries before agent escalation, with a maximum attempt limit.  
**Business Value:** Maximizes self-service resolution while preventing unproductive loops.  
**Acceptance Criteria:**

- After unsatisfactory answer, customer offered choice to ask follow-up or connect with agent/submit ticket (based on business hours)
- If Embrace cannot answer, customer offered choice to rephrase, ask different question, or connect with agent/submit ticket (based on business hours)
- Maximum 5 Embrace attempts before automatic escalation to live agent (business hours) or ticket submission (after hours)
- After 3rd attempt, soft nudge: "I notice we've tried a few approaches. You can continue trying, or speak with a live agent who might help faster."

### BR-07: Business Hours Live Agent Handoff

**Priority:** High  
**Description:** Offer live agent handoff during business hours when AI cannot resolve the issue.  
**Business Value:** Provides human escalation path while maintaining service quality.  
**Acceptance Criteria:**

- Business hours configurable by administrator
- During business hours: offer live agent option with warm handoff
- Outside business hours: offer ticket submission with SLA information
- Warm handoff includes full chat context passed to agent
- Agent can view complete conversation history before joining

### BR-08: Live Agent Option for Problem Reports

**Priority:** High  
**Description:** Offer live agent option during business hours for problem reports, with appropriate disclaimer.  
**Business Value:** Provides human support for complex issues with clear expectations.  
**Acceptance Criteria:**

- After gathering all problem information, check business hours
- During business hours: offer live agent with disclaimer about potential ticket conversion
- Disclaimer text: "A live agent can gather details of your problem, but resolution may require further work from our team. In that case, your chat will be converted to a ticket and we'll follow up per our normal ticket process and SLAs."
- User can choose live agent or proceed to ticket submission
- Outside business hours: proceed directly to ticket submission

### BR-09: Outage Detection and PagerDuty Integration

**Priority:** Critical  
**Description:** Detect potential outages and trigger PagerDuty alerts via Zendesk.  
**Business Value:** Ensures rapid response to production outages affecting multiple customers.  
**Acceptance Criteria:**

- AI asks outage screening questions: "Are MOST or ALL partners able to login?" and "Are MOST or ALL partners able to register deals?"
- Negative response to either question sets internal "Is Outage" flag to true
- Outage flag passed to Zendesk ticket custom field
- Zendesk automation triggers PagerDuty based on outage flag
- Outage tickets automatically assigned to Tier 1 queue with urgent priority

**Client Responsibility:** PartnerHub configures the Zendesk automation that triggers PagerDuty when "Is Outage" is true. The Contractor ensures the flag is correctly set on tickets.

### BR-10: Classic Platform ASPX Detection

**Priority:** High  
**Description:** Detect Classic customer ASPX page change requests and route to Professional Services.  
**Business Value:** Ensures billable custom development work is properly routed and expectations set.  
**Acceptance Criteria:**

- For Classic customers requesting changes, AI asks for page URL
- If URL contains ".aspx", route to Professional Services workflow
- AI informs customer: "This change involves a custom ASPX page. I'll route this to our Professional Services team."
- Professional Services tickets include disclaimer about potential billing
- SLA for Professional Services tickets: 24 hours

### BR-11: Module-Based Ticket Routing

**Priority:** High  
**Description:** Route tickets to appropriate queues based on PartnerHub module/product.  
**Business Value:** Ensures specialized teams handle module-specific issues efficiently.  
**Acceptance Criteria:**

- AI collects module information: PRM Admin, Partner Portal, Marketing View, News on Demand, Social on Demand, TCMA/FLOW, Amplifinity
- TCMA/FLOW issues routed to TCMA queue (24-hour SLA)
- News on Demand issues routed to NOD queue (24-hour SLA)
- Social on Demand issues routed to SOD queue (24-hour SLA)
- All other modules routed to Tier 1 queue (4-hour SLA)
- Zendesk "Program" field set based on module selection

### BR-12: Problem Information Gathering

**Priority:** High  
**Description:** Systematically gather all required problem report information through conversational prompts.  
**Business Value:** Ensures complete, actionable tickets for the support team.  
**Acceptance Criteria:**

- Required information collected:
  - Environment (PROD, STAGE, DEV)
  - PartnerHub module affected
  - Impacted user information
  - Page URL where issue occurs
  - Steps to replicate the issue
  - Troubleshooting steps already taken
- Optional information offered (customer may skip):
  - File attachments (screenshots, logs)
  - CC email addresses
- AI re-prompts for missing required information (maximum 2 attempts per field)

### BR-13: Change Request Processing

**Priority:** High  
**Description:** Guide customers through change requests with appropriate documentation and routing.  
**Business Value:** Enables self-service for simple changes and proper routing for complex requests.  
**Acceptance Criteria:**

- Embrace provides relevant documentation for self-service
- Customer can ask follow-up questions about documentation
- If customer wants to proceed with formal request, gather:
  - Module/feature affected
  - Detailed description of change
  - File attachments (mockups, workflow diagrams)
  - Time-sensitive event date (if applicable)
- Change request tickets include Professional Services billing disclaimer
- Change requests routed to Tier 1 queue (4-hour SLA)

### BR-14: Zendesk Ticket Creation

**Priority:** Critical  
**Description:** Create properly formatted Zendesk tickets with all gathered information.  
**Business Value:** Integrates with existing support workflow and ensures ticket quality.  
**Acceptance Criteria:**

- Ticket created in Zendesk via API after information gathering complete
- Full chat transcript included in ticket
- Custom fields populated: Environment, Module, Is Outage, Platform Type
- Queue assignment based on routing rules
- SLA timer starts upon ticket creation
- Ticket number returned and displayed to customer
- Attachments uploaded to ticket

### BR-15: Feedback Collection

**Priority:** Medium  
**Description:** Collect customer feedback on support experience.  
**Business Value:** Enables measurement of AI effectiveness and customer satisfaction, with data available for future AI optimization.  
**Acceptance Criteria:**

- Thumbs up/down rating offered at end of all interactions
- Feedback associated with session for analytics
- Feedback collection does not block session completion
- Feedback stored with session context for future analysis
- Data exportable for offline analysis upon request

### BR-16: Session Management and Context

**Priority:** High  
**Description:** Maintain conversation context throughout the support session.  
**Business Value:** Ensures coherent customer experience and complete information capture.  
**Acceptance Criteria:**

- Session persists across temporary disconnections (within 30-minute window)
- All gathered information retained throughout session
- Customer can review/modify previously provided information
- Session timeout warning displayed before expiration
- Incomplete sessions logged for analysis

---

## 5. Use Cases / Business Scenarios

### Use Case 1: Customer Asks a Question (Self-Service Resolution)

**Actor:** Customer (PX Platform)

**Flow:**

1. Customer accesses AI chat via widget in PartnerHub portal
2. AI presents options: Ask a Question, Request a Change, Report a Problem
3. Customer selects "Ask a question"
4. System looks up customer email → finds PX platform type
5. AI prompts: "What's your question?"
6. Customer types question about partner onboarding process
7. System calls Embrace API with question, platform type, and context
8. Embrace returns relevant documentation and answer
9. AI presents answer: "Here is the answer to your question: [EMBRACE CONTENT]. Did this answer your question?"
10. Customer confirms satisfaction
11. AI offers feedback: "Great! Please rate your experience:  "
12. Customer provides thumbs up
13. Chat ends successfully

**Success Outcome:** Question resolved via self-service; no ticket created; positive feedback captured.

---

### Use Case 2: Customer Asks a Question (Escalation to Live Agent)

**Actor:** Customer (Classic Platform)

**Flow:**

1. Customer accesses AI chat via email redirect link
2. AI presents options; customer selects "Ask a question"
3. System looks up customer email → platform not found
4. AI prompts: "Are you using PX or Classic?"
5. Customer responds: "Classic"
6. AI prompts: "What's your question?"
7. Customer asks about custom report configuration
8. System calls Embrace API
9. Embrace cannot find complete answer
10. AI responds: "I couldn't find a complete answer. Would you like to: 1) Rephrase your question, 2) Ask a different question, 3) Speak with a live agent"
11. Customer selects "Speak with a live agent"
12. System checks business hours → during business hours
13. AI offers live agent: "Would you like to chat with a live human agent now?"
14. Customer confirms
15. Warm handoff initiated; live agent joins with full context
16. Live agent resolves issue

**Success Outcome:** Customer escalated to human agent with full context; agent resolves without re-gathering information.

---

### Use Case 3: Customer Reports a Problem (Outage Detected)

**Actor:** Customer (PX Platform)

**Flow:**

1. Customer accesses AI chat; selects "Report a Problem"
2. AI gathers information:
   - Environment: "Production"
   - Module: "Partner Portal"
   - Impacted user: "All partners in our organization"
   - Page URL: "https://partners.acme.partnerhubprm.com/login"
3. AI asks: "Are MOST or ALL of your partners able to login to the partner portal at this time?"
4. Customer responds: "No, none of them can login"
5. System sets Is Outage = True internally, triggers PagerDuty via Zendesk
6. AI continues gathering: steps to replicate, troubleshooting steps, attachments
7. System checks business hours → during business hours
8. AI offers: "Would you like to report your problem to a live support agent? Note: A live agent can gather details, but resolution may require further work..."
9. Customer declines live agent, prefers ticket
10. System creates Zendesk ticket with:
    - Is Outage = True
    - Priority = Urgent
    - Queue = Tier 1
    - Full chat transcript
11. AI confirms: "Your support ticket has been created! Ticket #12345. Expected response time: 4 hours."
12. PagerDuty alert sent to on-call engineer

**Success Outcome:** Outage detected and escalated; PagerDuty notified; customer informed of ticket creation.

---

### Use Case 4: Classic Customer Requests ASPX Page Change

**Actor:** Customer (Classic Platform)

**Flow:**

1. Customer accesses AI chat; selects "Request a Change"
2. System identifies Classic platform
3. Embrace provides relevant documentation for self-service
4. Customer indicates they want to proceed with formal change request
5. AI asks: "What is the URL of the page where you want to make this change?"
6. Customer provides: "https://classic.partnerhub.com/custom/reports.aspx"
7. System detects ".aspx" in URL
8. AI responds: "I see this change involves a custom ASPX page. I'll need to gather some additional details to route this to our Professional Services team."
9. AI gathers: environment, impacted user, detailed change description, attachments
10. System creates ticket with:
    - Queue = Professional Services
    - SLA = 24 hours
    - Classic platform flag
    - ASPX page URL
11. AI confirms: "Your Professional Services request has been created! Ticket #12346. Expected response time: 24 hours. Note: This request is subject to our Professional Services policy and may be billable."

**Success Outcome:** Custom development request properly routed to Professional Services with billing expectation set.

---

### Use Case 5: Customer Requests Change (Self-Service via Documentation)

**Actor:** Customer (PX Platform)

**Flow:**

1. Customer accesses AI chat; selects "Request a Change"
2. System identifies PX platform
3. AI calls Embrace with change request description
4. Embrace returns relevant documentation for configuring the feature
5. AI presents: "I recognize your change is on one of our core functionalities. I've provided some documentation that may help you self-serve: [DOCUMENTATION]. Is there anything else I can help you with?"
6. Customer reviews documentation and realizes they can make the change themselves
7. Customer responds: "No, that documentation answered my question"
8. AI offers feedback rating
9. Customer provides positive feedback
10. Chat ends successfully

**Success Outcome:** Customer empowered to self-serve; no ticket created; support workload reduced.

---

## 6. Business Rules

### BR-RULE-01: Email Redirect Only

All email-initiated support requests receive automated redirect response to AI chat. No AI processing occurs on email content. Original email preserved in queue for manual review if customer doesn't engage with chat.

### BR-RULE-02: Platform Lookup First

For all support paths requiring platform context, system must attempt platform lookup via email before prompting customer. Manual identification only if lookup fails.

### BR-RULE-03: Embrace Before Escalation

For "Ask a Question" and "Request a Change" paths, Embrace API must be called before offering live agent escalation. Customers must explicitly request human agent or indicate dissatisfaction with the Embrace answer.

### BR-RULE-04: Multi-Attempt Embrace Loop

Customers may ask up to 5 follow-up questions to Embrace. After 3 attempts, system displays a soft nudge suggesting live agent option. After 5 attempts without resolution, system automatically routes to live agent (business hours) or ticket submission (after hours). Customer can request human assistance at any point.

### BR-RULE-05: Business Hours Live Agent Availability

Live agent handoff offered only during configured business hours. Outside business hours, ticket submission is the only option. Business hours configurable per time zone.

### BR-RULE-06: Outage Detection Criteria

Outage flag set to true when customer indicates MOST or ALL partners cannot:

- Login to partner portal, OR
- Register deals in partner portal

Outage flag triggers Zendesk automation → PagerDuty alert.

### BR-RULE-07: ASPX Page Routing

For Classic platform change requests where URL contains ".aspx", route to Professional Services queue. Non-ASPX Classic changes and all PX changes route through standard change request workflow.

### BR-RULE-08: Module-Based Queue Assignment

| Module                                                              | Queue        | SLA      |
| ------------------------------------------------------------------- | ------------ | -------- |
| TCMA/FLOW                                                           | TCMA Queue   | 24 hours |
| News on Demand                                                      | NOD Queue    | 24 hours |
| Social on Demand                                                    | SOD Queue    | 24 hours |
| All Others (PRM Admin, Partner Portal, Marketing View, Amplifinity) | Tier 1 Queue | 4 hours  |

Outage tickets always route to Tier 1 with urgent priority regardless of module.

### BR-RULE-09: Required vs Optional Information

**Required (must collect before ticket creation):**

- Environment
- Module
- Impacted user (for problems)
- Page URL (for problems)
- Steps to replicate (for problems)

**Optional (offer but don't require):**

- Troubleshooting steps taken
- File attachments
- CC email addresses
- Time-sensitive event date (for changes)

### BR-RULE-10: Professional Services Disclaimer

All change request tickets must include disclaimer: "Change requests are subject to our Professional Services policy and may be billable." Professional Services (ASPX) tickets include the same disclaimer.

### BR-RULE-11: Session Timeout

Sessions timeout after 30 minutes of inactivity. Warning displayed at 25 minutes. Incomplete sessions logged but no ticket created. Customer can start new session at any time.

### BR-RULE-12: Feedback Collection

Feedback rating offered at conclusion of all interactions (successful resolution, ticket creation, live agent handoff). Feedback is optional and does not block session completion.

---

## 7. Assumptions and Dependencies

### Assumptions

1. **User Access**: Customers have internet access and modern web browsers capable of running chat widget
2. **Email Access**: Customers check email and can click links to access chat interface
3. **Embrace Quality**: Embrace API returns relevant, accurate documentation for PartnerHub products
4. **Business Hours**: Support team maintains consistent business hours for live agent availability
5. **Platform Data**: Customer-to-platform mapping data is maintained and reasonably complete
6. **Zendesk Configuration**: Custom fields, triggers, and PagerDuty integration are configured
7. **Agent Training**: Support agents trained on handling warm handoffs from AI chat

### Dependencies

1. **Embrace API**: Depends on API availability, quality of indexed documentation, and response time < 10 seconds

2. **Zendesk**: Depends on API access/credentials, custom field configuration (Is Outage, Program, Platform Type), and PagerDuty integration trigger

3. **Platform Mapping Data**: Depends on email-to-platform mapping database and regular data updates from PartnerHub

4. **Hosting Infrastructure**: Depends on Railway hosting, PostgreSQL database service, and Cloudflare/CDN for widget delivery

5. **AI Services**: Depends on AI model API availability and sufficient rate limits (model selection and cost analysis in TRD)

---

## 8. Exclusions (Out of Scope)

### Explicitly Excluded from MVP

1. **Billing Determination** - No automated billing assessment or Professional Services approval workflows; billing handled by human agents post-ticket creation

2. **Analytics Dashboards** - No dashboards or reporting UI; all data (conversations, feedback, sessions) stored in database and directly accessible

3. **Voice Support** - Text chat only; no voice recognition or phone integration

4. **Mobile Application** - Web widget only; no native iOS/Android apps

5. **Proactive Support** - No outbound notifications or proactive outage alerts; reactive support only

6. **Multi-Language** - English only; no translation or localization

7. **Offline Mode** - Requires internet connection; no offline caching or queue

8. **CSM Workflow Integration** - CSM-initiated tickets remain separate; no AI involvement in CSM path

9. **Custom AI Training** - Uses existing AI models; no fine-tuning on PartnerHub-specific data

10. **Third-Party Integrations** - Zendesk only; no Salesforce, HubSpot, or other CRM integration

---

## 9. High-Level Risks

### Risk 1: Embrace API Quality and Relevance

**Description:** Embrace may return irrelevant or incorrect answers, reducing trust in the AI system.  
**Mitigation:** Feedback mechanism; monitor answer quality; easy escalation to human agent; regular review of low-rated interactions.  
**Impact:** High - affects core value proposition  
**Priority:** Address through monitoring and feedback loops

### Risk 2: Customer Adoption and Trust

**Description:** Customers may resist AI-driven support and demand immediate human agent access.  
**Mitigation:** Clear path to human agent; high-quality AI responses; feedback-driven improvements; communicate value of AI assistance.  
**Impact:** Medium - affects deflection goals  
**Priority:** Monitor adoption metrics; adjust messaging as needed

### Risk 3: Platform Mapping Data Completeness

**Description:** Incomplete email-to-platform mapping may require manual identification, adding friction.  
**Mitigation:** Graceful fallback to manual identification; work with PartnerHub to improve data coverage; track lookup success rate.  
**Impact:** Medium - affects user experience  
**Priority:** Monitor and improve data quality

### Risk 4: Business Hours Coverage

**Description:** Customers outside business hours cannot access live agents, causing potential frustration.  
**Mitigation:** Clear business hours communication; comprehensive ticket submission option; SLA commitments honored.  
**Impact:** Medium - affects customer satisfaction  
**Priority:** Consider extended hours if demand warrants

### Risk 5: Integration Complexity

**Description:** Zendesk and Embrace API integrations may have unexpected issues or limitations.  
**Mitigation:** Thorough API testing; graceful error handling; fallback to manual processes; monitoring and alerting.  
**Impact:** High - affects core functionality  
**Priority:** Comprehensive testing before launch

### Risk 6: Outage Detection Accuracy

**Description:** False positives (triggering PagerDuty for non-outages) or false negatives (missing real outages).  
**Mitigation:** Clear screening questions; human agent validation before major escalation; feedback loop for detection improvement.  
**Impact:** High - affects operational response  
**Priority:** Careful question design and monitoring

### Risk 7: Session State Loss

**Description:** Technical issues may cause loss of conversation context, requiring customers to repeat information.  
**Mitigation:** Robust session persistence; automatic save of gathered information; graceful disconnection recovery.  
**Impact:** Medium - affects user experience  
**Priority:** Implement reliable session management

---

## 10. Approvals

| Name                | Role                       | Signature | Date |
| :------------------ | :------------------------- | :-------- | :--- |
| Client Stakeholder  | PartnerHub Support Director |           |      |
| Client Stakeholder  | PartnerHub Executive        |           |      |
| The Contractor PM        | Project Manager            |           |      |
| The Contractor Tech Lead | Technical Authority        |           |      |

---

## Appendix A: Workflow Diagram Reference

Complete support workflow documented in:

- **[Unified Support Workflow](../project-docs/support-flow-charts/unified-support-workflow.md)**

### Key Workflow Features

1. **Three Entry Paths**: Email (redirect), Direct Chat
2. **Three Support Types**: Ask a Question, Request a Change, Report a Problem
3. **Platform Identification**: Automatic lookup or manual prompt
4. **Embrace Integration**: AI-powered documentation search
5. **Multi-Attempt Conversations**: Follow-up questions before escalation
6. **Live Agent Handoff**: During business hours on all paths
7. **Outage Detection**: Automatic PagerDuty triggering
8. **Module-Based Routing**: TCMA, NOD, SOD, Tier 1 queues
9. **Feedback Collection**: Thumbs up/down on all paths

---

## Appendix B: Terminology Reference

| Term             | Definition                                                                  |
| ---------------- | --------------------------------------------------------------------------- |
| **PX**           | Partner Experience - PartnerHub's modern SaaS platform                       |
| **Classic**      | Legacy PartnerHub platform with custom ASPX pages                            |
| **ASPX**         | Active Server Pages Extended - custom pages requiring Professional Services |
| **Embrace**      | PartnerHub's AI-powered documentation and knowledge system                   |
| **Tier 1 Queue** | First-level support queue for standard issues (4-hour SLA)                  |
| **Tier 2 Queue** | Technical queue for code-related issues (8-hour SLA)                        |
| **NOD**          | News on Demand - specialized content module                                 |
| **SOD**          | Social on Demand - specialized social media module                          |
| **TCMA**         | Through-Channel Marketing Automation - marketing automation module          |
| **Warm Handoff** | Live agent joins conversation with full context from AI chat                |
| **Deflection**   | Customer issue resolved without human agent involvement                     |
| **SLA**          | Service Level Agreement - response time commitment                          |
| **PagerDuty**    | Incident alerting system for outages                                        |

---

## Appendix C: Document Revision History

| Version | Date                 | Author                              | Description of Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------- | -------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1.0** | **December 2024**    | **The Contractor - Applied Engineering** | **Initial document creation with basic requirements for AI support agent.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **2.0** | **December 4, 2025** | **The Contractor - Applied Engineering** | **Complete rewrite incorporating updated workflow. Added: Multi-attempt Embrace conversations (BR-06), Live agent option for all paths including Report a Problem (BR-08), Email redirect as automated system not AI (BR-02), ASPX page detection (BR-10), Module-based routing (BR-11), Detailed use cases, Complete business rules, Updated terminology and appendices. Aligned with unified_support_workflow.mmd diagram. Clarified success metrics as The Contractor recommendations. Removed model-specific references (to be decided in TRD).** |

---

**Document Status**:  **Version 2.0 - Draft** - Pending Client Approval

---

**Document End**

_Technical specifications, architecture decisions, and implementation details will be defined in the companion Technical Requirements Document (TRD)._
