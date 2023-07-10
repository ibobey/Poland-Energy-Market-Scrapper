from typing import Protocol, NoReturn, TypeVar, List


class IManager(Protocol):

    __connection: TypeVar
    cursor: TypeVar

    def __connect_database(self) -> NoReturn:
        ...

    def __close_database_connection(self) -> NoReturn:
        ...

    def __set_credentials(self) -> NoReturn:
        ...

    def __create_database(self) -> bool:
        ...

    def __create_table_if_not_exists(self) -> bool:
        ...

    def commit(self) -> NoReturn:
        ...

    def query_database(self) -> bool:
        ...

    def insert_into(self) -> bool:
        ...

    def fetch_all(self) -> List:
        ...
