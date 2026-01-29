import pandas as pd
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
})

print(df.groupby("Department")["Salary"].agg(["min", "max", "mean"]))
