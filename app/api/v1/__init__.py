from fastapi import APIRouter

from app.core.config.settings import settings

from .routers import routers

__all__ = ("routers_version", )

routers_version = APIRouter(prefix=fr"/{settings.api.version}")
routers_version.include_router(routers)
