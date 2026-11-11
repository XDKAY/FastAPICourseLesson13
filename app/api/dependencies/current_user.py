from typing import Optional, Annotated
from datetime import datetime, timezone, timedelta
from fastapi import Cookie, Response, Depends, HTTPException, status
from app.core.config.settings import settings
from app.core.schemes.user import UserResponseScheme
from app.core.security.signature import signature
from .user_service import UserServiceDep


__all__ = ("CurrentUserDep", )


SessionTokenDep = Annotated[Optional[str], Cookie()]

def get_current_user(
    response: Response,
    user_service: UserServiceDep,
    session_token: Optional[str] = Cookie(default=None)
) -> UserResponseScheme:

    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не авторизован"
        )

    value, sig = session_token.rsplit(".", 1)
    user_id, last_time = value.split(".", 1)


    if not signature.verify(value, sig):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не авторизован"
        )

    timedelta_ = datetime.now(timezone.utc) - datetime.fromtimestamp(float(last_time), tz=timezone.utc)
    user_orm = user_service.get_by_id(user_id)

    if timedelta(minutes=3) <= timedelta_ < timedelta(minutes=5):
        value = f"{user_id}.{datetime.now(timezone.utc).timestamp()}"
        response.set_cookie(
            key="session_token",
            value=f"{value}.{signature.generate(value)}",
            max_age=settings.cookie.max_age,
            httponly=settings.cookie.httponly
        )

    elif timedelta_ >= timedelta(minutes=5):
        response.delete_cookie(key="session_token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не авторизован"
        )

    return UserResponseScheme.model_validate(user_orm)



CurrentUserDep = Annotated[UserResponseScheme, Depends(get_current_user)]
