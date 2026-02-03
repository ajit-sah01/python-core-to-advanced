import pandas as pd

df = pd.read_csv("data.csv")

df.drop_duplicates(inplace=True)
result = df.fillna(method="ffill", inplace=True)

print(result)