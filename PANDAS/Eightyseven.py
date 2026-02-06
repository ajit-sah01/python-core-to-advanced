import pandas as pd

dates = pd.date_range("2024-01-01", periods=10, freq="D")
data = pd.Series(range(10), index=dates)

weekly = data.resample("W").sum()
print(weekly)
