import pandas as pd

df = pd.read_csv("data.csv") 
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Salary"] >= Q1 - 1.5 * IQR) &
        (df["Salary"] <= Q3 + 1.5 * IQR)]

print(df)