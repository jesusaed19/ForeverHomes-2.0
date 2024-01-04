from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


router = APIRouter(tags=['Index'], responses={404: {"Error": "No se encontro"}})

router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/fencing")
async def fencing(request: Request):
    return templates.TemplateResponse("fencing.html", {"request": request})

@router.get("/Decks")
async def fencing(request: Request):
    return templates.TemplateResponse("decks.html", {"request": request})

@router.get("/Framing")
async def fencing(request: Request):
    return templates.TemplateResponse("framing.html", {"request": request})



