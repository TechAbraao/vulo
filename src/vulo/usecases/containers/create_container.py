from src.vulo.constants import ContainerExistsStrategy
from fastapi import HTTPException, status
from docker.errors import NotFound
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class CreateContainerUseCase:
    def __init__(self, repo, docker_client):
        self.repo = repo
        self.docker_client = docker_client

    def _docker_run(self, name: str, image: str, external_port: int, internal_port: int, cpus: float, memory: str):
        """
            # 1. Instruction: 
            #    docker run --name <name> -p <external:internal> --cpus="<cpus>" --memory="<memory>" <image> -d
        """
        return self.docker_client.containers.run(
            image,
            name=name,
            ports={f"{internal_port}/tcp": external_port},    
            nano_cpus=int(cpus * 1e9), 
            mem_limit=f"{memory}m",   
            detach=True
        )

    async def _containers_exists_with_strategy(self, strategy: ContainerExistsStrategy, name: str) -> bool:
        if strategy == ContainerExistsStrategy.DAEMON:
            try:
                self.docker_client.containers.get(name)
                return True, strategy
            except NotFound:
                return False, strategy
        elif strategy == ContainerExistsStrategy.DATABASE:
            exists_by_name = await self.repo.exists_by_name(name)
            if exists_by_name:
                return True, strategy
            return False, strategy
        else:
            raise ValueError(f"Unknown strategy: '{strategy}'. Expected one of: {list(ContainerExistsStrategy)}")
        
    # 1. E o Rollback pra caso não consiga persistir no SQLite o Container?
    async def execute(self, req, roles: str = None):

        logger.info(f"Checking for the existence of the container '{req.name}'.")
        container_exists, c_strategy = await self._containers_exists_with_strategy(
                strategy=ContainerExistsStrategy.DATABASE, name=req.name
            )

        if container_exists:
            logger.warning(f"Container already exists. The strategy used was '{c_strategy.name}'.")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=f"Container '{req.name}' already exists.")

        logger.info(f"Creating container: {req.name}.")
        container = (self._docker_run(name=req.name, image=req.image, cpus=req.cpus,
                                      external_port=req.external_port, internal_port=req.internal_port, memory=req.memory))
        logger.info(f"Container created: {container.short_id}.")

        logger.info(f"Saving container in database (historic).")
        container_saved = await self.repo.create(req)

        return True
