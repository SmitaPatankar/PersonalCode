# pip install pandas
# pip install sqlalchemy
# pip install pymysql

import pandas
import sqlalchemy
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/mydb')
df = pandas.read_sql("mytable", engine)
df = pandas.read_sql("mytable", engine, columns=['name', 'phone'])

query = "complicated query"
df = pandas.read_sql_query(query, engine)  # chunk_size

df = pandas.read_csv("mycsv.csv")
df.rename(columns={"name": "n", "surname": "s"}, inplace=True)
df.to_sql("mytable", engine, index=False, if_exists="append")  # fail, replace


##############################################################################

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "person"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)


engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

user = User()
user.id = 0
user.username = "smita"
session.add(user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.id)

session.close()
