from fastapi import APIRouter

from app.core.config.settings import settings

from .v1 import routers_version

__all__ = ("api_routers", )

api_routers = APIRouter(prefix=fr"/{settings.api.prefix}")
api_routers.include_router(routers_version)
