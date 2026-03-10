from src.vulo.models import Containers
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ContainersRepository:
    def __init__(self, db):
        self.db = db

    async def create(self, data):

        container = Containers(
            name=data.name,
            image=data.image,
            internal_port=data.internal_port,
            external_port=data.external_port,
            nano_cpus=data.cpus,
            mem_limit=data.memory
        )

        self.db.add(container)
        self.db.commit()
        self.db.refresh(container)

        return container

    async def exists_by_name(self, name: str):
        exists = self.db.query(Containers).filter(Containers.name == name).first()
        return exists is not None
