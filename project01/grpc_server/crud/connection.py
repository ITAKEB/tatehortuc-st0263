from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:secret@localhost/momdb')

Base = declarative_base()

Session = sessionmaker(engine)
