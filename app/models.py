from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from contextlib import contextmanager
import threading
import logging

logger = logging.getLogger(__name__)
db_name = 'db.sqlite3'
Base = declarative_base()
engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
Session = scoped_session(sessionmaker(bind=engine))
lock = threading.Lock()


@contextmanager
def session_scope():
    session = Session()
    session.expire_on_commit = False
    try:
        lock.acquire()
        yield session
        session.commit()
    except Exception as e:
        logger.error(f'action=session_scope error={e}')
        session.rollback()
        raise
    finally:
        session.expire_on_commit = True
        lock.release()


class ArticleInfo(Base):
    __tablename__ = 'scraper_article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    src = Column(String(200), nullable=False)
    content = Column(Text)
    updated_at = Column(DateTime(timezone='Asia/Tokyo'), nullable=False)

    @classmethod
    def create(cls, title, src, content, updated_at):
        article = ArticleInfo(
            title=title,
            src=src,
            content=content,
            updated_at=updated_at,
        )
        with session_scope() as session:
            session.add(article)


def init_db():
    Base.metadata.create_all(bind=engine)


init_db()
