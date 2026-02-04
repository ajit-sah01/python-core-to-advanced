import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "age": [20, 25, 30, 35],
    "income": [20000, 30000, 50000, 70000]
})

standard = StandardScaler()
minmax = MinMaxScaler()

print(standard.fit_transform(df))
print(minmax.fit_transform(df))
