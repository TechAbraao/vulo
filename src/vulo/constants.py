from enum import Enum

DEV = "dev"
PROD = "prod"
TEST = "test"

class ContainerExistsStrategy(Enum):
    DAEMON = "daemon"
    DATABASE = "database"
