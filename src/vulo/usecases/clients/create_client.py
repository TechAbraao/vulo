import secrets
import hashlib

class CreateClientUseCase:
    def __init__(self, repository):
        self.repository = repository

    def _hash_secret_key(self, secret_key: str) -> str:
        return hashlib.sha256(secret_key.encode()).hexdigest()

    async def execute(self, name: str):

        client_id = secrets.token_urlsafe(16)
        client_secret = secrets.token_urlsafe(32)
        client_secret_hash = self._hash_secret_key(client_secret)

        client = await self.repository.create(
            name=name,
            client_id=client_id,
            client_secret=client_secret_hash
        )

        return {
            "client_id": client.client_id,
            "client_secret": client_secret
        }