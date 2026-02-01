import pandas as pd
import numpy as np

df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=10),
    "sales": [10, 12, 15, 14, 18, 20, 22, 21, 25, 30],
    "profit": [2, 3, 4, 3, 5, 6, 7, 6, 8, 10]
})

mean = df["roll_mean_3"] = df["sales"].rolling(window=3).mean()
print(mean)