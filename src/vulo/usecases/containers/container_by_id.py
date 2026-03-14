from src.vulo.constants import ContainerStrategy
from docker.errors import NotFound
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ContainerByIdUseCase:
    def __init__(self, repo, docker_client):
        self.repo = repo
        self.docker_client = docker_client

    async def _find_container_with_strategy(self, strategy: ContainerStrategy = None):

        if strategy == ContainerStrategy.DATABASE:
            container_by_id = await self.repo.find_by_id(id=id)
            if not container_by_id:
                logger.warn(f"Container with id '{id}' not found.")
                raise HTTPException(404, detail=f"Container with id '{id}' not found.")
            return container_by_id
        elif strategy == ContainerStrategy.DAEMON:
            logger.info(f"Searching container with id '{id}' in database.")
            try:
                container_by_id = self.docker_client.containers.get(id)
            except NotFound:
                logger.warn(f"Container with id '{id}' not found.")
                raise HTTPException(404, detail=f"Container with id '{id}' not found.")
        else:
            raise ValueError(f"Unknown strategy: '{strategy}'. Expected one of: {list(ContainerStrategy)}")

    def _formatting_containers(self, c):
        return [{
                "id": c.short_id,
                "name": c.name,
                "status": c.status,
                "image": c.image.tags,
                "ports": c.ports,
                "created": c.attrs["Created"],
                "started_at": c.attrs["State"]["StartedAt"],
                "finished_at": c.attrs["State"]["FinishedAt"],
                "restart_count": c.attrs["RestartCount"],
                "platform": c.attrs["Platform"],
                "network": list(c.attrs["NetworkSettings"]["Networks"].keys()),
            }]

    async def execute(self, id: str, roles: str = None):

        logger.info(f"Searching container with id '{id}' in database.")
        try:
            container_by_id = self.docker_client.containers.get(id)
        except NotFound:
            logger.warning(f"Container with id '{id}' not found.")
            raise HTTPException(404, detail=f"Container with id '{id}' not found.")

        logger.info(f"Container found. Here are its details: '{container_by_id}'.")
        container_formatted = self._formatting_containers(container_by_id)
        return container_formatted
