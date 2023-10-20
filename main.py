import json
import os
import random
from typing import List

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    arabic: str
    latin: str
    arti: str


class QuranData(BaseModel):
    arti: str
    asma: str
    audio: str
    ayat: int
    keterangan: str
    nama: str
    nomor: str
    rukuk: str
    type: str
    urut: str


class Ayat(BaseModel):
    ar: str
    id: str
    nomor: str
    tr: str


@app.get("/")
def read_root():
    return {"Title : Muslim API"}


@app.get("/asmaul-husna")
async def root():
    with open('data/asmaul-husna.json') as f:
        data = json.load(f)
    return data


@app.get("/asmaul-husna/random", response_model=Data)
async def read_random_asmaul_husna():
    with open('data/asmaul-husna.json') as f:
        data = json.load(f)

    random_id = random.choice(list(data.keys()))
    return {"arabic": data[random_id]['arab'], "latin": data[random_id]['latin'], "arti": data[random_id]['artinya']}


@app.get("/asmaul-husna/{id}", response_model=Data)
async def read_asmaul_husna(id: str):
    with open('data/asmaul-husna.json') as f:
        data = json.load(f)

    if id in data:
        return {"arabic": data[id]['arab'], "latin": data[id]['latin'], "arti": data[id]['artinya']}
    else:
        raise HTTPException(status_code=404, detail="Not found")


@app.get("/quran", response_model=List[QuranData])
def get_quran():
    with open('data/quran.json') as file:
        data = json.load(file)

        return data


@app.get("/quran/{nomor}")
def get_quran_nor(nomor: str):
    with open('data/quran.json') as file:
        data = json.load(file)

    for item in data:
        if item['nomor'] == nomor:
            return item

    return {"message": "Not found"}


@app.get("/quran/{nomor}/detail", response_model=List[Ayat])
def read_quran_detail(nomor: str):
    file_path = f"data/surah/{nomor}.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        raise HTTPException(status_code=404, detail="Surah not found")
