from typing import Protocol, NoReturn, TypeVar, List


class IManager(Protocol):

    # Fields
    __HOST: str
    __PORT: int
    __DBNAME: str
    __USER: str
    __PASSWORD: str

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

    def query_database(self, query: str) -> bool:
        ...

    def insert_into(self,data: list) -> bool:
        ...

    def fetch_all(self) -> List:
        ...
