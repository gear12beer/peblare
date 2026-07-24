from datetime import datetime, UTC
from pathlib import Path
from uuid import uuid4
import secrets

from fastapi import HTTPException, UploadFile, status

from app.core.enums import ArtifactType
from app.core.logger import get_logger
from app.services.service_artifacts.validator import (
    validate_extension,
    validate_file,
)
from app.services.service_artifacts.slug import generate_slug
from app.services.service_artifacts.storage import save_file
from app.services.service_artifacts.response import build_publish_response

logger = get_logger(__name__)


async def publish_artifact(
    *,
    file: UploadFile,
    title: str | None = None,
):
    artifact_type = validate_extension(file.filename)

    content = await validate_file(file)

    artifact_id = uuid4()

    slug = generate_slug()

    save_file(
        artifact_id=artifact_id,
        extension=Path(file.filename).suffix.lower(),
        artifact_type=artifact_type.value,
        content=content,
    )

    logger.info(
        "Artifact published | slug=%s filename=%s",
        slug,
        file.filename,
    )

    return build_publish_response(
        artifact_id=artifact_id,
        slug=slug,
        artifact_type=artifact_type,
        filename=file.filename,
        size_bytes=len(content),
    )

