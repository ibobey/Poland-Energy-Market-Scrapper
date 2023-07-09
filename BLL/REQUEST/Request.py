from CREDENTIALS.User_Agents import User_Agents
import requests
from typing import List, NoReturn
import random
from time import sleep


class Request:

    __User_Agents: List[str]
    __data: str

    def __init__(self):
        self.__set_user_agents()

    def __set_user_agents(self) -> NoReturn:
        self.__User_Agents = User_Agents

    def scrap(self, url: str) -> bool:

        headers: dict = {"User-Agent": random.choice(self.__User_Agents)}
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            self.__data = response.content.decode('ascii')
            return True

        elif response.status_code == 429:
            print("To Many Requests")
            sleep(7)
            self.scrap(url=url)

        elif response.status_code == 403:
            print(f"Forbidden  {response.status_code} {url}")
            return False

        else:
            print(f"Unknown {response.status_code} {url}")
            return False

    def parse_data(self) -> str:
        return self.__data
