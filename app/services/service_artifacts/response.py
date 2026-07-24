from app.schemas.artifacts import PublishArtifactResponse
from app.core.config import ARTIFACT_BASE_URL


def build_publish_response(
    *,
    artifact,
):
    return PublishArtifactResponse(
        artifact_id=artifact["id"],
        slug=artifact["slug"],
        url=f"http://{artifact['slug'].lower()}.localhost:3000/",
        artifact_type=artifact["artifact_type"],
        filename=artifact["filename"],
        size_bytes=artifact["size_bytes"],
        created_at=artifact["created_at"],
    )