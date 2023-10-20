import json
import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    arabic: str
    latin: str
    arti: str


@app.get("/")
def read_root():
    return {"Title : Muslim API"}


@app.get("/asmaul-husna")
async def root():
    with open('asmaul-husna.json') as f:
        data = json.load(f)
    return data


@app.get("/asmaul-husna/random", response_model=Data)
async def read_random_asmaul_husna():
    with open('asmaul-husna.json') as f:
        data = json.load(f)

    random_id = random.choice(list(data.keys()))
    return {"arabic": data[random_id]['arab'], "latin": data[random_id]['latin'], "arti": data[random_id]['artinya']}


@app.get("/asmaul-husna/{id}", response_model=Data)
async def read_asmaul_husna(id: str):
    with open('asmaul-husna.json') as f:
        data = json.load(f)

    if id in data:
        return {"arabic": data[id]['arab'], "latin": data[id]['latin'], "arti": data[id]['artinya']}
    else:
        raise HTTPException(status_code=404, detail="Not found")
