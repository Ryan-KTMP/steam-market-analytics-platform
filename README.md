# Steam Market Analytics Platform

A Data Warehouse and Business Intelligence platform for analyzing the Steam game market using data collected from SteamSpy.

---

## Project Overview

The project aims to build an end-to-end analytics platform that collects, stores, processes, and visualizes Steam market data.

The system automatically retrieves game information from the SteamSpy API, loads it into a PostgreSQL Data Warehouse, and provides analytical dashboards through Power BI.

Current coverage:

- ~28,000 Steam games
- Daily automated data collection
- Historical snapshot tracking
- Business Intelligence dashboards

---

## Business Objectives

This platform helps answer questions such as:

- Which games dominate the Steam market?
- Which games are gaining popularity?
- Which games are losing active players?
- How do review scores relate to player activity?
- Which games show high market potential?

---

## Technology Stack

### Data Collection

- Python
- SteamSpy API

### Data Storage

- PostgreSQL 16

### Orchestration

- Apache Airflow

### Infrastructure

- Docker
- Docker Compose

### Visualization

- Power BI Desktop

---

## System Architecture

SteamSpy API
↓
Extract Layer
↓
Raw Layer
(raw.raw_steamspy_games)
↓
Staging Layer
(staging.stg_steam_games)
↓
Data Warehouse
(dim_game)
(fact_game_snapshot)
↓
SQL Views
↓
Power BI Dashboard

---

## Data Warehouse Design

### Dimension Tables

#### dim_game

Stores game master information.

Attributes:

- game_key
- app_id
- game_name
- effective_date
- is_current

---

### Fact Tables

#### fact_game_snapshot

Stores daily game metrics.

Metrics:

- owners_min
- owners_max
- owners_estimated
- positive_reviews
- negative_reviews
- review_score
- ccu

---

## ETL Pipeline

The ETL process runs automatically using Apache Airflow.

Workflow:

1. Extract data from SteamSpy API
2. Load raw JSON data
3. Transform into staging tables
4. Update dimension tables
5. Create daily fact snapshots

Schedule:

- Daily at 01:00 AM

---

## Dashboard Features

### Executive Dashboard

- Total Games
- Total Owners
- Average Review Score
- Market Overview

### Top Games Dashboard

- Top Owners
- Top Concurrent Players
- Top Rated Games

### Review Analytics Dashboard

- Review Distribution
- Positive vs Negative Reviews

---

## Project Structure

```text
steam-market-analytics-platform
│
├── airflow/
├── dashboard/
├── data/
├── docs/
├── sql/
├── src/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Future Enhancements

Planned improvements:

- Market Potential Score
- Game Growth Analysis
- Trend Detection
- Discount Impact Analysis
- Machine Learning Forecasting
- Recommendation Engine

---

## Author

Khuat Thai Minh Phuc

Data Warehouse & Business Intelligence Project