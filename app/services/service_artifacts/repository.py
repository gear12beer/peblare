from uuid import UUID

from fastapi import HTTPException, status

from app.core.supabase import supabase
from app.core.logger import get_logger

logger = get_logger(__name__)

def create_artifact(
    *,
    artifact_id: UUID,
    slug: str,
    title: str | None,
    password: str | None,
    artifact_type: str,
    filename: str,
    extension: str,
    mime_type: str,
    storage_path: str,
    size_bytes: int,
):

    data = {
        "id": str(artifact_id),
        "slug": slug,
        "title": title,
        "password": password,
        "artifact_type": artifact_type,
        "filename": filename,
        "extension": extension,
        "mime_type": mime_type,
        "storage_path": storage_path,
        "size_bytes": size_bytes,
    }

    try:

        response = (
            supabase
            .table("artifacts")
            .insert(data)
            .execute()
        )

        logger.info(
            "Artifact metadata created | id=%s",
            artifact_id,
        )

        return response.data[0]

    except Exception:

        logger.exception("Unable to save artifact metadata")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to save artifact metadata.",
        )