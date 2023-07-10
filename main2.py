from DAL.POSTGRES_MANAGEMENT.PostgresManager import *
import datetime

with PostgresManager() as pgm:

    date = pgm.get_last_record()
    print(date)
