# Product Management Portfolio

A collection of product documentation from AI and technology projects I've managed as Product Manager at The Contractor. Each project demonstrates end-to-end product leadership — from discovery and requirements through technical architecture and delivery.

> **Note:** All client names, company names, and identifying information have been anonymized to protect client confidentiality.

---

## Projects

### 1. [ReadAssist AI](./01-readassist-ai/) — AI-Powered Reading Fluency Assessment

An AI-driven reading assessment tool for K-5 classrooms that automates fluency evaluation using speech-to-text, pronunciation scoring, and LLM-powered feedback.

**Key highlights:**
- Integrated three AI services (Deepgram STT, SpeechAce pronunciation scoring, Gemini LLM) into a cohesive assessment pipeline
- Designed real-time metrics system tracking WCPM, accuracy, and fluency at sentence and paragraph level
- Built teacher dashboard with per-student analytics, exportable CSV reports, and AI-generated feedback

**Tech stack:** Cloudflare Workers, Remix, D1, KV, Deepgram, SpeechAce, Gemini, LangSmith

**Documents:** [Business Requirements](./01-readassist-ai/business-requirements.md) · [Technical Requirements](./01-readassist-ai/technical-requirements.md) · [Product Documentation](./01-readassist-ai/product-documentation.md) · [App Walkthrough](./01-readassist-ai/app-walkthrough.md)

---

### 2. [PartnerHub Support Agent](./02-partnerhub-support-agent/) — AI Customer Support Automation

An AI-powered support agent that handles tier-1 customer inquiries through an embeddable chat widget, with intelligent routing to human agents and seamless CRM integration.

**Key highlights:**
- Designed multi-channel support flow (chat, email, web form) with AI triage and automated ticket creation
- Defined state machine architecture for conversation management with context-aware responses
- Planned integration with Zendesk and existing CRM, including knowledge base indexing

**Tech stack:** Next.js, XState, OpenAI, Zendesk API, Railway

**Documents:** [Business Requirements](./02-partnerhub-support-agent/business-requirements.md) · [Technical Requirements](./02-partnerhub-support-agent/technical-requirements.md)

---

### 3. [CreativeBooks Platform](./03-creativebooks-platform/) — AI-Generated Personalized Children's Books

A self-service web platform enabling parents to create personalized ABC coloring books using AI-powered photo-to-line-art conversion and theme-based content generation.

**Key highlights:**
- Designed AI pipeline for photo upload → line art conversion → theme matching → book assembly
- Built quality validation system with automatic regeneration for failed AI outputs
- Planned multi-phase roadmap from MVP (single book) to platform (library, subscriptions, marketplace)

**Tech stack:** Next.js, tRPC, Supabase, Replicate (Nano-Banana), Stripe, PDF generation

**Documents:** [Business Requirements](./03-creativebooks-platform/business-requirements.md) · [Technical Requirements](./03-creativebooks-platform/technical-requirements.md) · [Platform Documentation](./03-creativebooks-platform/platform-documentation.md)

---

### 4. [LegacyVoice](./04-legacyvoice/) — AI-Powered Family Storytelling Platform

A mobile-first platform for preserving family stories through guided daily storytelling exercises, AI coaching, and shareable video narratives.

**Key highlights:**
- Designed hybrid BRD/PRD covering full product scope with 14 business requirements and acceptance criteria
- Architected phone-call-based recording flow using Twilio with AI transcription and coaching
- Planned CMS for non-technical content team to manage daily lessons without developer support

**Tech stack:** Next.js 15, Supabase, Twilio, ElevenLabs STT/TTS, Mux, OpenAI, QStash

**Documents:** [Product Requirements](./04-legacyvoice/product-requirements.md) · [Technical Requirements](./04-legacyvoice/technical-requirements.md) · [Product Blueprint](./04-legacyvoice/product-blueprint.md)

---

### 5. [SolarGrid Platform](./05-solargrid-platform/) — Energy Monitoring & Analytics Dashboard

A platform rebuild for real-time energy monitoring, aggregating data from solar inverters, batteries, and grid connections into actionable dashboards for energy companies.

**Key highlights:**
- Led discovery and blueprint for complex IoT data platform with multi-inverter scenarios
- Defined data architecture for time-series telemetry with configurable alerting
- Mapped integration requirements for external data sources and real-time monitoring

**Tech stack:** ETL pipelines, time-series databases, dashboard visualization

**Documents:** [Product Blueprint](./05-solargrid-platform/product-blueprint.md)

---

### 6. [BlueLake Data Integration](./06-bluelake-data-integration/) — Financial Data Pipeline & Reporting

An automated data integration platform connecting portfolio management systems with cloud storage, enabling asynchronous report generation and delivery for investment operations.

**Key highlights:**
- Designed async polling architecture for reliable report generation with status tracking
- Planned multi-environment deployment (development, production) with separate data pipelines
- Documented complete handoff including architecture, API server, and operational procedures

**Tech stack:** Python, Power Automate, Power Apps, cloud file storage APIs

**Documents:** [Architecture Overview](./06-bluelake-data-integration/architecture-overview.md)

---

### 7. [ZenWell AI Agent](./07-zenwell-ai-agent/) — Holistic Wellness AI Companion

A holistic AI wellness agent providing personalized health guidance across nutrition, fitness, mental health, and lifestyle through conversational AI.

**Key highlights:**
- Conducted full project evaluation with risk assessment (scored 25/32) and effort estimation (545–735 hours)
- Recommended phased delivery approach to manage scope and validate product-market fit
- Defined 10 MVP deliverables spanning AI agent, user profiles, and wellness tracking

**Documents:** [Project Brief](./07-zenwell-ai-agent/project-brief.md) · [Project Evaluation](./07-zenwell-ai-agent/project-evaluation.md)

---

## Skills Demonstrated

| Capability | Evidence |
|---|---|
| **Product Discovery** | Blueprints, BRDs, and PRDs for all 7 projects |
| **Technical Architecture** | TRDs with system diagrams, data models, and API design |
| **AI/ML Product Management** | Integration of LLMs, STT, TTS, image generation, and AI coaching |
| **Stakeholder Management** | Multi-stakeholder requirements across education, finance, energy, and SaaS |
| **Delivery Planning** | Cycle-based roadmaps, sprint plans, and cost analyses |
| **Cross-Domain Expertise** | EdTech, FinTech, Energy/IoT, SaaS, Consumer, and Wellness |
