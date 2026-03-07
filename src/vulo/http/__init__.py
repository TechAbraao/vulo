from fastapi import APIRouter

api = APIRouter(prefix="/api")
web = APIRouter(prefix="")

@api.get("/health")
async def get_health():
    return {"msg": "ok"}

from src.vulo.http.auth import *
from src.vulo.http.containers import *
from src.vulo.http.clients import *

