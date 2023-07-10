from DAL.PROTOCOLS.IManager import *
from DAL.POSTGRES_MANAGEMENT.PACKS.Queries import CREATE_DATABASE,CREATE_TABLE_IF_NOT_EXISTS,SET_DEFAULT_TIMEZONE
from DAL.POSTGRES_MANAGEMENT.PACKS.Queries import INSERT_INTO,GET_LAST_RECORD
from os import getenv
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction,ActiveSqlTransaction, InvalidTextRepresentation
from datetime import datetime


class PostgresManager(IManager):

    # Fields
    __HOST: str
    __PORT: int
    __DBNAME: str
    __USER: str
    __PASSWORD: str

    # Constructors
    def __init__(self):
        self.__set_credentials()

    def __enter__(self):
        self.__connect_database()
        # self.__create_database()
        self.__set_default_timezone()
        self.__create_table_if_not_exists()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close_database_connection()

    def __repr__(self):
        return f"Contex Manager Class {self.__name__}"

    # Database Backend Management Methods
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
        try:
            query = CREATE_TABLE_IF_NOT_EXISTS
            self.cursor.execute(query=query)
            self.commit()
            return True

        except Exception as E:
            print(E)

    def __set_default_timezone(self):
        query = SET_DEFAULT_TIMEZONE
        self.cursor.execute(query)
        self.commit()
        print("Timezone Updated")

    def commit(self) -> NoReturn:
        self.__connection.commit()

    def insert_into(self, data: List) -> bool:
        query = INSERT_INTO

        if data is None or len(data) == 0:
            return False

        for row in data:
            try:
                self.cursor.execute(query,row)

            except UniqueViolation:
                print("A")
                self.__connection.rollback()
                continue

            except InvalidTextRepresentation:
                self.__connection.rollback()
                continue

            except InFailedSqlTransaction:
                self.__connection.rollback()
                print("B")
                continue

        self.__connection.commit()
        return True

    def get_last_record(self) -> int :
        DATE_FORMAT = '%Y-%m-%d'
        query = GET_LAST_RECORD
        try:
            self.__connect_database()
            self.cursor.execute(query)
            date = self.cursor.fetchone()[1]
            date = date.strftime(DATE_FORMAT).replace("-","")
            return int(date)

        except Exception as E:
            print(E)
            default_date = datetime(year=2021,month=1,day=1).strftime(DATE_FORMAT).replace("-","")
            return int(default_date)
        finally:
            self.__close_database_connection()

    def fetch_all(self) -> List:
        return self.cursor.fetchall()


