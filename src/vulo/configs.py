from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Configs():
    _title: str = field(default="Vulo", init=False)
    _description: str = field(default="A lightweight PaaS for your home server", init=False)
    _version: str = field(default="1.0.0", init=False)

    app_mode: str = os.getenv("APP_MODE", None)
    app_host: str = os.getenv("APP_HOST", None)
    app_port: str = os.getenv("APP_PORT", None)

    @property
    def title(self) -> str:
        return self._title
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def version(self) -> str:
        return self._version