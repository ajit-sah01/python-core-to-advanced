import pandas as pd

df = pd.DataFrame({
    "name": ["ajit", "Nilam", None],
    "age": [20, 16, 19]
})

# Debugging checks
print(df.info())
print(df.isnull().sum())

# Testing condition
assert df["age"].dtype == "int64", "Age column type mismatch"
