from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    status,
)

from app.schemas.artifacts import PublishArtifactResponse
from app.services.service_artifacts.service import publish_artifact
from app.core.logger import get_logger

logger = get_logger(__name__)

artifact_router = APIRouter(
    prefix="/artifacts",
    tags=["Artifacts"],
)

@artifact_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PublishArtifactResponse,
)
async def publish_artifact_endpoint(
    file: UploadFile = File(...),
    title: str | None = Form(default=None),
):

    return await publish_artifact(
        file=file,
        title=title,
    )


