from fastapi import APIRouter, status, Request, Depends

from app.core.logger import get_logger

logger = get_logger(__name__)

health_router = APIRouter(
    prefix="/health",
    tags=["Health"] 
)

@health_router.get("/",status_code=status.HTTP_200_OK)
async def check_health(request: Request):
    request_id = getattr(request.state, "request_id", "unknown")
    logger.info(f"Healthcheck request_id : {request_id}")
    return {
        "message": "Backend is healthy and running."
    }