from DAL.POSTGRES_MANAGEMENT.PostgresManager import *
import datetime

with PostgresManager() as pgm:
    query = """
    INSERT INTO 
    market_data (date,time,cro,cros,croz,contract_status,imbalance)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    data = ('20230710','11:00',500,555,666,777,888)
    pgm.cursor.execute(query, data)
    print("INserted")
    pgm.commit()
