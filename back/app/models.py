from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

# Model definitions as sqlalchemy classes
# Each model = one DB table

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    type = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)