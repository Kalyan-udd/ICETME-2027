from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/templates/static", StaticFiles(directory="./templates/static"), name='static')

templates = Jinja2Templates(directory='templates')

posts: list[dict] = [

    {
        "id" : 1,
        "name" : "kalyan",
        "title" : "IC engines.",
        "description" : "research on IC engines for optimal fuel efficiency",
        "date_of_posted" : "20-april-2026"
    },

    {
        "id" : 2,
        "name" : "rohit",
        "title" : "diesel engines",
        "description" : "research on diesel engines for optimal fuel efficiency",
        "date_of_posted" : "26-april-2026"
    }

]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/api/posts")
async def get_posts():
    return posts