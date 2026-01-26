# ANATEL Homologation Validation System - Solution Diagrams

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | ANATEL Homologation Validation System |
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
        ANATEL_DB[("📊 ANATEL Database<br/>Homologation Records")]
    end

    subgraph Carrefour["Carrefour Marketplace Architecture"]
        Mirakl["🛍️ Mirakl Platform<br/>Marketplace Management"]
        Omni["🏷️ Omnilogic<br/>Categorization & Enrichment"]
        
        subgraph ValidationSystem["ANATEL Validation System (New)"]
            CM21["CM21<br/>Product Sync Endpoint"]
            Validator["License Validator<br/>3-Layer Validation"]
            CategoryFilter["Category Filter<br/>Homologable Check"]
        end
        
        BigQuery[("☁️ BigQuery<br/>ANATEL License Cache")]
        Crawler["🔄 Data Crawler<br/>Updates every 48h"]
    end

    Seller -->|"1. Submit Product"| Mirakl
    Mirakl -->|"2. Export for Categorization"| Omni
    Omni -->|"3. Return Enriched Data"| CM21
    CM21 -->|"4. Check Category"| CategoryFilter
    CategoryFilter -->|"5. Homologable Product"| Validator
    Validator -->|"6. Query License"| BigQuery
    Validator -->|"7. Return Result"| CM21
    CM21 -->|"8. Update Status"| Mirakl
    
    ANATEL_DB -->|"Sync"| Crawler
    Crawler -->|"Store"| BigQuery

    style ValidationSystem fill:#e1f5fe,stroke:#0288d1
    style Validator fill:#c8e6c9,stroke:#388e3c
    style BigQuery fill:#fff3e0,stroke:#f57c00
```

---

## 2. Product Registration Flow

### Complete Product Lifecycle

```mermaid
sequenceDiagram
    autonumber
    participant S as Seller
    participant M as Mirakl
    participant O as Omnilogic
    participant V as Validation System
    participant BQ as BigQuery
    participant A as ANATEL DB

    Note over A,BQ: Pre-requisite: Crawler syncs every 48h
    A->>BQ: Sync homologation data

    S->>M: Submit new product
    M->>O: CM51: Export for categorization
    O->>O: Categorize & Enrich product
    O->>V: CM21: Send enriched product
    
    V->>V: Check if category is homologable
    
    alt Non-homologable category
        V->>M: Pass through unchanged
        M->>S: Product published ✅
    else Homologable category
        V->>V: Identify product type
        V->>V: Check license field
        
        alt License field empty
            V->>M: Reject: Missing license
            M->>S: Status: Pending ⚠️
        else License provided
            V->>BQ: Query license validation
            BQ->>V: Return license data
            
            V->>V: Layer 1: License exists?
            V->>V: Layer 2: Status = vigente?
            V->>V: Layer 3: Matches product?
            
            alt All validations pass
                V->>M: Approve product
                M->>S: Product published ✅
            else Validation fails
                V->>M: Reject with reason
                M->>S: Status: Pending ⚠️
            end
        end
    end
```

---

## 3. Validation Decision Tree

### 3-Layer License Validation Logic

```mermaid
flowchart TD
    Start([Product Received<br/>from Omnilogic]) --> CategoryCheck{Is category<br/>in homologable list?}
    
    CategoryCheck -->|No| PassThrough[✅ Pass Through<br/>No validation needed]
    PassThrough --> Publish1([Product Published])
    
    CategoryCheck -->|Yes| IdentifyProduct[Identify Product Type<br/>Using brand/model]
    
    IdentifyProduct --> LicenseCheck{License field<br/>provided?}
    
    LicenseCheck -->|Empty/Missing| RejectMissing[❌ Reject<br/>Reason: Missing License]
    RejectMissing --> Pending1([Status: Pending<br/>Seller notified])
    
    LicenseCheck -->|Present| Layer1{LAYER 1<br/>License exists<br/>in ANATEL DB?}
    
    Layer1 -->|Not Found| RejectNotFound[❌ Reject<br/>Reason: License Not Found]
    RejectNotFound --> Pending2([Status: Pending<br/>Seller notified])
    
    Layer1 -->|Found| Layer2{LAYER 2<br/>Status =<br/>'vigente'?}
    
    Layer2 -->|Inactive/Expired| RejectInactive[❌ Reject<br/>Reason: License Inactive]
    RejectInactive --> Pending3([Status: Pending<br/>Seller notified])
    
    Layer2 -->|Active| Layer3{LAYER 3<br/>License matches<br/>product brand/model?}
    
    Layer3 -->|Mismatch| RejectMismatch[❌ Reject<br/>Reason: License Mismatch]
    RejectMismatch --> Pending4([Status: Pending<br/>Seller notified])
    
    Layer3 -->|Match| Approve[✅ Approved<br/>All validations passed]
    Approve --> Publish2([Product Published<br/>With license displayed])

    style Start fill:#e3f2fd,stroke:#1976d2
    style PassThrough fill:#c8e6c9,stroke:#388e3c
    style Approve fill:#c8e6c9,stroke:#388e3c
    style RejectMissing fill:#ffcdd2,stroke:#d32f2f
    style RejectNotFound fill:#ffcdd2,stroke:#d32f2f
    style RejectInactive fill:#ffcdd2,stroke:#d32f2f
    style RejectMismatch fill:#ffcdd2,stroke:#d32f2f
```

---

## 4. Integration Architecture

### API Integration Flow

```mermaid
flowchart LR
    subgraph Seller["Seller Systems"]
        SellerAPI["Seller API<br/>Product submission"]
    end
    
    subgraph Mirakl["Mirakl Platform"]
        CM51["CM51<br/>POST /products/export"]
        ProductDB[("Product<br/>Database")]
        StatusMgr["Status Manager<br/>Pending/Published"]
    end
    
    subgraph Omnilogic["Omnilogic Service"]
        Categorizer["Categorization<br/>Engine"]
        Enricher["Data<br/>Enricher"]
    end
    
    subgraph Validation["ANATEL Validation System"]
        CM21["CM21<br/>POST /products/sync"]
        CM22["CM22<br/>GET /sync/{ID}"]
        CM23["CM23<br/>GET /sync/{ID}/report"]
        ValidatorCore["Validator<br/>Core"]
    end
    
    subgraph DataLayer["Data Layer"]
        BigQuery[("BigQuery<br/>ANATEL Cache")]
        Crawler["Crawler<br/>Every 48h"]
    end
    
    subgraph ANATEL["ANATEL"]
        ANATELPortal["ANATEL Portal<br/>Public Database"]
    end

    SellerAPI --> ProductDB
    ProductDB --> CM51
    CM51 --> Categorizer
    Categorizer --> Enricher
    Enricher --> CM21
    CM21 --> ValidatorCore
    ValidatorCore --> BigQuery
    ValidatorCore --> CM21
    CM21 --> StatusMgr
    StatusMgr --> ProductDB
    
    ANATELPortal --> Crawler
    Crawler --> BigQuery

    style Validation fill:#e8f5e9,stroke:#2e7d32
    style DataLayer fill:#fff8e1,stroke:#ff8f00
```

---

## 5. Seller Resubmission Flow

### Product Correction Journey

```mermaid
flowchart TD
    Start([Product Rejected]) --> Notify[Seller receives<br/>rejection notification]
    Notify --> ViewReason[Seller views<br/>rejection reason in Mirakl]
    
    ViewReason --> Decision{Seller decision}
    
    Decision -->|Abandon| Abandon([Product remains<br/>in pending status])
    
    Decision -->|Correct| Identify[Identify issue type]
    
    Identify --> MissingLicense{Missing<br/>license?}
    MissingLicense -->|Yes| AddLicense[Add valid<br/>ANATEL license code]
    
    Identify --> InvalidLicense{Invalid<br/>license?}
    InvalidLicense -->|Yes| CorrectLicense[Correct license code<br/>or obtain new one]
    
    Identify --> MismatchLicense{License<br/>mismatch?}
    MismatchLicense -->|Yes| MatchLicense[Find correct license<br/>for product]
    
    AddLicense --> Resubmit[Resubmit product<br/>to Mirakl]
    CorrectLicense --> Resubmit
    MatchLicense --> Resubmit
    
    Resubmit --> Revalidate[Product goes through<br/>validation again]
    
    Revalidate --> Result{Validation<br/>result}
    
    Result -->|Pass| Published([✅ Product Published])
    Result -->|Fail| Start

    style Start fill:#ffcdd2,stroke:#d32f2f
    style Published fill:#c8e6c9,stroke:#388e3c
    style Revalidate fill:#e3f2fd,stroke:#1976d2
```

---

## 6. Data Flow Architecture

### ANATEL Database Synchronization

```mermaid
flowchart TB
    subgraph ANATEL["ANATEL Official Sources"]
        Portal["ANATEL Portal<br/>informacoes.anatel.gov.br"]
        Mosaico["MOSAICO System<br/>Homologation Database"]
        OpenData["Open Data<br/>Product Downloads"]
    end
    
    subgraph Crawler["Data Crawler Service"]
        Scheduler["Scheduler<br/>Every 48 hours"]
        Extractor["Data Extractor"]
        Transformer["Data Transformer"]
        Loader["BigQuery Loader"]
    end
    
    subgraph BigQuery["BigQuery Dataset"]
        Table[("br_digitalcomm_anatel_homologados.produtos")]
        
        subgraph Fields["Key Fields"]
            TipoProduto["tipo_produto"]
            Modelo["modelo"]
            Fabricante["fabricante"]
            NomeComercial["nome_comercial"]
            Status["status_homologacao"]
            DataHomologacao["data_homologacao"]
        end
    end
    
    subgraph Validation["Validation System"]
        Validator["License Validator"]
    end

    Portal --> Extractor
    Mosaico --> Extractor
    OpenData --> Extractor
    
    Scheduler --> Extractor
    Extractor --> Transformer
    Transformer --> Loader
    Loader --> Table
    
    Table --> Fields
    Fields --> Validator

    style BigQuery fill:#fff3e0,stroke:#f57c00
    style Crawler fill:#e1f5fe,stroke:#0288d1
```

---

## 7. State Machine: Product Status

### Product Status Transitions

```mermaid
stateDiagram-v2
    [*] --> Novo: Seller submits product
    
    Novo --> EmCategorizacao: Sent to Omnilogic
    
    EmCategorizacao --> Categorizado: Omnilogic success
    EmCategorizacao --> RejeitadoOmni: Omnilogic rejection
    
    Categorizado --> EmValidacao: Sent to ANATEL validator
    
    EmValidacao --> Aprovado: All validations pass
    EmValidacao --> AguardandoAlteracao: Validation fails
    
    Aprovado --> Publicado: Published to marketplace
    
    AguardandoAlteracao --> EmValidacao: Seller resubmits
    AguardandoAlteracao --> Cancelado: Seller abandons
    
    RejeitadoOmni --> EmCategorizacao: Seller corrects
    RejeitadoOmni --> Cancelado: Seller abandons
    
    Publicado --> [*]
    Cancelado --> [*]

    note right of EmValidacao
        3-Layer Validation:
        1. License exists
        2. License active
        3. License matches
    end note
    
    note right of AguardandoAlteracao
        Seller sees:
        - Rejection reason
        - Required action
    end note
```

---

## 8. Use Case Diagram

### System Actors and Use Cases

```mermaid
flowchart TB
    subgraph Actors["Actors"]
        Seller["🛒 Seller"]
        CatalogOps["👤 Catalog Operations"]
        Compliance["⚖️ Compliance Team"]
        System["🤖 Validation System"]
    end
    
    subgraph UseCases["Use Cases"]
        UC1["UC-01: Submit Product"]
        UC2["UC-02: View Rejection Reason"]
        UC3["UC-03: Correct and Resubmit"]
        UC4["UC-04: Monitor Validation Queue"]
        UC5["UC-05: Review Pending Products"]
        UC6["UC-06: Generate Compliance Reports"]
        UC7["UC-07: Validate License"]
        UC8["UC-08: Query ANATEL Database"]
        UC9["UC-09: Update Product Status"]
    end
    
    Seller --> UC1
    Seller --> UC2
    Seller --> UC3
    
    CatalogOps --> UC4
    CatalogOps --> UC5
    
    Compliance --> UC6
    
    System --> UC7
    System --> UC8
    System --> UC9
    
    UC1 -.->|triggers| UC7
    UC7 -.->|requires| UC8
    UC7 -.->|results in| UC9
    UC3 -.->|triggers| UC7

    style Seller fill:#bbdefb,stroke:#1976d2
    style CatalogOps fill:#c8e6c9,stroke:#388e3c
    style Compliance fill:#fff9c4,stroke:#fbc02d
    style System fill:#e1bee7,stroke:#8e24aa
```

---

## 9. Component Diagram

### System Components

```mermaid
flowchart TB
    subgraph Frontend["Mirakl Frontend"]
        SellerPortal["Seller Portal<br/>Product Registration"]
        AdminPortal["Admin Portal<br/>Catalog Management"]
    end
    
    subgraph Integration["Integration Layer"]
        CM21API["CM21 API<br/>/products/synchronization"]
        CM22API["CM22 API<br/>/sync/{id}"]
        CM23API["CM23 API<br/>/sync/{id}/report"]
    end
    
    subgraph Core["Validation Core"]
        CategoryService["Category Service<br/>Homologable check"]
        ProductIdentifier["Product Identifier<br/>Brand/Model matching"]
        LicenseValidator["License Validator<br/>3-Layer validation"]
        StatusUpdater["Status Updater<br/>Mirakl integration"]
    end
    
    subgraph Data["Data Services"]
        BigQueryClient["BigQuery Client<br/>License queries"]
        CacheService["Cache Service<br/>Performance optimization"]
        AuditLogger["Audit Logger<br/>Compliance tracking"]
    end
    
    subgraph External["External Dependencies"]
        MiraklAPI["Mirakl API"]
        OmnilogicAPI["Omnilogic API"]
        BigQueryDB[("BigQuery")]
    end

    SellerPortal --> MiraklAPI
    AdminPortal --> MiraklAPI
    
    OmnilogicAPI --> CM21API
    CM21API --> CategoryService
    CategoryService --> ProductIdentifier
    ProductIdentifier --> LicenseValidator
    LicenseValidator --> BigQueryClient
    BigQueryClient --> BigQueryDB
    LicenseValidator --> StatusUpdater
    StatusUpdater --> MiraklAPI
    
    CM21API --> AuditLogger
    LicenseValidator --> AuditLogger
    BigQueryClient --> CacheService

    style Core fill:#e8f5e9,stroke:#2e7d32
    style Integration fill:#e3f2fd,stroke:#1976d2
    style Data fill:#fff8e1,stroke:#ff8f00
```

---

## 10. Deployment Architecture

### Infrastructure Overview

```mermaid
flowchart TB
    subgraph GCP["Google Cloud Platform"]
        subgraph Compute["Compute"]
            AppEngine["App Engine / Cloud Run<br/>Validation Service"]
            CloudFunctions["Cloud Functions<br/>Crawler Service"]
        end
        
        subgraph Data["Data Services"]
            BigQuery[("BigQuery<br/>ANATEL Data")]
            CloudStorage["Cloud Storage<br/>Logs & Backups"]
        end
        
        subgraph Security["Security"]
            IAM["IAM<br/>Access Control"]
            SecretManager["Secret Manager<br/>API Keys"]
        end
        
        subgraph Monitoring["Monitoring"]
            CloudLogging["Cloud Logging"]
            CloudMonitoring["Cloud Monitoring"]
            Alerting["Alerting"]
        end
    end
    
    subgraph External["External Systems"]
        Mirakl["Mirakl Platform"]
        Omnilogic["Omnilogic"]
        ANATEL["ANATEL Portal"]
    end

    Omnilogic -->|HTTPS| AppEngine
    AppEngine -->|Query| BigQuery
    AppEngine -->|Update| Mirakl
    AppEngine --> CloudLogging
    CloudLogging --> CloudMonitoring
    CloudMonitoring --> Alerting
    
    CloudFunctions -->|Scheduled| ANATEL
    CloudFunctions -->|Load| BigQuery
    CloudFunctions --> CloudLogging
    
    IAM --> AppEngine
    IAM --> BigQuery
    SecretManager --> AppEngine

    style GCP fill:#e8f5e9,stroke:#2e7d32
    style Compute fill:#e3f2fd,stroke:#1976d2
    style Data fill:#fff8e1,stroke:#ff8f00
```

---

## Related Documents

- [Blueprint](../discovery-docs/anatel-blueprint.md) - Discovery document
- [PRD](./anatel-prd.md) - Product Requirements Document
- [SOW](./anatel-sow.md) - Statement of Work

---

*Document Version: 1.0*
*Author: Gabriela Souza*
