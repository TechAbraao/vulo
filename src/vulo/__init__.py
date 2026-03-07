from src.vulo.configs import Configs
from src.vulo.http import (api, web)
from fastapi import FastAPI, APIRouter
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def create_app(configs: Configs | None) -> FastAPI:
    _configs: Configs = configs or Configs()
    logger.info(f"Application version: {_configs.version}")

    modes_allowed = ["dev", "test", "prod"]
    if _configs.app_mode == modes_allowed[0]:
        logger.info(f"Application mode: {modes_allowed[0]}")
        pass

    if _configs.app_mode == modes_allowed[1]:
        logger.info(f"Application mode: {modes_allowed[1]}")
        pass

    if _configs.app_mode == modes_allowed[2]:
        logger.info(f"Application mode: {modes_allowed[2]}")
        pass
    logger.info(f"Application description: {_configs.description}")

    if not _configs.app_mode in modes_allowed:
        exit("\n * Select an application startup mode. These are: dev, test, or prod.\n")

    app = FastAPI(
                title=_configs.title, 
                version=_configs.version, 
                description=_configs.description
        )
    
    routes = [api, web]
    for route in routes:
        app.include_router(route)

    logger.info(f"The server initialized successfully. ;)")
    return app