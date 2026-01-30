import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ajit", "rajput", "Nilam"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "marks": [85, 90, 88]
})

print(pd.merge(df1, df2, on="id"))
