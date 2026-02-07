import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("product")["revenue"].sum()
print(result.sort_values(ascending=False))
