# EAN Validator System - Solution Diagrams

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | EAN Validator System |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |
| Document Type | Solution Architecture & Process Diagrams |

---

## 1. System Architecture Overview

### High-Level Architecture

```mermaid
graph TB
    subgraph External["External Systems"]
        Seller[("🛒 Seller<br/>Product Registration")]
        GS1[("🌐 GS1 Registry<br/>EAN Database")]
    end

    subgraph Carrefour["Carrefour Marketplace Architecture"]
        Mirakl["🛍️ Mirakl Platform<br/>Marketplace Management"]
        Omni["🏷️ Omnilogic<br/>Categorization"]
        VTEX["🛒 VTEX<br/>E-commerce Frontend"]
        
        subgraph ValidationSystem["EAN Validator System (New)"]
            Endpoint["API Endpoint<br/>Product Receiver"]
            FormatValidator["Format Validator<br/>Check Digit"]
            LookupService["Lookup Service<br/>Internal + External"]
            MatchEngine["Match Engine<br/>Product Verification"]
            StatusUpdater["Status Updater<br/>Approval/Rejection"]
        end
        
        subgraph DataStores["Data Stores"]
            Cache[("💾 EAN Cache<br/>Validated Products")]
            GOLD[("📦 GOLD<br/>Internal Products")]
        end
    end

    Seller -->|"1. Submit Product"| Mirakl
    Mirakl -->|"2. Product Data"| Endpoint
    Endpoint -->|"3. Validate Format"| FormatValidator
    FormatValidator -->|"4. Lookup EAN"| LookupService
    LookupService -->|"5a. Query"| Cache
    LookupService -->|"5b. Query"| GOLD
    LookupService -->|"5c. Query"| GS1
    LookupService -->|"6. Match Data"| MatchEngine
    MatchEngine -->|"7. Update Status"| StatusUpdater
    StatusUpdater -->|"8. Result"| Mirakl
    Mirakl -->|"9. If Approved"| Omni
    Omni -->|"10. Publish"| VTEX
    
    MatchEngine -->|"Cache Valid EAN"| Cache

    style ValidationSystem fill:#e1f5fe,stroke:#0288d1
    style DataStores fill:#fff3e0,stroke:#f57c00
    style MatchEngine fill:#c8e6c9,stroke:#388e3c
```

---

## 2. Validation Flow - Complete Process

### End-to-End Validation Sequence

```mermaid
sequenceDiagram
    autonumber
    participant S as Seller
    participant M as Mirakl
    participant V as EAN Validator
    participant C as EAN Cache
    participant G as GOLD DB
    participant GS1 as GS1 API

    S->>M: Submit product with EAN
    M->>V: Send product for validation
    
    Note over V: BR-01: Check EAN Present
    alt EAN Missing
        V->>M: Reject (REJ-01: Missing EAN)
        M->>S: Error: EAN required
    else EAN Present
        Note over V: BR-02: Validate Format
        V->>V: Check length (8/12/13/14)
        V->>V: Check numeric only
        V->>V: Validate check digit
        
        alt Invalid Format
            V->>M: Reject (REJ-02/03: Invalid)
            M->>S: Error: Invalid format
        else Valid Format
            Note over V: BR-03: Internal Lookup
            V->>C: Query EAN Cache
            alt Found in Cache
                C->>V: Return product data
                V->>V: Compare attributes
            else Not in Cache
                V->>G: Query GOLD DB
                alt Found in GOLD
                    G->>V: Return product data
                    V->>V: Compare attributes
                else Not in GOLD
                    Note over V: BR-04: External Lookup
                    V->>GS1: Query EAN
                    alt Found in GS1
                        GS1->>V: Return product data
                        V->>V: Compare attributes
                    else Not Found
                        V->>M: Reject (REJ-04: Not found)
                        M->>S: Error: EAN not registered
                    end
                end
            end
            
            Note over V: BR-05: Match Check
            alt Match >= 80%
                V->>C: Store in cache
                V->>M: Approve product
                M->>S: Success: Product validated
            else Match 60-80%
                V->>M: Queue for manual review
            else Match < 60%
                V->>M: Reject (REJ-05: Mismatch)
                M->>S: Error: EAN doesn't match product
            end
        end
    end
```

---

## 3. Validation Decision Tree

### Complete Decision Logic

```mermaid
flowchart TD
    Start([Product Received]) --> EANCheck{BR-01<br/>EAN Present?}
    
    EANCheck -->|No| REJ01[❌ REJ-01<br/>Missing EAN]
    REJ01 --> Pending1([Pending Correction])
    
    EANCheck -->|Yes| LengthCheck{BR-02<br/>Valid Length?<br/>8/12/13/14 digits}
    
    LengthCheck -->|No| REJ02[❌ REJ-02<br/>Invalid Format]
    REJ02 --> Pending2([Pending Correction])
    
    LengthCheck -->|Yes| NumericCheck{BR-02<br/>Numeric Only?}
    
    NumericCheck -->|No| REJ02B[❌ REJ-02<br/>Invalid Format]
    REJ02B --> Pending3([Pending Correction])
    
    NumericCheck -->|Yes| CheckDigit{BR-02<br/>Valid Check Digit?}
    
    CheckDigit -->|No| REJ03[❌ REJ-03<br/>Invalid Check Digit]
    REJ03 --> Pending4([Pending Correction])
    
    CheckDigit -->|Yes| CacheLookup{BR-03<br/>Found in Cache?}
    
    CacheLookup -->|Yes| MatchCheck1{BR-05<br/>Match Score?}
    
    CacheLookup -->|No| GOLDLookup{BR-03<br/>Found in GOLD?}
    
    GOLDLookup -->|Yes| MatchCheck2{BR-05<br/>Match Score?}
    
    GOLDLookup -->|No| GS1Lookup{BR-04<br/>Found in GS1?}
    
    GS1Lookup -->|Yes| MatchCheck3{BR-05<br/>Match Score?}
    
    GS1Lookup -->|No| REJ04[❌ REJ-04<br/>EAN Not Found]
    REJ04 --> Pending5([Pending Correction])
    
    MatchCheck1 -->|≥ 80%| Approve1[✅ Approved]
    MatchCheck1 -->|60-80%| Review1[⚠️ Manual Review]
    MatchCheck1 -->|< 60%| REJ05A[❌ REJ-05<br/>Product Mismatch]
    
    MatchCheck2 -->|≥ 80%| Approve2[✅ Approved]
    MatchCheck2 -->|60-80%| Review2[⚠️ Manual Review]
    MatchCheck2 -->|< 60%| REJ05B[❌ REJ-05<br/>Product Mismatch]
    
    MatchCheck3 -->|≥ 80%| Approve3[✅ Approved]
    MatchCheck3 -->|60-80%| Review3[⚠️ Manual Review]
    MatchCheck3 -->|< 60%| REJ05C[❌ REJ-05<br/>Product Mismatch]
    
    Approve1 --> CacheStore[Store in Cache]
    Approve2 --> CacheStore
    Approve3 --> CacheStore
    CacheStore --> Published([Proceed to Omnilogic])
    
    REJ05A --> Pending6([Pending Correction])
    REJ05B --> Pending7([Pending Correction])
    REJ05C --> Pending8([Pending Correction])

    style Start fill:#e3f2fd,stroke:#1976d2
    style Approve1 fill:#c8e6c9,stroke:#388e3c
    style Approve2 fill:#c8e6c9,stroke:#388e3c
    style Approve3 fill:#c8e6c9,stroke:#388e3c
    style REJ01 fill:#ffcdd2,stroke:#d32f2f
    style REJ02 fill:#ffcdd2,stroke:#d32f2f
    style REJ02B fill:#ffcdd2,stroke:#d32f2f
    style REJ03 fill:#ffcdd2,stroke:#d32f2f
    style REJ04 fill:#ffcdd2,stroke:#d32f2f
    style REJ05A fill:#ffcdd2,stroke:#d32f2f
    style REJ05B fill:#ffcdd2,stroke:#d32f2f
    style REJ05C fill:#ffcdd2,stroke:#d32f2f
    style Review1 fill:#fff9c4,stroke:#fbc02d
    style Review2 fill:#fff9c4,stroke:#fbc02d
    style Review3 fill:#fff9c4,stroke:#fbc02d
```

---

## 4. Lookup Hierarchy

### Internal-First Lookup Strategy

```mermaid
flowchart LR
    subgraph Priority1["Priority 1: Validated Cache"]
        Cache[("💾 EAN Cache<br/>Previously Validated<br/>Fastest lookup")]
    end
    
    subgraph Priority2["Priority 2: GOLD Database"]
        GOLD[("📦 GOLD DB<br/>Pre-validated Products<br/>Internal source")]
    end
    
    subgraph Priority3["Priority 3: External Registry"]
        GS1[("🌐 GS1 API<br/>Official Registry<br/>External source")]
    end

    Start([EAN to Validate]) --> Cache
    Cache -->|Not Found| GOLD
    GOLD -->|Not Found| GS1
    
    Cache -->|Found| Match1[Compare Attributes]
    GOLD -->|Found| Match2[Compare Attributes]
    GS1 -->|Found| Match3[Compare Attributes]
    GS1 -->|Not Found| Reject([Reject: Not Found])
    
    Match1 --> Decision{Match Score}
    Match2 --> Decision
    Match3 --> Decision
    
    Decision -->|Pass| Approve([Approve + Cache])
    Decision -->|Fail| RejectMismatch([Reject: Mismatch])

    style Priority1 fill:#e8f5e9,stroke:#2e7d32
    style Priority2 fill:#fff8e1,stroke:#ff8f00
    style Priority3 fill:#fce4ec,stroke:#c2185b
```

### Lookup Cost Comparison

```mermaid
graph LR
    subgraph Speed["Response Time"]
        S1["Cache: ~10ms"]
        S2["GOLD: ~50ms"]
        S3["GS1: ~500ms"]
    end
    
    subgraph Cost["API Cost"]
        C1["Cache: Free"]
        C2["GOLD: Free"]
        C3["GS1: Per-call fee"]
    end
    
    subgraph Reliability["Data Freshness"]
        R1["Cache: Validated"]
        R2["GOLD: Pre-validated"]
        R3["GS1: Source of truth"]
    end
```

---

## 5. Product Matching Logic

### Attribute Comparison Flow

```mermaid
flowchart TD
    subgraph Input["Input Data"]
        SellerData["Seller Submission<br/>• Brand: 'Samsung'<br/>• Model: 'Galaxy S23'<br/>• Category: 'Smartphones'"]
        LookupData["Lookup Result<br/>• Brand: 'SAMSUNG'<br/>• Model: 'GALAXY S23 256GB'<br/>• Category: 'Mobile Phones'"]
    end
    
    subgraph Normalization["Text Normalization"]
        N1["Lowercase conversion"]
        N2["Remove special characters"]
        N3["Trim whitespace"]
        N4["Remove accents"]
    end
    
    subgraph Comparison["Attribute Comparison"]
        BrandMatch["Brand Match<br/>Fuzzy similarity"]
        ModelMatch["Model Match<br/>Fuzzy similarity"]
        CategoryMatch["Category Match<br/>Exact or parent"]
    end
    
    subgraph Scoring["Score Calculation"]
        Score["Weighted Score<br/>Brand: 40%<br/>Model: 40%<br/>Category: 20%"]
    end
    
    subgraph Decision["Decision"]
        D1["≥ 80% → Approve"]
        D2["60-80% → Manual Review"]
        D3["< 60% → Reject"]
    end

    SellerData --> N1
    LookupData --> N1
    N1 --> N2 --> N3 --> N4
    N4 --> BrandMatch
    N4 --> ModelMatch
    N4 --> CategoryMatch
    BrandMatch --> Score
    ModelMatch --> Score
    CategoryMatch --> Score
    Score --> D1
    Score --> D2
    Score --> D3
```

### Match Score Matrix

```mermaid
graph TB
    subgraph ScoreMatrix["Match Decision Matrix"]
        Header["Brand | Model | Category | Decision"]
        R1["  ✅   |   ✅   |    ✅    | APPROVE"]
        R2["  ✅   |   ✅   |    ❌    | APPROVE (warn)"]
        R3["  ✅   |   ❌   |    ✅    | MANUAL REVIEW"]
        R4["  ❌   |   ✅   |    ✅    | MANUAL REVIEW"]
        R5["  ✅   |   ❌   |    ❌    | MANUAL REVIEW"]
        R6["  ❌   |   ✅   |    ❌    | MANUAL REVIEW"]
        R7["  ❌   |   ❌   |    ✅    | REJECT"]
        R8["  ❌   |   ❌   |    ❌    | REJECT"]
    end

    style R1 fill:#c8e6c9,stroke:#388e3c
    style R2 fill:#c8e6c9,stroke:#388e3c
    style R3 fill:#fff9c4,stroke:#fbc02d
    style R4 fill:#fff9c4,stroke:#fbc02d
    style R5 fill:#fff9c4,stroke:#fbc02d
    style R6 fill:#fff9c4,stroke:#fbc02d
    style R7 fill:#ffcdd2,stroke:#d32f2f
    style R8 fill:#ffcdd2,stroke:#d32f2f
```

---

## 6. Seller Resubmission Flow

### Correction Journey

```mermaid
flowchart TD
    Start([Product Rejected]) --> Notify[Seller Notification<br/>via Mirakl]
    
    Notify --> ViewReason[View Rejection Reason<br/>in Mirakl Portal]
    
    ViewReason --> Identify{Identify Issue}
    
    Identify -->|REJ-01| FixMissing[Add EAN code<br/>from product packaging]
    Identify -->|REJ-02/03| FixFormat[Verify EAN code<br/>correct digits]
    Identify -->|REJ-04| FixNotFound[Verify product is<br/>registered with GS1]
    Identify -->|REJ-05| FixMismatch[Verify correct EAN<br/>for this product]
    
    FixMissing --> Resubmit[Resubmit Product]
    FixFormat --> Resubmit
    FixNotFound --> ContactGS1[Contact GS1 or<br/>get correct EAN]
    ContactGS1 --> Resubmit
    FixMismatch --> VerifyEAN[Find correct EAN<br/>for product]
    VerifyEAN --> Resubmit
    
    Resubmit --> Revalidate[Full Validation<br/>Process Again]
    
    Revalidate --> Result{Result}
    
    Result -->|Pass| Published([✅ Published])
    Result -->|Fail| Start

    style Start fill:#ffcdd2,stroke:#d32f2f
    style Published fill:#c8e6c9,stroke:#388e3c
    style Revalidate fill:#e3f2fd,stroke:#1976d2
```

---

## 7. Manual Review Queue

### Review Process Flow

```mermaid
flowchart TD
    subgraph Triggers["Queue Triggers"]
        T1["Partial Match<br/>(60-80% score)"]
        T2["API Failure<br/>(GS1 timeout)"]
        T3["Edge Cases<br/>(configurable)"]
    end
    
    subgraph Queue["Review Queue"]
        Q1["Queue Entry<br/>• Product ID<br/>• EAN Code<br/>• Match Score<br/>• Seller Data<br/>• Lookup Data<br/>• Timestamp"]
    end
    
    subgraph Review["Reviewer Actions"]
        View["View Details<br/>Compare data side-by-side"]
        Decide{Decision}
        ApproveBtn["✅ Approve<br/>+ Reason"]
        RejectBtn["❌ Reject<br/>+ Reason"]
    end
    
    subgraph Outcome["Outcomes"]
        Approved["Product Approved<br/>→ Cache Updated<br/>→ Proceed to Omnilogic"]
        Rejected["Product Rejected<br/>→ Seller Notified<br/>→ Pending Correction"]
    end

    T1 --> Q1
    T2 --> Q1
    T3 --> Q1
    Q1 --> View
    View --> Decide
    Decide -->|Approve| ApproveBtn
    Decide -->|Reject| RejectBtn
    ApproveBtn --> Approved
    RejectBtn --> Rejected

    style Approved fill:#c8e6c9,stroke:#388e3c
    style Rejected fill:#ffcdd2,stroke:#d32f2f
    style Queue fill:#e3f2fd,stroke:#1976d2
```

---

## 8. Integration Architecture

### API Integration Points

```mermaid
flowchart LR
    subgraph Mirakl["Mirakl Platform"]
        ProductAPI["Product API<br/>Registration events"]
        StatusAPI["Status API<br/>Update product status"]
        NotifyAPI["Notification API<br/>Seller alerts"]
    end
    
    subgraph Validator["EAN Validator"]
        Receiver["Webhook Receiver<br/>POST /validate"]
        Processor["Validation Processor"]
        Responder["Status Responder"]
    end
    
    subgraph Internal["Internal Data"]
        CacheAPI["Cache API<br/>GET/PUT EAN data"]
        GOLDAPI["GOLD API<br/>GET product data"]
    end
    
    subgraph External["External APIs"]
        GS1API["GS1 API<br/>GET EAN registration"]
    end

    ProductAPI -->|"Product webhook"| Receiver
    Receiver --> Processor
    Processor -->|"Lookup"| CacheAPI
    Processor -->|"Lookup"| GOLDAPI
    Processor -->|"Lookup"| GS1API
    Processor --> Responder
    Responder -->|"Update status"| StatusAPI
    Responder -->|"Notify seller"| NotifyAPI

    style Validator fill:#e8f5e9,stroke:#2e7d32
    style Internal fill:#fff8e1,stroke:#ff8f00
    style External fill:#fce4ec,stroke:#c2185b
```

---

## 9. Data Model

### Cache Schema

```mermaid
erDiagram
    EAN_CACHE {
        string ean_code PK "Primary key"
        string brand "Manufacturer name"
        string model "Model/SKU"
        string category "Product category"
        string description "Product description"
        string source "GOLD|GS1|MANUAL"
        timestamp validated_at "Validation timestamp"
        int validation_count "Times validated"
        timestamp last_used "Last lookup time"
    }
    
    VALIDATION_LOG {
        uuid id PK "Log entry ID"
        string ean_code FK "EAN validated"
        string product_id "Mirakl product ID"
        string seller_id "Seller identifier"
        string result "APPROVED|REJECTED|REVIEW"
        string rejection_code "REJ-01 to REJ-05"
        float match_score "0.0 to 1.0"
        json seller_data "Submitted attributes"
        json lookup_data "Retrieved attributes"
        timestamp created_at "Log timestamp"
    }
    
    REVIEW_QUEUE {
        uuid id PK "Queue entry ID"
        string ean_code "EAN to review"
        string product_id "Mirakl product ID"
        string seller_id "Seller identifier"
        float match_score "Similarity score"
        json seller_data "Submitted attributes"
        json lookup_data "Retrieved attributes"
        string status "PENDING|APPROVED|REJECTED"
        string reviewer_id "Who reviewed"
        string decision_reason "Approval/rejection reason"
        timestamp created_at "Queue entry time"
        timestamp reviewed_at "Review completion time"
    }
    
    EAN_CACHE ||--o{ VALIDATION_LOG : "validates"
    VALIDATION_LOG ||--o| REVIEW_QUEUE : "may queue"
```

---

## 10. Deployment Architecture

### Infrastructure Overview

```mermaid
flowchart TB
    subgraph GCP["Google Cloud Platform"]
        subgraph Compute["Compute Layer"]
            CloudRun["Cloud Run<br/>EAN Validator Service"]
            CloudFunctions["Cloud Functions<br/>Webhook Handler"]
        end
        
        subgraph Data["Data Layer"]
            BigQuery[("BigQuery<br/>EAN Cache")]
            CloudSQL[("Cloud SQL<br/>Review Queue")]
            Firestore[("Firestore<br/>Validation Logs")]
        end
        
        subgraph Integration["Integration Layer"]
            PubSub["Pub/Sub<br/>Event Queue"]
            APIGateway["API Gateway<br/>External APIs"]
        end
        
        subgraph Monitoring["Monitoring"]
            CloudLogging["Cloud Logging"]
            CloudMonitoring["Cloud Monitoring"]
            Alerting["Alerting"]
        end
    end
    
    subgraph External["External Systems"]
        Mirakl["Mirakl"]
        GOLD["GOLD DB"]
        GS1["GS1 API"]
    end

    Mirakl -->|"Webhook"| CloudFunctions
    CloudFunctions -->|"Queue"| PubSub
    PubSub -->|"Process"| CloudRun
    CloudRun -->|"Query"| BigQuery
    CloudRun -->|"Query"| GOLD
    CloudRun -->|"API Call"| APIGateway
    APIGateway -->|"External"| GS1
    CloudRun -->|"Store"| CloudSQL
    CloudRun -->|"Log"| Firestore
    CloudRun --> CloudLogging
    CloudLogging --> CloudMonitoring
    CloudMonitoring --> Alerting

    style GCP fill:#e8f5e9,stroke:#2e7d32
    style Compute fill:#e3f2fd,stroke:#1976d2
    style Data fill:#fff8e1,stroke:#ff8f00
```

---

## 11. EAN Format Validation Detail

### Check Digit Calculation

```mermaid
flowchart TD
    subgraph Input["Input EAN-13"]
        EAN["5 9 0 1 2 3 4 1 2 3 4 5 ?"]
        Positions["1 2 3 4 5 6 7 8 9 10 11 12 13"]
    end
    
    subgraph Step1["Step 1: Apply Weights"]
        Weights["1 3 1 3 1 3 1 3 1 3 1 3"]
        Calc1["5×1 + 9×3 + 0×1 + 1×3 + 2×1 + 3×3..."]
    end
    
    subgraph Step2["Step 2: Sum Products"]
        Sum["5 + 27 + 0 + 3 + 2 + 9 + 4 + 3 + 2 + 9 + 4 + 15 = 83"]
    end
    
    subgraph Step3["Step 3: Calculate Check"]
        Mod["83 mod 10 = 3"]
        Check["10 - 3 = 7"]
        Final["Check Digit = 7"]
    end
    
    subgraph Result["Valid EAN"]
        ValidEAN["5901234123457 ✅"]
    end

    Input --> Step1
    Step1 --> Step2
    Step2 --> Step3
    Step3 --> Result
```

---

## Related Documents

- [Blueprint](../discovery-docs/ean-validator-blueprint.md) - Discovery document
- [PRD](./ean-validator-prd.md) - Product Requirements Document
- [Assumptions Log](./assumptions-decisions-log.md) - Assumptions tracking
- [SOW](./ean-validator-sow.md) - Statement of Work

---

*Document Version: 1.0*
*Author: Gabriela Souza*
