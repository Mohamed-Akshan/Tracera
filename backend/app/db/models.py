
from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from app.db.database import Base


# Get the current UTC time
def current_time():
    return datetime.now(timezone.utc)


# 1. Store investigations
class Investigation(Base):
    __tablename__ = "investigations"

    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=False)

    status = Column(String(30), default="open")

    created_at = Column(
        DateTime(timezone=True),
        default=current_time
    )


# 2. Store uploaded evidence file information
class EvidenceFile(Base):
    __tablename__ = "evidence_files"

    id = Column(Integer, primary_key=True)

    investigation_id = Column(
        Integer,
        ForeignKey("investigations.id"),
        nullable=False
    )

    filename = Column(String(255), nullable=False)

    file_path = Column(Text)

    status = Column(String(30), default="pending")

    uploaded_at = Column(
        DateTime(timezone=True),
        default=current_time
    )
