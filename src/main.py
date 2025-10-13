"""Main FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import cerner_router, dashboard
from api.agents import router as agents_router
from api.custom_query import router as custom_query_router
from core.config import settings
from db.session import db_manager
from utils.helpers import setup_logging

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager for startup/shutdown events."""
    try:
        await db_manager.connect()
        print(
            "PHA Server ready - Dashboard endpoints use real database connections only!"
        )
    except Exception as e:
        print(f"Failed to initialize database connection: {e}")

    yield

    try:
        if db_manager.client:
            db_manager.close()
    except Exception as e:
        print(f"Error during shutdown: {e}")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
# app.include_router(connections.router, prefix="/connections", tags=["Database Connections"])
# app.include_router(healthcare.router, prefix="/healthcare", tags=["Healthcare Queries"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Patient Dashboard"])
app.include_router(agents_router, prefix="/agents", tags=["agents"])
app.include_router(cerner_router.router)
app.include_router(custom_query_router, prefix="/api/v1")
# app.include_router(routes.router, prefix="/route")
# app.include_router(epic_tools.router)
# app.include_router(epic_router.router)
# app.include_router(cerner_tools.router)
# app.include_router(test_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
    )
