from src.vulo.configs import Configs
from src.vulo import create_app
## import docker
import uvicorn

## Instanciando a aplicação.
app = create_app(Configs())

## Instanciando o client do Docker (se conecta ao Daemon Local)
## client = docker.from_env()

if __name__ == "__main__":
    configs = Configs()
    uvicorn.run(
            app=app, 
            host=configs.app_host,
            port=configs.app_port,
            reload=True
        )