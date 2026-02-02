import pandas as pd
import sqlite3

conn = sqlite3.connect("app.db")
df = pd.read_sql("SELECT * FROM users", conn)
conn.close()
