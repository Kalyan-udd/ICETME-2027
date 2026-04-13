from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/templates/static", StaticFiles(directory="./templates/static"), name='static')

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.post("/")
async def registration(request: Request):
    return templates.TemplateResponse(request, "registration.html")