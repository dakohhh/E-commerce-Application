import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)



def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()