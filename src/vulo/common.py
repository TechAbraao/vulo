from src.vulo.db import SessionLocal
import docker

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_docker():
    client = docker.from_env()
    try:
        yield client
    finally:
        client.close()