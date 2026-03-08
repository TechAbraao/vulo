from sqlalchemy import Column, Integer, String
from src.vulo.db import Base
import uuid

class Clients(Base):
    __tablename__ = "clients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    client_id = Column(String)
    client_secret = Column(String)

class Containers(Base):
    __tablename__ = "containers"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

class Tokens():
    pass