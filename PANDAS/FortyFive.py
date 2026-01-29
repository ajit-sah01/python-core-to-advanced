import pandas as pd
df = pd.DataFrame({
    "Sales": [1200, 1500, 1800]
}, index=pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-03"]))

print(df.loc["2026-01-02"])
