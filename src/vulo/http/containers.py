from src.vulo.schemas import ContainerCreate as ContainerCreateReq
from fastapi import HTTPException
from src.vulo.http import api

@api.post("/containers")
async def post_containers(req: ContainerCreateReq):
    
    return {"data": f"{req}"}

@api.get("/containers")
async def get_containers():
    pass

@api.get("/containers/{id}")
async def get_by_id_containers(id: str):
    pass

@api.put("/containers")
async def put_containers():
    pass

@api.delete("/containers")
async def delete_containers():
    pass