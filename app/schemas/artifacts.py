from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime

from app.core.enums import ArtifactType

class PublishArtifactResponse(BaseModel):
    artifact_id: UUID
    slug: str
    url: HttpUrl
    artifact_type: ArtifactType
    filename: str
    size_bytes: int
    created_at: datetime