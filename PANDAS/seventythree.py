import pandas as pd
import sqlite3

conn = sqlite3.connect("students.db")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)
conn.close()
