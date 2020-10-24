from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    effect: int
    limit: int
    draw_again: bool
    quantity: int
    variable: bool
    autofail: bool
    autosucceed: bool
    symbol: bool
    appliedModifiers: List[int]

class cards(BaseModel):
    Counterspell: false
    'Ritual Candles': false
    "Ritual Candles (second copy)": false
    "Recall the Future": false
    "Recall the Future (second copy)": false
    Defiance: false

class Character(BaseModel):
    name: str
    effect: int
    autosucceed: bool


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/simulate/")
async def create_simulation(bag: List[Token], cards: Cards, character: Optional[Character]):
    return "REEEEE"