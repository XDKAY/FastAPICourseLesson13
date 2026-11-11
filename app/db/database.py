from typing import Any


class Database:
    __VAULT: list[Any] = []

    def append(self, data: Any) -> None:
        self.__VAULT.append(data)

    def get_data(self) -> list[Any]:
        return self.__VAULT

database = Database()
