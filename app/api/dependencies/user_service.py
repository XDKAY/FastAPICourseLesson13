from typing import Annotated

from fastapi import Depends

from .repository import UserRepositoryDep

from app.core.services.user import UserService

__all__ = ("UserServiceDep", )


def get_user_service(repository: UserRepositoryDep) -> UserService:
    return UserService(repository)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
