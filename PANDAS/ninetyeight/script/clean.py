def clean_data(df):

    # remove missing values
    df = df.dropna()

    # example cleaning
    df["salary"] = df["salary"].astype(float)

    print("Data cleaned successfully")

    return df
