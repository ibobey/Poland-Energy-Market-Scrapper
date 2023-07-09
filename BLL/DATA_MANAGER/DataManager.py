import pandas as pd
from pandas import DataFrame


class DataManager:

    data: DataFrame
    records: list
    raw_data: str

    def __init__(self, raw_data: str):

        self.raw_data = raw_data

        self.__convert_data()
        self.__rename_columns()
        self.__edit_data()
        self.__convert_data_to_list()

    def __convert_data(self):
        pass

    def __rename_columns(self):
        pass

    def __edit_data(self):
        pass

    def __convert_data_to_list(self):
        pass

    def get_edited_data(self):
        pass



"""def url_mapper(b):
    return "http://abc.com/" + str(b)

def ma(word):
    return word + "mama"


dates = map(url_mapper, [process for process in map(url_mapper,DateGenerator())])
for i in dates:
    print(i)"""