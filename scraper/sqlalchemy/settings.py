from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///{db.name}', echo=True)
Base = declarative_base()

db_name = '/db.sqlite3'
