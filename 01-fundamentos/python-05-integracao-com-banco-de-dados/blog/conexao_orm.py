from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# postgresql://usuario:senha@host/database
DATABASE_URI = "postgresql://postgres:1q2w3e4r@localhost/blog"