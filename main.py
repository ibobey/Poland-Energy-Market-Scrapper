from BLL.DATE.DateGenerator import *
from BLL.REQUEST.Request import *
from BLL.DATA_MANAGER.DataManager import *
from concurrent.futures import ThreadPoolExecutor

RAW_URL = "https://www.pse.pl/getcsv/-/export/csv/EN_CENY_NIEZB_RB/data/"
THREAD = 8


def main():
    scrapper = Request()
    urls = map(scrapper.scrap, [process for process in map(lambda date_: RAW_URL + str(date_), DateGenerator())])
    download = map(scrapper.scrap,urls)
    for i in download:
        print(i)

main()

"""
if __name__ == "__main__":
    with ThreadPoolExecutor(THREAD) as executor:
        scrapper = Request()
        raw_web_data = executor.map(scrapper.scrap, [process for process in map(lambda date_: RAW_URL + str(date_), DateGenerator())])
        executor.map()
"""


