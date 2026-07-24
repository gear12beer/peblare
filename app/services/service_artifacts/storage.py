from pathlib import Path
from uuid import UUID

UPLOAD_DIR = Path("uploads")


def save_file(
    *,
    artifact_id: UUID,
    extension: str,
    artifact_type: str,
    content: bytes,
) -> Path:

    storage_dir = UPLOAD_DIR / artifact_type

    storage_dir.mkdir(parents=True, exist_ok=True)

    path = storage_dir / f"{artifact_id}{extension}"

    with open(path, "wb") as fp:
        fp.write(content)

    return path