import pandas as pd

df = pd.read_csv("data.csv")


filtered_one = df[df["Age"] > 25]

filtered_two = df[
    (df["Age"] > 25) & (df["Salary"] > 30000)
]
