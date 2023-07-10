from BLL.DATE.DateGenerator import *
from BLL.REQUEST.Request import *
from BLL.DATA_MANAGEMENT.DataManager import *
from concurrent.futures import ThreadPoolExecutor
from DAL.POSTGRES_MANAGEMENT.PostgresManager import *


def update_download_records():

    RAW_URL = "https://www.pse.pl/getcsv/-/export/csv/EN_CENY_NIEZB_RB/data/"
    THREAD = 6

    last_record_date_from_database = PostgresManager().get_last_record()
    start_date_for_scrapping = last_record_date_from_database

    scrapper = Request()
    with PostgresManager() as pgm:
        with ThreadPoolExecutor(THREAD) as executor:
            for result in executor.map(scrapper.scrap, [process for process in map(lambda date_: RAW_URL + str(date_), DateGenerator(start=start_date_for_scrapping))]):
                edited_data = DataManager(raw_data=result).get_edited_data()
                if edited_data is not None:
                    pgm.insert_into(data=edited_data)



if __name__ == "__main__":
    update_download_records()






# DataAccess Layer Need to overcome Database Stuff