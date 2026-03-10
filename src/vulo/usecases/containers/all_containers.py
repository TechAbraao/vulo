
class AllContainersUseCase:
    def __init__(self, repo, docker_client):
        self.repo = repo,
        self.docker_client = docker_client

    def _formatting_containers(self, containers):
         return [
             {
                "id": c.short_id,
                "name": c.name,
                "status": c.status,       
                "image": c.image.tags,  
                "ports": c.ports,        
                # "labels": c.labels,     # É necessário realmente retornar as labels?  
                "created": c.attrs["Created"],
                "started_at": c.attrs["State"]["StartedAt"],
                "finished_at": c.attrs["State"]["FinishedAt"],
                "restart_count": c.attrs["RestartCount"],
                "platform": c.attrs["Platform"],
                "network": list(c.attrs["NetworkSettings"]["Networks"].keys()),
             } for c in containers]

    async def execute(self, roles: str = None):
        all_containers = (self._formatting_containers(self.docker_client.containers.list(all=True)))
        return all_containers