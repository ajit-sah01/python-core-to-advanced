def analyze_data(df):

    # Example analysis
    summary = df.groupby("department")["salary"].mean()

    print("\nAverage salary by department:")
    print(summary)

    return summary
