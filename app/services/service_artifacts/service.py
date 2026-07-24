from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile 

from app.core.logger import get_logger
from app.core.config import CONTENT_TYPES
from app.services.service_artifacts.validator import (
    validate_extension,
    validate_file,
)
from app.services.service_artifacts.slug import generate_slug
from app.services.service_artifacts.storage import (
    upload_file,
    delete_file,
    )
from app.services.service_artifacts.response import build_publish_response
from app.services.service_artifacts.repository import create_artifact

logger = get_logger(__name__)


async def publish_artifact(
    *,
    file: UploadFile,
    title: str | None = None,
    password: str | None = None,
):
    extension = Path(file.filename).suffix.lower()

    artifact_type = validate_extension(file.filename)

    content = await validate_file(file)

    artifact_id = uuid4()

    slug = generate_slug()

    storage_path = upload_file(
        content=content,
        artifact_id=artifact_id,
        extension=extension,
        artifact_type=artifact_type.value,
    )

    try:
        artifact = create_artifact(
            artifact_id=artifact_id,
            slug=slug,
            title=title,
            password=password,
            artifact_type=artifact_type.value,
            filename=file.filename,
            extension=extension,
            mime_type=CONTENT_TYPES[extension],
            storage_path=storage_path,
            size_bytes=len(content),
        )
    except Exception:
        delete_file(storage_path)
        raise 
        
    logger.info(
        "Artifact published | slug=%s storage=%s",
        slug,
        storage_path,
    )

    return build_publish_response(artifact=artifact)