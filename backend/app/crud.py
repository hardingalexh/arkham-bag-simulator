from sqlalchemy.orm import Session

from . import models, schemas


def get_simulation(db: Session, simulation_id: int):
    return db.query(models.Simulation).filter(models.Simulation.id == simulation_id).first()

def create_simulation(db: Session, simulation: schemas.SimulationCreate):
    db_simulation = models.Simulation(status=simulation.status)
    db.add(db_simulation)
    db.commit()
    db.refresh(db_simulation)
    return db_simulation

def create_cached_simulation(db: Session, simulation: schemas.CachedSimulationCreate):
    db_cached_simulation = models.CachedSimulation(status=simulation.status)
    db.add(db_cached_simulation)
    db.commit()
    db.refresh(db_cached_simulation)
    return db_cached_simulation


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item