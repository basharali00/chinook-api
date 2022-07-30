from db import statments
from db.session import con
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

app = FastAPI()

class Album(BaseModel):
    albumID: int
    title: str
    artistID: int

    # class Config:
    #     orm_mode = True

class AlbumResponse(BaseModel):
    message: str
    data: List[Album]


@app.get("/", response_model=AlbumResponse)
def read_root():
    cursor = con.execute(statments.SELECT_ALBUMS)
    temp_results = cursor.fetchall()
    results = []
    result = {}
    for temp_result in temp_results:
        result["albumID"] = temp_result[0]
        result["title"] = temp_result[1]
        result["artistID"] = temp_result[2]
        results.append(result)
    return {"message": "success", "data": results} 