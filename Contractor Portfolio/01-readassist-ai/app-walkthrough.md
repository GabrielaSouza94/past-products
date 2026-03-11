# ReadAssist AI App Walkthrough

This guide walks through both the Student and Teacher flows of the ReadAssist AI Reading Fluency Assessment System.

## Table of Contents

1. [Student Flow](#student-flow)
   - [Starting a Test](#starting-a-test)
   - [Student Assessment Page](#student-assessment-page)
   - [Completion](#completion)
2. [Teacher Dashboard](#teacher-dashboard)
   - [Understanding Test and Class Parameters](#understanding-test-and-class-parameters)
   - [Dashboard Overview](#dashboard-overview)
   - [Student Details Modal](#student-details-modal)
3. [URL Reference](#url-reference)
4. [CSV Export Structure](#csv-export-structure)
   - [Attempts Report](#1-attempts-report)
   - [Final Results Report](#2-final-results-report)

---

## Student Flow

### Starting a Test

**URL Pattern:**

| Environment | Base URL |
|-------------|----------|
| Staging | `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start` |
| Production | `https://readassist-ai-fluency-training-production.tech-c12.workers.dev/students/start` |

Append `?testId={T}&classId={C}` where T = 1–3 and C = 1–5 (15 combinations per environment).

> **IMPORTANT:** Always land on the `/start` page first. This creates a session and assigns a student anonymous ID to link attempts.

**Steps:**
1. Input the student's **first name** and **last name**
2. Click **"Start Test"** to continue to the assessment page

![Student Start Page](./images/walkthrough/student-start-page.png)

---

### Student Assessment Page

On this page:
1. Click **"Record"** and read the passage on the left
2. You can **re-record** or **play your recording** to verify before submitting

![Student Assessment Page](./images/walkthrough/student-assessment-page.png)

#### Handling Failed Attempts

If you fail to meet the fluency or accuracy threshold, you must **acknowledge the words you missed** or mispronounced. After acknowledging every word, you can record again and submit.

![Word Acknowledgment](./images/walkthrough/word-acknowledgment.png)

#### Progressive Reading

The system auto-guides through each reading step:
1. **Sentence progression** — Read sentences progressively (sentence 1, then 1+2, then 1+2+3, etc.)

![Sentence Reading](./images/walkthrough/sentence-reading.png)

2. **Paragraph reads** — After completing sentence progression, do **two full paragraph reads**

![Paragraph Reading](./images/walkthrough/paragraph-reading.png)

---

### Completion

Upon completion, you are redirected to the **results page**, which saves results to the database.

> **WARNING:** Reloading this page produces an error—results are saved only on first load.

![Completion Page](./images/walkthrough/completion-page.png)

---

## Teacher Dashboard

### Understanding Test and Class Parameters

There are **3 tests** and **5 classes** pre-configured with corresponding teachers.

Any test works in any class. To see results, **match exact test and class parameters** in the teacher dashboard URL.

#### Example: Same Test, Different Classes

If you start test #1 in classes #1 and #3:
- Student URL: `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=1&classId=1`
- Teacher URL: `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=1&classId=1`

- Student URL: `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=1&classId=3`
- Teacher URL: `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=1&classId=3`

#### Example: Different Tests, Same Class

If you start test #1 and test #3 in class #1:
- Student URL: `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=1&classId=1`
- Student URL: `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=3&classId=1`

Results appear in separate teacher dashboards:
- `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=1&classId=1`
- `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=3&classId=1`

> **Remember:** Results only appear for the exact query parameters used in the student assessment.

---

### Dashboard Overview

**URL Pattern:**

| Environment | Base URL |
|-------------|----------|
| Staging | `https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher` |
| Production | `https://readassist-ai-fluency-training-production.tech-c12.workers.dev/teacher` |

Append `?testId={T}&classId={C}` where T = 1–3 and C = 1–5 (15 combinations per environment).

#### Student Anonymous ID Format

Each student gets a **Student Anonymous ID**: first two letters of first name + first two letters of last name + random 4-character ID (anonymized but identifiable).
- Example: "John Smith" → `JoSm_X7K2`

#### Session Types

| Type | Description | Metrics Shown |
|------|-------------|---------------|
| **Active Sessions** | Students currently taking the assessment | BEST scores from the **current attempt only** |
| **Completed Sessions** | Students who finished the entire assessment | BEST scores from **ALL attempts** |

Filter between these using the respective filter buttons.

![Teacher Dashboard](./images/walkthrough/teacher-dashboard.png)

#### Refreshing Data

To see progress updates:
- **Refresh button** (faster)
- Browser refresh

#### CSV Export

Click **"Download CSV Report"** to export results.

![Dashboard Controls](./images/walkthrough/dashboard-controls.png)

#### Viewing Student Details

Completed sessions have a **"View Details"** button that opens the Student Details Modal.

![View Details Button](./images/walkthrough/view-details-button.png)

---

### Student Details Modal

The Student Details Modal contains:
- Per-sentence metrics
- Per-paragraph metrics
- Top 3 words with troubles
- AI-generated feedback

![Student Details Modal Overview](./images/walkthrough/student-details-modal.png)

---

#### Per-Sentence Metrics

Each test is split into N sentences with detailed metrics from two coaches:
- **Coach DG** (Deepgram) — Speech-to-text with confidence scoring
- **Coach SA** (SpeechAce) — Pronunciation quality assessment

Metrics per coach: WCPM, Fluency, Accuracy.

> **IMPORTANT:** Metrics are the **AVERAGE** of all attempts. Example: two attempts for sentence #1 with fluency 50 and 100 yields 75.

**Additional Information:**
- **Highlighted words** — Words the student re-tried in this sentence read
- **Words added** — Words spoken not in the expected text
- **Words skipped** — Expected words not spoken
- **Attempt count** — Attempts before continuing to next step

> **IMPORTANT:** Highlighted words are from this specific sentence read. For sentence #3, this may include words from sentences #1 or #2 (due to progressive reading).

![Per-Sentence Metrics](./images/walkthrough/per-sentence-metrics.png)

---

#### Per-Paragraph Metrics

Two paragraph reads with the same metric logic as sentences.

![Per-Paragraph Metrics](./images/walkthrough/per-paragraph-metrics.png)

---

#### Words with Trouble

The **top 3 words** the student needed to retry most often.

![Words with Trouble](./images/walkthrough/words-with-trouble.png)

---

#### AI Feedback

AI-generated feedback from Coach DG and Coach SA results, intended for teachers, highlighting:
- What the student did well
- What they can work on

![AI Feedback](./images/walkthrough/ai-feedback.png)

---

#### Original Text

The expected reading content (test content) for teacher reference.

![Original Text](./images/walkthrough/original-text.png)

---

#### Teacher Notes

Form on the right for teachers to leave feedback and save insights about student performance.

![Teacher Notes](./images/walkthrough/teacher-notes.png)

---

## CSV Export Structure

Clicking **"Download CSV Report"** produces **two CSV files**:

1. **Attempts Report** — Detailed per-attempt data for each student
2. **Final Results Report** — Summary results for completed assessments

> **IMPORTANT:** **Allow pop-ups** in your browser for this feature. CSV export opens files in new tabs/windows. If files don't appear, check your pop-up blocker settings.

---

### 1. Attempts Report

Each row represents a single attempt for a specific sentence/step.

| Column | Description |
|--------|-------------|
| `Attempt ID` | Unique identifier for this attempt |
| `Student ID` | Student's anonymous ID (e.g., `RORO_CrCT`) |
| `Class ID` | Class identifier |
| `Test ID` | Test identifier |
| `Sentence ID` | Sentence being read |
| `Step Number` | Step in the progressive reading sequence |
| `Attempt Number` | Which attempt for the current step (1st, 2nd, 3rd, etc.) |
| `Deepgram Transcript` | Text transcribed from student's audio by Deepgram |
| `Deepgram WCPM` | Words Correct Per Minute from Deepgram |
| `Deepgram Accuracy` | Accuracy percentage from Deepgram (0-100) |
| `Deepgram Confidence` | Overall confidence score from Deepgram (0-1) |
| `SpeechAce WCPM` | Words Correct Per Minute from SpeechAce |
| `SpeechAce Accuracy` | Pronunciation accuracy from SpeechAce (0-100) |
| `SpeechAce Fluency` | Fluency score from SpeechAce (0-100) |
| `SpeechAce Has Irrelevant Speech` | Whether student spoke unrelated words (Yes/No) |
| `Deepgram Teacher Feedback` | AI-generated feedback from Coach DG |
| `SpeechAce Teacher Feedback` | AI-generated feedback from Coach SA |
| `Highlighted Words` | JSON array of words the student needed to retry |
| `Passed` | Whether this attempt passed the threshold (Yes/No) |
| `Duration (ms)` | Audio recording length in milliseconds |
| `Created At` | Timestamp when the attempt was created |
| `Updated At` | Timestamp when the attempt was last updated |

**Use Case:** Analyze individual progress, mistake patterns, and difficult sentences/words.

---

### 2. Final Results Report

Each row represents one completed student assessment.

| Column | Description |
|--------|-------------|
| `Student ID` | Student's anonymous ID |
| `Teacher ID` | Teacher's identifier |
| `Class ID` | Class identifier |
| `Test ID` | Test identifier |
| `WCPM` | Best Words Correct Per Minute across all attempts |
| `Accuracy` | Best accuracy score across all attempts (0-100) |
| `Fluency` | Best fluency score across all attempts (0-100) |
| `AI Feedback (Deepgram)` | Final AI-generated feedback from Coach DG |
| `AI Feedback (SpeechAce)` | Final AI-generated feedback from Coach SA |
| `Original Text` | Expected text the student was to read |
| `Teacher Notes` | Notes entered by the teacher in the student details modal |
| `Finalized At` | Timestamp when assessment was completed and saved |
| `Created At` | Timestamp when the result record was created |
| `Updated At` | Timestamp when the result was last updated |

**Use Case:** High-level performance overview for grade reporting, class-wide tracking, and identifying students needing support.

---

## URL Reference

### Student Start URLs

| Environment | Test | Class | URL |
|-------------|------|-------|-----|
| Staging | 1 | 1 | https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=1&classId=1 |
| Staging | 2 | 1 | https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=2&classId=1 |
| Staging | 3 | 1 | https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/students/start?testId=3&classId=1 |
| Production | 1 | 1 | https://readassist-ai-fluency-training-production.tech-c12.workers.dev/students/start?testId=1&classId=1 |
| Production | 2 | 1 | https://readassist-ai-fluency-training-production.tech-c12.workers.dev/students/start?testId=2&classId=1 |
| Production | 3 | 1 | https://readassist-ai-fluency-training-production.tech-c12.workers.dev/students/start?testId=3&classId=1 |

### Teacher Dashboard URLs

| Environment | Test | Class | URL |
|-------------|------|-------|-----|
| Staging | 1 | 1 | https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=1&classId=1 |
| Staging | 2 | 1 | https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=2&classId=1 |
| Staging | 3 | 1 | https://readassist-ai-fluency-training-staging.tech-c12.workers.dev/teacher?testId=3&classId=1 |
| Production | 1 | 1 | https://readassist-ai-fluency-training-production.tech-c12.workers.dev/teacher?testId=1&classId=1 |
| Production | 2 | 1 | https://readassist-ai-fluency-training-production.tech-c12.workers.dev/teacher?testId=2&classId=1 |
| Production | 3 | 1 | https://readassist-ai-fluency-training-production.tech-c12.workers.dev/teacher?testId=3&classId=1 |

> **Note:** Replace `classId=1` with any class from 1-5 to access different classes.
