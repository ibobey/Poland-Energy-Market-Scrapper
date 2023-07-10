

SET_DEFAULT_TIMEZONE = ""

CREATE_TABLE_IF_NOT_EXISTS = ""

INSERT_INTO = ""

GET_LAST_RECORD = ""

CREATE_DATABASE = """
    CREATE DATABASE poland_market_data
        WITH
        OWNER = postgres
        ENCODING = 'UTF8'
        CONNECTION LIMIT = -1
        IS_TEMPLATE = False;
"""