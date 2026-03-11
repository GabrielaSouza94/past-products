# ReadAssist AI - Technical Documentation

## Project Overview

**ReadAssist AI** is a K-12 reading fluency assessment system. Students read text aloud, and the system uses AI to analyze fluency, pronunciation, and provide real-time feedback.

### Key Capabilities

- **Progressive Sentence Accumulation** - Students build fluency by reading progressively (sentence 1, then 1+2, then 1+2+3, etc.)
- **Dual Speech-to-Text Analysis** - Every attempt is processed by both Deepgram and SpeechAce simultaneously
- **AI-Generated Feedback** - Gemini 2.5 Flash Lite provides age-appropriate, encouraging feedback
- **Word-Level Pronunciation Feedback** - Identifies and highlights words that need practice
- **Teacher Dashboard** - Real-time session tracking, attempt review, and CSV export
- **COPPA Compliant** - No PII storage, anonymous student identifiers only

---

## System Architecture

### High-Level Architecture Diagram

```mermaid
flowchart TB
    subgraph CLIENT["Client Layer"]
        STUDENT["Student Chromebooks<br/>(Chrome 90+)"]
        TEACHER["Teacher Dashboard<br/>(Web App)"]
    end

    subgraph AUTH["Authentication Layer"]
        BASIC_AUTH["HTTP Basic Authentication"]
    end

    subgraph EDGE["Cloudflare Edge Network"]
        PAGES["Cloudflare Pages<br/>(Static Assets)"]
        WORKERS["Cloudflare Workers<br/>(API & Logic)"]
        WAF["WAF & DDoS<br/>Protection"]
    end

    subgraph APIS["External APIs"]
        DEEPGRAM["Deepgram<br/>(STT)"]
        SPEECHACE["SpeechAce<br/>(STT)"]
        GEMINI["Gemini 2.5<br/>Flash Lite"]
    end

    subgraph DATA["Data Layer"]
        D1["Cloudflare D1<br/>(SQLite)"]
        KV["Cloudflare KV<br/>(Session)"]
    end

    subgraph OBSERVABILITY["Observability"]
        LANGSMITH["LangSmith<br/>(Tracing)"]
    end

    STUDENT --> BASIC_AUTH
    TEACHER --> BASIC_AUTH
    BASIC_AUTH --> PAGES
    BASIC_AUTH --> WORKERS
    WORKERS --> DEEPGRAM
    WORKERS --> SPEECHACE
    WORKERS --> GEMINI
    WORKERS --> D1
    WORKERS --> KV
    WORKERS --> LANGSMITH
    GEMINI --> LANGSMITH

    style CLIENT fill:#e0f2fe
    style AUTH fill:#fef3c7
    style EDGE fill:#d1fae5
    style APIS fill:#fce7f3
    style DATA fill:#e0e7ff
    style OBSERVABILITY fill:#f3e8ff
```

### Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | React + React Router 7 | UI framework with SSR |
| **Styling** | Tailwind CSS 4 | Utility-first CSS |
| **Backend** | Cloudflare Workers | Serverless edge compute |
| **Database** | Cloudflare D1 (SQLite) | Persistent data storage |
| **Session Store** | Cloudflare KV | Temporary session state |
| **STT Provider 1** | Deepgram Nova-3 | Word-level confidence scoring |
| **STT Provider 2** | SpeechAce | Pronunciation quality scoring |
| **LLM** | Gemini 2.5 Flash Lite | Feedback generation |
| **Observability** | LangSmith | Tracing & prompt management |
| **ORM** | Drizzle ORM | Type-safe database access |

---

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    teachers ||--o{ classes : "has"
    teachers ||--o{ test_results : "owns"
    classes ||--o{ attempts : "contains"
    classes ||--o{ test_results : "has"
    tests ||--o{ sentences : "contains"
    tests ||--o{ attempts : "has"
    tests ||--o{ test_results : "has"
    sentences ||--o{ attempts : "references"
    sentences ||--o{ attempt_step : "references"
    sentences ||--o{ test_step_result : "references"
    attempts ||--|| attempt_stt : "has"
    attempts ||--o{ attempt_step : "contains"
    test_results ||--o{ test_step_result : "contains"

    teachers {
        int id PK
        string name
        string email UK
        timestamp created_at
        timestamp updated_at
    }

    classes {
        int id PK
        int teacher_id FK
        string name
        string code UK
        timestamp created_at
        timestamp updated_at
    }

    tests {
        int id PK
        string title
        real fluency_threshold
        int max_attempts_per_step
        timestamp created_at
        timestamp updated_at
    }

    sentences {
        int id PK
        int test_id FK
        string content
        int sequence_number
        timestamp created_at
        timestamp updated_at
    }

    attempts {
        string id PK
        string student_anonymous_id
        int class_id FK
        int test_id FK
        int sentence_id FK
        int step_number
        int attempt_number
        int paragraph_read_number
        string deepgram_transcript
        real deepgram_wcpm
        real deepgram_accuracy
        real deepgram_confidence
        real deepgram_fluency
        real speechace_wcpm
        real speechace_accuracy
        real speechace_fluency
        boolean speechace_has_irrelevant_speech
        string deepgram_teacher_feedback
        string speechace_teacher_feedback
        string highlighted_words
        boolean passed
        int duration_ms
        timestamp created_at
        timestamp updated_at
    }

    attempt_step {
        string attempt_sentence_id PK
        string attempt_id FK
        string student_anonymous_id
        int class_id FK
        int test_id FK
        int sentence_id FK
        int step_number
        int attempt_number
        int paragraph_read_number
        string deepgram_transcript
        real deepgram_wcpm
        real deepgram_accuracy
        real deepgram_fluency
        real speechace_wcpm
        real speechace_accuracy
        real speechace_fluency
        string words_skipped
        string words_added
        string words_highlighted
        string step_type
        boolean passed
        timestamp created_at
        timestamp updated_at
    }

    attempt_stt {
        string attempt_id PK_FK
        string raw_deepgram
        string raw_speechace
        string raw_gemini
    }

    test_results {
        int id PK
        string student_anonymous_id
        int teacher_id FK
        int class_id FK
        int test_id FK
        string finalized_at
        int wcpm
        int accuracy
        int fluency
        string ai_feedback_deepgram
        string ai_feedback_speechace
        string original_text
        string teacher_notes
        timestamp created_at
        timestamp updated_at
    }

    test_step_result {
        int id PK
        int test_results_id FK
        int sentence_id FK
        int paragraph_read_number
        int wcpm_deepgram
        int accuracy_deepgram
        int fluency_deepgram
        int wcpm_speechace
        int accuracy_speechace
        int fluency_speechace
        string words_skipped
        string words_added
        string words_highlighted
        int attempts
        string step_type
    }
```

### Table Descriptions

| Table | Purpose |
|-------|---------|
| `teachers` | Teacher accounts with name and email |
| `classes` | Classrooms linked to teachers via `teacher_id` |
| `tests` | Reading assessments with fluency thresholds and attempt limits |
| `sentences` | Individual sentences within a test, ordered by `sequence_number` |
| `attempts` | Individual reading attempts with dual STT results |
| `attempt_step` | Per-sentence metrics within an attempt |
| `attempt_stt` | Raw API responses from Deepgram, SpeechAce, and Gemini |
| `test_results` | Finalized student test results with aggregated metrics |
| `test_step_result` | Aggregated per-step results for teacher review |

---

## Data Flow Diagrams

### Submit Attempt Flow

```mermaid
sequenceDiagram
    autonumber
    participant S as Student
    participant B as Browser
    participant W as Worker
    participant DG as Deepgram
    participant SA as SpeechAce
    participant G as Gemini
    participant LS as LangSmith
    participant DB as Database
    participant KV as KV Store

    S->>B: Click Record
    B->>B: MediaRecorder starts
    S->>B: Read Text Aloud
    S->>B: Click Stop
    B->>B: MediaRecorder stops

    B->>W: POST /api/submit-attempt<br/>(audio + metadata)

    rect rgb(230, 245, 255)
        Note over W,SA: Parallel STT Processing
        par Deepgram
            W->>DG: Process Audio
            DG-->>W: Transcript + Confidence
        and SpeechAce
            W->>SA: Process Audio
            SA-->>W: Pronunciation Scores
        end
    end

    W->>W: Extract Metrics<br/>Calculate WCPM<br/>Identify Issues

    rect rgb(255, 240, 245)
        Note over W,G: LLM Feedback Generation
        W->>LS: Pull Current Prompt
        LS-->>W: Prompt Template
        W->>G: Generate Feedback
        G-->>W: Pass/Fail + Words to Highlight
        W->>LS: Log Trace
    end

    rect rgb(240, 255, 240)
        Note over W,KV: Data Persistence
        par Save to DB
            W->>DB: Insert attempts
            W->>DB: Insert attempt_step
            W->>DB: Insert attempt_stt
        and Save to KV
            W->>KV: Store session state<br/>(1-hour TTL)
        end
    end

    W-->>B: Response: { pass, highlightedWords, attemptId }
    B->>S: Display Results
```

### Progressive Sentence Accumulation Flow

```mermaid
flowchart TB
    START([Student Starts Test]) --> S1

    subgraph SENTENCE_MODE["Sentence Mode"]
        S1["Step 1: Read Sentence 1"] --> AI1{AI Analysis}
        AI1 -->|Pass OR Max Attempts| S2["Step 2: Read Sentences 1+2"]
        AI1 -->|Below Threshold| HL1["Highlight Words<br/>Student Review"]
        HL1 --> RETRY1["Retry Reading"]
        RETRY1 --> AI1

        S2 --> AI2{AI Analysis}
        AI2 -->|Pass OR Max Attempts| S3["Step 3: Read Sentences 1+2+3"]
        AI2 -->|Below Threshold| HL2["Highlight Words<br/>Student Review"]
        HL2 --> RETRY2["Retry Reading"]
        RETRY2 --> AI2

        S3 --> AI3{AI Analysis}
        AI3 -->|Pass OR Max Attempts| MORE["Continue Pattern..."]
        AI3 -->|Below Threshold| HL3["Highlight Words"]
        HL3 --> RETRY3["Retry"]
        RETRY3 --> AI3

        MORE --> LAST["Final Sentence Step"]
    end

    LAST -->|All Sentences Mastered| PARA_MODE

    subgraph PARA_MODE["Full Paragraph Mode"]
        P1["Read 1: Complete Paragraph"] --> PAI1{AI Analysis}
        PAI1 -->|Pass OR Max Attempts| P2["Read 2: Complete Paragraph"]
        PAI1 -->|Below Threshold| PHL1["Highlight & Review"]
        PHL1 --> PR1["Retry"]
        PR1 --> PAI1

        P2 --> PAI2{AI Analysis}
        PAI2 -->|Pass OR Max Attempts| COMPLETE
        PAI2 -->|Below Threshold| PHL2["Highlight & Review"]
        PHL2 --> PR2["Retry"]
        PR2 --> PAI2
    end

    COMPLETE([Assessment Complete!])

    style SENTENCE_MODE fill:#e0f2fe
    style PARA_MODE fill:#d1fae5
    style COMPLETE fill:#bbf7d0
```

### Word Highlighting Flow (TR-16)

```mermaid
flowchart TB
    AUDIO["Audio Submitted"] --> STT

    subgraph STT["STT Processing"]
        DG["Deepgram:<br/>Word-level confidence scores"]
        SA["SpeechAce:<br/>Word quality scores"]
        THRESH["Threshold: 75% confidence"]
    end

    STT --> LLM

    subgraph LLM["Gemini LLM Analysis"]
        INPUT["Input: STT results + expected text"]
        OUTPUT["Output: listOfWordsToHighlight"]
    end

    LLM --> CHECK{Words Below<br/>Threshold?}

    CHECK -->|No| PASS["PASS!<br/>Progress to Next Step"]

    CHECK -->|Yes| UI

    subgraph UI["Struggling Words UI"]
        HIGHLIGHT["Highlight words in text"]
        AUDIO_INST["Play audio instruction<br/>(auto-play once)"]
        DISABLE["Disable record button"]
    end

    UI --> ACK

    subgraph ACK["Student Acknowledgment"]
        CLICK["Click each highlighted word"]
        VISUAL["Visual feedback on click"]
        TRACK["Track reviewed words"]
    end

    ACK --> REVIEWED{All Words<br/>Reviewed?}

    REVIEWED -->|No| WAIT["Keep Button Disabled"]
    WAIT --> ACK

    REVIEWED -->|Yes| ENABLE["Enable Record Button"]
    ENABLE --> RETRY["Student Can Retry"]

    style PASS fill:#bbf7d0
    style UI fill:#fef3c7
    style ACK fill:#e0e7ff
```

### Complete System Flow

```mermaid
flowchart LR
    subgraph STUDENT["Student Flow"]
        A1["Enter Name/Grade"] --> A2["View Sentences"]
        A2 --> A3["Record Audio"]
        A3 --> A4["Submit Attempt"]
    end

    subgraph PROCESSING["Backend Processing"]
        B1["Validate Request"]
        B2["Parallel STT"]
        B3["Gemini Analysis"]
        B4["Save Results"]
        B1 --> B2 --> B3 --> B4
    end

    subgraph FEEDBACK["Feedback Loop"]
        C1{Pass?}
        C2["Show Highlighted Words"]
        C3["Student Reviews"]
        C4["Progress to Next Step"]
    end

    subgraph TEACHER["Teacher Dashboard"]
        D1["View Active Sessions"]
        D2["Review Attempts"]
        D3["Add Notes"]
        D4["Export CSV"]
    end

    A4 --> B1
    B4 --> C1
    C1 -->|No| C2 --> C3 --> A3
    C1 -->|Yes| C4 --> A2

    B4 --> D1
    D1 --> D2 --> D3 --> D4

    style STUDENT fill:#e0f2fe
    style PROCESSING fill:#fce7f3
    style FEEDBACK fill:#fef3c7
    style TEACHER fill:#d1fae5
```

---

## Metrics Calculation

### WCPM (Words Correct Per Minute)

Each STT provider calculates WCPM differently:

**Deepgram Calculation:**
```typescript
// Words with confidence >= 75% are considered "correct"
const correctWords = words.filter(w => w.confidence >= 0.75);
const durationSeconds = endTime - startTime;
const wcpm = Math.round((correctWords.length / durationSeconds) * 60);
```

**SpeechAce Calculation:**
```typescript
// SpeechAce provides WCPM directly in the response
const wcpm = response.text_score.fluency.overall_metrics.word_correct_per_minute;
```

**Best WCPM Selection:**
```typescript
// The system uses the maximum WCPM from both providers
const bestWcpm = Math.max(deepgramWcpm ?? 0, speechaceWcpm ?? 0);
```

### Metrics Flow Diagram

```mermaid
flowchart LR
    subgraph DEEPGRAM["Deepgram Metrics"]
        D1["Word Confidence Scores"]
        D2["Filter >= 75%"]
        D3["Count / Duration * 60"]
        D4["WCPM"]
        D1 --> D2 --> D3 --> D4
    end

    subgraph SPEECHACE["SpeechAce Metrics"]
        S1["API Response"]
        S2["Extract word_correct_per_minute"]
        S3["WCPM"]
        S1 --> S2 --> S3
    end

    subgraph BEST["Best Selection"]
        B1["Math.max(deepgram, speechace)"]
        B2["Final WCPM"]
        B1 --> B2
    end

    D4 --> B1
    S3 --> B1

    style DEEPGRAM fill:#e0f2fe
    style SPEECHACE fill:#fce7f3
    style BEST fill:#bbf7d0
```

### Accuracy Calculation

**Deepgram:**
```typescript
// Average confidence across all words, converted to percentage
const avgConfidence = words.reduce((sum, w) => sum + w.confidence, 0) / words.length;
const accuracy = Math.round(avgConfidence * 100);
```

**SpeechAce:**
```typescript
// Direct pronunciation score from API
const accuracy = response.text_score.speechace_score.pronunciation;
```

### Fluency Calculation

**Deepgram:**
```typescript
// Fluency = accuracy * confidence * similarity
const fluency = (accuracy / 100) * confidence * similarityScore;
```

**SpeechAce:**
```typescript
// Direct fluency score from API
const fluency = response.text_score.speechace_score.fluency;
```

### Final Metrics Aggregation

```typescript
// Extract best metrics from attempt
function extractAttemptMetrics(attempt) {
  return {
    wcpm: Math.max(attempt.deepgramWcpm ?? 0, attempt.speechaceWcpm ?? 0),
    fluencyScore: Math.max(attempt.speechaceFluency ?? 0, attempt.deepgramFluency ?? 0),
    accuracyScore: Math.max(attempt.deepgramAccuracy ?? 0, attempt.speechaceAccuracy ?? 0),
  };
}
```

---

## API Routes

### Student Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/students/start` | GET | Entry page for student to enter name/grade |
| `/students/assessment` | GET | Main assessment interface |
| `/students/assessment/completed` | GET | Assessment completion screen |

### Teacher Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/teachers` | GET | Teacher dashboard with session tracking |

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/submit-attempt` | POST | Submit audio recording for processing |
| `/api/start-session` | POST | Initialize student session |
| `/api/active-sessions` | GET | Fetch in-progress student sessions |
| `/api/completed-sessions` | GET | Fetch completed student sessions |
| `/api/student-detail-results` | GET | Get detailed results for a student |
| `/api/save-teacher-notes` | POST | Save teacher qualitative feedback |
| `/api/export-attempts-csv` | GET | Export all attempts as CSV |
| `/api/export-results-csv` | GET | Export final results as CSV |

### URL Parameter Routing

- **Student Portal:** `/students/assessment?testId={id}&classId={id}`
- **Teacher Portal:** `/teachers?classId={id}`

Both routes require HTTP Basic Authentication.

---

## External Service Integrations

### Integration Overview

```mermaid
flowchart TB
    subgraph APP["ReadAssist AI Application"]
        WORKER["Cloudflare Worker"]
    end

    subgraph STT["Speech-to-Text Services"]
        DEEPGRAM["Deepgram Nova-3<br/>api.deepgram.com"]
        SPEECHACE["SpeechAce<br/>api.speechace.co"]
    end

    subgraph LLM_SERVICE["LLM Service"]
        GEMINI["Gemini 2.5 Flash Lite<br/>generativelanguage.googleapis.com"]
    end

    subgraph OBS["Observability"]
        LANGSMITH["LangSmith<br/>api.smith.langchain.com"]
    end

    WORKER -->|"Audio Buffer<br/>model: nova-3"| DEEPGRAM
    WORKER -->|"FormData<br/>include_fluency: 1"| SPEECHACE
    WORKER -->|"STT Results + Prompt"| GEMINI
    WORKER -->|"Traces + Prompt Pull"| LANGSMITH
    GEMINI -.->|"Traced"| LANGSMITH

    DEEPGRAM -->|"Transcript<br/>Word Confidence"| WORKER
    SPEECHACE -->|"Pronunciation<br/>Fluency Scores"| WORKER
    GEMINI -->|"Pass/Fail<br/>Highlighted Words"| WORKER

    style APP fill:#e0f2fe
    style STT fill:#fce7f3
    style LLM_SERVICE fill:#fef3c7
    style OBS fill:#f3e8ff
```

### Deepgram Integration

**Endpoint:** `https://api.deepgram.com/v1/listen`

**Configuration:**
```typescript
{
  smart_format: true,
  model: 'nova-3',
  language: 'en-US'
}
```

**Response Processing:**
- Extract word-level confidence scores
- Calculate accuracy from average confidence
- Identify words below 75% confidence threshold
- Calculate WCPM from correct words and duration

### SpeechAce Integration

**Endpoint:** `https://api.speechace.co/api/scoring/text/v9/json`

**Request Parameters:**
```typescript
{
  text: expectedText,
  user_audio_file: audioFile,
  include_fluency: '1',
  no_mc: '1'
}
```

**Response Processing:**
- Extract pronunciation score (accuracy)
- Extract fluency score
- Get WCPM from `word_correct_per_minute`
- Identify words with quality below 70%
- Detect irrelevant speech from `score_issue_list`

### Gemini LLM Integration

**Model:** `gemini-2.5-flash-lite`

**Input:**
```typescript
{
  deepgram: { wcpm, acc, transcript, wordsWithIssues },
  speechace: { wcpm, acc, fluency, lowQualityWords, irrelevantSpeech },
  expectedSentences: [{ id, content, sequenceNumber }],
  fluency_threshold: number
}
```

**Output Schema:**
```typescript
{
  ui: {
    listOfWordsToHighlight: string[],
    deepgramTeacherFeedback: string,
    speechaceTeacherFeedback: string,
    passOrNoPass: boolean,
    reasonForNoPass: string,
    similarity: number,
    wordsSkipped: string[],
    wordsAdded: string[]
  }
}
```

### LangSmith Integration

**Features:** Prompt Hub (version-controlled prompt storage), Tracing (complete LLM interaction logging), Playground (web-based prompt testing).

**Usage:**
```typescript
// Pull prompt at runtime
const prompt = await Langsmith.pullPrompt();

// Replace variables using mustache templates
const finalPrompt = Langsmith.replacePromptVariables(template, variables, inputs);

// Trace LLM calls
const result = await llmRequest
  .withConfig({ callbacks: [Langsmith.tracer] })
  .invoke(prompt, { runName: `attempt-${attemptId}` });
```

---

## Audio Recording

**Technology:** Web Audio API with MediaRecorder

**Configuration:**
```typescript
{
  mimeType: 'audio/webm;codecs=opus',
  echoCancellation: true,
  noiseSuppression: true,
  sampleRate: 44100
}
```

**Constraints:**
- Maximum audio file size: 10MB
- Supported formats: `audio/webm`, `audio/mp3`, `audio/wav`, `audio/mpeg`, `audio/ogg`

### Audio Recording State Machine

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Requesting: Click Record
    Requesting --> Recording: Permission Granted
    Requesting --> Error: Permission Denied
    Recording --> Processing: Click Stop
    Processing --> Complete: Audio Blob Ready
    Complete --> Idle: Reset
    Error --> Idle: Dismiss

    state Recording {
        [*] --> Capturing
        Capturing --> Capturing: Audio Chunks
    }

    state Processing {
        [*] --> CreatingBlob
        CreatingBlob --> Validating
        Validating --> [*]
    }
```

---

## Session State Management

### KV Storage

Sessions are stored in Cloudflare KV with a 1-hour TTL:

**Key Format:** `{classId}:{testId}:{studentAnonymousId}`

**Value Structure:**
```typescript
{
  attemptId: string,
  classId: number,
  testId: number,
  stepNumber: number,
  attemptNumber: number,
  metrics: {
    fluencyScore: number,
    accuracyScore: number,
    wcpm: number,
    highlightedWords: string[]
  },
  passed: boolean,
  completed: boolean,
  createdAt: number
}
```

### Session Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created: Start Session
    Created --> InProgress: First Attempt
    InProgress --> InProgress: Retry Attempt
    InProgress --> StepComplete: Pass Step
    StepComplete --> InProgress: Next Step
    StepComplete --> Completed: All Steps Done
    Completed --> [*]: Finalize Results

    note right of InProgress
        KV stores current state
        1-hour TTL
    end note

    note right of Completed
        Save to test_results
        Remove from KV
    end note
```

---

## Privacy & COPPA Compliance

### Data Minimization

- No full names stored — only anonymous identifiers (e.g., "J_Smith_7B3X")
- Audio deleted immediately after STT processing
- No persistent cookies or tracking
- Only anonymized metrics retained: WCPM, accuracy, transcriptions, feedback

### LangSmith Data Handling

- No PII transmitted to LangSmith
- Only anonymized attempt IDs and metrics traced
- Only text-based transcriptions, scores, and feedback logged

### Security Measures

- HTTPS-only communication
- HTTP Basic Authentication for access control
- URL parameter validation
- Input validation on all forms
- Rate limiting via Cloudflare
- No direct database access from client

### Data Flow Privacy

```mermaid
flowchart LR
    subgraph INPUT["User Input"]
        NAME["Full Name"]
        AUDIO["Audio Recording"]
    end

    subgraph TRANSFORM["Transformation"]
        ANON["Anonymize:<br/>J_Smith_7B3X"]
        PROCESS["Process & Delete"]
    end

    subgraph STORED["Stored Data"]
        ID["Anonymous ID"]
        METRICS["WCPM, Accuracy"]
        TRANSCRIPT["Transcript"]
        FEEDBACK["AI Feedback"]
    end

    NAME --> ANON --> ID
    AUDIO --> PROCESS --> METRICS
    PROCESS --> TRANSCRIPT
    PROCESS --> FEEDBACK

    style INPUT fill:#fee2e2
    style TRANSFORM fill:#fef3c7
    style STORED fill:#d1fae5
```

---

## Database Migrations

Drizzle ORM manages 25 migration files in `db/migrations/`:

```bash
# Local
npm run db:migrate:local

# Staging
npm run db:migrate:staging

# Production
npm run db:migrate:production
```

---

## Environment Configuration

### Wrangler Configuration

- **Local Development:** `local-dev` D1 database
- **Staging:** `staging-db` D1 with staging KV namespace
- **Production:** `readassist-production-db` D1 with production KV namespace

### Environment Variables

| Variable | Description |
|----------|-------------|
| `LANGSMITH_TRACING` | Enable LangSmith tracing |
| `LANGSMITH_PROJECT` | LangSmith project name |
| `LANGSMITH_INSTRUCTOR_PROMPT_ID` | Prompt ID in LangSmith Hub |
| `LANGSMITH_API_URL` | LangSmith API endpoint |
| `SPEECHACE_API_URL` | SpeechAce API endpoint |
| `GEMINI_TEMPERATURE` | LLM temperature setting |
| `BASIC_AUTH_USERNAME` | HTTP Basic Auth username |

### Environment Diagram

```mermaid
flowchart TB
    subgraph LOCAL["Local Development"]
        L_WORKER["Cloudflare Worker<br/>(wrangler dev)"]
        L_D1["local-dev D1"]
        L_KV["Preview KV"]
        L_WORKER --> L_D1
        L_WORKER --> L_KV
    end

    subgraph STAGING["Staging Environment"]
        S_WORKER["Cloudflare Worker<br/>(staging)"]
        S_D1["staging-db D1"]
        S_KV["Staging KV"]
        S_WORKER --> S_D1
        S_WORKER --> S_KV
    end

    subgraph PRODUCTION["Production Environment"]
        P_WORKER["Cloudflare Worker<br/>(production)"]
        P_D1["readassist-production-db D1"]
        P_KV["Production KV"]
        P_WORKER --> P_D1
        P_WORKER --> P_KV
    end

    style LOCAL fill:#e0f2fe
    style STAGING fill:#fef3c7
    style PRODUCTION fill:#d1fae5
```

---

## Glossary

| Term | Definition |
|------|------------|
| **Attempt** | Single student reading instance, processed by both STT providers |
| **WCPM** | Words Correct Per Minute — primary fluency metric |
| **Progressive Accumulation** | Reading pattern: sentence 1, then 1+2, then 1+2+3, etc. |
| **Reading Step** | Single assessment unit with its own retry limit |
| **Word Highlighting** | Visual marking of mispronounced words for review |
| **Auto-Progression** | Advancing to next step after max attempts, regardless of pass/fail |
| **D1** | Cloudflare's serverless SQLite database |
| **KV** | Cloudflare's key-value storage service |
