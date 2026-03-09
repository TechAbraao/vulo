from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Configs():
    _title: str = field(default="Vulo", init=False)
    _description: str = field(default="A lightweight PaaS for your home server", init=False)
    _version: str = field(default="1.0.0", init=False)
    _database_dev: str = field(default="sqlite:///./src/vulo/db/vulo-dev.db", init=False)
    _maintainers: list[dict] = field(default_factory=lambda: [
        {
            "name": "Abraão Santos",
            "github": "github.com/TechAbraao"
        }, 
        {
            "name": "Vinicius Mattera",
            "github": "github.com/Mattera-dev"
        }
    ], init=False)

    app_mode: str = os.getenv("APP_MODE", "dev")
    app_host: str = os.getenv("APP_HOST", None)
    app_port: str = os.getenv("APP_PORT", None)
    admin_username: str = os.getenv("ADMIN_USERNAME", None)
    admin_password: str = os.getenv("ADMIN_PASSWORD", None)

    @property
    def title(self) -> str:
        return self._title
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def version(self) -> str:
        return self._version
    
    @property
    def database_dev(self) -> str:
        return self._database_dev
    
    @property
    def maintainers(self) -> list[dict]:
        return self._maintainers