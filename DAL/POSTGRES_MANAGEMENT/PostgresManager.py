from DAL.PROTOCOLS.IManager import *
from DAL.POSTGRES_MANAGEMENT.PACKS.Queries import CREATE_DATABASE
from os import getenv
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction,ActiveSqlTransaction


class PostgresManager(IManager):

    # Fields
    __HOST: str
    __PORT: int
    __DBNAME: str
    __USER: str
    __PASSWORD: str

    __connection: TypeVar("connection")
    cursor: TypeVar("cursor")

    # Constructors
    def __init__(self):
        self.__set_credentials()

    def __enter__(self):
        self.__connect_database()
        self.__create_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close_database_connection()

    def __repr__(self):
        return f"Contex Manager Class {self.__name__}"

    def __connect_database(self) -> NoReturn:
        try:
            self.__connection = psycopg2.connect(
                host=self.__HOST,
                port=self.__PORT,
                dbname=self.__DBNAME,
                user=self.__USER,
                password=self.__PASSWORD
            )
            self.cursor = self.__connection.cursor()
            print("Connected")
        except OperationalError:
            raise OperationalError("Cannot Connected Check Credentials or Database Status")

    def __close_database_connection(self) -> NoReturn:
        try:
            self.cursor.close()
            self.__connection.close()
            print("Closed")
        except OperationalError as E:
            raise OperationalError(E)

    def __set_credentials(self) -> NoReturn:

        if load_dotenv("CREDENTIALS/pg.env") is None:
            raise Exception("Credentials cannot verified")

        self.__HOST = getenv("HOST")
        self.__PORT = int(getenv("PORT"))
        self.__DBNAME = getenv("DBNAME")
        self.__USER = getenv("USER")
        self.__PASSWORD = getenv("PASSWORD")
        print("Credentials Setted")

    def __create_database(self) -> bool:
        try:
            query = CREATE_DATABASE
            self.cursor.execute(query)
            print("Database Created")
            return False

        except ActiveSqlTransaction:
            return True

        except OperationalError as E:
            raise OperationalError(E)

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


