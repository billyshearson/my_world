from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

db_name = 'db.sqlite3'
Base = declarative_base()
engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
Session = scoped_session(sessionmaker(bind=engine))
print(engine)


class ArticleInfo(Base):
    __tablename__ = 'scraper_article'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    src = Column(String(200))
    content = Column(Text)
    updated_at = Column(DateTime(timezone='Asia/Tokyo'))


def init_db():
    Base.metadata.create_all(bind=engine)


init_db()
