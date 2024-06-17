from pydantic import BaseModel

# Data structures definitions w/ pydantic
class UserBase(BaseModel):
    title: str
    type: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode: True