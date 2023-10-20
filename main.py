import json
import os
import random
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

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


@app.get("/", response_class=HTMLResponse)
def read_home():
    return """
    <html style="height: 100%;">
        <head>
            <title>Muslim API</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <style>
                .hero {
                    height: 100%;
                    background: #007BFF;
                    color: white;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-direction: column;
                    text-align: center;
                }
                .hero a {
                    color: black;
                    margin: 5px;
                }
                .btn-light {
                    color: #fff;
                }
            </style>
        </head>
        <body>
            <div class="hero">
                <h1>Welcome to Muslim API</h1>
                <p>A REST API that provides access to data related to Asmaul Husna and Quran.</p>
                <a href="/api/asmaul-husna" class="btn btn-light">Asmaul Husna</a>
                <a href="/api/quran" class="btn btn-light">Quran Surah</a>
                <a href="/docs" class="btn btn-light">Docs</a>
            </div>
        </body>
    </html>
    """

@app.get("/api/")
def read_root():
    return {"Title": "Muslim API"}


@app.get("/api/asmaul-husna")
async def root():
    with open('data/asmaul-husna.json') as f:
        data = json.load(f)
    return data


@app.get("/api/asmaul-husna/random", response_model=Data)
async def read_random_asmaul_husna():
    with open('data/asmaul-husna.json') as f:
        data = json.load(f)

    random_id = random.choice(list(data.keys()))
    return {"arabic": data[random_id]['arab'], "latin": data[random_id]['latin'], "arti": data[random_id]['artinya']}


@app.get("/api/asmaul-husna/{id}", response_model=Data)
async def read_asmaul_husna(id: str):
    with open('data/asmaul-husna.json') as f:
        data = json.load(f)

    if id in data:
        return {"arabic": data[id]['arab'], "latin": data[id]['latin'], "arti": data[id]['artinya']}
    else:
        raise HTTPException(status_code=404, detail="Not found")


@app.get("/api/quran", response_model=List[QuranData])
def get_quran():
    with open('data/quran.json') as file:
        data = json.load(file)

        return data


@app.get("/api/quran/{nomor}")
def get_quran_nor(nomor: str):
    with open('data/quran.json') as file:
        data = json.load(file)

    for item in data:
        if item['nomor'] == nomor:
            return item

    return {"message": "Not found"}


@app.get("/api/quran/{nomor}/detail", response_model=List[Ayat])
def read_quran_detail(nomor: str):
    file_path = f"data/surah/{nomor}.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        raise HTTPException(status_code=404, detail="Surah not found")
