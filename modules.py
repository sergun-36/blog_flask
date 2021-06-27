from settings import dev_db_settings as db_settings
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base

engine= create_engine(URL.create(**db_settings))
DeclarativeBase = declarative_base()
#print(URL.create(**db_settings))

class User(Base):
	__tablename__ = "users_2"
	id = Column(Integer, primary_key=True)
	email = Column(String)
	name = Column(String)
	password = Column(String)
