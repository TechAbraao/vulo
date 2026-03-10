
class ContainerByIdUseCase:
    def __init__(self, repo):
        self.repo = repo
        
    async def execute(self, roles: str = None):
        pass