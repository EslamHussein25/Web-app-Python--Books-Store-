from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from appdata import *

DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@localhost:{port}/{Database_Name}"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Books(Base):
   __tablename__ = 'books'
   id = Column(Integer, primary_key=True, nullable=False , unique=True)
   title = Column(String(50))
   author = Column(String(50))
   published_year = Column(String(50))

#create all tables in database if not found 
Base.metadata.create_all(bind=engine)

#create session object to connect with database every time 
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

