include .env

START=uvicorn src.vulo.app:app --reload --host $(APP_HOST) --port $(APP_PORT)

start:
	$(START)