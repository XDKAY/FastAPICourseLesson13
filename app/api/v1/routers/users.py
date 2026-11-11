from fastapi import APIRouter
from app.core.schemes.user import UserResponseScheme
from app.api.dependencies.current_user import CurrentUserDep

router = APIRouter(tags=["Users"])


@router.get("/profile")
def profile_handler(current_user: CurrentUserDep) -> UserResponseScheme:
    return current_user
