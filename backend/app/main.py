from typing import Optional, List
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from joblib import Parallel, delayed

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
    defiance_second_copy: str
    defiance_level_2: bool

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/simulate/")
async def create_simulation(bag: List[Token], cards: cards, character: Optional[str] = ''):
    results = []
    results = Parallel(n_jobs=6)(delayed(resolveToken)(token, bag, cards, character) for token in bag)
    flattened_results = [result for token_result in results for result in token_result]

    test_results = analyzeResults(flattened_results)
    output = {
        'iterations': len(flattened_results),
        'test_results': test_results
    }
    json_output = jsonable_encoder(output)
    return JSONResponse(content=json_output)