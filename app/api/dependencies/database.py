from typing import Annotated

from fastapi import Depends

from app.db.database import database, Database


__all__ = ("DatabaseDep", )


def get_database() -> Database:
    return database


DatabaseDep = Annotated[Database, Depends(get_database)]
