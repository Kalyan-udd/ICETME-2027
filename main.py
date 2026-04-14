from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/registration")
async def register(request: Request):
    return templates.TemplateResponse(request, "registration.html")

@app.get("/about")
async def about_page(request: Request):
    # This tells FastAPI to look inside your 'templates' folder and serve about.html
    return templates.TemplateResponse("about.html", {"request": request})
