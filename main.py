from typing import Optional, List
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from simulation import resolveToken
from analysis import analyzeResults

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Token(BaseModel):
    label: str
    modifier: int
    limit: int
    draw_again: bool
    quantity: int
    variable: bool
    automatic_failure: bool
    automatic_success: bool
    symbol: bool

class cards(BaseModel):
    counterspell: bool
    ritual_candles: bool
    ritual_candles_second_copy: bool
    recall_the_future: str
    recall_the_future_second_copy: str
    defiance: str
    defiance_level_2: bool

class Character(BaseModel):
    name: str
    effect: int
    autosucceed: bool

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/simulate/")
async def create_simulation(bag: List[Token], cards: cards, character: Optional[Character]):
    results = []
    for token in bag:
        print("drawing token: " + token.label)
        token_results = resolveToken(token, bag, cards, character)
        results += token_results
    test_results = analyzeResults(results)
    json_test_results = jsonable_encoder(test_results)
    return JSONResponse(content=json_test_results)