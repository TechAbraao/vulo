from pydantic import BaseModel

class ContainerCreate(BaseModel):
    name: str
    internal_port: int  
    external_port: int   
    image: str
    memory: int
    cpus: float

class ClientCreate(BaseModel):
    name: str