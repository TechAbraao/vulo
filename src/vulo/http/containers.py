from fastapi import HTTPException
from src.vulo.http import api

@api.post("/containers")
async def post_containers():
    pass

@api.get("/containers")
async def get_containers():
    pass

@api.put("/containers")
async def put_containers():
    pass

@api.delete("/containers")
async def delete_containers():
    pass