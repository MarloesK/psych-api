import random
from typing import List, Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from helpers import load_json
from models import Pineapple

app = FastAPI()
limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute"])

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello Psych Fan!🍍"}


@app.get("/cast", tags=['cast'])
def read_cast(character: Optional[str] = None):
    data = load_json('data/cast.json')

    if character:
        data = [actor for actor in data if character.lower() in actor['role'].lower()]
        if len(data) == 0:
            return JSONResponse(status_code=404, content={"detail": "Character not found"})

    return JSONResponse(content=data)


@app.get("/episodes", tags=['episodes'])
def read_episodes():
    return {"message": "Coming Soon!"}


@app.get("/quotes", tags=['quotes'])
def read_quotes(limit: int = 5):
    data = load_json('data/quotes.json')
    return JSONResponse(content=data[:limit])


@app.get("/pineapples", response_model=List[Pineapple], tags=['pineapple'])
def read_pineapples(
        limit: int = 5,
        season: Optional[int] = None,
        episode: Optional[int] = None
):
    data = load_json('data/pineapples.json')

    if season:
        data = [item for item in data if item['season'] == season]
    if episode:
        data = [item for item in data if item['episode'] == episode]

    return JSONResponse(content=data[:limit])


@app.get("/pineapples/random", response_model=Pineapple, tags=['pineapple'])
def read_random_pineapple():
    data = load_json('data/pineapples.json')
    return JSONResponse(content=random.choice(data))


@app.get("/nicknames", tags=['nicknames'])
def read_nicknames(limit: int = 5):
    data = load_json('data/gus_nicknames.json')
    return JSONResponse(content=data[:limit])


@app.get("/trivia", tags=['trivia'])
def read_trivia(limit: int = 5):
    data = load_json('data/trivia.json')
    return JSONResponse(content=data[:limit])
