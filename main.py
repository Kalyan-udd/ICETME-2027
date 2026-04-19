import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

static_dir = os.path.join(BASE_DIR, "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name='static')

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, 'templates'))

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/registration")
async def register(request: Request):
    return templates.TemplateResponse(request, "registration.html")

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(request, 'about.html')

@app.get("/travel")
def travel(request: Request):
    return templates.TemplateResponse(request, 'travel.html')

@app.get("/important_dates")
async def importantdates(request: Request):
    return templates.TemplateResponse(request, 'timetable.html')