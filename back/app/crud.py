from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from dataclasses import asdict
from fastapi import HTTPException

# Interaction functions w/ DB using SQLAlchemy

def get_users(db: Session):
    return db.query(User).all()

def create_new_user(db: Session, user: UserCreate) -> User:
    db_user = User(title=user.title, type=user.type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def rm_new_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user

    raise HTTPException(status_code=404, detail=f"L'utiliasteur n'existe pas")

def update_new_user(db: Session, user: UserCreate, user_id: int) -> User:
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if db_user:
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        
        db.commit()
        db.refresh(db_user)
        return db_user
    
    raise HTTPException(status_code=404, detail="L'utilisateur n'existe pas")
