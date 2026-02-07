import pandas as pd

df = pd.read_csv("students.csv")

avg_marks = df.groupby("subject")["marks"].mean()

top_students = df.sort_values("marks", ascending=False).head(5)

print(avg_marks)
print(top_students)
