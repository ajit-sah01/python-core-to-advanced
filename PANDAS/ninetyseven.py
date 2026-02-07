import pandas as pd

df = pd.DataFrame({"a":[1,2,3]})

# BAD
# for i in range(len(df)):
#     df.loc[i,"b"] = df.loc[i,"a"]*2

# GOOD
df["b"] = df["a"] * 2
