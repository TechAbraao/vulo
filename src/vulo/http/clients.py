from src.vulo.repos.clients_repository import ClientRepository
from src.vulo.usecases.clients.create_client import CreateClientUseCase
from src.vulo.usecases.clients.all_clients import AllClientsUseCase
from src.vulo.usecases.clients.client_by_id import ClientByIdUseCase
from src.vulo.usecases.clients.delete_client_by_id import DeleteClientByIdUseCase
from src.vulo.schemas import ClientCreate as ClientCreateReq
from src.vulo.security import basic_auth
from fastapi import HTTPException, Depends, status
from src.vulo.common import get_db
from sqlalchemy.orm import Session
from src.vulo.http import api

@api.post("/clients", tags=["Clients"], status_code=status.HTTP_201_CREATED)
async def post_clients(
        req: ClientCreateReq, db: Session = Depends(get_db),
        credentials = Depends(basic_auth)
    ):

    repo = ClientRepository(db)
    usecase = CreateClientUseCase(repo)
    client = await usecase.execute(req.name)

    return client

@api.get("/clients", tags=["Clients"], status_code=status.HTTP_200_OK)
async def get_clients(db: Session = Depends(get_db), credentials = Depends(basic_auth)):
    
    repo = ClientRepository(db)
    usecase = AllClientsUseCase(repo)
    clients = await usecase.execute()

    return clients

@api.get("/clients/{id}", tags=["Clients"], status_code=status.HTTP_200_OK)
async def get_by_id_clients(
        id: str, db: Session = Depends(get_db),
        credentials = Depends(basic_auth)
    ):
    
    repo = ClientRepository(db)
    usecase = ClientByIdUseCase(repo)
    client_by_id = await usecase.execute(id)

    return client_by_id

@api.delete("/clients/{id}", tags=["Clients"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_clients(id: str, db: Session = Depends(get_db), credentials = Depends(basic_auth)) -> None:
    
    repo = ClientRepository(db)
    usecase = DeleteClientByIdUseCase(repo)
    deleted = await usecase.execute(id)
    
    return None

# TODO: Implementação futura
#
# @api.put("/clients", tags=["Clients"])
# async def put_clients():
#     pass