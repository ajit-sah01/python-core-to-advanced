import pandas as pd
import numpy as np

df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=10),
    "sales": [10, 12, 15, 14, 18, 20, 22, 21, 25, 30],
    "profit": [2, 3, 4, 3, 5, 6, 7, 6, 8, 10]
})

cat = df["category"] = ["A", "A", "A", "B", "B", "B", "A", "A", "B", "B"]

gruop = df["group_roll_mean"] = (
    df.groupby("category")["sales"]
      .rolling(2)
      .mean()
      .reset_index(level=0, drop=True)
)

print(cat)
print(gruop)