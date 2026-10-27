from app.db.database import Base, engine
from app.db import models


# Create all database tables
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tracera database tables created successfully!")


# Run only when executing this file directly
if __name__ == "__main__":
    create_tables()