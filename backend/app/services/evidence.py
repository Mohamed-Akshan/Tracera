
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile, HTTPException

from app.db.database import SessionLocal
from app.db.models import Investigation, EvidenceFile


# Folder for uploaded files
UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_TYPES = {".log", ".txt", ".json", ".pdf"}


# Save uploaded evidence
def save_evidence(investigation_id: int, file: UploadFile):

    with SessionLocal() as db:

        # Check if investigation exists
        investigation = db.get(Investigation, investigation_id)

        if not investigation:
            raise HTTPException(404, "Investigation not found")

        # Check file format
        filename = Path(file.filename or "").name
        extension = Path(filename).suffix.lower()

        if extension not in ALLOWED_TYPES:
            raise HTTPException(400, "Unsupported file format")

        # Read file (maximum 10 MB)
        content = file.file.read(10 * 1024 * 1024 + 1)

        if not content:
            raise HTTPException(400, "Empty file")

        if len(content) > 10 * 1024 * 1024:
            raise HTTPException(413, "File is too large")

        # Save with a unique name
        file_path = UPLOAD_DIR / f"{uuid4().hex}{extension}"
        file_path.write_bytes(content)

        # Save file information to PostgreSQL
        evidence = EvidenceFile(
            investigation_id=investigation_id,
            filename=filename,
            file_path=str(file_path),
            status="pending"
        )

        try:
            db.add(evidence)
            db.commit()
            db.refresh(evidence)

        except Exception:
            db.rollback()
            file_path.unlink(missing_ok=True)
            raise

        return {
            "id": evidence.id,
            "filename": evidence.filename,
            "status": evidence.status
        }
