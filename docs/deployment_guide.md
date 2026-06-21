# Deployment Guide

## Clone repository

git clone <repository>

## Create virtual environment

py -3.12 -m venv .venv

## Activate

.\.venv\Scripts\Activate.ps1

## Install dependencies

pip install -r requirements.txt

## Start Docker

docker compose up -d

## Run ETL

python -m src.extract.steamspy_extractor

python -m src.extract.load_raw_steamspy

python -m src.staging.staging_loader

python -m src.warehouse.load_dim_date

python -m src.warehouse.load_dim_game

python -m src.warehouse.load_fact_game_snapshot