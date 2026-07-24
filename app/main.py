from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health.router import health_router

from app.middleware.middleware import (
    request_context_middleware,
    global_exception_handler,
)

from app.core.logger import get_logger

from app.core.config import (
    LOCAL_ORIGIN,
    PRODUCTION_ORIGIN,
    SERVER_ENV
)

logger = get_logger(__name__)

def create_app() -> FastAPI:
    """
    Factory function to create and configure the FastAPI application
    """
    app = FastAPI(
        title="Geneone Backend API",
        version="0.1.0" 
    )

    origins = []
    if SERVER_ENV == "dev":
        logger.info("Running in development mode")
        origins.append(LOCAL_ORIGIN)
    elif SERVER_ENV == "prod":
        logger.info("Running in production mode")
        origins.append(PRODUCTION_ORIGIN)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.middleware("http")(request_context_middleware)
    app.add_exception_handler(Exception, global_exception_handler)


    app.include_router(health_router)

    return app 

app = create_app()