import string


def is_valid_password(password: str) -> None:
    if not any(char in password for char in string.ascii_lowercase):
        raise ValueError("Пароль должен содержать хотя бы одну букву в нижнем регистре")

    if not any(char in password for char in string.ascii_uppercase):
        raise ValueError("Пароль должен содержать хотя бы одну букву в верхнем регистре")

    if not any(char in password for char in string.digits):
        raise ValueError("Пароль должен содержать хотя бы одну цифру")

    if not any(char in password for char in string.punctuation):
        raise ValueError("Пароль должен содержать хотя бы один знак пунктуации")
