
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

from app.db.database import SessionLocal
from app.db.models import Investigation, EvidenceFile


# Folder for uploaded evidence
UPLOAD_DIR = Path(__file__).resolve().parents[2] / "data" / "uploads"

# Supported file formats
ALLOWED_TYPES = {".log", ".txt", ".json", ".pdf"}

# Maximum file size: 10 MB
MAX_FILE_SIZE = 10 * 1024 * 1024


# Save an uploaded evidence file
def save_evidence(investigation_id: int, file: UploadFile):

    # Check whether the investigation exists
    with SessionLocal() as db:

        investigation = db.get(Investigation, investigation_id)

        if investigation is None:
            raise HTTPException(
                status_code=404,
                detail="Investigation not found"
            )

        # Get the original filename safely
        filename = (file.filename or "").replace("\\", "/").split("/")[-1]

        file_type = Path(filename).suffix.lower()

        # Accept only supported formats
        if file_type not in ALLOWED_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Only LOG, TXT, JSON and PDF files are allowed"
            )

        # Create the investigation's upload folder
        folder = UPLOAD_DIR / f"investigation-{investigation_id}"
        folder.mkdir(parents=True, exist_ok=True)

        # Generate a unique filename
        unique_name = f"{uuid4().hex}{file_type}"
        file_path = folder / unique_name

        try:
            # Save the file in small pieces
            size = 0

            with open(file_path, "wb") as saved_file:

                while chunk := file.file.read(1024 * 1024):

                    size += len(chunk)

                    if size > MAX_FILE_SIZE:
                        raise HTTPException(
                            status_code=413,
                            detail="File exceeds the 10 MB limit"
                        )

                    saved_file.write(chunk)

            # Reject empty files
            if size == 0:
                raise HTTPException(
                    status_code=400,
                    detail="Cannot upload an empty file"
                )

            # Save file information in PostgreSQL
            evidence = EvidenceFile(
                investigation_id=investigation_id,
                filename=filename,
                file_path=str(file_path),
                file_type=file_type,
                chunk_count=0,
                status="pending"
            )

            db.add(evidence)
            db.commit()
            db.refresh(evidence)

            return {
                "id": evidence.id,
                "investigation_id": investigation_id,
                "filename": evidence.filename,
                "status": evidence.status
            }

        except Exception:
            db.rollback()

            # Remove the file if saving failed
            file_path.unlink(missing_ok=True)
            raise
