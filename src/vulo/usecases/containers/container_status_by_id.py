from docker.errors import NotFound
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ContainerStatusById:
    def __init__(self, repo, docker_client):
        self.repo = repo
        self.docker_client = docker_client

    async def _container_exists(self, id: str) -> bool:
        try:
            container = self.docker_client.containers.get(id)
            return True, container
        except NotFound:
            return False, id

    async def execute(self, roles: str = None, id: str = None):
        found, container_by_id = await self._container_exists(id=id)
        if not found:
            logger.warn(f"Container with id '{container_by_id}' not found.")
            raise HTTPException(404, detail=f"Container with id '{container_by_id}' not found.")
        
        return container_by_id.status
