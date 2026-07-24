import os 
from dotenv import load_dotenv

from app.core.enums import ArtifactType

load_dotenv()

SERVER_ENV=os.getenv("SERVER_ENV")

# Origin Environment Variables for CORS configuration
LOCAL_ORIGIN=os.getenv("LOCAL_ORIGIN","http://localhost:3000")
PRODUCTION_ORIGIN=os.getenv("PRODUCTION_ORIGIN","")

ALLOWED_EXTENSIONS = {
    ".html": ArtifactType.HTML,
#    ".md": ArtifactType.MARKDOWN,
#    ".json": ArtifactType.JSON,
#    ".csv": ArtifactType.CSV,
#    ".txt": ArtifactType.TEXT,
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

ARTIFACT_BASE_URL = os.getenv("ARTIFACT_BASE_URL","http://localhost:3000")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")