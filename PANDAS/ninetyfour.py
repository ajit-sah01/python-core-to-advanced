import pandas as pd

# Extract
df = pd.read_csv("raw_data.csv")

# Transform
total =  df["total"] = df["price"] * df["qty"]

# Load
result = df.to_csv("processed_data.csv", index=False)

print(total)
print(result)
