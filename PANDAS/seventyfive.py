import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:password@localhost/database"
)

df = pd.read_sql("SELECT * FROM orders", engine)
print(df)
