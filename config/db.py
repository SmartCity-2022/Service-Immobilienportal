from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
url = os.getenv('DB_URL')

SQLALCHEMY_DATABASE_URL = url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()