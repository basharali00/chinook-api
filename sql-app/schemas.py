from typing import Union

from pydantic import BaseModel

class AlbumBase(BaseModel):
    albumID: int
    title = str
    artistID = int


class AlbumCreate(AlbumBase):
    pass


class ArtistBase(BaseModel):
    artistID: int
    name: str