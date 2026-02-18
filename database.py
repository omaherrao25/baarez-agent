from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./memory.db" # pointing to local SQLite file

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # allow multiple threads to access SQLite DB to handle multiple requests

SessionLocal = sessionmaker(bind=engine) # create db session factory

Base = declarative_base() # base class for models, all ORM models inherit from this