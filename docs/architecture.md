# Steam Market Analytics Platform Architecture

## Overview

This project collects Steam market data from SteamSpy API and transforms it into a structured analytics warehouse.

## Data Flow

SteamSpy API
    ↓
Raw Layer
    ↓
Staging Layer
    ↓
Warehouse Layer
    ↓
Analytics Layer
    ↓
Power BI Dashboard

## Schemas

### raw

Stores original API payloads.

### staging

Stores cleaned and standardized records.

### warehouse

Stores dimensional model and fact tables.

### audit

Stores ETL logs, data quality issues, and watermarks.

### analytics

Stores reporting views used by BI tools.