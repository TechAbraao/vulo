from sqlalchemy import Column, Integer, String, Float
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
    name = Column(String(36))
    image = Column(String(36))
    internal_port = Column(Integer)
    external_port = Column(Integer)
    nano_cpus = Column(Float)
    mem_limit = Column(String(20))

class Users(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String)
    password = Column(String)
    roles = Column(String)

class Tokens():
    pass
