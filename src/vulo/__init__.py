from src.vulo.configs import Configs
from src.vulo.db import Base, engine
from src.vulo.http import (api, web)
from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def create_app(configs: Configs | None) -> FastAPI:
    _configs: Configs = configs or Configs()
    logger.info(f"Application version: {_configs.version}")

    app = FastAPI(title=_configs.title, version=_configs.version, description=_configs.description)

    modes_allowed = ["dev", "prod", "test"]
    if _configs.app_mode == modes_allowed[0]:
        logger.info(f"Application mode: {modes_allowed[0]}")

        from src.vulo.models import Clients, Containers, Users
        @app.on_event("startup")
        def create_db():
            logger.info(f"Creating a database and registering the tables")
            Base.metadata.create_all(bind=engine)
        
    if _configs.app_mode == modes_allowed[1]:
        logger.info(f"Application mode: {modes_allowed[1]}")
        
        from src.vulo.models import Clients, Containers, Users
        @app.on_event("startup")
        def create_db():
            logger.info(f"Creating a database and registering the tables")
            Base.metadata.create_all(bind=engine)

    if _configs.app_mode == modes_allowed[2]:
        logger.info(f"Application mode: {modes_allowed[2]}")
        pass

    logger.info(f"Application description: {_configs.description}")

    if not _configs.app_mode in modes_allowed:
        exit("\n * Select an application startup mode. These are: dev, test, or prod.\n")

    routes = [api, web]
    for route in routes:
        logger.info(f"Include router (recording routes): {route}")
        app.include_router(route)

    logger.info(f"The server initialized successfully. ;)")
    return app

