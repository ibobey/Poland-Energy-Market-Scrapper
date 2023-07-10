from DAL.POSTGRES_MANAGEMENT.PostgresManager import *

with PostgresManager() as pgm:
    print("Hi")