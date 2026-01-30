import pandas as pd
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ajit", "Rahul", "Neha"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "marks": [85, 90, 88]
})
df3 = pd.DataFrame({
    "id": [4],
    "name": ["Amit"],
    "marks": [92]
})

pd.merge(df1, df2, on="id")

print(pd.concat([df1.reset_index(), df3], ignore_index=True))


