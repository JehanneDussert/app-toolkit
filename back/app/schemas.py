from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    title: str
    type: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    title: str
    type: str