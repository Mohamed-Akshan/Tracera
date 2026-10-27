
from pydantic import BaseModel, ConfigDict


# Data required to create an investigation
class InvestigationCreate(BaseModel):
    title: str = "New investigation"
    description: str | None = None


# Data allowed when updating an investigation
class InvestigationUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None


# Data returned to the frontend
class InvestigationResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    summary: str | None

    model_config = ConfigDict(from_attributes=True)
