from src.vulo.configs import Configs
from src.vulo import create_app
import uvicorn
import os

app = create_app(Configs())

if __name__ == "__main__":
    configs = Configs()
    uvicorn.run(
            app=app, 
            host=configs.app_host,
            port=configs.app_port,
            reload=True
        )