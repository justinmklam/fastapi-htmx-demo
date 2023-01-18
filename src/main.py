# import fastapi
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/basic-form")
async def basic_form(request: Request, name: str = Form(...), email: str = Form(...)):
    return name, email


@app.get("/select-cars")
async def select_cars(car: str = ""):
    return car


@app.get("/search")
async def search(search: str = ""):
    data = ["apple", "orange", "lemon", "peach", "pear"]
    filtered = [fruit for fruit in data if search in fruit]
    return filtered
