import pandas as pd
import numpy as np

arr = np.array([5, 10, 15, 20])
df = pd.DataFrame(arr, columns=["numbers"])

df["square"] = np.square(df["numbers"])
df["sqrt"] = np.sqrt(df["numbers"])

print(df)
