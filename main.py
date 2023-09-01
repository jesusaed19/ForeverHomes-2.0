from fastapi import FastAPI, Request, Response, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from schemas.email import Email
from lib.email import email


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/thanks", response_class=HTMLResponse)
# async def thanks(request: Request):
    
#     return templates.TemplateResponse("contact.html", {"request": request})

@app.post('/thanks', response_class=HTMLResponse)
async def dataemail(request: Request, data_email = Email, name: str = Form(), mail: str = Form(), project: str = Form()):
    data_email.name = name
    data_email.mail = mail
    data_email.project = project
    
    email(data_email.mail, data_email.name, data_email.project)
    
    return templates.TemplateResponse("contact.html", {"request": request})
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@app.get("/thanksyou", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})