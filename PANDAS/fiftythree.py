import pandas as pd
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ajit", "Rahul", "Neha"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "marks": [85, 90, 88]
})

pd.merge(df1, df2, on="id")


df1 = df1.set_index("id")
df2 = df2.set_index("id")

print(df1.join(df2))
