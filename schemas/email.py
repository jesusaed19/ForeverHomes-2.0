from pydantic import BaseModel

class Email(BaseModel):
    mail: str
    name: str
    project: str