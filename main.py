
import time
from functools import lru_cache

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


# https://commonvoice.mozilla.org/api/v1/uz/clips/leaderboard?cursor=[6,26]

@app.get('/leaderboard/clips')
def leaderboard_clips():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/leaderboard?cursor=[0,3]')
    return data.json()


@app.get('/leaderboard/votes')
def leaderboard_votes():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/votes/leaderboard?cursor=[0,3]')
    return data.json()


@app.get('/leaderboard/clips/all')
def leaderboard_clips():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/leaderboard?cursor=[0,50]')
    return data.json()


@app.get('/leaderboard/votes/all')
def leaderboard_votes():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/votes/leaderboard?cursor=[0,50]')
    return data.json()


@app.get('/stats/clips')
def stats_clips():
    data = requests.get('https://commonvoice.mozilla.org/api/v1/uz/clips/stats')
    return data.json()


@lru_cache()
def fetch_text_stats(ttl_hash=None):
    data = requests.get('https://commonvoice.mozilla.org/sentence-collector/stats?locales=uz')
    return data.json()


def get_ttl_hash(seconds=28800):
    """Return the same value withing `seconds` time period"""
    return round(time.time() / seconds)


@app.get('/stats/texts')
def stats_texts(reset: bool = False):
    if reset:
        fetch_text_stats.cache_clear()
    return fetch_text_stats(ttl_hash=get_ttl_hash())
