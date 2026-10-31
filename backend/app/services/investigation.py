
from app.db.database import SessionLocal
from app.db.models import Investigation


# 1. Create an investigation
def create_investigation(data):

    with SessionLocal() as db:

        investigation = Investigation(**data.model_dump())

        db.add(investigation)
        db.commit()
        db.refresh(investigation)

        return investigation


# 2. Get all investigations
def list_investigations():

    with SessionLocal() as db:

        return db.query(Investigation).order_by(
            Investigation.created_at.desc()
        ).all()


# 3. Get one investigation
def get_investigation(investigation_id):

    with SessionLocal() as db:

        return db.get(Investigation, investigation_id)


# 4. Update an investigation
def update_investigation(investigation_id, data):

    with SessionLocal() as db:

        investigation = db.get(Investigation, investigation_id)

        if not investigation:
            return None

        # Update only the provided fields
        updates = data.model_dump(exclude_unset=True, exclude_none=True)

        for key, value in updates.items():
            setattr(investigation, key, value)

        db.commit()
        db.refresh(investigation)

        return investigation
