from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#uvicorn folder.main:appname --- if we use this syntax then . means the the folder outside folder sqlite:///./Products/products.db
#uvicorn main:appname --- if we use this syntax then . means the the current folder sqlite:///./products.db

SQLALCHEMY_DATABASE_URL = 'sqlite:///./Products/products.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()