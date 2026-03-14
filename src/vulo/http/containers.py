from src.vulo.schemas import ContainerCreate as ContainerCreateReq
from src.vulo.repos.containers_repository import ContainersRepository
from src.vulo.usecases.containers.all_containers import AllContainersUseCase
from src.vulo.usecases.containers.create_container import CreateContainerUseCase
from src.vulo.usecases.containers.container_status_by_id import ContainerStatusById
from src.vulo.usecases.containers.container_by_id import ContainerByIdUseCase
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

@api.delete("/containers/{id}", tags=["Containers"])
async def delete_container_by_id(id: str):
    # TODO:
    return None

@api.put("/containers", tags=["Containers"])
async def put_containers():
    
    # TODO: 
    
    return None

@api.get("/containers/{id}", tags=["Containers"])
async def get_by_id_containers(id: str, db: Session = Depends(get_db), client=Depends(get_docker)):

    repo = ContainersRepository(db=db)
    usecase = ContainerByIdUseCase(repo=repo, docker_client=client)
    container_by_id = await usecase.execute(id=id)

    return container_by_id


@api.get("/containers/{id}/status", tags=["Containers"], status_code=status.HTTP_200_OK)
async def status_containers(id: str, db: Session = Depends(get_db), client = Depends(get_docker)):

    repo = ContainersRepository(db=db)
    usecase = ContainerStatusById(docker_client=client, repo=repo)
    current_status = await usecase.execute(id=id)

    return {"status": f"{current_status}"}

@api.patch("/containers/{id}/status", tags=["Containers"], status_code=status.HTTP_200_OK)
async def status_containers(id: str, db: Session = Depends(get_db), client=Depends(get_docker)):

    # TODO:
    
    return None
