from typing import Annotated

from fastapi import Depends

from app.core.repositories.user import UserRepository
from .database import DatabaseDep


__all__ = ("UserRepositoryDep", )


def get_user_repository(database: DatabaseDep) -> UserRepository:
    return UserRepository(database)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repository)]
