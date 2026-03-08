from fastapi import HTTPException
import secrets
import hashlib

class CreateClientUseCase:
    def __init__(self, repo):
        self.repo = repo

    def _create_client(self, length: int):
        return secrets.token_urlsafe(length)

    def _hash_secret_key(self, secret_key: str) -> str:
        return hashlib.sha256(secret_key.encode()).hexdigest()

    async def execute(self, name: str):

        exists = await self.repo.exists_by_name(name)
        if exists:
            raise HTTPException(status_code=409, detail=f"Client '{name}' already exists.")

        client_id = self._create_client(16)
        client_secret =  self._create_client(32)
        client_secret_hash = self._hash_secret_key(client_secret)


        client = await self.repo.create(
            name=name,
            client_id=client_id,
            client_secret=client_secret_hash
        )

        return {
            "client_id": client.client_id,
            "client_secret": client_secret
        }