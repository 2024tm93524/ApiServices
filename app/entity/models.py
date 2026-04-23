from sqlalchemy import Column, Integer, String
from app.db.database import Base

class ArtistEntity(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    genre = Column(String)
    albums_published = Column(Integer)

class BookEntity(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)