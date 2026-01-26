import pandas as pd

data = [
    ["Ajit", 19],
    ["Rahul", 21],
    ["Neha", 20]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)


print(df.loc[0])

print(df.loc[1:2])

