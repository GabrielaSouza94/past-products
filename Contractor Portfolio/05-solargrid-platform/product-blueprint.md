# SolarGrid Energy Platform Rebuild — Blueprint

**Client:** SolarGrid Energy (SolarGrid Field Services, LLC)
**Contact:** Martin Janda, mjanda@solargridpower.net
**Date:** 2026-03-10
**Version:** 1.0
**Authors:** Roberto Ronderos, Gabriela Souza
**Status:** Active — Phase 1 Discovery in progress (Mar 9–27, 2026)

---

## 1. Problem Definition

### 1.1 Business Context

SolarGrid Energy is an energy field services company that deploys and monitors distributed power infrastructure — solar arrays, generators, battery storage, power conditioning (inverters), and electrical loads — across multiple physical locations for B2B clients. Each client (tenant) needs real-time visibility into their energy assets to make operational decisions: when to run generators, how battery storage is performing, whether solar production matches forecasts, and whether equipment faults require attention.

SolarGrid invested approximately one year with a previous development team to build this monitoring platform on MySQL + Ruby on Rails 8 + NextJS + AWS ECS/CDK. That engagement failed to deliver a production-ready product. SolarGrid is now seeking a strategic build partner to evaluate the existing codebase, determine a keep-vs-rebuild strategy, and deliver a production-grade platform.

### 1.2 Core Problem Statement

**SolarGrid Energy's B2B clients lack a reliable, real-time monitoring and management platform for their distributed energy infrastructure.** Without this platform:

- Operations managers cannot see the current state of solar production, generation, battery storage, and load across their locations from a single view
- Equipment faults and data feed issues go undetected until manual inspection
- Historical trend analysis and forecasting are unavailable, preventing data-driven operational decisions
- Configuration management of deployed equipment (component assignments, electrical connections, external data source mappings) is manual and error-prone
- No multi-tenant isolation exists at the architectural level, blocking SolarGrid from safely onboarding multiple clients

### 1.3 Target Users

| Persona | Role | Primary Needs |
|---------|------|---------------|
| **Operations Manager** | Tenant employee monitoring energy infrastructure daily | Real-time company & location dashboards, alerting, trend analysis, drill-down from summary to component detail |
| **Tenant Admin** | Client-side user managing their tenant configuration | External source credentials, location configuration, notification rules, user management |
| **SolarGrid Configuration Admin** | SolarGrid internal staff configuring equipment and deployments | Component setup (solar/generator/storage/inverter/sensor specs), location component assignments, electrical connection topology, data series mapping |
| **SolarGrid Support** | SolarGrid internal staff providing cross-tenant support | Access to all tenant data for troubleshooting (requires dedicated admin access pattern) |

### 1.4 Scope Overview

This platform is a **Production-Ready** engagement (not an MVP). It encompasses:

- **20+ screens/views** across dashboard, detail, configuration, and security sections
- **Event-driven ETL pipeline** processing telemetry from Sol-Ark inverters and SolarGrid IoT devices through 3 cascading statistics levels (Component → Location → Company)
- **5 external integrations**: Sol-Ark API, SolarGrid IoT, Weather API, Solar Production Forecast API, Google Maps
- **Multi-tenant architecture** with strict data isolation throughout every layer
- **Real-time updates** via event subscriptions for live dashboard refresh

**Existing tech stack under evaluation (Phase 1):** MySQL, Ruby on Rails 8 (Ruby 3.2.2, Rails 8.0.0), NextJS, AWS CDK, AWS ECS. Phase 1 Audit + ADRs will determine keep/modify/replace per component. [Figma prototype]([Figma Design Link Removed]) (20+ screens) exists from previous team.

### 1.5 Scope Exclusions

- Sol-Ark extract processes (already in production, maintained solely by SolarGrid)
- Existing SolarGrid reports: Energy Transactions, Daily Generator Stats, Twice Daily Generator Fuel Levels
- Custom component type definition by tenants (components must be programmatically supported)
- Mobile native applications (responsive web only)

---

## 2. User Stories

### 2.1 Real-Time Monitoring & Dashboards

#### Company-Level Dashboard

| ID | Story | Priority |
|----|-------|----------|
| MON-01 | As an Operations Manager, I want to see a company-wide summary of solar production (current output, predicted output, deployed capacity, today's total) so I can assess overall solar performance at a glance. | Must |
| MON-02 | As an Operations Manager, I want to see a company-wide summary of fuel supply (current flow rate, fuel level %, today's usage) so I can monitor fuel consumption across all locations. | Must |
| MON-03 | As an Operations Manager, I want to see a company-wide summary of generation (current production, deployed capacity, today's total) so I can track generator output. | Must |
| MON-04 | As an Operations Manager, I want to see a company-wide summary of battery status (energy output, energy input, stored energy, deployed capacity) so I can monitor storage utilization. | Must |
| MON-05 | As an Operations Manager, I want to see a company-wide summary of electrical load (current consumption, today's total energy) so I can track power demand. | Must |
| MON-06 | As an Operations Manager, I want to see a status overview of all external data feeds (link status color-coded, last access time, last error time) so I can quickly identify connectivity issues. | Must |
| MON-07 | As an Operations Manager, I want to see a table of all locations with key metrics (usage, consumption, stored energy, battery runtime, solar production, generation, errors, warnings) so I can compare location performance. | Must |
| MON-08 | As an Operations Manager, I want location rows highlighted red (errors > 0), orange (warnings > 0), or default (no issues) so I can spot problems immediately. | Must |
| MON-09 | As an Operations Manager, I want a geographic map of all locations with color-coded pins (green/orange/red matching location status) and mouseover tooltips showing key metrics, so I can see the spatial distribution and status of my infrastructure. | Must |
| MON-10 | As an Operations Manager, I want to see a list of unresolved alerts across the company so I can prioritize issue resolution. | Must |
| MON-11 | As an Operations Manager, I want to double-click any summary card to navigate to the corresponding detail screen with appropriate context. | Must |
| MON-12 | As an Operations Manager, I want summary-level temporal data displayed in my browser's timezone so times are meaningful to me regardless of location timezones. | Must |

#### Geographic Dashboard

| ID | Story | Priority |
|----|-------|----------|
| GEO-01 | As an Operations Manager, I want a full-screen geographic map view with a scrolling ticker showing real-time location status updates. | Should |
| GEO-02 | As an Operations Manager, I want to configure which metrics appear in the ticker component. | Should |

### 2.2 Location & Component Detail Views

#### Location Details

| ID | Story | Priority |
|----|-------|----------|
| LOC-01 | As an Operations Manager, I want to view detailed metrics for a single location (solar, fuel, generation, battery, load, weather) in cards similar to the company dashboard but scoped to one location. | Must |
| LOC-02 | As an Operations Manager, I want to select which location to view from a dropdown. | Must |
| LOC-03 | As an Operations Manager, I want to see per-category alert status indicators (Solar, Fuel, Generator, Battery, Load) color-coded by severity (green = no alerts, orange = moderate, red = severe) for the current location. | Must |
| LOC-04 | As an Operations Manager, I want to see an equipment schematic/connection diagram showing the electrical topology of all components at the location, including power flow direction and monitoring assignments. | Must |
| LOC-05 | As an Operations Manager, I want to see a chronological alert log of unresolved alerts for the current location with details from the Alerts data source. | Must |
| LOC-06 | As an Operations Manager, I want to see location information (name, GPS coordinates, city, state, country, deployment date, active status). | Must |
| LOC-07 | As an Operations Manager, I want to view statistical summaries (average, variance, std deviation, sample count, min/max dates) for each data series at the location level. | Should |
| LOC-08 | As an Operations Manager, I want location-level temporal data displayed in the location's configured timezone. | Must |
| LOC-09 | As an Operations Manager, I want to see current weather conditions (temperature, general conditions) for the location, reported in my preferred temperature unit. | Should |
| LOC-10 | As an Operations Manager, I want to see the forecasted next generator run time based on storage level/capacity and load. | Should |

#### Solar Details

| ID | Story | Priority |
|----|-------|----------|
| SOL-01 | As an Operations Manager, I want a data grid showing each solar component's current production, predicted production, deployed capacity, today's total, and predicted total for today. | Must |
| SOL-02 | As an Operations Manager, I want to click a solar component row to see its activity chart (actual vs predicted production) and associated documentation. | Must |
| SOL-03 | As an Operations Manager, I want to view and download documentation files uploaded for each solar component. | Should |

#### Generation Details

| ID | Story | Priority |
|----|-------|----------|
| GEN-01 | As an Operations Manager, I want a data grid of all generators showing key telemetry values and alert/fault count. | Must |
| GEN-02 | As an Operations Manager, I want to click a generator to see detailed readings (oil pressure, coolant temp, fuel level, voltages, currents, power per phase), rated capacity, serial number, and last known fault. | Must |
| GEN-03 | As an Operations Manager, I want to view generator maintenance information (runtime, number of starts, time to maintenance). | Must |
| GEN-04 | As an Operations Manager, I want a chart showing today's total generation across all generators by location. | Should |

#### Load Details

| ID | Story | Priority |
|----|-------|----------|
| LOAD-01 | As an Operations Manager, I want a data grid of all load components showing current power consumption and power type. | Must |
| LOAD-02 | As an Operations Manager, I want a power consumption chart showing total power across the company by location. | Should |

#### Storage Details

| ID | Story | Priority |
|----|-------|----------|
| STOR-01 | As an Operations Manager, I want a data grid showing each storage component's state of charge, charge/discharge rate, deployed capacity, battery model, and number of batteries. | Must |
| STOR-02 | As an Operations Manager, I want a battery state card showing SOC, current charge/discharge, and estimated battery runtime for a selected storage component. | Must |

### 2.3 Historical Analysis & Trends

| ID | Story | Priority |
|----|-------|----------|
| TRND-01 | As an Operations Manager, I want to select one or more data series from a categorized dropdown, specify a date/time range (5-minute granularity), and view a time series chart for Company, Location, or Component level statistics. | Must |
| TRND-02 | As an Operations Manager, I want trend charts available on the Dashboard Summary, Location Details, Solar Details, Generation Details, Load Details, and Storage Details screens. | Must |
| TRND-03 | As an Operations Manager, I want the X-axis scale to adapt dynamically to the selected date range and the Y-axis to support multiple measurement types. | Must |

### 2.4 Alert Management & Notifications

| ID | Story | Priority |
|----|-------|----------|
| ALT-01 | As a Tenant Admin, I want to configure notification groups with a list of recipients and their contact information. | Must |
| ALT-02 | As a Tenant Admin, I want to configure which alert conditions trigger notifications for each group. | Must |
| ALT-03 | As a Tenant Admin, I want to set call priority order for notification recipients. | Must |
| ALT-04 | As a Tenant Admin, I want to define effective schedules (days/times) when notification groups are active. | Must |
| ALT-05 | As an Operations Manager, I want alerts classified by category (Solar, Generation, Load, Storage, Fuel, External Sources) and severity (severe, moderate, informational). | Must |

### 2.5 Location & Component Configuration

#### Location Configuration

| ID | Story | Priority |
|----|-------|----------|
| CFG-01 | As a Tenant Admin, I want to configure location general settings: name, active status, GPS coordinates, city/state/country, timezone, deployment date. | Must |
| CFG-02 | As a Tenant Admin, I want to upload, view, and download documentation files associated with a location. | Must |
| CFG-03 | As a Tenant Admin, I want to add, edit, and remove solar array components at a location, specifying panel model, number of panels, and telemetry source. | Must |
| CFG-04 | As a Tenant Admin, I want to add, edit, and remove generator components at a location, specifying generator model, fuel type, output type, and telemetry source. | Must |
| CFG-05 | As a Tenant Admin, I want to add, edit, and remove energy storage components at a location, specifying battery model, units deployed, voltage type, total storage, sustained power, and telemetry source. | Must |
| CFG-06 | As a Tenant Admin, I want to add, edit, and remove power conditioning (inverter) components at a location, specifying the component model and telemetry source. | Must |
| CFG-07 | As a Tenant Admin, I want to add, edit, and remove load components at a location, specifying power type, rated power, and telemetry source. | Must |
| CFG-08 | As a Tenant Admin, I want to add, edit, and remove sensor components at a location, specifying sensor type and equipment model. | Must |
| CFG-09 | As a Tenant Admin, I want to define power connections between components through power conditioning connection ports, specifying power flow direction, power type, and bidirectionality. | Must |
| CFG-10 | As a Tenant Admin, I want to assign SolarGrid monitors to components and configure their network/device relationships. | Must |
| CFG-11 | As a Tenant Admin, I want to see a visual connection diagram that updates in real-time as I add, modify, or remove connections. | Must |
| CFG-12 | As a Tenant Admin, I want location validation status to indicate whether the configuration is complete and valid for data processing. | Must |
| CFG-13 | As a Tenant Admin, I want power connection setup to enforce electrical compatibility (power types, connection port constraints, maximum power calculations). | Must |

#### Component Setup (SolarGrid-Managed)

| ID | Story | Priority |
|----|-------|----------|
| CMP-01 | As an SolarGrid Admin, I want to define generation equipment specifications (model, rated capacity, supported fuel types, output types). | Must |
| CMP-02 | As an SolarGrid Admin, I want to define power conditioning specifications (model, power connections with ports and power types). | Must |
| CMP-03 | As an SolarGrid Admin, I want to define solar panel specifications (model, rated power, electrical characteristics). | Must |
| CMP-04 | As an SolarGrid Admin, I want to define energy storage specifications (model, voltage, stored energy, charge/discharge characteristics). | Must |
| CMP-05 | As an SolarGrid Admin, I want to define SolarGrid monitor configurations (general setup, modbus networks, devices, telemetry processes). | Must |
| CMP-06 | As an SolarGrid Admin, I want to define sensor specifications (type, operational parameters). | Must |
| CMP-07 | As an SolarGrid Admin, I want to see which locations each equipment model is deployed at. | Should |
| CMP-08 | As an SolarGrid Admin, I want to upload and manage documentation for each equipment type. | Should |

### 2.6 External Data Source Management

| ID | Story | Priority |
|----|-------|----------|
| EXT-01 | As a Tenant Admin, I want to see the health status of each external data source link (green/orange/red based on error recency and severity). | Must |
| EXT-02 | As a Tenant Admin, I want to configure and validate authentication credentials for external data sources (e.g., Sol-Ark username/password). | Must |
| EXT-03 | As a Tenant Admin, I want to view static data retrieved from external sources (locations, location details, inverters) organized by record type. | Must |
| EXT-04 | As a Tenant Admin, I want to view incoming staged data with date range filtering. | Should |
| EXT-05 | As a Tenant Admin, I want to support multiple API credentials per external data source to cover non-overlapping data sets for a single tenant. | Should |

### 2.7 ETL & Data Processing (Backend)

| ID | Story | Priority |
|----|-------|----------|
| ETL-01 | As the system, I must process staged Sol-Ark inverter telemetry into Component.Statistics by mapping telemetry fields to configured data series, applying conversion factors, and respecting the location's timezone. | Must |
| ETL-02 | As the system, I must raise a Component Data Updated Event after processing new/updated telemetry, including CompanyID, LocationID, CategoryIDs, and ComponentIDs in the payload. | Must |
| ETL-03 | As the system, I must aggregate component-level statistics to location-level statistics using standardized frequency interpolation (linear imputation) and configured aggregation types (Sum, Average, Min, Max, Latest). | Must |
| ETL-04 | As the system, I must aggregate location-level statistics to company-level statistics using the same interpolation approach. | Must |
| ETL-05 | As the system, I must update .Current data sources with the latest value for each data series, only replacing values with newer ReportDateTime. | Must |
| ETL-06 | As the system, I must incrementally update .Calcs (standard deviation, variance, average) for each data series without full recalculation. | Must |
| ETL-07 | As the system, I must process location events FIFO in a single-threaded manner per LocationID while allowing parallel processing across different locations. | Must |
| ETL-08 | As the system, I must support historical re-synchronization from staged data for all 3 statistics levels. | Must |
| ETL-09 | As the system, I must cache static lookups (inverter-to-component mappings, data series metadata) aggressively and define a cache invalidation strategy. | Must |
| ETL-10 | As the system, I must process SolarGrid IoT generator configuration and telemetry data into component statistics. | Must |
| ETL-11 | As the system, I must periodically download weather data and solar production forecasts for all active locations. | Must |
| ETL-12 | As the system, I must collect external data source statistics (last access, last error, active errors) for health monitoring. | Must |
| ETL-13 | As the system, I must calculate and update the forecasted next generation run for each location based on storage level/capacity and load. | Should |
| ETL-14 | As the system, I must remove orphaned metadata and statistics when components/locations are deleted. | Should |
| ETL-15 | As the system, I must validate external source credentials on demand and periodically. | Must |

### 2.8 User & Security Management

| ID | Story | Priority |
|----|-------|----------|
| SEC-01 | As the system, I must enforce tenant-level data isolation at every data access layer so that a user from Company A can never see, query, or access Company B's data. | Must |
| SEC-02 | As a Tenant Admin, I want to manage users within my tenant (invite, assign roles). | Must |
| SEC-03 | As an SolarGrid Support user, I need a mechanism to access any tenant's data for troubleshooting without being a member of that tenant. | Must |
| SEC-04 | As the system, I must implement user sign-up/invitation workflows for onboarding new tenant users. | Must |
| SEC-05 | As the system, I must securely store external data source authentication credentials. | Must |

### 2.9 Cross-Cutting / UX

| ID | Story | Priority |
|----|-------|----------|
| UX-01 | As any user, I want to show/hide and reorder cards on each screen so I can customize my view to what matters most. | Must |
| UX-02 | As any user, I want every field to have an information icon/tooltip explaining what the value represents. | Must |
| UX-03 | As any user, I want the application to render correctly on 1920x1080, 414x896, and 768x1024 in both portrait and landscape. | Must |
| UX-04 | As any user, I want all text in the application to use an internationalization (i18n) framework with no hardcoded strings. | Must |
| UX-05 | As any user, I want deep link URLs that allow me to navigate directly to any screen with specific parameters (e.g., a specific location, component, or date range). | Must |
| UX-06 | As any user, I want loading indicators on regions that are being refreshed so I know data is being fetched. | Must |
| UX-07 | As any user, I want standard browser navigation (forward/back) to work with correctly restored screen state. | Must |
| UX-08 | As any user, I want real-time updates to dashboard data via subscriptions so I see new telemetry without manual refresh. | Must |
| UX-09 | As any user, I want values displayed in my preferred unit of measure (energy rate, energy, temperature, volumetric) with proper unit conversion. | Should |
| UX-10 | As any user, I want the application to support Sol-Ark inverter and generator fault history tracking. | Should |

---

## 3. Success Criteria

### 3.1 Functional Criteria

| # | Criterion | Measurement |
|---|-----------|-------------|
| F-01 | All 20+ screens render correctly with live data from the 3-tier statistics hierarchy | Manual QA across all screens with production-representative data |
| F-02 | ETL pipeline processes Sol-Ark telemetry end-to-end (Staging → Component → Location → Company) within 60 seconds of data arrival | Automated timing tests with realistic telemetry volume |
| F-03 | Dashboard updates reflect new data within 5 seconds of event processing via real-time subscriptions | End-to-end latency measurement |
| F-04 | Multi-tenant isolation prevents cross-tenant data access at every API endpoint and database query | Automated security tests: attempt cross-tenant access with valid auth for different tenant |
| F-05 | Historical re-synchronization reprocesses staged data and produces identical statistics output | Automated regression test comparing fresh sync vs incremental |
| F-06 | Alert system correctly categorizes issues by category and severity, with alerts appearing on dashboards within seconds of detection | Automated alert trigger tests per category |
| F-07 | Configuration screens support full CRUD lifecycle for locations, all 6 component types, connections, and notification rules | End-to-end configuration workflow tests |
| F-08 | Equipment schematic renders accurate electrical topology matching configured connections and updates dynamically | Visual verification against known test configurations |
| F-09 | Time series interpolation produces correct standardized-frequency data for all 5 aggregation types (Sum, Average, Min, Max, Latest) | Unit tests with known input/output data sets from client's sample data |
| F-10 | Sol-Ark field mapping handles all inverter variants (12k, 15k, 30k, 60k) with correct field extraction and conversion | Integration tests with sample telemetry from each inverter model |

### 3.2 Non-Functional Criteria

| # | Criterion | Measurement |
|---|-----------|-------------|
| NF-01 | All API queries complete within 10 seconds (design target: < 2 seconds for common queries) | Performance profiling under simulated load |
| NF-02 | Application renders correctly at 1920x1080, 414x896, 768x1024 in portrait and landscape | Cross-device testing (desktop, tablet, mobile) |
| NF-03 | Full i18n implementation: zero hardcoded text in application code | Code review and grep verification |
| NF-04 | Deep link navigation works for all screens with parameterized URLs | Automated URL navigation tests |
| NF-05 | All new functionality has automated tests (unit, integration, and/or E2E) | Test coverage reporting |
| NF-06 | Static data caching with TTL logic reduces redundant API calls by > 90% | Cache hit rate monitoring |
| NF-07 | Version-based concurrency control prevents lost updates on concurrent writes | Concurrency conflict simulation tests |
| NF-08 | FIFO event processing per location with parallel processing across locations | Ordered delivery verification under concurrent component updates |

### 3.3 Phase 1 (Discovery) Specific Criteria — Option 4

| # | Criterion | Deliverable | Owner |
|---|-----------|-------------|-------|
| P1-01 | Codebase audit with keep/modify/replace recommendation per component (Rails API, NextJS frontend, MySQL, AWS infra). Must validate Martin's 10 failure points (epoch millis, aggregation methods, API-to-metric mapping, Better Auth, etc.) | Codebase & Architecture Audit Report | Lead Engineer |
| P1-02 | Heuristic evaluation of all 20+ Figma screens. Usability, visual consistency, accessibility, responsive gap analysis (3 breakpoints). Prioritized recommendations. | UI/UX Assessment & Recommendations | UI/UX Designer |
| P1-03 | 6 Architecture Decision Records: Frontend framework, API framework, Database, Infrastructure, Authentication, Caching strategy. Each with options considered, decision, rationale, trade-offs. | ADRs | Lead Engineer (Roberto sign-off) |
| P1-04 | TRD Platform sections: frontend architecture, API design, auth & security, infrastructure & CI/CD, caching strategy, build sequencing | TRD — Platform | Lead Engineer |
| P1-05 | TRD Data sections: data model (full ERD), ETL pipeline architecture (3-level cascade), integration specs (all 5 APIs with model-specific field mapping), time series processing, notification system | TRD — Data | Engineer 2 |
| P1-06 | Merged, coherent TRD with no contradictions between platform and data sections. All ADR decisions reflected. | TRD — Final Assembly | Lead Engineer |
| P1-07 | Redesigned Hi-Fi prototype: design system, 6–8 key screens redesigned, configuration screen patterns, responsive adaptation (3 breakpoints), interactive navigation | Hi-Fi Prototype | UI/UX Designer |
| P1-08 | Phase 2 scope, timeline, team composition, and cost estimate derived from TRD findings | Phase 2 Proposal | Gabi + Roberto |

---

## 4. Data Architecture Summary

### 4.1 Data Hierarchy

```
Company (Tenant)
 Company.Statistics            ← Aggregated time series across all locations
 Company.Statistics.Current    ← Latest values per company
 Company.Statistics.Calcs      ← Statistical calculations (avg, variance, std dev)
 Company.Statistics.MetaData   ← Company-level data series definitions
 Company.Alerts                ← Company-level alerts

 Location 1
    Location.Statistics           ← Aggregated time series for location
    Location.Statistics.Current   ← Latest values per location
    Location.Statistics.Calcs     ← Location-level statistics
    Location.Statistics.MetaData  ← Location-level data series definitions
    Location.Alerts               ← Location-level alerts
   
    Component: Solar Array (pv1)
       Component.Statistics          ← Raw telemetry time series
       Component.Statistics.Current  ← Latest known values
       Component.Statistics.MetaData ← Series definitions + field mapping
   
    Component: Generator (gen1)
    Component: Storage/Battery (bank1)
    Component: Power Conditioning/Inverter (solark1)
    Component: Load (AC1)
    Component: Sensor (temp1)

 Location 2 ...
 Location N ...

External & Configuration Data Stores
 External.Source                ← External data source definitions per tenant
 External.Source.MetaData       ← External source metadata
 External.Source.SolarkStatic   ← Staged static data (locations, inverters) from Sol-Ark
 External.Source.Staging        ← Incoming raw telemetry staging area
 External.Source.Statistics     ← Health/connectivity metrics per external source

 Configuration.Location.*       ← Location general config, component assignments
    Configuration.Location.Component.{Solar,Generation,Storage,Conditioning,Load,Sensor}
    Configuration.Location.Component.Mapping  ← External source → component mapping
    Configuration.Location.Connection          ← Electrical connections between components

 Configuration.{Solar,Generation,Storage,Conditioning,Sensor}.Spec ← Equipment specifications
 Configuration.Monitor.*        ← SolarGrid monitor, network, device configs
 Documentation                  ← File references per equipment type
 Static.*                       ← Reference data (Measurement, Unit)
```

### 4.2 Event-Driven Processing Flow

```
Sol-Ark API / SolarGrid IoT
        
        
  External.Source.Staging (raw telemetry)
        
        
  ETL: Field Mapping + Conversion (via Component.Statistics.MetaData)
        
        
  Component.Statistics → Component Data Updated Event
                                    
                         
                                             
              Component       Location.Statistics
            .Statistics     (interpolation + aggregation
              .Current        via .MetaData definitions)
            .Calcs updated         
                                   
                            Location Data Updated Event
                                   
                         
                                            
                  Location      Company.Statistics
                .Statistics     (aggregation via
                  .Current       .MetaData definitions)
                .Calcs updated        
                                      
                               Company Data Updated Event
                                      
                            
                                               
                     Company      Dashboard
                   .Statistics   Subscriptions
                     .Current   (real-time UI)
                   .Calcs updated

Processing rules:
- Events per LocationID processed FIFO, single-threaded
- Different LocationIDs processed in parallel
- Interpolation uses linear imputation at standardized frequency (typically 300s)
- Aggregation types per series: Sum, Average, Min, Max, Latest
```

### 4.3 Alert Categories

| CategoryID | Category | Components |
|------------|----------|------------|
| 0 | Generation | Generators (fuel-based power sources) |
| 1 | Solar | Solar arrays / PV strings |
| 2 | Load | Electrical loads / consumers |
| 3 | Storage | Battery banks / energy storage |
| 4 | Fuel | Fuel supply and flow |
| 5 | External Sources | Data feed connectivity |

---

## 5. Integrations

| # | Integration | Purpose | Documentation Status | Risk |
|---|-------------|---------|---------------------|------|
| 1 | **Sol-Ark API** | Inverter telemetry (5-min intervals), static data (locations, inverters) | Proprietary, limited public docs; inconsistent fields across models (12k/15k/30k/60k) | **High** — model-specific field mapping required |
| 2 | **SolarGrid IoT** | Generator configuration + telemetry (power output, fuel, coolant, runtime) | Custom API; sample data provided | Medium |
| 3 | **Weather API** | Current conditions + forecast per location | To be selected during discovery | Low |
| 4 | **Solar Forecast API** | Solar production predictions per location | To be selected during discovery | Low |
| 5 | **Google Maps API** | Geographic map with location pins | Well-documented | Low |

---

## 6. Open Questions Requiring Resolution

These questions (identified in the client's own documentation) must be resolved during Discovery:

| # | Question | Impact Area |
|---|----------|-------------|
| 1 | For data points outside standard deviation, include in running statistics? | Statistics calculations |
| 2 | What conditions determine green/orange/red location status? | Dashboard + map display logic |
| 3 | Do components need planned outage/maintenance windows? | Configuration + alerting |
| 4 | Maximum age of data before excluding from instantaneous summaries (e.g., lost contact with running generator)? | Data freshness rules |
| 5 | Maximum granularity available from solar production forecast APIs? | Forecast integration |
| 6 | Will the network diagram library support custom icons per component type? | Equipment schematic rendering |
| 7 | How to securely store external link authentication credentials? | Security architecture |
| 8 | How to combine liquid and gas fuel flow rates? Report in energy flow rate? | Fuel metrics normalization |
| 9 | How to handle missing data/gaps in time series charts? (Linear interpolation vs visual discontinuity) | Charting behavior |
| 10 | Multi-language support for alert descriptions and measurement labels? | i18n scope |
| 11 | Auto-expiration for alerts? | Alert lifecycle |
| 12 | Standard deviation at component, location, AND company levels — all necessary? | Processing load |
| 13 | Company.Statistics concurrency: will multi-source updates create IO bottleneck? | Architecture design |
| 14 | Need for configurable synthetic statistics at Location/Company level? | Feature scope |
| 15 | Partitioning strategy for .Current data sources? | Database design |
| 16 | Need for separate History tables for statistics? | Data retention strategy |
| 17 | Strategy for static data sorting/filtering without denormalization? | Query performance |

---

## 7. Key Assumptions

1. **Sol-Ark is the only external data source for initial release.** Other sources will be added iteratively.
2. **Phase 1 (Discovery) must complete before committing to Phase 2 scope.** The codebase audit findings may significantly alter the build approach and estimate.
3. **Multi-tenant architecture is foundational** — it is not an afterthought to be added post-launch.
4. **English is the primary language** with i18n framework in place for future localization.
5. **"Day" boundaries are defined per location timezone** — all daily aggregations respect the location's IANA timezone.
6. **All dates/times stored as epoch milliseconds** except staged data from external sources.
7. **ComponentID is unique within a location** but not necessarily globally unique.
8. **Data series ID is globally unique across all tenants.**
9. **Configuration screens for component setup are SolarGrid-managed** — tenant users have read-only access at most.
10. **Client's detailed specs (~4,300+ lines across 3 documents) serve as the primary requirements source.** The Blueprint does not replace them but provides the structured overlay for project execution.

---

## 8. Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation | Status |
|------|----------|------------|------------|--------|
| Previous team failure may indicate hidden scope/complexity issues | High | Medium | Root cause identified: technical competence and requirements adherence (not scope). Audit validates specific failure points. | **Mitigated** — root causes understood |
| Sol-Ark API inconsistency across inverter models | High | Confirmed | Model-specific field mapping with automated tests per variant; sample data for all models; E2 researching in W1 | Active |
| ~20 open design questions (from client's requirements doc) could expand scope | Medium | High | Cap at 2h per client sync. Unresolved by W2 Fri are flagged as open items for Phase 2, not solved in Phase 1. 17 actionable questions tracked in Section 6 (3 already answered in client docs). | Active |
| Competitive bids may create pricing pressure | Medium | Confirmed | Martin confirmed Option 4 (Feb 27). Demonstrate quality in Phase 1 deliverables. | **Mitigated** — engagement secured |
| Event-driven pipeline concurrency issues | Medium | Medium | FIFO per location, parallel across locations; design with idempotency in TRD-Data | Active |
| Existing codebase may be unsalvageable (requiring full rewrite) | Medium | Medium | Codebase audit (W1) provides data for keep/rebuild ADR decisions (W2) | Active |
| Time series interpolation edge cases (gaps, timezone boundaries, DST) | Medium | Medium | Comprehensive unit tests with edge case scenarios from client's sample data | Active |
| E2 requires hand-holding from LE (breaks parallelism) | Medium | Low-Medium | E2 JD requires self-sufficiency. Early warning: >2 questions/day to LE by W1 Wed | Active |
| TRD merge reveals conflicts between LE and E2 sections | Medium | Medium | W2 Fri cross-review catches conflicts early. Daily LE+E2 async check-ins | Active |
| Compressed 3-week timeline leaves no buffer for rework | Medium | Medium | Quality built in through 4 review gates (G1–G4). Issues at G1/G2 have recovery time. | Active |
| ~~Repo/Figma/Confluence access pending~~ | ~~Low~~ | ~~Confirmed~~ | ~~All access obtained~~ | **Resolved** |

---

## 9. Engagement Summary

| Attribute | Value |
|-----------|-------|
| **Engagement Model** | Project-Based (Discovery SOW + Implementation SOW) |
| **Build Type** | Production-Ready |
| **Client Readiness** | Level 2 (Requirements Ready) |
| **Risk Score** | 17/32 (Medium) |
| **Phase 1 (Discovery)** | Option 4: 3 weeks (Mar 9–27, 2026), ~225 deliverable hours, $12,000 |
| **Phase 1 Team** | Lead Engineer (100%), Engineer 2 (75%), UI/UX Designer (35%), TPM Gabi (20%), Director Roberto (10%) |
| **Phase 1 Deliverables** | Codebase Audit, UI/UX Assessment, ADRs (6), TRD (Platform + Data), Hi-Fi Prototype, Phase 2 Proposal |
| **Phase 2 (Build) Est.** | 640–800 hours (~16–20 weeks) — to be refined by Phase 1 findings |
| **MSA + SOW** | Signed March 3, 2026 |

**Note:** No standalone Blueprint or PRD deliverables in Phase 1. Martin's documentation (2,800+ lines of screen specs, 1,500+ lines of ETL specs) already serves as the product requirements. The TRD references his docs directly and resolves outstanding design questions inline. This Blueprint is an internal reference document, not a client deliverable.

---

## 10. Next Steps

### Pre-Engagement (Completed)

- [x] MSA + SOW signed (March 3, 2026)
- [x] Editable Figma access obtained
- [x] Repo access and QA/demo environment credentials obtained
- [x] Root causes of previous team failure understood — primarily technical competence and requirements adherence (epoch millis not used, only SUM aggregation implemented, API-to-metric mapping broken, Better Auth confusion)
- [x] Confluence access obtained (LE reviews during codebase audit for delta analysis against Martin's requirements; not conducting a separate standalone review — Martin's documentation is the authoritative source)
- [x] Option 4 confirmed by Martin (Feb 27, 2026)

### Phase 1 Discovery — In Progress (Mar 9–27, 2026)

**Week 1 (Mar 9–13): Audit + Assessment + Research**
- [ ] Codebase & Architecture Audit — LE clones repo, audits Rails API, NextJS frontend, MySQL schema, AWS infra, validates Martin's 10 failure points
- [ ] UI/UX Assessment — Designer catalogs all 20+ Figma screens, heuristic evaluation, responsive gap analysis
- [ ] E2 deep-reads all client documentation (4,300+ lines), researches Sol-Ark API and all integrations
- [ ] G1 Review Gate: Audit report reviewed by Roberto (Fri Mar 13)

**Week 2 (Mar 16–20): ADRs + TRD Writing + Prototype Start**
- [ ] 6 ADRs written and signed off (G2 gate: Wed Mar 18)
- [ ] TRD-Platform sections started (LE)
- [ ] TRD-Data sections started: data model ERD, ETL pipeline architecture (E2)
- [ ] Hi-Fi prototype started: design system + key screen redesigns (UI/UX)
- [ ] Client design review session (Thu Mar 19)
- [ ] LE + E2 first cross-review of TRD drafts (Fri Mar 20)

**Week 3 (Mar 23–27): TRD Completion + Merge + Assembly + Phase 2**
- [ ] TRD-Platform and TRD-Data sections completed
- [ ] TRD merged, coherence reviewed (G3 gate: Wed Mar 25)
- [ ] Hi-Fi prototype completed with interactive navigation
- [ ] Phase 2 Proposal drafted
- [ ] G4 Final sign-off: all deliverables (Thu Mar 26)
- [ ] Deliverables packaged for client delivery (Fri Mar 27)

---

_Internal documentation — The Contractor Team_
_Source documents: Dashboard Requirements.docx, Dashboard Deliverables.docx, Requirements - ETL.docx, Data Definition.xlsx, sample data files, and project evaluation_
