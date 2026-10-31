
from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from app.db.database import engine

from app.models.schemas import (
    InvestigationCreate,
    InvestigationUpdate,
    InvestigationResponse
)

from app.services.investigation import (
    create_investigation,
    list_investigations,
    get_investigation,
    update_investigation
)


router = APIRouter()


# Check backend health
@router.get("/health")
def health_check():
    return {"status": "healthy"}


# Check PostgreSQL connection
@router.get("/health/database")
def database_health():

    try:
        with engine.connect() as db:
            db.execute(text("SELECT 1"))

        return {"database": "connected"}

    except Exception:
        raise HTTPException(503, "Database connection failed")


# 1. Create an investigation
@router.post("/investigations", response_model=InvestigationResponse)
def create_investigation_api(data: InvestigationCreate):

    return create_investigation(data)


# 2. Get all investigations
@router.get("/investigations", response_model=list[InvestigationResponse])
def list_investigations_api():

    return list_investigations()


# 3. Get one investigation
@router.get("/investigations/{investigation_id}", response_model=InvestigationResponse)
def get_investigation_api(investigation_id: int):

    investigation = get_investigation(investigation_id)

    if not investigation:
        raise HTTPException(404, "Investigation not found")

    return investigation


# 4. Update an investigation
@router.patch("/investigations/{investigation_id}", response_model=InvestigationResponse)
def update_investigation_api(investigation_id: int, data: InvestigationUpdate):

    investigation = update_investigation(investigation_id, data)

    if not investigation:
        raise HTTPException(404, "Investigation not found")

    return investigation
