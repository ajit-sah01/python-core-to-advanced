import pandas as pd

# Load
df = pd.read_csv("sales.csv")

# Clean
df.dropna(inplace=True)

# Feature Engineering
df["total"] = df["price"] * df["qty"]

# Analysis
summary = df.groupby("product")["total"].sum()

# Save
summary.to_csv("final_report.csv")
