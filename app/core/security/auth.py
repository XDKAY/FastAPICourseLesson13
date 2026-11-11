from typing import Optional
from app.core.schemes.user import UserResponseScheme
from app.core.services.user import UserService
from app.core.security.password import verify_password

__all__ = ("user_authentication", )


def user_authentication(
    user_service: UserService, username: str, password: str
) -> Optional[UserResponseScheme]:

    user = user_service.get_by_username(username)

    if not user:
        return None

    if not verify_password(user.password.get_secret_value(), password):
        return None

    return UserResponseScheme.model_validate(user)
