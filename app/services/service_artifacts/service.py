from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile 

from app.core.logger import get_logger
from app.services.service_artifacts.validator import (
    validate_extension,
    validate_file,
)
from app.services.service_artifacts.slug import generate_slug
from app.services.service_artifacts.storage import upload_file
from app.services.service_artifacts.response import build_publish_response

logger = get_logger(__name__)


async def publish_artifact(
    *,
    file: UploadFile,
    title: str | None = None,
):
    extension = Path(file.filename).suffix.lower()

    artifact_type = validate_extension(file.filename)

    content = await validate_file(file)

    artifact_id = uuid4()

    slug = generate_slug()

    upload_result = upload_file(
        content=content,
        artifact_id=artifact_id,
        extension=extension,
        artifact_type=artifact_type.value,
    )

    logger.info(
        "Artifact published | slug=%s storage=%s",
        slug,
        upload_result,
    )

    return build_publish_response(
        artifact_id=artifact_id,
        slug=slug,
        artifact_type=artifact_type,
        filename=file.filename,
        size_bytes=len(content),
    )