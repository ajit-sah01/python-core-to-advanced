import pandas as pd

index = pd.MultiIndex.from_tuples([
    ("A", 1),
    ("A", 2),
    ("B", 1)
])

df = pd.DataFrame({"score": [90, 85, 88]}, index=index)

print(df)