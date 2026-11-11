from typing import Optional
from abc import ABC, abstractmethod

from app.core.schemes.user import (
    UserRequestScheme,
    UserResponseScheme,
)

from app.core.models.user import UserModel
from app.db.database import Database


class AbstractRepository(ABC):

    __MODEL = None

    @abstractmethod
    def add(self, user: UserRequestScheme) -> UserResponseScheme:
        ...

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[UserResponseScheme]:
        ...

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[UserResponseScheme]:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserResponseScheme]:
        ...


class UserRepository(AbstractRepository):
    __MODEL = UserModel

    def __init__(self, database: Database) -> None:
        self._database = database

    def add(self, user: UserRequestScheme) -> UserResponseScheme:
        user_orm = self.__MODEL.model_validate(user)
        self._database.append(user_orm)
        return UserResponseScheme.model_validate(user_orm)

    def get_by_id(self, id: str) -> Optional[UserResponseScheme]:
        for user_orm in self._database.get_data():
            if user_orm.id == id:
                return UserResponseScheme.model_validate(user_orm)

        return None

    def get_by_username(self, username: str) -> Optional[UserResponseScheme]:
        for user_orm in self._database.get_data():
            if user_orm.username == username:
                return UserResponseScheme.model_validate(user_orm)

        return None

    def get_by_email(self, email: str) -> Optional[UserResponseScheme]:
        for user_orm in self._database.get_data():
            if user_orm.email == email:
                return UserResponseScheme.model_validate(user_orm)

        return None
