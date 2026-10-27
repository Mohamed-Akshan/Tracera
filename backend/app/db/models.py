
from datetime import datetime, timezone

from sqlalchemy import (
    Column, Integer, String, Text,
    DateTime, ForeignKey, JSON
)

from app.db.database import Base


# Get the current UTC time
def current_time():
    return datetime.now(timezone.utc)


# 1. Store investigations
class Investigation(Base):
    __tablename__ = "investigations"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(30), default="created")
    summary = Column(Text)
    report = Column(JSON)

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
    file_type = Column(String(20))
    chunk_count = Column(Integer, default=0)
    status = Column(String(30), default="pending")

    uploaded_at = Column(
        DateTime(timezone=True),
        default=current_time
    )


# 3. Store AI investigation findings
class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True)

    investigation_id = Column(
        Integer,
        ForeignKey("investigations.id"),
        nullable=False
    )

    title = Column(String(255), nullable=False)
    explanation = Column(Text)
    severity = Column(String(30))
    confidence = Column(String(30))
    evidence = Column(JSON)
    review_status = Column(String(30), default="pending")

    created_at = Column(
        DateTime(timezone=True),
        default=current_time
    )


# 4. Store AI workspace messages
class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)

    investigation_id = Column(
        Integer,
        ForeignKey("investigations.id"),
        nullable=True
    )

    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=current_time
    )
