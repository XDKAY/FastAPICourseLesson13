from fastapi import APIRouter

from .auth import router as auth_router
from .users import router as users_router

routers = APIRouter()
routers.include_router(auth_router)
routers.include_router(users_router)
