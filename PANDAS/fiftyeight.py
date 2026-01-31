import pandas as pd
df = pd.DataFrame({"Grade": ["A", "B", "A", "C"]})

result = df["Grade"] = pd.Categorical(
    df["Grade"],
    categories=["A", "B", "C"],
    ordered=True
   )
print(result)
