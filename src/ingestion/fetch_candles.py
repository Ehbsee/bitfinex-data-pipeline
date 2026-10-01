import requests
import pandas as pd

url = "https://api-pub.bitfinex.com/v2/candles/trade:1h:tBTCUSD/hist"
r = requests.get(url, params={"limit": 24, "sort": 1}, timeout=30)
r.raise_for_status()

df = pd.DataFrame(r.json(), columns=["mts", "open", "close", "high", "low", "volume"])
df["time"] = pd.to_datetime(df["mts"], unit="ms", utc=True)
print(df)