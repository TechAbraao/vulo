from fastapi import HTTPException

class ClientByIdUseCase():
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, id: str, roles: str = None):
        
        client = await self.repo.find_by_id(id)
        if not client:
            raise HTTPException(404, detail=f"Client with id '{id}' not found.")
        
        return client