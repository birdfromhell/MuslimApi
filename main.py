import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    arabic: str
    latin: str
    arti: str


@app.get("/")
async def root():
    with open('asmaul-husna.json') as f:
        data = json.load(f)
    return data
