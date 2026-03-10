from src.vulo.models import Clients
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ClientRepository:
    def __init__(self, db):
        self.db = db

    async def create(self, name: str, client_id: str, client_secret: str):

        client = Clients(
            name=name,
            client_id=client_id,
            client_secret=client_secret
        )

        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)

        return client
    
    async def exists_by_name(self, name: str):
        exists = self.db.query(Clients).filter(Clients.name == name).first()
        return exists is not None
    
    async def find_all(self):
        all_clients = self.db.query(Clients).all()
        return all_clients

    async def find_by_id(self, id: str):
        client = self.db.query(Clients).filter(Clients.id == id).first()
        return client

    async def find_all_by_id(self, id: str):
        pass

    async def delete_by_id(self, id: str) -> bool:
        client = self.db.query(Clients).filter(Clients.id == id).first()

        if not client:
            return False

        self.db.delete(client)
        self.db.commit()
        return True
