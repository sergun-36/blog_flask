from settings import dev_db_settings as db_settings
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base

engine= create_engine(URL.create(**db_settings))
DeclarativeBase = declarative_base()
#print(URL.create(**db_settings))

class User(DeclarativeBase):
	__tablename__ = "users_sa"
	id = Column(Integer, primary_key = True)
	email = Column('email', String, unique=True)
	name = Column('name', String)
	password = Column('password', String)

	def __rep__(self):
		return "".format(self.name)

class Post(DeclarativeBase):
	__tablename__ = "posts_2"
	id = Column(Integer, primary_key = True)
	title = Column('title', String)
	text = Column('text', String)
	author = Column(Integer, ForeignKey("users_sa.id"))