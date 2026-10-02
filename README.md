# Bitfinex Data Pipeline

A small Python pipeline that pulls hourly OHLCV (open, high, low, close, volume) candle data for BTC/USD from the public Bitfinex API and saves it as raw JSON.

Built as a hands-on learning project toward a data engineering career.

## What it does

- Calls the Bitfinex v2 public candles endpoint (no API key required)
- Fetches the previous 24 complete hourly candles (UTC)
- Excludes the current, unfinished candle
- Saves the raw API response as JSON to `data/raw/`, named by symbol and date

## Tech

Python 3.12, `requests`, `pandas`, Git/GitHub

## Setup

powershell
git clone https://github.com/Ehbsee/bitfinex-data-pipeline.git
cd bitfinex-data-pipeline
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src\ingestion\fetch_candles.py


## Project structure


src/ingestion/fetch_candles.py   # fetches candles, writes raw JSON
data/raw/                        # output (git-ignored)


## Notes on the data

Bitfinex returns each candle as `[MTS, OPEN, CLOSE, HIGH, LOW, VOLUME]`. The order is Open, **Close**, High, Low, which differs from the usual OHLC convention. Timestamps are in milliseconds (UTC).

## Roadmap (not yet built)

- [ ] Upload raw JSON to an S3 landing zone
- [ ] Schedule daily runs (cron or AWS Lambda + EventBridge)
- [ ] Convert JSON to Parquet and query with Athena
- [ ] Load into PostgreSQL with upserts
- [ ] Aggregations (daily OHLC, moving averages, volatility)
- [ ] Dashboard (Streamlit)

## What I learned

- How the Bitfinex candles API works, including time windows and candle ordering
- Separating raw data (JSON) from processed data
- Virtual environments, `.gitignore`, and keeping data out of version control