import pandas as pd

df = pd.read_csv("data.csv")

df = df[df["Age"].between(0, 120)]

print(df)