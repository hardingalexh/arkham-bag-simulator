from typing import Optional, List
from pydantic import BaseModel

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

from joblib import Parallel, delayed

from simulation import resolveToken
from analysis import analyzeResults

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
async def create_simulation(simulation: schemas.SimulationCreate, db: Session = Depends(get_db)):
    # check to see if this simulation has been run before
    cached_simulation_search = crud.find_cached_simulation(db, simulation)

    if cached_simulation_search is None:
        # run simulation
        # db_simulation = crud.create_simulation(db, simulation)
        results = []
        results = Parallel(n_jobs=6)(delayed(resolveToken)(token, simulation.bag, simulation.cards, simulation.character) for token in simulation.bag)
        flattened_results = [result for token_result in results for result in token_result]
        test_results = analyzeResults(flattened_results)
        # write simulation to cache table
        db_cached_simulation = crud.create_cached_simulation(db, simulation, len(flattened_results), test_results)
        output = db_cached_simulation
        output.status = "result"
    else:
        output = cached_simulation_search
        output.status = "cached"
    
    # encode result as json and return
    json_output = jsonable_encoder(output)
    return JSONResponse(content=json_output)