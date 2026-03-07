from pydantic import BaseModel

class ContainerCreate(BaseModel):
    name: str
    host: str
    port: int
    image: str
    memory: int
    cpus: int

class ClientCreate(BaseModel):
    name: str