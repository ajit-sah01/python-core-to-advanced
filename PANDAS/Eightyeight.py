import pandas as pd

dates = pd.date_range("2024-01-01", periods=3, freq="D")
ts = pd.Series([10, 20, 30], index=dates)

ts_utc = ts.tz_localize("UTC")
ts_india = ts_utc.tz_convert("Asia/Kolkata")

print(ts_india)
