import pandas as pd

def clean_data(file):
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    df["salary"] = df["salary"].astype(float)
    return df

data = clean_data("data.csv")
print(data.head())
