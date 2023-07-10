

SET_DEFAULT_TIMEZONE = "SET SESSION timezone TO 'Europe/Warsaw';"

CREATE_TABLE_IF_NOT_EXISTS = """
CREATE TABLE IF NOT EXISTS public.market_data
(
    id serial NOT NULL,
    date time with time zone,
    cro double precision,
    cros double precision,
    croz double precision,
    contract_status double precision,
    imbalance double precision,
    PRIMARY KEY (id),
    UNIQUE (date)
);

ALTER TABLE IF EXISTS public.market_data
    OWNER to postgres;

COMMENT ON TABLE public.market_data
    IS 'Energy Prices on Balancing Market';
"""

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