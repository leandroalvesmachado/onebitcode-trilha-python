"""Conexão ao banco de dados."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
password = '1q2w3e4r'
host = 'localhost'
database = 'blog'

# postgresql://usuario:senha@host/database
DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
