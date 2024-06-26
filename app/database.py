
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)