from pydantic import BaseModel

__all__ = ("ApplicationSettings", )


class CookieSettings(BaseModel):
    max_age: int = 300
    httponly: bool = True


class ApiSettings(BaseModel):
    version: str = "v1"
    prefix: str = "api"


class ApplicationSettings(BaseModel):
    title: str = "FastAPI Course Lesson 13"


class Settings(BaseModel):
    application: ApplicationSettings = ApplicationSettings()
    cookie: CookieSettings = CookieSettings()
    api: ApiSettings = ApiSettings()

settings = Settings()
