from src.vulo.schemas import ContainerCreate as ContainerCreateReq
from fastapi import HTTPException
from src.vulo.http import api

@api.post("/containers", tags=["Containers"])
async def post_containers(req: ContainerCreateReq):
    
    return {"data": f"{req}"}

@api.get("/containers", tags=["Containers"])
async def get_containers():
    pass

@api.get("/containers/{id}", tags=["Containers"])
async def get_by_id_containers(id: str):
    pass

@api.put("/containers", tags=["Containers"])
async def put_containers():
    pass

@api.delete("/containers/{id}", tags=["Containers"])
async def delete_containers():
    pass