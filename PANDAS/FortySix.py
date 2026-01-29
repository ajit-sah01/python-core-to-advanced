import pandas as pd 
df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
})

grouped = df.groupby("Department")
print(grouped.mean())
