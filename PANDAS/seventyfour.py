import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://user:password@localhost/database"
)

df = pd.read_sql("SELECT * FROM employees", engine)
print(df)
