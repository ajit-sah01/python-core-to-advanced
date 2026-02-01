import pandas as pd
import numpy as np

df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=10),
    "sales": [10, 12, 15, 14, 18, 20, 22, 21, 25, 30],
    "profit": [2, 3, 4, 3, 5, 6, 7, 6, 8, 10]
})

profit = df["rolling_corr"] = (
    df["sales"].rolling(3).corr(df["profit"])
)
print(profit)