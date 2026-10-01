import json
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

SYMBOL = "tBTCUSD"

def fetch_last_24h(symbol=SYMBOL):
    now = datetime.now(timezone.utc)
    end_dt = now.replace(minute=0, second=0, microsecond=0)  # start of current hour
    start_dt = end_dt - timedelta(hours=24)

    params = {
        "start": int(start_dt.timestamp() * 1000),
        "end": int(end_dt.timestamp() * 1000) - 1,  # exclude unfinished candle
        "limit": 24,
        "sort": 1,
    }
    url = f"https://api-pub.bitfinex.com/v2/candles/trade:1h:{symbol}/hist"
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json(), start_dt

if __name__ == "__main__":
    data, start_dt = fetch_last_24h()
    print(f"Fetched {len(data)} candles")

    out_dir = Path("data/raw")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{SYMBOL}_1h_{start_dt:%Y-%m-%d}.json"
    out_file.write_text(json.dumps(data))
    print(f"Saved to {out_file}")