from fastapi import HTTPException

class AllClientsUseCase():
    def __init__(self, repo):
        self.repo = repo

    async def execute(self):
        all_clients = await self.repo.find_all()
        return all_clients