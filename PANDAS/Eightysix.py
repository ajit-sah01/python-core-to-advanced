import pandas as pd

dates = pd.date_range("2024-01-01", periods=6, freq="D")
sales = pd.Series([100, 120, 140, 160, 180, 200], index=dates)

print(sales)
print(sales.rolling(3).mean())
