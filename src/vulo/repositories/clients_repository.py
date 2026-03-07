from src.vulo.models import Clients

class ClientRepository:
    def __init__(self, db):
        self.db = db

    async def create(
            self, name: str, client_id: str, client_secret: str
        ):

        client = Clients(
            name=name,
            client_id=client_id,
            client_secret=client_secret
        )

        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)

        return client