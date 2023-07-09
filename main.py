from BLL.DATE.DateGenerator import *
from BLL.REQUEST.Request import *
from BLL.DATA_MANAGER.DataManager import *
from concurrent.futures import ThreadPoolExecutor


RAW_URL = "https://www.pse.pl/getcsv/-/export/csv/EN_CENY_NIEZB_RB/data/"
THREAD = 3


if __name__ == "__main__":

    scrapper = Request()

    with ThreadPoolExecutor(THREAD) as executor:
        for result in executor.map(scrapper.scrap, [process for process in map(lambda date_: RAW_URL + str(date_), DateGenerator())]):
            dataManager = DataManager(raw_data=result)
            edited_data = dataManager.get_edited_data()
            print(edited_data)


