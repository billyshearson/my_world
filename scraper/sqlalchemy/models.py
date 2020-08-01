from .settings import Base, engine
from sqlalchemy import Column, DateTime, Float, Integer, create_engine, desc


from .base import session_scope
import contextlib

import logging

logger = logging.getLogger(__name__)


class Article(Base):
    __tablename__ = 'scraper_article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(50))
    src = Column('src', String(200))
    content = Column('content', Text())
    updated_at = Column('updated_at', DateTime())

    @classmethod
    def create(cls, title, src, content, updated_at):
        article = cls(
            title=title,
            src=src,
            content=content,
            updated_at=updated_at
        )

        try:
            with session_scope() as session:
                session.add(article)
            return article
        except Exception as e:
            return False

    def save(self):
        with session_scope() as session:
            session.add(article)
