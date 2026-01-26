# Products Without Offer Blocker - Solution Diagrams

---

## Cover Page

| Field | Value |
|-------|-------|
| Project Name | Products Without Offer Blocker |
| Client | Carrefour Brasil |
| Document Author | Gabriela Souza |
| Version | 1.0 |

---

## 1. System Architecture Overview

### Before vs. After

```mermaid
graph TB
    subgraph Before["BEFORE: Current Flow"]
        B_Seller["🛒 Seller"] --> B_Mirakl["Mirakl"]
        B_Mirakl --> B_Omni["Omnilogic 💰"]
        B_Omni --> B_EAN["EAN Lookup 💰"]
        B_EAN --> B_VTEX["VTEX 💰"]
        B_VTEX --> B_Check{Has Offer?}
        B_Check -->|Yes| B_Pub["Published ✅"]
        B_Check -->|No| B_Hidden["Hidden ❌<br/>(Costs incurred, no revenue)"]
    end
    
    subgraph After["AFTER: With Blocker"]
        A_Seller["🛒 Seller"] --> A_Validator["🛡️ Offer Validator"]
        A_Validator --> A_Check{Has Offer?}
        A_Check -->|Yes| A_Mirakl["Mirakl"]
        A_Check -->|No| A_Block["Blocked 🚫<br/>(No costs incurred)"]
        A_Mirakl --> A_Omni["Omnilogic 💰"]
        A_Omni --> A_EAN["EAN Lookup 💰"]
        A_EAN --> A_VTEX["VTEX 💰"]
        A_VTEX --> A_Pub["Published ✅"]
    end

    style A_Validator fill:#c8e6c9,stroke:#388e3c
    style A_Block fill:#ffcdd2,stroke:#d32f2f
    style B_Hidden fill:#ffcdd2,stroke:#d32f2f
```

---

## 2. Validation Flow

### Complete Decision Logic

```mermaid
flowchart TD
    Start([Product Registration<br/>Received]) --> TypeCheck{New Registration<br/>or Update?}
    
    TypeCheck -->|Update| PassThrough[✅ Pass Through<br/>to Pipeline]
    
    TypeCheck -->|New Registration| PriceCheck{Price<br/>Present?}
    
    PriceCheck -->|No/Null| REJ01[❌ REJ-01<br/>Price is required]
    
    PriceCheck -->|Yes| PriceNumeric{Price<br/>Numeric?}
    
    PriceNumeric -->|No| REJ03[❌ REJ-03<br/>Price must be valid number]
    
    PriceNumeric -->|Yes| PriceZero{Price<br/>> 0?}
    
    PriceZero -->|No| REJ02[❌ REJ-02<br/>Price must be > 0]
    
    PriceZero -->|Yes| StockCheck{Stock<br/>Present?}
    
    StockCheck -->|No/Null| REJ04[❌ REJ-04<br/>Stock is required]
    
    StockCheck -->|Yes| StockNumeric{Stock<br/>Numeric?}
    
    StockNumeric -->|No| REJ06[❌ REJ-06<br/>Stock must be valid number]
    
    StockNumeric -->|Yes| StockZero{Stock<br/>> 0?}
    
    StockZero -->|No| REJ05[❌ REJ-05<br/>Stock must be > 0]
    
    StockZero -->|Yes| Approved[✅ Approved<br/>Proceed to Mirakl]
    
    REJ01 --> Block([Blocked + Logged])
    REJ02 --> Block
    REJ03 --> Block
    REJ04 --> Block
    REJ05 --> Block
    REJ06 --> Block
    
    Approved --> Pipeline([Enter Pipeline])
    PassThrough --> Pipeline

    style Start fill:#e3f2fd,stroke:#1976d2
    style Approved fill:#c8e6c9,stroke:#388e3c
    style PassThrough fill:#c8e6c9,stroke:#388e3c
    style REJ01 fill:#ffcdd2,stroke:#d32f2f
    style REJ02 fill:#ffcdd2,stroke:#d32f2f
    style REJ03 fill:#ffcdd2,stroke:#d32f2f
    style REJ04 fill:#ffcdd2,stroke:#d32f2f
    style REJ05 fill:#ffcdd2,stroke:#d32f2f
    style REJ06 fill:#ffcdd2,stroke:#d32f2f
```

---

## 3. Sequence Diagram

### Valid Registration Flow

```mermaid
sequenceDiagram
    autonumber
    participant S as Seller
    participant V as Offer Validator
    participant M as Mirakl
    participant O as Omnilogic
    participant E as EAN Lookup
    participant VT as VTEX

    S->>V: Submit product (price=100, stock=50)
    V->>V: Validate price (✓ present, ✓ numeric, ✓ > 0)
    V->>V: Validate stock (✓ present, ✓ numeric, ✓ > 0)
    V->>M: Forward to Mirakl
    M->>O: Send for enrichment
    O->>M: Return enriched data
    M->>E: Validate EAN
    E->>M: EAN valid
    M->>VT: Register in VTEX
    VT->>M: Registration complete
    M->>S: Success: Product published
```

### Blocked Registration Flow

```mermaid
sequenceDiagram
    autonumber
    participant S as Seller
    participant V as Offer Validator
    participant L as Logger
    participant M as Mirakl

    S->>V: Submit product (price=0, stock=null)
    V->>V: Validate price (✗ zero)
    V->>V: Validate stock (✗ null)
    V->>L: Log blocked attempt
    V->>S: Error: Price must be > 0, Stock is required
    
    Note over M: Product never reaches Mirakl
    Note over S: No enrichment costs incurred
```

---

## 4. Integration Architecture

### System Integration Points

```mermaid
flowchart LR
    subgraph Seller["Seller Systems"]
        API["Seller API"]
        Portal["Seller Portal"]
    end
    
    subgraph Validator["Offer Validator"]
        Endpoint["API Endpoint"]
        Logic["Validation Logic"]
        Logger["Logger"]
    end
    
    subgraph Pipeline["Existing Pipeline"]
        Mirakl["Mirakl"]
        Omni["Omnilogic"]
        EAN["EAN Services"]
        VTEX["VTEX"]
    end
    
    subgraph Storage["Storage"]
        Logs[("Validation<br/>Logs")]
    end

    API --> Endpoint
    Portal --> Endpoint
    Endpoint --> Logic
    Logic -->|Valid| Mirakl
    Logic -->|Invalid| Logger
    Logger --> Logs
    Logic -->|Invalid| API
    Logic -->|Invalid| Portal
    
    Mirakl --> Omni
    Omni --> EAN
    EAN --> VTEX

    style Validator fill:#e8f5e9,stroke:#2e7d32
```

---

## 5. Validation Matrix

### Price Validation

```mermaid
flowchart LR
    subgraph PriceValidation["Price Validation"]
        P1["null"] -->|❌| R1["REJ-01"]
        P2["''"] -->|❌| R1
        P3["0"] -->|❌| R2["REJ-02"]
        P4["-5"] -->|❌| R2
        P5["ABC"] -->|❌| R3["REJ-03"]
        P6["10.5$"] -->|❌| R3
        P7["100"] -->|✅| OK1["Valid"]
        P8["99.99"] -->|✅| OK1
    end

    style R1 fill:#ffcdd2,stroke:#d32f2f
    style R2 fill:#ffcdd2,stroke:#d32f2f
    style R3 fill:#ffcdd2,stroke:#d32f2f
    style OK1 fill:#c8e6c9,stroke:#388e3c
```

### Stock Validation

```mermaid
flowchart LR
    subgraph StockValidation["Stock Validation"]
        S1["null"] -->|❌| R4["REJ-04"]
        S2["''"] -->|❌| R4
        S3["0"] -->|❌| R5["REJ-05"]
        S4["-10"] -->|❌| R5
        S5["ABC"] -->|❌| R6["REJ-06"]
        S6["10 units"] -->|❌| R6
        S7["50"] -->|✅| OK2["Valid"]
        S8["100"] -->|✅| OK2
    end

    style R4 fill:#ffcdd2,stroke:#d32f2f
    style R5 fill:#ffcdd2,stroke:#d32f2f
    style R6 fill:#ffcdd2,stroke:#d32f2f
    style OK2 fill:#c8e6c9,stroke:#388e3c
```

---

## 6. Use Case Diagram

### Actors and Use Cases

```mermaid
flowchart TB
    subgraph Actors["Actors"]
        Seller["🛒 Seller"]
        System["🤖 Validator"]
        Ops["👤 Operations"]
    end
    
    subgraph UseCases["Use Cases"]
        UC1["UC-01: Submit valid product"]
        UC2["UC-02: Submit without stock"]
        UC3["UC-03: Submit without price"]
        UC4["UC-04: Submit without offer"]
        UC5["UC-05: Submit invalid format"]
        UC6["UC-06: Update existing product"]
        UC7["View blocked attempts"]
        UC8["Analyze rejection patterns"]
    end

    Seller --> UC1
    Seller --> UC2
    Seller --> UC3
    Seller --> UC4
    Seller --> UC5
    Seller --> UC6
    
    System --> UC7
    
    Ops --> UC7
    Ops --> UC8

    style Seller fill:#bbdefb,stroke:#1976d2
    style System fill:#c8e6c9,stroke:#388e3c
    style Ops fill:#fff9c4,stroke:#fbc02d
```

---

## 7. Data Flow

### Validation Data Flow

```mermaid
flowchart TD
    subgraph Input["Input Data"]
        Product["Product Data<br/>• product_id<br/>• name<br/>• description<br/>• price<br/>• stock<br/>• ..."]
    end
    
    subgraph Extract["Extract Offer Fields"]
        Price["price"]
        Stock["stock"]
        ProductID["product_id"]
    end
    
    subgraph Validate["Validation"]
        V1["Check if Update"]
        V2["Validate Price"]
        V3["Validate Stock"]
    end
    
    subgraph Output["Output"]
        Success["Forward to Pipeline"]
        Failure["Return Errors"]
        Log["Write to Log"]
    end

    Product --> Price
    Product --> Stock
    Product --> ProductID
    
    ProductID --> V1
    V1 -->|Update| Success
    V1 -->|New| V2
    
    Price --> V2
    V2 -->|Valid| V3
    V2 -->|Invalid| Failure
    
    Stock --> V3
    V3 -->|Valid| Success
    V3 -->|Invalid| Failure
    
    Failure --> Log

    style Success fill:#c8e6c9,stroke:#388e3c
    style Failure fill:#ffcdd2,stroke:#d32f2f
```

---

## 8. Cost Impact Visualization

### Cost Flow Comparison

```mermaid
flowchart TB
    subgraph Without["Without Blocker"]
        W1["100 Products<br/>Submitted"]
        W2["70 with Offer"]
        W3["30 without Offer"]
        W4["All 100 → Pipeline<br/>Cost: $100"]
        W5["70 Published<br/>Revenue: $X"]
        W6["30 Hidden<br/>Revenue: $0"]
        
        W1 --> W2
        W1 --> W3
        W2 --> W4
        W3 --> W4
        W4 --> W5
        W4 --> W6
    end
    
    subgraph With["With Blocker"]
        B1["100 Products<br/>Submitted"]
        B2["70 with Offer"]
        B3["30 without Offer"]
        B4["70 → Pipeline<br/>Cost: $70"]
        B5["30 → Blocked<br/>Cost: $0"]
        B6["70 Published<br/>Revenue: $X"]
        
        B1 --> B2
        B1 --> B3
        B2 --> B4
        B3 --> B5
        B4 --> B6
    end

    style W6 fill:#ffcdd2,stroke:#d32f2f
    style B5 fill:#c8e6c9,stroke:#388e3c
    style B6 fill:#c8e6c9,stroke:#388e3c
```

---

## 9. Deployment Architecture

### Infrastructure

```mermaid
flowchart TB
    subgraph GCP["Google Cloud Platform"]
        subgraph Compute["Compute"]
            CloudRun["Cloud Run<br/>Offer Validator"]
        end
        
        subgraph Data["Data"]
            Firestore[("Firestore<br/>Validation Logs")]
        end
        
        subgraph Monitoring["Monitoring"]
            Logging["Cloud Logging"]
            Metrics["Cloud Monitoring"]
        end
    end
    
    subgraph External["External Systems"]
        Seller["Seller API"]
        Mirakl["Mirakl"]
    end

    Seller -->|HTTPS| CloudRun
    CloudRun -->|Valid| Mirakl
    CloudRun -->|Log| Firestore
    CloudRun --> Logging
    Logging --> Metrics

    style Compute fill:#e3f2fd,stroke:#1976d2
    style Data fill:#fff8e1,stroke:#ff8f00
```

---

## 10. Error Response Format

### API Response Structure

```mermaid
graph TB
    subgraph SuccessResponse["Success Response (200)"]
        S1["status: 'success'"]
        S2["message: 'Product accepted'"]
        S3["product_id: '12345'"]
    end
    
    subgraph ErrorResponse["Error Response (400)"]
        E1["status: 'blocked'"]
        E2["errors: [...]"]
        E3["• code: 'REJ-02'"]
        E4["• field: 'price'"]
        E5["• message: 'Price must be > 0'"]
    end

    style SuccessResponse fill:#c8e6c9,stroke:#388e3c
    style ErrorResponse fill:#ffcdd2,stroke:#d32f2f
```

---

## Related Documents

- [Blueprint](../discovery-docs/offer-blocker-blueprint.md)
- [PRD](./offer-blocker-prd.md)
- [SOW](./offer-blocker-sow.md)
- [Assumptions Log](./assumptions-decisions-log.md)

---

*Document Version: 1.0*
*Author: Gabriela Souza*
