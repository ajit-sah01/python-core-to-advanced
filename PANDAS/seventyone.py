import pandas as pd

for chunk in pd.read_csv("large_file.csv", chunksize=5000):
    print(chunk.head())
