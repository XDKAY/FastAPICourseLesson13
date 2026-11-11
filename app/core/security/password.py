def verify_password(database_password: str, password: str) -> bool:
    return database_password == password
