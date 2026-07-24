import uuid 

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.request_context import request_id_ctx
from app.core.logger import get_logger

logger = get_logger("app")

async def request_context_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    request_id_ctx.set(request_id)

    logger.info(f"[{request_id}] {request.method} {request.url.path}")

    try:
        response = await call_next(request)
        logger.info(f"[{request_id}] {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"[{request_id}] Unhandled error: {str(e)}")
        raise

async def global_exception_handler(request: Request, exc: Exception):
    request_id = getattr(request.state, "request_id", "unknown")

    logger.error(f"[{request_id}] Crash: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "request_id": request_id
        },
    )