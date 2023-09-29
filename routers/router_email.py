from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from schemas.email import Email
from lib.email import email

router = APIRouter(tags=['Email'], responses={404: {"Error": "No se encontro"}})


router.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@router.post('/thanks', response_class=HTMLResponse)
async def dataemail(request: Request, data_email = Email, name: str = Form(), mail: str = Form(), project: str = Form()):
    data_email.name = name
    data_email.mail = mail
    data_email.project = project
    
    email(data_email.mail, data_email.name, data_email.project)
    
    return templates.TemplateResponse("contact.html", {"request": request})