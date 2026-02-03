import pandas as pd
df = pd.read_csv("data.csv")
df["total_amount"] = df["price"] * df["quantity"]
result =  df["is_premium"] = df["total_amount"] > 10000
print(result)
