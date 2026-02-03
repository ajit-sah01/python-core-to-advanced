import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data.csv") 

scaler = MinMaxScaler()
result = df[["Salary"]] = scaler.fit_transform(df[["Salary"]])
print(result)
