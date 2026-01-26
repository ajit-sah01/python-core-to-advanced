import pandas as pd

data = [
    ["Ajit", 19],
    ["nilam", 17],
    ["nilajit", 2]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)
