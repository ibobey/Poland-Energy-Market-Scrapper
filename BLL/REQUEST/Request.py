import requests
from typing import List, NoReturn


class Request:

    __User_Agents: List[str]

    def __init__(self):
        self.__set_user_agents()

    def __set_user_agents(self) -> NoReturn:
        pass

    def download(self, url: str) -> bool:
        pass

    def export_data(self) -> str:
        pass