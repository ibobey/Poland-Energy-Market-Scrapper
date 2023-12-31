import pandas as pd
from pandas.errors import EmptyDataError
from pandas import DataFrame
from typing import NoReturn
import io


class DataManager:

    data: DataFrame
    records: list
    __raw_data: str
    __records: list

    def __init__(self, raw_data: str):

        self.__raw_data = raw_data

        self.__convert_data()
        self.__rename_columns()
        self.__edit_data()
        self.__convert_data_to_list()

    def __convert_data(self) -> NoReturn:
        # self.data = pd.DataFrame([x.split(';') for x in self.__raw_data.split('\n')])
        try:
            self.data = pd.read_csv(io.StringIO(self.__raw_data),sep=";")
        except EmptyDataError:
            self.records = None
    def __rename_columns(self) -> NoReturn:
        try:
            column_list_renamed: dict = {'Date': 'date',
                                         'Period': 'period',
                                         'CRO': 'cro',
                                         'CROs': 'cros',
                                         'CROz': 'croz',
                                         'Aggregated Market Participants contracting status': 'contract_status',
                                         'Imbalance': 'imbalance'
                                         }
            self.data.rename(columns=column_list_renamed, inplace=True)
        except Exception:
            self.__records = None

    def __edit_data(self) -> NoReturn:
        try:

            self.data.date = self.data.date.astype(str)

            self.data.period = self.data.period - 1
            self.data.period = self.data.period.astype(str)
            self.data.period = self.data.period + ":00"

            cols_edit = ['cro', 'cros', 'croz', 'contract_status', 'imbalance']
            for i in cols_edit:
                self.data[i] = self.data[i].str.replace(",", ".")
                self.data[i] = self.data[i].astype(float)

        except Exception:
            self.__records = None
    def __convert_data_to_list(self) -> NoReturn:
        try:
            self.__records = self.data.values.tolist()
        except Exception:
            self.__records = None

    def get_edited_data(self) -> list:
        return self.__records




"""
dates = map(url_mapper, [process for process in map(url_mapper,DateGenerator())])
for i in dates:
    print(i)
"""