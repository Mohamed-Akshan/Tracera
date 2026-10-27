
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Investigation


# 1. Create a new investigation
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

        investigations = db.scalars(
            select(Investigation).order_by(
                Investigation.created_at.desc()
            )
        ).all()

        return investigations


# 3. Get one investigation
def get_investigation(investigation_id):

    with SessionLocal() as db:

        investigation = db.get(
            Investigation, investigation_id
        )

        return investigation


def update_investigation(investigation_id, data):
    with SessionLocal() as db:
        # 1. Find the investigation by ID
        investigation = db.get(Investigation, investigation_id)
        
        # 2. If not found → return None
        if investigation is None:
            return None

        # 3. Get only the fields that the user actually sent
        updates = data.model_dump(
            exclude_unset=True,   # ignore fields not sent
            exclude_none=True     # ignore fields sent as null
        )

        # 4. Update those fields on the object
        for key, value in updates.items():
            setattr(investigation, key, value)

        # 5. Save changes to database
        db.commit()
        db.refresh(investigation)
        return investigation
