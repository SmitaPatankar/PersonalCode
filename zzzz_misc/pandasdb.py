import pandas as pd
import sqlalchemy
import pymysql

engine = sqlalchemy.create_engine("mysql+pymysql://user:pwd@host:port/dbname")

df = pd.read_sql_table("customers", engine, columns=["mycol"])

df = pd.read_sql_query("", engine, chunksize=5)

df.to_sql("customers", engine, index=False, if_exists="append")  # replace  # fail

pd.read_sql(query, engine)  # wrapper of 2
