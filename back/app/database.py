from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# import os

# DATABASE_URL = f"sqlite:///{os.path.abspath('../migrations/db.sqlite')}"
DATABASE_URL = "sqlite:///./migrations/db.sqlite"

# Create SQLAlchemy engine to connect w/ SQLite DB
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SQLAlchemy session maker
# Enables to create sessions to interact w/ DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models that will be used to map DB tables
Base = declarative_base()

# Returns an SQLAlchemy session
# yield is a special function creating generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
