from fastapi import FastAPI

from app.api import api_routers
from app.core.config.settings import settings

app = FastAPI(
    title=settings.application.title
)
app.include_router(api_routers)
