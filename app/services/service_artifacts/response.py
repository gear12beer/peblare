from datetime import UTC, datetime

from app.schemas.artifacts import PublishArtifactResponse
from app.core.config import ARTIFACT_BASE_URL


def build_publish_response(
    *,
    artifact_id,
    slug,
    artifact_type,
    filename,
    size_bytes,
):

    return PublishArtifactResponse(
        artifact_id=artifact_id,
        slug=slug,
        url=f"http:{slug}//{ARTIFACT_BASE_URL}",
        artifact_type=artifact_type,
        filename=filename,
        size_bytes=size_bytes,
        created_at=datetime.now(UTC),
    )