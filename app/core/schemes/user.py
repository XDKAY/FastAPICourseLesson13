from typing import Annotated
from datetime import datetime
from pydantic import (
    BaseModel,
    SecretStr,
    EmailStr,
    ConfigDict,
    Field,
    field_validator,
)

from app.core.utils.password import is_valid_password


class UserBaseModel(BaseModel):
    username: Annotated[
        str,
        Field(
            examples=["Alex"],
            min_length=3,
            max_length=50,
        )
    ]
    email: EmailStr
    password: Annotated[
        SecretStr,
        Field(
            examples=["qwerty123!ABC"],
            min_length=8,
            max_length=20,
        )
    ]

    @field_validator("username")
    @classmethod
    def _validate_username(cls, username: str) -> str:
        if not username.isalpha():
            raise ValueError("Имя пользователя должно содержать только буквы")

        return username

    @field_validator("password")
    @classmethod
    def _validate_password(cls, password: SecretStr) -> SecretStr:
        is_valid_password(password.get_secret_value())
        return password


class UserRequestScheme(UserBaseModel):
    ...


class UserResponseScheme(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )

    id: str
    username: str
    email: str
    created_at: datetime
    password: Annotated[SecretStr, Field(exclude=True)]
