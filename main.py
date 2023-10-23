import json
import os
import random
from typing import List
from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.middleware import Middleware
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute"])

app = FastAPI(middleware=[Middleware(SlowAPIMiddleware, limiter=limiter)])


class AsmaulData(BaseModel):
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


# Initializing data
with open('data/asmaul-husna.json') as f:
    asmaul_husna_data = json.load(f)

with open('data/quran.json') as f:
    quran_data = json.load(f)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return PlainTextResponse(str(exc), status_code=429)


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
    return asmaul_husna_data


@app.get("/api/asmaul-husna/random", response_model=AsmaulData)
async def read_random_asmaul_husna():
    random_id = random.choice(list(asmaul_husna_data.keys()))
    return {"arabic": asmaul_husna_data[random_id]['arab'], "latin": asmaul_husna_data[random_id]['latin'],
            "arti": asmaul_husna_data[random_id]['artinya']}


@app.get("/api/asmaul-husna/{id}", response_model=AsmaulData)
async def read_asmaul_husna(id: str):
    if id in asmaul_husna_data:
        return {"arabic": asmaul_husna_data[id]['arab'], "latin": asmaul_husna_data[id]['latin'],
                "arti": asmaul_husna_data[id]['artinya']}
    else:
        raise HTTPException(status_code=404, detail=f"Asmaul husna with id {id} is not found")


@app.get("/api/quran", response_model=List[QuranData])
def get_quran():
    return quran_data


@app.get("/api/quran/{nomor}")
def get_quran_nor(nomor: str):
    for item in quran_data:
        if item['nomor'] == nomor:
            return item

    raise HTTPException(status_code=404, detail=f"Quran with nomor {nomor} is not found")


@app.get("/api/quran/{nomor}/detail", response_model=List[Ayat])
def read_quran_detail(nomor: str):
    file_path = f"data/surah/{nomor}.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        raise HTTPException(status_code=404, detail=f"Surah with nomor {nomor} is not found")
