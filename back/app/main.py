from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.schemas import UserCreate, User
from app.crud import get_users, create_new_user, rm_new_user, update_new_user

app = FastAPI()

# SQLAlchemy instruction that creates all DB metadata tables
Base.metadata.create_all(bind=engine)

# GLOBAL ROUTES

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

@app.put("/users/", response_model=User)
def update_user(user: UserCreate, user_id: int, db: Session = Depends(get_db)):
    
    return update_new_user(db=db, user=user, user_id=user_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)