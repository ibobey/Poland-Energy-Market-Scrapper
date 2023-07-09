from datetime import date,datetime,timedelta


class DateGenerator:

    # Fields
    now: datetime
    __start_date: datetime
    __end_date: datetime
    __cursor: datetime

    # Consts
    DATE_FORMAT = '%Y%m%d'

    # Contractors

    def __init__(self, start: int= None, end:int = None):
        self.__get_current_date()

        self.start = start
        self.end = end

        self.__set_dates()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cursor <= self.__end_date:
            result = self.__cursor
            self.__cursor += timedelta(days=1)
            # return result =>> returns datetime object
            return result.strftime('%Y%m%d')
        else:
            raise StopIteration

    def __repr__(self):
        return "Generator object"

    # CLass Default Methods

    def __get_current_date(self):
        now = date.today().strftime(self.DATE_FORMAT)
        now = datetime.strptime(now, self.DATE_FORMAT)
        self.now = now

    def __set_dates(self):
        if self.start is None:
            self.__start_date = datetime.strptime('20210101', self.DATE_FORMAT)
        else:
            self.__start_date = datetime.strptime(str(self.start), self.DATE_FORMAT)

        if self.end is None:
            self.__end_date = self.now
        else:
            self.__end_date = datetime.strptime(str(self.end), self.DATE_FORMAT)

        self.__cursor = self.__start_date


"""def url_mapper(b):
    return "http://abc.com/" + str(b)

def ma(word):
    return word + "mama"


dates = map(url_mapper, [process for process in map(url_mapper,DateGenerator())])
for i in dates:
    print(i)"""