from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import requests

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/leaderboard/clips')
def leaderboard():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/leaderboard')
    return data.json()


@app.get('/leaderboard/votes')
def leaderboard():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/votes/leaderboard')
    return data.json()
