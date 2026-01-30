import pandas as pd

df = pd.DataFrame({
    "Gender": ["M", "F", "M", "F", "M"],
    "Result": ["Pass", "Fail", "Pass", "Pass", "Fail"]
})

print(pd.crosstab(df["Gender"], df["Result"]))
