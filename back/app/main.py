from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import UserCreate, User
from crud import get_users, create_new_user, rm_new_user

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/users/", response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(db=db, user=user)

@app.delete("/users/", response_model=User)
def rm_user(user_id: int, db: Session = Depends(get_db)):
    return rm_new_user(db=db, user_id=user_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)