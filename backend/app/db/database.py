
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings


# Connect to PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)


# Create database sessions
SessionLocal = sessionmaker(
    bind=engine
)


# Base class for our database tables
Base = declarative_base()
