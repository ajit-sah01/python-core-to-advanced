import pandas as pd

df = pd.DataFrame({
    "marks": [60, 70, 80, 90, 100],
    "attendance": [65, 75, 85, 95, 100]
})

print(df.head())
print(df.describe())
print(df.corr())
