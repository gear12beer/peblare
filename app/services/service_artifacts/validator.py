from pathlib import Path

from fastapi import HTTPException, UploadFile, status

from app.core.config import (
    ALLOWED_EXTENSIONS,
    MAX_FILE_SIZE,
)

from app.core.enums import ArtifactType

def validate_extension(filename: str) -> ArtifactType:

    extension = Path(filename).suffix.lower()

    artifact_type = ALLOWED_EXTENSIONS.get(extension)

    if artifact_type is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported file type.",
        )

    return artifact_type

async def validate_file(file: UploadFile) -> bytes:

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum file size is 10 MB.",
        )

    return content

