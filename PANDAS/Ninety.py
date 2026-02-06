import pandas as pd

df = pd.DataFrame({
    "department": ["IT", "IT", "HR", "HR"],
    "salary": [40000, 60000, 30000, 45000]
})

def salary_range(x):
    return x.max() - x.min()

result = df.groupby("department")["salary"].agg(
    total="sum",
    average="mean",
    range=salary_range
)

print(result)
