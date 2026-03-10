from src.vulo.schemas import ContainerCreate as ContainerCreateReq
from src.vulo.repos.containers_repository import ContainersRepository
from src.vulo.usecases.containers.all_containers import AllContainersUseCase
from src.vulo.usecases.containers.create_container import CreateContainerUseCase
from fastapi import Depends, status
from src.vulo.common import get_db, get_docker
from sqlalchemy.orm import Session
from src.vulo.http import api
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@api.get("/containers", tags=["Containers"], status_code=status.HTTP_200_OK)
async def get_containers(db: Session = Depends(get_db), client = Depends(get_docker)):
    
    repo = ContainersRepository(db)
    usecase = AllContainersUseCase(repo=repo, docker_client=client)
    containers = await usecase.execute()

    return containers

@api.post("/containers", tags=["Containers"], status_code=status.HTTP_201_CREATED)
async def post_containers(req: ContainerCreateReq, db: Session = Depends(get_db), client = Depends(get_docker)):

    repo = ContainersRepository(db)
    usecase = CreateContainerUseCase(repo=repo, docker_client=client)
    result = await usecase.execute(req=req)

    return None

@api.get("/containers/{id}", tags=["Containers"])
async def get_by_id_containers(id: str):
    pass

@api.put("/containers", tags=["Containers"])
async def put_containers():
    pass

@api.delete("/containers/{id}", tags=["Containers"])
async def delete_containers(id: str):
    pass

@api.patch("/containers/{id}/status", tags=["Containers"])
async def status_containers(id: str):
    pass