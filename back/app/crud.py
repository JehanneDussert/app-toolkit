from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def get_users(db: Session):
    return db.query(User).all()

def create_new_user(db: Session, user: UserCreate):
    db_user = User(title=user.title, type=user.type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user