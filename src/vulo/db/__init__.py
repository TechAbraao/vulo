from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.vulo.configs import Configs

configs = Configs()
DATABASE_URL = configs.database_dev

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()