
from datetime import datetime

from pydantic import BaseModel, ConfigDict


# Data required to create an investigation
class InvestigationCreate(BaseModel):
    title: str = "New investigation"


# Data allowed when updating an investigation
class InvestigationUpdate(BaseModel):
    title: str | None = None
    status: str | None = None


# Data returned to the frontend
class InvestigationResponse(BaseModel):
    id: int
    title: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
