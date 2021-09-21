from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

engine = create_engine("sqlite:///abc.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    password = Column(String)
    def __init__(self, username, password):
        self.username = username
        self.password = password
user = User("smita", "patankar")
session.add(user)
session.commit()

s = session.query(User).all()
for r in s:
    print(r.username)
