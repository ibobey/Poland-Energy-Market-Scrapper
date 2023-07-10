from DAL.POSTGRES_MANAGEMENT.PostgresManager import *
import datetime

with PostgresManager() as pgm:

    data = [

        ['20190714','11:00',444,555,666,777,888],
        ['20190715','12:00',444,555,666,777,888]]

    pgm.insert_into(data=data)
