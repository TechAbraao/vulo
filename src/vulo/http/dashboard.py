from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.vulo.http import web, templates

@web.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/index.jinja2",
        context={"title": "Minha Página", "items": ["A", "B", "C"]},
    )

@web.get("/signin")
async def signin(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/index.jinja2",
        context={"title": "Minha Página", "items": ["A", "B", "C"]},
    )