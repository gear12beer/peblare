from uuid import UUID

from fastapi import HTTPException, status

from app.core.config import SUPABASE_BUCKET
from app.core.logger import get_logger
from app.core.supabase import supabase

logger = get_logger(__name__)

CONTENT_TYPES = {
    ".html": "text/html",
    ".md": "text/markdown",
    ".json": "application/json",
    ".csv": "text/csv",
    ".txt": "text/plain",
}


def upload_file(
    *,
    content: bytes,
    artifact_id: UUID,
    extension: str,
    artifact_type: str,
) -> str:

    storage_path = f"static/{artifact_type}/{artifact_id}{extension}"

    try:

        supabase.storage.from_(SUPABASE_BUCKET).upload(
            path=storage_path,
            file=content,
            file_options={
                "content-type": CONTENT_TYPES[extension],
                "upsert": "false",
            },
        )

        logger.info("Uploaded %s", storage_path)

        return storage_path

    except Exception as exc:

        logger.exception(exc)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to upload artifact.",
        )