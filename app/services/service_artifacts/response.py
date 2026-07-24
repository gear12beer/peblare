from datetime import UTC, datetime

from app.schemas.artifacts import PublishArtifactResponse


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
        url=f"http://localhost:3000/{slug}",
        artifact_type=artifact_type,
        filename=filename,
        size_bytes=size_bytes,
        created_at=datetime.now(UTC),
    )