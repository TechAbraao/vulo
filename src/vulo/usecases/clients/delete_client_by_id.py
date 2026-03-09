
from fastapi import HTTPException, status

class DeleteClientByIdUseCase():
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, id: str, roles: str = None) -> bool:

        deleted = await self.repo.delete_by_id(id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client does not exist."
            )

        return True