# ReadAssist AI - Business Requirements Document (BRD)

## 1. Cover Page

| Field               | Details                                                   |
| ------------------- | --------------------------------------------------------- |
| **Project Name**    | ReadAssist AI -- Reading Fluency Assessment (Proof of Concept) |
| **Client**          | ReadAssist EdTech                                            |
| **Document Author** | The Contractor                             |
| **Date**            | November 18, 2025                                         |
| **Version**         | 2.2                                                       |
| **Status**          | Final Draft                                               |

---

## 2. Introduction

### 2.1 Document Purpose

This Business Requirements Document (BRD) defines the business needs,
functional requirements, and success criteria for the **ReadAssist AI Reading
Fluency Assessment Proof of Concept (PoC)**.
The goal of this document is to serve as the foundation for development,
testing, and validation of a standalone AI-powered assessment system
that automates and enhances reading fluency evaluations in classroom
environments.

### 2.2 Project Scope

**In Scope (for PoC):**

- Development of a **standalone web-based PoC platform** accessible on Chromebooks.
- Dual speech-to-text (STT) provider integration (Deepgram and SpeechAce) for A/B testing and comparative analysis.
- Integration of **existing AI models** for speech recognition and fluency analysis.
- AI-guided reading assessment where the system listens to the student's reading and provides feedback after processing.
- Teacher observation interface to allow **post-assessment comments and feedback.**
- Data collection for comparison between **AI-assessed and teacher-assessed results.**
- Data storage during POC period for teacher review and export. Data retention and deletion decisions are at ReadAssist's discretion.
- Audio files are deleted immediately after STT processing. Only anonymized metrics, scores, transcriptions, and feedback (from STT providers, LLM, and teachers) are retained.
- LangSmith integration for comprehensive tracing of all STT and LLM interactions.
- LangSmith Prompt Hub integration enabling web-based prompt management by educational stakeholders.
- Observability infrastructure for iterative LLM prompt optimization.
- Progressive sentence accumulation reading methodology.
- Adaptive word-level feedback and review system.
- Per-reading-step performance metrics collection.
- Attempt limiting with automatic progression.

**Out of Scope:**

- Integration with the existing ReadAssist EdTech application.
- Advanced analytics dashboards or scoring visualizations.
- Development of proprietary AI models or training pipelines.
- Production-level performance SLAs.
- Mobile app version.
- Multi-language or multi-accent support.
- Offline use cases.
- Test creation or editing interface.
- Teacher account registration or management UI.
- Class creation or student enrollment UI.
- User authentication system (login/logout).
- Student profile management.
- Test assignment workflow UI.
- Real-time teacher monitoring of in-progress attempts.
- Support for more than 5 teachers or 5 classes.
- Administrator or admin role and interfaces.
- Long-term data retention or archival systems.
- Phoneme-level pronunciation analysis.
- Interactive word correction exercises beyond simple acknowledgment.
- AI-generated audio pronunciation modeling.

### 2.3 Audience

This document is intended for:

- ReadAssist EdTech Product and Technical Stakeholders.
- The Contractor Project Management and Engineering Teams.
- Quality Assurance and Test Engineers.
- Future Product and Educational Research Stakeholders.

---

## 3. Business Context

### 3.1 Background

ReadAssist EdTech has developed a proven literacy platform serving
thousands of students. Reading fluency assessments are currently
conducted manually by teachers, consuming hours of instructional time
and producing inconsistent results due to human fatigue and
subjectivity.

The target user population is K-12 students (ages 5-18), encompassing a wide range of reading proficiency levels from early literacy to advanced comprehension.

The company aims to validate an **AI-driven fluency assessment system**
that reduces teacher workload, ensures consistency, and delivers faster,
more actionable feedback to students and educators alike.

### 3.2 Problem to Solve

Manual reading fluency assessments:

- Require significant teacher time (up to 3 hours per cycle).
- Create inconsistent scoring and feedback quality.
- Delay student progress due to lack of immediate insights.

### 3.3 Business Objectives

1. Prove the **technical feasibility and classroom viability** of an AI-driven reading fluency solution.
2. Measure accuracy, efficiency, and consistency compared to human assessments.
3. Validate user experience and AI usability through real-life testing.
4. Collect data to inform an **investment decision** for MVP and full-scale implementation.
5. Conduct comprehensive A/B testing between two STT providers (Deepgram and SpeechAce) to inform data-driven MVP technology decisions.

### 3.4 Success Metrics

- A functional PoC platform is deployed and accessible from Chromebooks in testing schools.
- Minimum **25 real classroom assessments** completed across multiple classrooms and tests using both AI providers simultaneously.
- Data collected and analyzed to measure accuracy, usability, and efficiency gains.
- Comparative data collected from both STT providers for 100% of attempts, enabling quantitative A/B analysis.
- Teacher CSV exports demonstrate usability of data collection system.
- LangSmith tracing captures 100% of POC attempts with complete metadata.
- LangSmith provides sufficient tools and observability for ReadAssist team to optimize and increase performance of prompts.
- Findings documented in a subsequent **Product Requirements Document (PRD)** to guide MVP development.

---

## 4. Business Requirements

| ID        | Priority | Requirement                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Business Value                                                                                                                                                                                                  | Acceptance Criteria                                                                                                                                                                                                                                                                                                 |
| --------- | -------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BR-01** | Critical | AI Listening and Evaluation                   | The system listens as the student reads text aloud and performs AI-based analysis using two STT providers simultaneously for comparative evaluation. Student receives AI-generated feedback based on analysis results.                                                                                                                                                                                                                                                                                                                                                   | Enables automation of teacher-led assessment with comprehensive provider comparison.                                                                                                                            | Student audio captured; both STT providers generate fluency scores/feedback.                                                                                                                                                                                                                                        |
| **BR-02** | High     | Baseline Attempt and Feedback Loop            | Students build reading fluency progressively by accumulating sentences (reading sentence 1, then sentences 1+2, then 1+2+3, etc.). At each reading step, the AI provides feedback and allows retries. Configurable retry limit per reading step prevents extended frustration while maintaining engagement.                                                                                                                                                                                                                                                              | Validates progressive fluency building methodology and reinforces learning through iterative feedback.                                                                                                          | Student progresses through accumulated sentence readings; AI provides feedback when fluency threshold not met; Student can retry at each reading step; Configurable maximum attempts per reading step enforced; Auto-progression after maximum attempts reached.                                                    |
| **BR-03** | High     | Teacher Feedback Interface                    | Teachers observe the session and can leave qualitative comments post-assessment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Keeps teacher involvement for oversight and human insight.                                                                                                                                                      | Teacher can enter feedback after session completion.                                                                                                                                                                                                                                                                |
| **BR-04** | Medium   | Session Tracking and Data Storage             | Session data is stored during the POC period to enable teacher review, feedback, and CSV export. Audio files are deleted immediately after STT processing. Only anonymized metrics (WCPM, accuracy), transcriptions, and feedback from STT providers, LLM, and teachers are retained.                                                                                                                                                                                                                                                                                    | Ensures accountability and controlled test data.                                                                                                                                                                | Session metadata stored for evaluation; audio files deleted immediately.                                                                                                                                                                                                                                            |
| **BR-05** | Critical | Standalone Platform                           | The PoC must operate independently of ReadAssist's main app while allowing future integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Simplifies testing and scalability.                                                                                                                                                                             | Accessible as independent web app; modular for future integration.                                                                                                                                                                                                                                                  |
| **BR-06** | High     | Chromebook Compatibility                      | The system must function reliably in web browsers on Chromebooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Supports real classroom environments.                                                                                                                                                                           | Verified across school devices and browsers.                                                                                                                                                                                                                                                                        |
| **BR-07** | High     | Whitelisting and Firewall Access              | The platform must be whitelisted by school networks for accessibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Ensures reliable access during testing.                                                                                                                                                                         | Tested and confirmed in school firewall configurations.                                                                                                                                                                                                                                                             |
| **BR-08** | Medium   | Concurrency Support                           | System supports up to 100 simultaneous sessions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Allows multi-classroom testing during pilot.                                                                                                                                                                    | Performance verified with concurrent users.                                                                                                                                                                                                                                                                         |
| **BR-09** | Medium   | Comparative Data Collection                   | Collect comparative data between both STT providers, as well as between AI-generated and teacher-provided feedback, to inform ROI projections and technology selection decisions.                                                                                                                                                                                                                                                                                                                                                                                        | Enables investment and product decision-making.                                                                                                                                                                 | Matching datasets collected for analysis.                                                                                                                                                                                                                                                                           |
| **BR-10** | Critical | Privacy Compliance                            | Audio files deleted immediately after processing. Only anonymized assessment metrics, scores, transcriptions, and feedback retained. No personally identifiable information (PII) stored. ReadAssist obtains all required permissions to comply with COPPA.                                                                                                                                                                                                                                                                                                                   | Guarantees legal compliance and child safety.                                                                                                                                                                   | Verified compliance statement and zero PII persistence.                                                                                                                                                                                                                                                             |
| **BR-11** | High     | Multiple Pre-Configured Reading Tests         | The system shall include three distinct reading assessments. Each test will consist of a reading passage divided into individual sentences, fluency and accuracy score thresholds, and a maximum retry limit per reading step provided by ReadAssist's educational team.                                                                                                                                                                                                                                                                                                      | Enables assessment across different reading proficiency levels aligned with ReadAssist's educational framework.                                                                                                      | Three tests configured with ReadAssist-provided content and thresholds; Test content structured as individual sentences for progressive reading; no test creation interface in POC.                                                                                                                                      |
| **BR-12** | Critical | POC Configuration and URL-Based Access Model  | The system shall be pre-configured by the development team to support a maximum of five teachers and five classes, with all teacher and class information provided by ReadAssist. Access is provided through pre-configured URLs containing test and class identifiers. The development team will provide ready-to-use URLs to ReadAssist for distribution to educators and students. Backend data structures maintain separation between classes.                                                                                                                                 | Eliminates complex user management overhead; accelerates POC deployment while maintaining data integrity across multiple classrooms.                                                                            | Maximum 5 teachers and 5 classes supported; URL-based access functional; data correctly segregated by class; URLs provided to ReadAssist team; teacher views limited to assigned class.                                                                                                                                  |
| **BR-13** | Critical | Dual Speech Recognition Provider Evaluation   | Each student attempt shall be analyzed simultaneously by both STT providers. Results from both systems shall be captured and presented to teachers for comparative evaluation.                                                                                                                                                                                                                                                                                                                                                                                           | Generates comprehensive comparative data to inform cost-effective, high-accuracy provider selection for MVP.                                                                                                    | Both providers process all attempts; comparative results displayed to teachers; data stored for analysis.                                                                                                                                                                                                           |
| **BR-14** | High     | AI-Generated Feedback with Teacher Validation | The system shall generate student-facing feedback using AI language models and present it to teachers for review. Teachers may add qualitative observations. Both AI-generated and teacher-provided feedback shall be captured.                                                                                                                                                                                                                                                                                                                                          | Validates AI feedback quality against educator expertise; combines automation efficiency with human pedagogical insight.                                                                                        | AI feedback generated and visible; teacher feedback capturable; both stored for comparison.                                                                                                                                                                                                                         |
| **BR-15** | High     | Prompt Observability and Tracing              | The system shall implement comprehensive tracing and metadata capture for all AI interactions during the POC period to enable workflow optimization. This includes: (1) Complete tracing of STT API interactions with raw outputs from both providers, (2) Full LLM request/response logging including input prompts and generated outputs, (3) LLM reasoning and processing traces for debugging. The system shall enable non-technical educational stakeholders to iteratively refine LLM prompts through LangSmith's Playground interface without code modifications. | Enables data-driven optimization of AI accuracy and feedback quality. Empowers educational experts to iterate on prompts independently. Provides comprehensive audit trail for POC validation and ROI analysis. | All STT and LLM interactions traced in LangSmith with complete request/response data. ReadAssist team can modify and deploy prompts via LangSmith Playground UI. Development team demonstrates trace query workflow.                                                                                                     |
| **BR-16** | Critical | Adaptive Word-Level Feedback                  | When student performance falls below fluency/accuracy thresholds, the system identifies and highlights specific mispronounced words within the reading text. Students must acknowledge review of each highlighted word before being permitted to retry the reading step. System provides age-appropriate instruction and encouragement during the review process.                                                                                                                                                                                                        | Provides targeted intervention without complex phoneme analysis infrastructure; maintains student focus on specific improvement areas; validates effectiveness of word-level feedback in POC environment.       | Mispronounced words identified from STT analysis; Words highlighted within reading text for student visibility; Student interaction required to acknowledge word review; Retry disabled until all words reviewed; Age-appropriate instructional guidance displayed; Word review data captured for teacher analysis. |
| **BR-17** | High     | Reading Step Metrics Granularity              | System captures detailed performance metrics for each reading step within an assessment attempt. Metrics include fluency percentage, accuracy percentage, words per minute, retry attempt count, and identified problem words. Data is structured to enable teacher analysis of student progression through the reading assessment.                                                                                                                                                                                                                                      | Enables granular analysis of where students succeed or struggle; informs targeted intervention strategies; validates progressive building methodology effectiveness.                                            | Performance metrics captured per reading step; Metrics include fluency %, accuracy %, WPM, retry count, highlighted words; Data from both STT providers captured per step; Teacher dashboard displays per-step breakdown.                                                                                           |

---

## 5. Use Cases / Business Scenarios

### Use Case 1: Student Completes AI-Guided Assessment

**Actor:** Student

**Flow:**

1. Student accesses pre-configured URL provided by teacher (contains test identifier and class identifier)
2. System displays assigned reading passage
3. Student reads aloud while system captures audio
4. System processes audio through both STT providers simultaneously
5. AI analyzes results and provides feedback after processing
6. If student fails to meet threshold, system highlights mispronounced words. Student reviews highlighted words and retries (up to configurable maximum attempts per reading step). System automatically progresses after maximum attempts reached.
   6.5. Student builds reading fluency progressively through sentence accumulation, receiving targeted feedback at each step.
7. After successfully completing all accumulated sentence readings, student reads the complete paragraph two additional times to demonstrate mastery and fluency consistency.
8. Session automatically concludes; results stored

**Success Outcome:** Student receives timely feedback; dual provider data collected without user awareness

---

### Use Case 2: Teacher Reviews Assessment Data and Exports Results

**Actor:** Teacher

**Flow:**

1. Teacher accesses class-specific dashboard URL provided by development team
2. System displays all student attempts for assigned class
3. Teacher selects individual attempt to review details
4. System presents side-by-side comparison of STT provider results (WCPM, accuracy, transcription)
5. Teacher reviews AI-generated student feedback
6. Teacher adds qualitative observations and pedagogical notes
7. System saves teacher feedback for comparative analysis
8. Teacher exports complete class data as CSV file for external analysis
9. CSV includes all attempts with dual STT metrics, AI feedback, and teacher notes

**Success Outcome:** Teacher validates AI accuracy; provides human expertise data; comparative STT performance captured; teacher can analyze data offline or share with ReadAssist team

---

## 6. Business Rules

| ID                              | Rule                                    | Description                                                                                                                                                                                                                            |
| ------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BR-RULE-01**                  | One baseline attempt per session        | Each session starts with an initial reading baseline.                                                                                                                                                                                  |
| **BR-RULE-02**                  | Retry until fluency threshold met       | Student can retry each reading step up to a configurable maximum number of attempts per step. After maximum attempts reached, system automatically progresses to next reading step regardless of score to prevent student frustration. |
| **BR-RULE-03**                  | Teacher feedback post-session           | Teachers can add notes only after AI session completion.                                                                                                                                                                               |
| **BR-RULE-04**                  | POC-Limited Data Retention              | Audio files deleted immediately after STT processing. Only anonymized metrics, transcriptions, and feedback stored during POC for teacher analysis and export.                                                                         |
| **BR-RULE-05**                  | COPPA compliance                        | ReadAssist must manage consent and legal authorization under COPPA.                                                                                                                                                                         |
| **BR-RULE-06 (Created by GPT)** | AI feedback consistency                 | AI responses should maintain consistent tone regardless of accent or speed.                                                                                                                                                            |
| **BR-RULE-07 (Created by GPT)** | Age-appropriate language                | All feedback must be encouraging and suitable for children aged 5-18 (K-12).                                                                                                                                                           |
| **BR-RULE-08**                  | URL-Based Access Only                   | Pre-configured URLs control all access; no user registration or login interface required.                                                                                                                                              |
| **BR-RULE-09**                  | Maximum POC Capacity                    | System limited to 5 teachers, 5 classes, and 3 tests for POC scope.                                                                                                                                                                    |
| **BR-RULE-10**                  | Dual Provider Processing                | All attempts must be processed by both STT providers for comparative data collection.                                                                                                                                                  |
| **BR-RULE-11**                  | Pre-Configuration Requirement           | All tests, teachers, and classes configured by development team prior to classroom deployment.                                                                                                                                         |
| **BR-RULE-12**                  | ReadAssist-Provided Content                  | Test passages (structured as individual sentences), fluency score thresholds, accuracy thresholds, and maximum retry attempts per reading step determined by ReadAssist educational team.                                                   |
| **BR-RULE-13**                  | Teacher Data Export                     | Teachers can export their class data as CSV for offline analysis and sharing with ReadAssist team.                                                                                                                                          |
| **BR-RULE-14**                  | LLM Feedback Storage and Teacher Review | AI-generated feedback must be stored before teacher review. Teachers must review AI feedback before adding their own observations. Both AI and teacher feedback must be retained for comparative analysis.                             |
| **BR-RULE-15**                  | Comprehensive API Tracing               | All external API interactions (both STT providers and LLM) must be traced with complete request/response payloads during POC period for optimization analysis.                                                                         |
| **BR-RULE-16**                  | Prompt Hub Management                   | LLM prompts must be stored and versioned in LangSmith's Prompt Hub, enabling non-technical users to edit prompts through the web-based Playground interface without code deployment.                                                   |

---

## 7. Assumptions and Dependencies

### Assumptions

- Students and teachers have reliable internet access on Chromebook devices.
- Teachers review student attempts post-assessment via dashboard.
- ReadAssist provides teacher identifiers, class identifiers, and test specifications.
- Audio files are processed and immediately deleted; only text-based metrics and feedback are persisted.
- ReadAssist team will provide teacher identifiers (email or ID number) and class identifiers for pre-configuration.
- ReadAssist team will provide three reading passages (2 minutes or less), each with fluency score thresholds (WCPM) and maximum retry limits.
- Teachers will distribute provided URLs to students without modification.
- Students will access the platform using the complete URLs provided.
- School networks allow access to STT provider APIs in addition to Cloudflare infrastructure.
- Test duration limited to six weeks post-release.
- ReadAssist team will iterate on LLM prompts during POC using LangSmith's Playground interface.
- LangSmith Developer plan provides sufficient capacity for POC tracing (up to 5,000 traces/month).

### Dependencies

- Use of existing STT APIs (Deepgram and SpeechAce) and language model API (Google Gemini 2.5 Flash LITE).
- The Contractor-managed hosting and infrastructure.
- ReadAssist's internal approvals for COPPA compliance.
- School IT departments for firewall whitelisting and network permissions.
- ReadAssist's UX/UI design team for future MVP iterations.
- ReadAssist team provides the following data **two weeks before POC deployment**:
  - Teacher identifiers (email or ID number) for up to 5 teachers
  - Class identifiers for up to 5 classes with associated teacher IDs
  - Three reading passages (each 2 minutes or less)
  - Fluency score threshold (WCPM) for each test
  - Maximum retry limit for each test
- Development team provides pre-configured URLs to ReadAssist team **one week before classroom testing begins**.
- Both STT provider APIs remain accessible and operational throughout POC period.
- LangSmith account provisioning with appropriate workspace permissions for ReadAssist team.
- LangSmith API key configuration for development environment.
- Training provided to ReadAssist team on LangSmith Playground usage and prompt editing workflow.

---

## 8. Exclusions (Out of Scope)

### Directly Inferred from PoC Definition

- Full ReadAssist platform integration.
- Advanced dashboards or analytics visualization.
- Production-level SLAs.
- Mobile app development.
- Continuous AI learning or model fine-tuning.
- Multi-language or multi-accent support.
- Long-term data retention or archival systems.
- Offline operation.
- Test creation or editing interface.
- Teacher account registration or management UI.
- Class creation or student enrollment UI.
- User authentication system (login/logout).
- Student profile management.
- Test assignment workflow UI.
- Real-time teacher monitoring of in-progress attempts.
- Support for more than 5 teachers or 5 classes.
- Administrator or admin role and interfaces.

### Additional Suggested Exclusions

- Integration with parent or guardian portals.
- Real-time classroom dashboards.
- Custom scoring rubric builder.
- Adaptive lesson generation.
- Gamification or progress rewards.
- Cross-language pronunciation analysis.
- Integration with third-party LMS systems.
- Automated teacher replacement features.
- Persistent voice profiles per student.
- AI-driven personalized learning beyond fluency assessment.

---

## 9. High-Level Risks

| ID      | Description                                                                                                  | Mitigation                                                                                                             | Impact | Priority |
| ------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------ | -------- |
| **R1**  | Speech recognition variance across accents and devices                                                       | Use proven, existing API models; normalize input volume                                                                | High   | High     |
| **R2**  | Teacher adoption and trust                                                                                   | Include teacher observer role with comment capability                                                                  | Medium | High     |
| **R3**  | Firewall restrictions                                                                                        | Early coordination with school IT teams for whitelisting                                                               | Medium | Medium   |
| **R4**  | Undefined fluency scoring standard                                                                           | Define rubric in next PRD iteration                                                                                    | High   | High     |
| **R5**  | Limited sample size for testing                                                                              | Increase test count or extend pilot duration if needed                                                                 | Medium | Medium   |
| **R6**  | Privacy and COPPA compliance                                                                                 | Zero PII storage; legal oversight by ReadAssist                                                                             | High   | Critical |
| **R7**  | Uneven microphone or background noise quality                                                                | Pre-test audio calibration; device guidance prompts                                                                    | Medium | Medium   |
| **R8**  | Overfitting feedback for a narrow age group                                                                  | Include variety of reading levels in testing                                                                           | Medium | Medium   |
| **R10** | Dual STT processing increases costs beyond budget                                                            | Monitor usage closely; adjust test duration if needed                                                                  | Medium | Medium   |
| **R11** | One STT provider API outage affects data collection completeness                                             | Implement error handling and retry logic; display error message to user if provider fails                              | High   | High     |
| **R12** | ReadAssist provides test content too late for deployment                                                          | Set firm deadline 2 weeks before launch; have placeholder texts                                                        | Medium | High     |
| **R13** | LangSmith trace volume exceeds Developer plan limits (5,000 traces/month), incurring pay-as-you-go charges   | Monitor trace consumption weekly. Budget for overage charges at $0.0005 per base trace and $0.0045 per extended trace. | Low    | Medium   |
| **R14** | Educational stakeholders unfamiliar with LangSmith Playground interface, requiring ongoing developer support | Provide comprehensive training session. Offer initial hands-on support during first iterations.                        | Medium | High     |
| **R15** | LangSmith service outage prevents prompt deployment or trace collection                                      | Monitor LangSmith status page. Service failure will impact application functionality requiring immediate attention.    | Medium | Medium   |

---

## 10. High-Level Roadmap / Timeline

### Phase 1 -- Proof of Concept (Oct--Dec 2025)

- Build and deploy PoC platform.
- Conduct pilot with teachers and students.
- Collect and compare AI vs teacher assessment data.
- Evaluate usability, accuracy, and feedback quality.

### Phase 2 -- Minimum Viable Product (2026)

- Integrate validated fluency metrics and scoring rubric.
- Expand access to selected ReadAssist cohorts.
- Improve UX/UI and scalability.

### Phase 3 -- General Availability (2026)

- Integrate AI features into ReadAssist's main platform.
- Implement SLAs, full compliance, and support structure.

---

## 11. Approvals

| Name                | Role                | Signature | Date |
| ------------------- | ------------------- | --------- | ---- |
| ReadAssist Product Owner | Business Owner      |           |      |
| The Contractor PM        | Project Manager     |           |      |
| The Contractor Tech Lead | Technical Authority |           |      |

---

## 12. Appendices

### Appendix A -- PoC Workflow Overview

**Revised PoC Workflow Overview:**

1. **Pre-Deployment Phase**:

   - ReadAssist provides teacher/class info and three test passages
   - Development team pre-configures database with 5 teachers, 5 classes, 3 tests
   - Development team generates and provides URLs to ReadAssist team

2. **Classroom Deployment**:

   - Teacher distributes student URLs (containing test identifier and class identifier)
   - Students access platform via provided URLs

3. **Assessment Execution**:

   - Student reads aloud from assigned test
   - System captures audio
   - Audio processed simultaneously by both STT providers
   - Audio file deleted immediately after processing
   - AI generates student-facing feedback
   - Only anonymized metrics, transcriptions, and feedback stored

4. **Teacher Review**:

   - Teacher accesses class dashboard via provided URL
   - Reviews side-by-side STT provider comparison data
   - Reviews AI-generated student feedback
   - Adds qualitative teacher observations
   - Exports class data as CSV

5. **Data Collection and Analysis**:
   - Teacher exports and shares CSV data with ReadAssist team
   - Data used by ReadAssist to evaluate STT provider performance and ROI

### Appendix B -- Terminology Reference

| Term                         | Definition                                                                                                                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AI Tutor**                 | The AI-driven system that listens and analyzes reading.                                                                                                                                                                                                             |
| **Baseline Attempt**         | The student's first reading used for reference.                                                                                                                                                                                                                     |
| **Fluency Assessment**       | The process of evaluating reading accuracy and speed.                                                                                                                                                                                                               |
| **Observer Feedback**        | Teacher's comments after AI evaluation.                                                                                                                                                                                                                             |
| **COPPA**                    | Children's Online Privacy Protection Act; governs data handling.                                                                                                                                                                                                    |
| **PoC**                      | Proof of Concept -- limited scope prototype for validation.                                                                                                                                                                                                         |
| **Standalone Platform**      | System deployed independently of ReadAssist's main app.                                                                                                                                                                                                                  |
| **URL-Based Access**         | Access control method using pre-configured URLs with embedded identifiers instead of authentication.                                                                                                                                                                |
| **Test Identifier**          | Unique identifier for each of the three pre-configured reading assessments.                                                                                                                                                                                         |
| **Class Identifier**         | Unique code or ID assigned to each classroom cohort.                                                                                                                                                                                                                |
| **STT Providers**            | Deepgram and SpeechAce speech-to-text services used for dual processing.                                                                                                                                                                                            |
| **Dual STT Processing**      | Simultaneous audio analysis by both STT providers for comparative evaluation.                                                                                                                                                                                       |
| **Pre-Configuration**        | Development team setup of tests, teachers, and classes prior to classroom deployment.                                                                                                                                                                               |
| **A/B Testing**              | Comparative evaluation methodology using two STT providers on identical data.                                                                                                                                                                                       |
| **Fluency Score Threshold**  | Target Words Correct Per Minute (WCPM) that determines assessment completion.                                                                                                                                                                                       |
| **Maximum Retry Limit**      | Number of attempts a student may make before assessment concludes.                                                                                                                                                                                                  |
| **Reading Passage**          | Text content for students to read aloud, designed for 2 minutes or less duration.                                                                                                                                                                                   |
| **Audio File Deletion**      | Immediate removal of recorded audio files after STT processing; only text-based results retained.                                                                                                                                                                   |
| **Anonymized Metrics**       | Assessment data stored without PII: WCPM scores, accuracy percentages, transcriptions, and feedback.                                                                                                                                                                |
| **Progressive Accumulation** | Reading methodology where students build paragraph by reading accumulated sentences (1, then 1+2, then 1+2+3, etc.)                                                                                                                                                 |
| **Reading Step**             | Each stage of progressive reading where student attempts to read accumulated sentences                                                                                                                                                                              |
| **Word Highlighting**        | Visual indication of mispronounced words requiring student review                                                                                                                                                                                                   |
| **Attempt Limiting**         | Configurable maximum retry attempts per reading step before auto-progression                                                                                                                                                                                        |
| **Per-Step Metrics**         | Performance data captured for each individual reading step within an assessment                                                                                                                                                                                     |
| **LangSmith**                | Development platform for LLM applications providing tracing, prompt management, evaluation, and monitoring. Used in ReadAssist AI for observability of STT and LLM interactions, and for enabling non-technical prompt iteration through web-based Playground interface. |

### Appendix C -- Document Revision History

| Version | Date                  | Author                            | Description of Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------- | --------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.0** | **October 27, 2025**  | **The Contractor** | **Initial document creation including business requirements (BR-01 through BR-10), business rules (BR-RULE-01 through BR-RULE-07), use cases, project scope, success metrics, assumptions and dependencies, risks, roadmap, and appendices.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **2.0** | **October 29, 2025**  | **The Contractor** | **Added BR11 (Multiple Pre-Configured Reading Tests), BR12 (POC Configuration and URL-Based Access Model), BR13 (Dual Speech Recognition Provider Evaluation), and BR14 (AI-Generated Feedback with Teacher Validation). Added corresponding business rules BR-RULE-08 through BR-RULE-13. Updated A/B testing approach to process all attempts with both STT providers simultaneously instead of single provider. Revised Use Case 1 (Student Completes AI-Guided Assessment) and Use Case 2 (Teacher Reviews Assessment Data and Exports Results) to reflect dual STT processing workflow and comparative data collection. Updated project scope to clarify pre-configuration model and URL-based access.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **2.1** | **November 04, 2025** | **The Contractor** | **Added BR15 (Prompt Observability and Tracing) with LangSmith integration for comprehensive metadata capture and prompt management. Added BR-RULE-14 (LLM Feedback Storage and Teacher Review), BR-RULE-15 (Comprehensive API Tracing), and BR-RULE-16 (Prompt Hub Management). Updated Section 2.2 (Project Scope) to include LangSmith tracing and prompt management infrastructure. Updated Section 7 (Assumptions and Dependencies) to include LangSmith capacity assumptions, account provisioning, API configuration, and ReadAssist team training requirements. Added three new risks in Section 9: R13 (LangSmith trace volume overage charges), R14 (Educational stakeholder LangSmith Playground adoption), and R15 (LangSmith service outage impact). Updated Section 3.4 (Success Metrics) to include LangSmith tracing coverage and prompt optimization capability validation. Added LangSmith definition to Appendix B (Terminology Reference).**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **2.2** | **November 18, 2025** | **The Contractor** | **Updated BR-02 to reflect progressive sentence accumulation reading methodology where students read accumulated sentences (1, then 1+2, then 1+2+3, etc.) with configurable retry limits and auto-progression. Updated BR-11 to specify test passages are divided into individual sentences with fluency and accuracy thresholds per reading step. Added BR-16 (Adaptive Word-Level Feedback) for mispronounced word highlighting and student review acknowledgment. Added BR-17 (Reading Step Metrics Granularity) for capturing detailed per-step performance data including retry counts and highlighted words. Updated BR-RULE-02 to specify configurable maximum attempts per step with auto-progression. Updated BR-RULE-12 to include sentence structure, accuracy thresholds, and per-step retry limits. Updated Section 2.2 (Project Scope) to add progressive sentence accumulation, adaptive word-level feedback, per-step metrics collection, and attempt limiting as in-scope items; added phoneme-level analysis, interactive word correction exercises, and AI audio pronunciation modeling as out-of-scope items. Updated Use Case 1 to include word highlighting workflow (Step 6), progressive accumulation description (Step 6.5), and final paragraph mastery requirement of two additional complete reads (Step 7). Added five new terms to Appendix B: Progressive Accumulation, Reading Step, Word Highlighting, Attempt Limiting, and Per-Step Metrics.** |

---
