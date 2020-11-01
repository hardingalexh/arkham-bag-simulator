from typing import List, Optional

from pydantic import BaseModel


import uuid

class Token(BaseModel):
    id: int
    label: str
    modifier: int
    limit: int
    draw_again: bool
    quantity: int
    variable: bool
    automatic_failure: bool
    automatic_success: bool
    symbol: bool

class Cards(BaseModel):
    counterspell: bool
    ritual_candles: bool
    ritual_candles_second_copy: bool
    recall_the_future: str
    recall_the_future_second_copy: str
    defiance: str
    defiance_second_copy: str
    defiance_level_2: bool

# Simulation
class SimulationBase(BaseModel):
    status: str
    iterations: int
    bag: List[Token]
    cards: Cards
    character: Optional[str]

class SimulationCreate(SimulationBase):
    pass

class Simulation(SimulationBase):
    id: uuid.UUID

    class Config:
        orm_mode = True

# Cached Simulation
class CachedSimulationBase(BaseModel):
    iterations: int
    bag: List[Token]
    cards: Cards
    character: Optional[str]
    test_results: dict

class CachedSimulationCreate(CachedSimulationBase):
    pass

class CachedSimulation(CachedSimulationBase):
    id: uuid.UUID

    class Config:
        orm_mode = True