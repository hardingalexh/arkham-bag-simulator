from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

import uuid

from .database import Base

class Simulation(Base):
    __tablename__ = "simulations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    status = Column(String, index=True)
    bag = Column(JSONB)
    cards = Column(JSONB)
    character = Column(String)
    iterations = Column(Integer)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="items")

class CachedSimulation(Base):
    __tablename__ = "cached_simulations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    iterations = Column(Integer)
    test_results = Column(JSONB)
    bag = Column(JSONB)
    cards = Column(JSONB)
    character = Column(String)

