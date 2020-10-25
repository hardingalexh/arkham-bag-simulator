from typing import Optional, List
from pydantic import BaseModel

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from joblib import Parallel, delayed

from .simulation import resolveToken
from .analysis import analyzeResults

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/simulate/")
async def create_simulation(simulation: schemas.SimulationCreate, bag: List[schemas.Token], cards: schemas.Cards, character: Optional[str] = '', db: Session = Depends(get_db)):
    db_simulation = crud.create_simulation(db, simulation)
    results = []
    results = Parallel(n_jobs=6)(delayed(resolveToken)(token, bag, cards, character) for token in bag)
    flattened_results = [result for token_result in results for result in token_result]

    test_results = analyzeResults(flattened_results)
    output = {
        'db_simulation': db_simulation,
        'iterations': len(flattened_results),
        'test_results': test_results
    }
    json_output = jsonable_encoder(output)
    return JSONResponse(content=json_output)