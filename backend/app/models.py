from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid

from .database import Base


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#     items = relationship("Item", back_populates="owner")


class Simulation(Base):
    __tablename__ = "simulations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    status = Column(String, index=True)
    iterations = Column(Integer)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="items")

class CachedSimulation(Base):
    __tablename__ = "cached_simulations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    bag = Column(JSON)
    cards = Column(JSON)
    character = Column(JSON)

