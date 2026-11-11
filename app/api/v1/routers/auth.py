from datetime import datetime, timezone

from fastapi import (
    APIRouter,
    HTTPException,
    Response,
    status,
)
from app.core.config.settings import settings
from app.core.schemes.user import (
    UserRequestScheme,
    UserResponseScheme,
)
from app.core.security.auth import user_authentication
from app.core.security.signature import signature
from app.api.dependencies.user_service import UserServiceDep


router = APIRouter(tags=["Auth"])


@router.post(
    "/register",
    response_model=UserResponseScheme,
    status_code=status.HTTP_201_CREATED
)
def register_handler(user: UserRequestScheme, user_service: UserServiceDep):
    existing_user = user_service.get_by_username(user.username) or \
                    user_service.get_by_email(user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким именем или email уже существует"
        )

    user_response = user_service.add(user)

    return user_response


@router.post("/login")
def login_handler(
    user: UserRequestScheme,
    user_service: UserServiceDep,
    response: Response
) -> dict[str, str]:
    existing_user = user_authentication(user_service, user.username, user.password.get_secret_value())

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не авторизован"
        )

    value = f"{existing_user.id}.{datetime.now(timezone.utc).timestamp()}"
    sig = signature.generate(value)

    response.set_cookie(
        key="session_token",
        value=f"{value}.{sig}",
        max_age=settings.cookie.max_age,
        httponly=settings.cookie.httponly,
    )

    return {
        "message": "Добро пожаловать!"
    }


@router.post("/logout")
def logout_handler(response: Response) -> dict[str, str]:
    response.delete_cookie(key="session_token")
    return {"message": "Заглядывай!"}
