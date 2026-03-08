from src.vulo.configs import Configs
from fastapi import APIRouter

api = APIRouter(prefix="/api")
web = APIRouter(prefix="")

@api.get("/system/health", tags=["System"])
async def get_health_check():
    return {"msg": "ok"}

@api.get("/system/infos", tags=["System"])
async def get_system_infos():
    configs = Configs()

    
    res = {
        "title": configs.title,
        "description": configs.description,
        "version": configs.version,
        "maintainers": configs.maintainers
    }

    return res

from src.vulo.http.auth import *
from src.vulo.http.containers import *
from src.vulo.http.clients import *

