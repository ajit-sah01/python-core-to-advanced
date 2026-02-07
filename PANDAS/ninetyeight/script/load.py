import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Data loaded successfully")
    return df
