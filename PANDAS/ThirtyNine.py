import pandas as pd

df = pd.read_csv("data.csv")


unique_values = df["Department"].unique()
unique_count = df["Department"].nunique()

print(unique_values)
print(unique_count)
