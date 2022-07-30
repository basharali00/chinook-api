from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Album(Base):
    __tablename__ = "album"

    albumID = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artistID = Column(Integer, ForeignKey("artist.artistID"))

    # not clear for me? what is back_populate 
    artists = relationship("Artist", back_populate="owner")


class Artist(Base):
    __tablename__ = "artist"

    artistID = Column(Integer, primary_key=True, index=True)
    name = Column(String)